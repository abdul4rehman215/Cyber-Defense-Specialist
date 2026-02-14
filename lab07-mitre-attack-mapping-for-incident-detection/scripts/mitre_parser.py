#!/usr/bin/env python3
import json

class MitreAttackParser:
    def __init__(self, json_file_path="../data/enterprise-attack.json"):
        self.json_file_path = json_file_path
        self.techniques = {}
        self.tactics = {}
        self.load_data()

    def load_data(self):
        with open(self.json_file_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)
        self.parse_techniques()
        self.parse_tactics()

    def parse_techniques(self):
        for obj in self.data.get("objects", []):
            if obj.get("type") == "attack-pattern":
                for ref in obj.get("external_references", []):
                    if ref.get("source_name") == "mitre-attack":
                        tid = ref.get("external_id")
                        self.techniques[tid] = {
                            "id": tid,
                            "name": obj.get("name"),
                            "description": obj.get("description", ""),
                            "tactics": obj.get("kill_chain_phases", []),
                            "platforms": obj.get("x_mitre_platforms", [])
                        }

    def parse_tactics(self):
        for obj in self.data.get("objects", []):
            if obj.get("type") == "x-mitre-tactic":
                self.tactics[obj.get("x_mitre_shortname")] = {
                    "name": obj.get("name"),
                    "description": obj.get("description")
                }

    def get_technique_by_id(self, technique_id):
        return self.techniques.get(technique_id)

    def search_techniques_by_keyword(self, keyword):
        keyword = keyword.lower()
        return [
            t for t in self.techniques.values()
            if keyword in t["name"].lower() or keyword in t["description"].lower()
        ]

if __name__ == "__main__":
    parser = MitreAttackParser()
    print(f"Loaded {len(parser.techniques)} techniques")
    print(f"Loaded {len(parser.tactics)} tactics")
