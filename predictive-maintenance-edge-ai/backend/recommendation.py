def get_maintenance_recommendation(probability):
    if probability >= 0.80:
        return {
            "risk": "Critical",
            "action": "Stop the machine immediately and perform maintenance.",
            "color": "red"
        }

    elif probability >= 0.60:
        return {
            "risk": "High",
            "action": "Schedule maintenance within the next 24 hours.",
            "color": "orange"
        }

    elif probability >= 0.30:
        return {
            "risk": "Medium",
            "action": "Continue monitoring and inspect during the next maintenance cycle.",
            "color": "yellow"
        }

    return {
        "risk": "Low",
        "action": "Machine is operating normally.",
        "color": "green"
    }