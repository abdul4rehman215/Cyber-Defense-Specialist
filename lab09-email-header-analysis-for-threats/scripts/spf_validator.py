#!/usr/bin/env python3

import dns.resolver
from ipaddress import ip_address, ip_network


class SPFValidator:

    def __init__(self):
        self.qualifiers = {
            '+': 'Pass',
            '-': 'Fail',
            '~': 'SoftFail',
            '?': 'Neutral'
        }

    def get_spf_record(self, domain):

        try:
            answers = dns.resolver.resolve(domain, 'TXT')

            for rdata in answers:
                record = ''.join([
                    part.decode() if isinstance(part, bytes) else part
                    for part in rdata.strings
                ])

                if record.startswith("v=spf1"):
                    return record

            return None

        except Exception as e:
            print(f"DNS Error: {e}")
            return None

    def parse_spf(self, spf_record):

        mechanisms = []
        modifiers = {}

        if not spf_record:
            return mechanisms, modifiers

        record = spf_record.replace("v=spf1", "").strip()
        parts = record.split()

        for part in parts:

            if '=' in part:
                key, value = part.split('=', 1)
                modifiers[key] = value
            else:
                mechanisms.append(part)

        return mechanisms, modifiers

    def check_ip4_mechanism(self, mechanism, sender_ip):

        try:
            network = mechanism.split(':')[1]
            return ip_address(sender_ip) in ip_network(network, strict=False)
        except Exception:
            return False

    def validate_ip(self, domain, sender_ip):

        print(f"\nValidating SPF: {domain} from {sender_ip}")

        spf_record = self.get_spf_record(domain)

        if not spf_record:
            print("No SPF record found.")
            return "None"

        mechanisms, modifiers = self.parse_spf(spf_record)

        for mech in mechanisms:

            qualifier = '+'

            if mech[0] in self.qualifiers:
                qualifier = mech[0]
                mech = mech[1:]

            if mech.startswith("ip4:"):
                if self.check_ip4_mechanism(mech, sender_ip):
                    return self.qualifiers[qualifier]

            if mech == "all":
                return self.qualifiers[qualifier]

        return "Neutral"

    def create_spf_record(self, domain, authorized_ips, include_domains=None):

        record = "v=spf1 "

        for ip in authorized_ips:
            record += f"ip4:{ip} "

        if include_domains:
            for inc in include_domains:
                record += f"include:{inc} "

        record += "mx -all"

        return record.strip()


def main():

    validator = SPFValidator()

    test_cases = [
        ('company.com', '192.0.2.10'),
        ('company.com', '203.0.113.50')
    ]

    for domain, ip in test_cases:
        result = validator.validate_ip(domain, ip)
        print(f"Result: {result}\n")

    spf = validator.create_spf_record(
        'mycompany.com',
        ['192.0.2.0/24', '198.51.100.10'],
        ['_spf.google.com']
    )

    print(f"Sample SPF: {spf}")


if __name__ == "__main__":
    main()
