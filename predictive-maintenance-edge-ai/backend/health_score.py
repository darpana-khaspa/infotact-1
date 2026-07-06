def calculate_health_score(failure_probability):
    """
    Calculate machine health score from failure probability.

    Parameters:
        failure_probability (float): Value between 0 and 1.

    Returns:
        float: Health score (0-100)
    """
    failure_probability = max(0.0, min(1.0, failure_probability))
    return round((1 - failure_probability) * 100, 2)


def get_machine_health(failure_probability):
    """
    Returns machine health details based on failure probability.
    """

    score = calculate_health_score(failure_probability)

    if score >= 80:
        return {
            "health_score": score,
            "risk_level": "Low",
            "status": "Healthy",
            "color": "green",
            "recommendation": "Machine is operating normally."
        }

    elif score >= 60:
        return {
            "health_score": score,
            "risk_level": "Medium",
            "status": "Monitor",
            "color": "yellow",
            "recommendation": "Inspect the machine during the next maintenance cycle."
        }

    elif score >= 40:
        return {
            "health_score": score,
            "risk_level": "High",
            "status": "Warning",
            "color": "orange",
            "recommendation": "Schedule maintenance as soon as possible."
        }

    else:
        return {
            "health_score": score,
            "risk_level": "Critical",
            "status": "Critical",
            "color": "red",
            "recommendation": "Stop the machine immediately and perform maintenance."
        }