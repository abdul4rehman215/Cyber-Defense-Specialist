#!/usr/bin/env python3

class TrafficAlertSystem:
    def __init__(self):
        self.alert_threshold = {
            'sql_injection': 1,
            'xss': 1,
            'path_traversal': 1,
            'unusual_user_agent': 3
        }

    def check_alerts(self, analysis_results):
        alerts = []
        for key, threshold in self.alert_threshold.items():
            if analysis_results.get(key, 0) >= threshold:
                alerts.append(f"ALERT: {key} detected")
        return alerts

    def send_alert(self, alert_message):
        with open("alerts.log", "a") as f:
            f.write(alert_message + "\n")
        print(alert_message)

if __name__ == "__main__":
    system = TrafficAlertSystem()
    sample_data = {
        'sql_injection': 2,
        'xss': 0,
        'path_traversal': 1,
        'unusual_user_agent': 4
    }

    alerts = system.check_alerts(sample_data)
    for alert in alerts:
        system.send_alert(alert)
