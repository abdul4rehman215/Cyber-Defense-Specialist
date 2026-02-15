#!/usr/bin/env python3

import requests
import logging
from datetime import datetime


class TheHiveConnector:
    """
    Connector for TheHive case management platform.
    Handles case creation and management.
    """

    def __init__(self, url: str, username: str = None, password: str = None):
        self.url = url.rstrip("/")
        self.username = username
        self.password = password
        self.session = requests.Session()

    def login(self, username: str, password: str) -> bool:
        try:
            login_url = f"{self.url}/api/login"
            response = self.session.post(
                login_url,
                json={"user": username, "password": password}
            )

            if response.status_code == 200:
                return True

            logging.error("TheHive login failed")
            return False

        except Exception as e:
            logging.error(f"TheHive login error: {e}")
            return False

    def create_case(self, title: str, description: str, severity: int = 2,
                    tags: list = None) -> str:
        try:
            case_data = {
                "title": title,
                "description": description,
                "severity": severity,
                "startDate": int(datetime.now().timestamp() * 1000),
                "tlp": 2,
                "pap": 2,
                "tags": tags or []
            }

            response = self.session.post(
                f"{self.url}/api/case",
                json=case_data
            )

            if response.status_code == 201:
                case_id = response.json().get("id")
                return case_id

            logging.error("Failed creating case in TheHive")
            return None

        except Exception as e:
            logging.error(f"Case creation error: {e}")
            return None

    def add_observable(self, case_id: str, data_type: str, data: str) -> bool:
        try:
            observable = {
                "dataType": data_type,
                "data": data,
                "tlp": 2,
                "pap": 2
            }

            response = self.session.post(
                f"{self.url}/api/case/{case_id}/observable",
                json=observable
            )

            return response.status_code == 201

        except Exception as e:
            logging.error(f"Add observable error: {e}")
            return False

    def update_case_status(self, case_id: str, status: str) -> bool:
        try:
            response = self.session.patch(
                f"{self.url}/api/case/{case_id}",
                json={"status": status}
            )

            return response.status_code == 200

        except Exception as e:
            logging.error(f"Case status update error: {e}")
            return False
