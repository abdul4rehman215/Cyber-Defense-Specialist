#!/usr/bin/env python3

import json
from typing import Dict, Any


class AlertEnricher:

    def __init__(self):
        self.threat_intel = self.load_threat_intel()

    def load_threat_intel(self) -> Dict[str, Any]:

        return {
            "malicious_ips": [
                "203.0.113.10",
                "198.51.100.25"
            ],
            "malicious_domains": [
                "malicious.com",
                "bad-domain.net"
            ],
            "known_hashes": [
                "abcd1234malwarehash"
            ]
        }

    def check_ip_reputation(self, ip_address: str) -> Dict[str, Any]:

        if ip_address in self.threat_intel["malicious_ips"]:
            return {
                "is_malicious": True,
                "threat_level": "HIGH",
                "description": "IP found in threat intelligence feed"
            }

        if (ip_address.startswith("192.168.") or
                ip_address.startswith("10.") or
                ip_address.startswith("172.16.")):
            return {
                "is_malicious": False,
                "threat_level": "INTERNAL",
                "description": "Internal network IP"
            }

        return {
            "is_malicious": False,
            "threat_level": "UNKNOWN",
            "description": "No reputation data found"
        }

    def enrich_alert(self, alert: Dict[str, Any]) -> Dict[str, Any]:

        enriched = alert.copy()

        source_rep = self.check_ip_reputation(alert.get("source_ip", ""))
        dest_rep = self.check_ip_reputation(alert.get("destination_ip", ""))

        enriched["source_ip_reputation"] = source_rep
        enriched["destination_ip_reputation"] = dest_rep

        enriched["is_external_threat"] = source_rep["is_malicious"]

        indicators = []

        if source_rep["is_malicious"]:
            indicators.append("Malicious Source IP")

        if dest_rep["is_malicious"]:
            indicators.append("Malicious Destination IP")

        enriched["threat_indicators"] = indicators

        return enriched

    def enrich_alert_batch(self, alerts: list) -> list:

        enriched_alerts = []

        for alert in alerts:
            enriched_alerts.append(self.enrich_alert(alert))

        return enriched_alerts


def main():

    print("=== Alert Enrichment Test ===")

    with open("data/sample_alerts.json", "r") as f:
        alerts = json.load(f)

    enricher = AlertEnricher()
    enriched = enricher.enrich_alert_batch(alerts)

    print(json.dumps(enriched, indent=4))


if __name__ == "__main__":
    main()
