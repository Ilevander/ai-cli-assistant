from datetime import datetime


def get_current_datetime() -> str:
    """Return the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_current_date() -> str:
    """Return the current date."""
    return datetime.now().strftime("%Y-%m-%d")


def get_current_time() -> str:
    """Return the current time."""
    return datetime.now().strftime("%H:%M:%S")


def get_day_of_week() -> str:
    """Return the current day of the week."""
    return datetime.now().strftime("%A")