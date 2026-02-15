#!/usr/bin/env python3

import os
import sys
import hashlib
import magic
import json
from datetime import datetime


class AttachmentScanner:

    def __init__(self):
        self.suspicious_extensions = [
            '.exe', '.scr', '.bat', '.cmd', '.vbs',
            '.js', '.jar', '.zip', '.rar'
        ]
        self.scan_results = []

    def calculate_hash(self, filepath):

        md5 = hashlib.md5()
        sha256 = hashlib.sha256()

        with open(filepath, 'rb') as f:
            while chunk := f.read(4096):
                md5.update(chunk)
                sha256.update(chunk)

        return md5.hexdigest(), sha256.hexdigest()

    def get_file_info(self, filepath):

        size = os.path.getsize(filepath)
        mime = magic.from_file(filepath, mime=True)
        description = magic.from_file(filepath)

        return {
            "size": size,
            "mime_type": mime,
            "description": description
        }

    def calculate_risk_score(self, filepath, filename):

        risk_score = 0
        warnings = []

        extension = os.path.splitext(filename)[1].lower()

        if extension in self.suspicious_extensions:
            risk_score += 30
            warnings.append("Suspicious file extension")

        file_info = self.get_file_info(filepath)

        if "executable" in file_info["description"].lower():
            risk_score += 25
            warnings.append("Executable file detected")

        if filename.count('.') > 1:
            risk_score += 40
            warnings.append("Double extension detected")

        size = file_info["size"]

        if size < 100:
            risk_score += 10
            warnings.append("Unusually small file size")

        if size > 50 * 1024 * 1024:
            risk_score += 20
            warnings.append("Unusually large file size")

        return risk_score, warnings

    def scan_file(self, filepath):

        filename = os.path.basename(filepath)

        print(f"\n[SCANNING] {filename}")
        print("-" * 50)

        md5, sha256 = self.calculate_hash(filepath)
        file_info = self.get_file_info(filepath)
        risk_score, warnings = self.calculate_risk_score(filepath, filename)

        if risk_score >= 50:
            level = "HIGH"
        elif risk_score >= 25:
            level = "MEDIUM"
        elif risk_score >= 10:
            level = "LOW"
        else:
            level = "CLEAN"

        print(f"Size: {file_info['size']} bytes")
        print(f"MIME: {file_info['mime_type']}")
        print(f"MD5: {md5}")
        print(f"SHA256: {sha256}")
        print(f"Risk Score: {risk_score}")
        print(f"Threat Level: {level}")
        print(f"Warnings: {warnings}")

        self.scan_results.append({
            "file": filename,
            "risk_score": risk_score,
            "threat_level": level,
            "warnings": warnings
        })

    def scan_directory(self, directory):

        if not os.path.exists(directory):
            print("Directory not found.")
            return

        for file in os.listdir(directory):
            full_path = os.path.join(directory, file)
            if os.path.isfile(full_path):
                self.scan_file(full_path)

        self.generate_report()

    def generate_report(self):

        high_risk = [r for r in self.scan_results if r["threat_level"] == "HIGH"]

        summary = {
            "timestamp": datetime.now().isoformat(),
            "total_files": len(self.scan_results),
            "high_risk": len(high_risk),
            "results": self.scan_results
        }

        os.makedirs("reports", exist_ok=True)

        output_file = f"reports/attachment_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(output_file, "w") as f:
            json.dump(summary, f, indent=4)

        print("\nReport saved:", output_file)


def main():

    scanner = AttachmentScanner()

    if len(sys.argv) < 2:
        print("Usage: python3 attachment_scanner.py <file_or_directory>")
        sys.exit(1)

    target = sys.argv[1]

    if os.path.isfile(target):
        scanner.scan_file(target)
        scanner.generate_report()
    elif os.path.isdir(target):
        scanner.scan_directory(target)
    else:
        print("Invalid target.")


if __name__ == "__main__":
    main()
