#!/usr/bin/env python3

"""
Threat Intelligence Data Normalizer
Complete implementation for Ubuntu 24.04 (Python 3.12)
"""

import json
import os
from datetime import datetime
from collections import defaultdict


class ThreatNormalizer:

    def __init__(self):
        self.normalized_data = []
        self.duplicate_count = 0

    def load_raw_data(self, data_file):

        if not os.path.exists(data_file):
            raise FileNotFoundError(f"Raw data file not found: {data_file}")

        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("Invalid data format: Expected list of indicators")

        return data

    def normalize_confidence(self, confidence_value):

        if confidence_value is None:
            return 50

        if isinstance(confidence_value, float) and 0 <= confidence_value <= 1:
            confidence_value = int(confidence_value * 100)

        confidence_value = int(confidence_value)

        if confidence_value < 0:
            confidence_value = 0
        if confidence_value > 100:
            confidence_value = 100

        return confidence_value

    def normalize_severity(self, risk_score):

        if risk_score >= 80:
            return "HIGH"
        elif risk_score >= 60:
            return "MEDIUM"
        elif risk_score >= 40:
            return "LOW"
        else:
            return "INFO"

    def normalize_tags(self, tags):

        if tags is None:
            return []

        if isinstance(tags, str):
            tags = [tags]

        normalized = []

        tag_mapping = {
            "c2": "command_control",
            "cmd": "command_control",
            "phish": "phishing",
            "malware": "malware"
        }

        for tag in tags:
            tag = tag.strip().lower()
            tag = tag_mapping.get(tag, tag)
            normalized.append(tag)

        return list(set(normalized))

    def deduplicate_indicators(self, indicators):

        unique = {}

        for indicator in indicators:
            key = f"{indicator['value']}_{indicator['type']}"

            if key not in unique:
                unique[key] = indicator
            else:
                self.duplicate_count += 1

                if indicator["confidence"] > unique[key]["confidence"]:
                    unique[key] = indicator
                else:
                    existing_tags = set(unique[key].get("tags", []))
                    new_tags = set(indicator.get("tags", []))
                    unique[key]["tags"] = list(existing_tags.union(new_tags))

        return list(unique.values())

    def normalize_dataset(self, raw_data):

        normalized = []

        for indicator in raw_data:

            normalized_indicator = {
                "id": indicator.get("id"),
                "value": indicator.get("value"),
                "type": indicator.get("type"),
                "first_seen": indicator.get("first_seen"),
                "last_seen": indicator.get("last_seen"),
                "confidence": self.normalize_confidence(indicator.get("confidence")),
                "risk_score": indicator.get("risk_score"),
                "severity": self.normalize_severity(indicator.get("risk_score", 0)),
                "tags": self.normalize_tags(indicator.get("tags"))
            }

            normalized.append(normalized_indicator)

        normalized = self.deduplicate_indicators(normalized)
        self.normalized_data = normalized

        return normalized

    def save_normalized_data(self, output_file):

        metadata = {
            "normalization_timestamp": datetime.utcnow().isoformat(),
            "total_indicators": len(self.normalized_data),
            "duplicates_removed": self.duplicate_count
        }

        output_structure = {
            "metadata": metadata,
            "indicators": self.normalized_data
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output_structure, f, indent=4)

    def generate_statistics(self):

        stats = {
            "total": len(self.normalized_data),
            "by_type": defaultdict(int),
            "by_severity": defaultdict(int),
            "average_confidence": 0
        }

        total_conf = 0

        for indicator in self.normalized_data:
            stats["by_type"][indicator["type"]] += 1
            stats["by_severity"][indicator["severity"]] += 1
            total_conf += indicator["confidence"]

        if len(self.normalized_data) > 0:
            stats["average_confidence"] = round(
                total_conf / len(self.normalized_data), 2
            )

        stats["by_type"] = dict(stats["by_type"])
        stats["by_severity"] = dict(stats["by_severity"])

        return stats


def main():

    print("Threat Intelligence Data Normalizer")
    print("=" * 50)

    try:
        data_files = sorted(
            [f for f in os.listdir("data") if f.startswith("collected_")]
        )

        if not data_files:
            raise FileNotFoundError("No collected data files found in data/")

        latest_file = os.path.join("data", data_files[-1])

        normalizer = ThreatNormalizer()

        raw_data = normalizer.load_raw_data(latest_file)

        normalizer.normalize_dataset(raw_data)

        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        output_file = f"data/normalized_{timestamp}.json"

        normalizer.save_normalized_data(output_file)

        stats = normalizer.generate_statistics()

        print("\nNormalization Summary:")
        print(f"Total Indicators: {stats['total']}")
        print(f"Average Confidence: {stats['average_confidence']}")
        print(f"By Type: {stats['by_type']}")
        print(f"By Severity: {stats['by_severity']}")
        print(f"Output File: {output_file}")

    except Exception as e:
        print(f"Error during normalization: {e}")


if __name__ == "__main__":
    main()
