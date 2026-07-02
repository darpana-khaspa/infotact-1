def calculate_health_score(failure_probability):
    """
    Converts failure probability into a machine health score.

    failure_probability should be between 0 and 1.
    Example: 0.25 means 25% failure risk.
    """

    failure_probability = max(0, min(1, failure_probability))

    health_score = (1 - failure_probability) * 100

    return round(health_score, 2)


def get_health_status(health_score):
    """
    Returns machine health status based on health score.
    """

    if health_score >= 80:
        return "Healthy"

    elif health_score >= 60:
        return "Moderate"

    elif health_score >= 40:
        return "Warning"

    else:
        return "Critical"