#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from connectors.wazuh_connector import WazuhConnector
from connectors.thehive_connector import TheHiveConnector


class TestSOARIntegration(unittest.TestCase):

    def test_wazuh_authentication(self):

        connector = WazuhConnector(
            "https://localhost:55000",
            "wazuh",
            "wazuh"
        )

        result = connector.authenticate()
        self.assertTrue(result)

    def test_thehive_login(self):

        connector = TheHiveConnector("http://localhost:9000")

        result = connector.login(
            "admin@thehive.local",
            "admin123"
        )

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
