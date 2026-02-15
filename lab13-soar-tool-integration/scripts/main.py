#!/usr/bin/env python3

import yaml
import logging
import sys
import os
from workflows.orchestrator import WorkflowOrchestrator


def setup_logging(config: dict):

    log_level = getattr(logging, config["logging"]["level"].upper(), logging.INFO)

    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(config["logging"]["file"]),
            logging.StreamHandler(sys.stdout)
        ]
    )


def load_config(config_file: str = 'config.yaml') -> dict:

    try:
        with open(config_file, "r") as f:
            config = yaml.safe_load(f)

        required_sections = ["wazuh", "thehive", "playbooks", "logging"]

        for section in required_sections:
            if section not in config:
                raise ValueError(f"Missing configuration section: {section}")

        return config

    except Exception as e:
        print(f"Configuration error: {e}")
        sys.exit(1)


def main():

    config = load_config()

    setup_logging(config)

    logging.info("Starting SOAR Integration Platform")

    orchestrator = WorkflowOrchestrator(config)

    if not orchestrator.wazuh.authenticate():
        logging.error("Wazuh authentication failed")
        sys.exit(1)

    if not orchestrator.thehive.login(
        config["thehive"]["username"],
        config["thehive"]["password"]
    ):
        logging.error("TheHive authentication failed")
        sys.exit(1)

    orchestrator.process_alerts(
        poll_interval=config["wazuh"]["poll_interval"]
    )


if __name__ == "__main__":
    main()
