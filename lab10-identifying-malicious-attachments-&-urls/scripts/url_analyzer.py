#!/usr/bin/env python3

import requests
import re
import urllib.parse
import sys
import json
import os
from bs4 import BeautifulSoup
from datetime import datetime


class URLAnalyzer:

    def __init__(self):
        self.suspicious_keywords = [
            'login', 'verify', 'account', 'suspended', 'urgent',
            'winner', 'prize', 'bitcoin', 'pharmacy'
        ]
        self.url_shorteners = [
            'bit.ly', 'tinyurl.com', 'goo.gl', 't.co'
        ]
        self.results = []

    def extract_domain(self, url):

        parsed = urllib.parse.urlparse(url)
        return parsed.netloc

    def analyze_url_structure(self, url):

        risk_score = 0
        warnings = []

        if re.search(r'\d{1,3}(\.\d{1,3}){3}', url):
            risk_score += 25
            warnings.append("IP address used instead of domain")

        domain = self.extract_domain(url)

        for shortener in self.url_shorteners:
            if shortener in domain:
                risk_score += 20
                warnings.append("URL shortener detected")

        if domain.count('.') > 3:
            risk_score += 15
            warnings.append("Excessive subdomains")

        if len(url) > 200:
            risk_score += 15
            warnings.append("Excessive URL length")

        if "%" in url or "@" in url:
            risk_score += 10
            warnings.append("Suspicious encoding or characters")

        return risk_score, warnings

    def fetch_url_content(self, url):

        info = {
            "status_code": None,
            "content_type": None,
            "redirects": 0,
            "forms": 0,
            "external_links": 0,
            "text": ""
        }

        try:
            headers = {"User-Agent": "Mozilla/5.0 SecurityScanner"}
            response = requests.get(url, headers=headers, timeout=5)

            info["status_code"] = response.status_code
            info["content_type"] = response.headers.get("Content-Type", "")
            info["redirects"] = len(response.history)

            if "text/html" in info["content_type"]:
                soup = BeautifulSoup(response.text, "html.parser")
                info["forms"] = len(soup.find_all("form"))
                info["external_links"] = len(
                    [a for a in soup.find_all("a", href=True)
                     if url not in a['href']]
                )
                info["text"] = soup.get_text().lower()

        except Exception as e:
            info["error"] = str(e)

        return info

    def analyze_content(self, content_info):

        risk_score = 0
        warnings = []

        text = content_info.get("text", "")

        for keyword in self.suspicious_keywords:
            if keyword in text:
                risk_score += 5
                warnings.append(f"Keyword detected: {keyword}")

        if content_info.get("forms", 0) > 3:
            risk_score += 20
            warnings.append("Excessive forms detected")

        if content_info.get("redirects", 0) > 2:
            risk_score += 15
            warnings.append("Redirect chain detected")

        return risk_score, warnings

    def analyze_url(self, url):

        print(f"\n[ANALYZING] {url}")
        print("-" * 60)

        if not url.startswith(("http://", "https://")):
            url = "http://" + url

        structure_score, structure_warn = self.analyze_url_structure(url)
        content_info = self.fetch_url_content(url)
        content_score, content_warn = self.analyze_content(content_info)

        total_score = structure_score + content_score
        warnings = structure_warn + content_warn

        if total_score >= 50:
            level = "HIGH"
        elif total_score >= 25:
            level = "MEDIUM"
        elif total_score >= 10:
            level = "LOW"
        else:
            level = "CLEAN"

        print(f"Risk Score: {total_score}")
        print(f"Threat Level: {level}")
        print(f"Warnings: {warnings}")

        self.results.append({
            "url": url,
            "risk_score": total_score,
            "threat_level": level,
            "warnings": warnings
        })

    def analyze_url_list(self, url_file):

        if not os.path.exists(url_file):
            print("File not found.")
            return

        with open(url_file, "r") as f:
            urls = f.read().splitlines()

        for url in urls:
            if url.strip():
                self.analyze_url(url.strip())

        self.generate_report()

    def generate_report(self):

        summary = {
            "timestamp": datetime.now().isoformat(),
            "total_urls": len(self.results),
            "high_risk": len([r for r in self.results if r["threat_level"] == "HIGH"]),
            "results": self.results
        }

        os.makedirs("reports", exist_ok=True)

        output_file = f"reports/url_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(output_file, "w") as f:
            json.dump(summary, f, indent=4)

        print("\nReport saved:", output_file)


def main():

    analyzer = URLAnalyzer()

    if len(sys.argv) < 2:
        print("Usage: python3 url_analyzer.py <url_or_file>")
        sys.exit(1)

    target = sys.argv[1]

    if target.startswith(("http://", "https://")):
        analyzer.analyze_url(target)
        analyzer.generate_report()
    elif os.path.isfile(target):
        analyzer.analyze_url_list(target)
    else:
        print("Invalid input.")


if __name__ == "__main__":
    main()
