#!/usr/bin/env python3
import json
from mitre_parser import MitreAttackParser

class AutoMapper:
    def __init__(self, parser):
        self.parser = parser
        self.indicators = {
            "powershell.exe": ["T1059.001"],
            "mimikatz.exe": ["T1003.001"],
            "service": ["T1543.003"],
            "port_445": ["T1046"]
        }

    def map_indicators(self, indicators):
        mapped = set()
        for ind in indicators:
            if ind in self.indicators:
                mapped.update(self.indicators[ind])
        return mapped

    def create_incident_report(self, name, indicators, output):
        techniques = self.map_indicators(indicators)
        details = [self.parser.get_technique_by_id(t) for t in techniques]

        report = {
            "incident": name,
            "techniques": details
        }

        with open(output, "w") as f:
            json.dump(report, f, indent=2)

if __name__ == "__main__":
    parser = MitreAttackParser()
    mapper = AutoMapper(parser)
    mapper.create_incident_report(
        "Sample Incident",
        ["powershell.exe", "mimikatz.exe"],
        "../reports/incident_report.json"
    )
