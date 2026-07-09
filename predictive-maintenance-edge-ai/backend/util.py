from datetime import datetime

def get_current_timestamp():
    """
    Returns the current date and time.
    """
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
