#!/usr/bin/env python3

"""
Threat Intelligence Collector
Complete implementation for Ubuntu 24.04 (Python 3.12)
"""

import json
import hashlib
import ipaddress
import logging
import os
import re
from datetime import datetime


class ThreatCollector:

    def __init__(self, config_file="config/sources.json"):
        self.config = self.load_config(config_file)
        self.collected_data = []
        self.setup_logging()

    def load_config(self, config_file):
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Configuration file not found: {config_file}")

        with open(config_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def setup_logging(self):
        log_file = "logs/collection.log"

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )

    def validate_ip(self, ip_string):
        try:
            ipaddress.ip_address(ip_string.strip())
            return True
        except ValueError:
            return False

    def validate_domain(self, domain_string):
        domain_string = domain_string.strip().lower()

        if "." not in domain_string:
            return False

        pattern = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$"
        return re.match(pattern, domain_string) is not None

    def validate_hash(self, hash_string):
        hash_string = hash_string.strip().lower()

        if not re.fullmatch(r"[a-f0-9]+", hash_string):
            return None

        length = len(hash_string)

        if length == 32:
            return "MD5"
        elif length == 40:
            return "SHA1"
        elif length == 64:
            return "SHA256"

        return None

    def enrich_indicator(self, indicator, indicator_type):

        now = datetime.utcnow().isoformat()

        unique_string = f"{indicator}_{indicator_type}_{now}"
        unique_id = hashlib.sha256(unique_string.encode()).hexdigest()

        enriched = {
            "id": unique_id,
            "value": indicator,
            "type": indicator_type,
            "first_seen": now,
            "last_seen": now,
            "confidence": 50,
            "tags": ["threat_intel"],
            "risk_score": 0
        }

        return enriched

    def calculate_risk_score(self, indicator_data):

        score = indicator_data.get("confidence", 50)

        if indicator_data["type"] == "ip":
            score += 10
        elif indicator_data["type"] == "domain":
            score += 20
        elif indicator_data["type"] == "hash":
            score += 30

        if score > 100:
            score = 100

        if score < 0:
            score = 0

        return score

    def collect_from_file(self, filename, indicator_type):

        if not os.path.exists(filename):
            logging.warning(f"File not found: {filename}")
            return []

        collected = []

        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                value = line.strip()
                if not value:
                    continue

                valid = False

                if indicator_type == "ip":
                    valid = self.validate_ip(value)
                elif indicator_type == "domain":
                    valid = self.validate_domain(value)
                elif indicator_type == "hash":
                    valid = self.validate_hash(value) is not None

                if valid:
                    enriched = self.enrich_indicator(value, indicator_type)
                    enriched["risk_score"] = self.calculate_risk_score(enriched)
                    collected.append(enriched)
                    self.collected_data.append(enriched)

        return collected

    def save_collected_data(self, output_file=None):

        if output_file is None:
            timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
            output_file = f"data/collected_{timestamp}.json"

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(self.collected_data, f, indent=4)

        logging.info(f"Collected data saved to {output_file}")

        return output_file

    def run_collection(self):

        logging.info("Starting threat collection process")

        local_feeds = self.config["data_sources"]["local_feeds"]

        for feed in local_feeds:
            if "domain" in feed:
                self.collect_from_file(feed, "domain")
            elif "ip" in feed:
                self.collect_from_file(feed, "ip")

        output_file = self.save_collected_data()

        summary = {
            "total_indicators": len(self.collected_data),
            "output_file": output_file
        }

        logging.info(f"Collection completed: {summary}")

        return summary


def main():

    print("Threat Intelligence Collector")
    print("=" * 50)

    try:
        collector = ThreatCollector()
        summary = collector.run_collection()

        print("\nCollection Summary:")
        print(f"Total Indicators: {summary['total_indicators']}")
        print(f"Output File: {summary['output_file']}")

    except Exception as e:
        logging.error(f"Error during collection: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
