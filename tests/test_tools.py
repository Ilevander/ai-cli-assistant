from datetime import datetime

from ai_assistant.tools.datetime import (
    get_current_date,
    get_current_datetime,
    get_current_time,
    get_day_of_week,
)


def test_get_current_datetime():
    result = get_current_datetime()

    datetime.strptime(result, "%Y-%m-%d %H:%M:%S")


def test_get_current_date():
    result = get_current_date()

    datetime.strptime(result, "%Y-%m-%d")


def test_get_current_time():
    result = get_current_time()

    datetime.strptime(result, "%H:%M:%S")


def test_get_day_of_week():
    result = get_day_of_week()

    assert result in [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]