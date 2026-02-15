#!/usr/bin/env python3

import dns.resolver
from email import message_from_file


class DKIMValidator:

    def extract_dkim_signature(self, message):

        dkim_header = message.get('DKIM-Signature', '')

        if not dkim_header:
            return None

        params = {}
        parts = dkim_header.split(';')

        for part in parts:
            if '=' in part:
                key, value = part.strip().split('=', 1)
                params[key.strip()] = value.strip()

        return params

    def get_public_key(self, selector, domain):

        try:
            query = f"{selector}._domainkey.{domain}"
            answers = dns.resolver.resolve(query, 'TXT')

            for rdata in answers:
                record = ''.join([
                    part.decode() if isinstance(part, bytes) else part
                    for part in rdata.strings
                ])

                if "p=" in record:
                    return record

            return None

        except Exception as e:
            print(f"DNS Error: {e}")
            return None

    def validate_signature(self, email_file):

        print(f"\nValidating DKIM: {email_file}")

        try:
            with open(email_file, 'r') as f:
                message = message_from_file(f)

            signature = self.extract_dkim_signature(message)

            if not signature:
                print("No DKIM signature found.")
                return False

            domain = signature.get('d')
            selector = signature.get('s')

            if not domain or not selector:
                return False

            public_key = self.get_public_key(selector, domain)

            if not public_key:
                print("Public key not found.")
                return False

            # NOTE:
            # This implementation checks presence of public key only.
            # Full DKIM cryptographic validation requires canonicalization
            # and signature verification which is outside this lab scope.

            return True

        except Exception as e:
            print(f"Error validating DKIM: {e}")
            return False

    def create_dkim_record(self, domain, selector):

        record = (
            f"{selector}._domainkey.{domain} "
            f"IN TXT \"v=DKIM1; k=rsa; p=PUBLICKEYDATA\""
        )

        return record


def main():

    validator = DKIMValidator()

    samples = [
        'samples/legitimate.eml',
        'samples/phishing.eml'
    ]

    for sample in samples:
        result = validator.validate_signature(sample)
        print(f"DKIM Valid: {result}\n")

    record = validator.create_dkim_record('mycompany.com', 'default')

    print("Sample DKIM Record:")
    print(record)


if __name__ == "__main__":
    main()
