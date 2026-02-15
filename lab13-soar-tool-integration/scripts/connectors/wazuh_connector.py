#!/usr/bin/env python3

import requests
import logging
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class WazuhConnector:
    """
    Connector for Wazuh SIEM API integration.
    Handles authentication and alert retrieval.
    """

    def __init__(self, url: str, username: str, password: str):
        self.url = url.rstrip("/")
        self.username = username
        self.password = password
        self.token = None

    def authenticate(self) -> bool:
        try:
            response = requests.post(
                f"{self.url}/security/user/authenticate",
                auth=HTTPBasicAuth(self.username, self.password),
                verify=False
            )

            if response.status_code == 200:
                self.token = response.json()["data"]["token"]
                return True

            logging.error("Wazuh authentication failed")
            return False

        except Exception as e:
            logging.error(f"Wazuh authentication error: {e}")
            return False

    def _headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    def get_alerts(self, limit: int = 10, min_level: int = 0) -> list:
        if not self.token:
            if not self.authenticate():
                return []

        try:
            params = {
                "limit": limit,
                "sort": "-timestamp",
                "q": f"rule.level>={min_level}"
            }

            response = requests.get(
                f"{self.url}/alerts",
                headers=self._headers(),
                params=params,
                verify=False
            )

            if response.status_code == 200:
                return response.json().get("data", {}).get("affected_items", [])

            logging.error("Failed retrieving alerts")
            return []

        except Exception as e:
            logging.error(f"Alert retrieval error: {e}")
            return []

    def get_agent_info(self, agent_id: str) -> dict:
        if not self.token:
            if not self.authenticate():
                return {}

        try:
            response = requests.get(
                f"{self.url}/agents/{agent_id}",
                headers=self._headers(),
                verify=False
            )

            if response.status_code == 200:
                return response.json().get("data", {})

            return {}

        except Exception as e:
            logging.error(f"Agent info error: {e}")
            return {}
