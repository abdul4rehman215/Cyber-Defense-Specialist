#!/usr/bin/env python3

import dns.resolver


class DMARCValidator:

    def __init__(self):
        self.policies = ['none', 'quarantine', 'reject']

    def get_dmarc_record(self, domain):

        try:
            query = f"_dmarc.{domain}"
            answers = dns.resolver.resolve(query, 'TXT')

            for rdata in answers:
                record = ''.join([
                    part.decode() if isinstance(part, bytes) else part
                    for part in rdata.strings
                ])

                if record.startswith("v=DMARC1"):
                    return record

            return None

        except Exception as e:
            print(f"DNS Error: {e}")
            return None

    def parse_dmarc(self, dmarc_record):

        params = {}

        if not dmarc_record:
            return params

        parts = dmarc_record.split(';')

        for part in parts:
            part = part.strip()

            if '=' in part:
                key, value = part.split('=', 1)
                params[key.strip()] = value.strip()

        return params

    def validate_policy(self, domain, spf_result, dkim_result):

        print(f"\nValidating DMARC: {domain}")
        print(f"SPF: {spf_result}, DKIM: {dkim_result}")

        dmarc_record = self.get_dmarc_record(domain)

        if not dmarc_record:
            print("No DMARC record found.")
            return "None"

        policy = self.parse_dmarc(dmarc_record)
        policy_action = policy.get('p', 'none')

        # Alignment logic (simplified)
        if spf_result == "Pass" or dkim_result:
            return "Pass (Aligned)"

        if policy_action == "reject":
            return "Reject"
        elif policy_action == "quarantine":
            return "Quarantine"
        else:
            return "None"

    def create_dmarc_record(self, domain, policy='quarantine', pct=100):

        record = (
            f"_dmarc.{domain} IN TXT "
            f"\"v=DMARC1; p={policy}; pct={pct}; rua=mailto:dmarc@{domain}\""
        )

        return record


def main():

    validator = DMARCValidator()

    test_cases = [
        ('company.com', 'Pass', True),
        ('company.com', 'Fail', False),
        ('company.com', 'Pass', False)
    ]

    for domain, spf, dkim in test_cases:
        result = validator.validate_policy(domain, spf, dkim)
        print(f"DMARC Result: {result}\n")

    record = validator.create_dmarc_record('mycompany.com', 'quarantine', 100)

    print("Sample DMARC Record:")
    print(record)


if __name__ == "__main__":
    main()
