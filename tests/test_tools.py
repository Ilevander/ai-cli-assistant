from datetime import datetime

from ai_assistant.tools.datetime import (
    get_current_date,
    get_current_datetime,
    get_current_time,
    get_day_of_week,
)

from ai_assistant.tools.files import (
    file_exists,
    list_files,
    read_file,
    write_file,
)

# Datetime tool
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

# Files tool
def test_file_exists(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello", encoding="utf-8")

    assert file_exists(str(file))


def test_read_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello", encoding="utf-8")

    assert read_file(str(file)) == "Hello"


def test_write_file(tmp_path):
    file = tmp_path / "test.txt"

    result = write_file(str(file), "Hello")

    assert file.read_text(encoding="utf-8") == "Hello"
    assert result == f"File written successfully: {file}"


def test_list_files(tmp_path):
    file1 = tmp_path / "one.txt"
    file2 = tmp_path / "two.txt"

    file1.write_text("One", encoding="utf-8")
    file2.write_text("Two", encoding="utf-8")

    result = list_files(str(tmp_path))

    assert sorted(result) == ["one.txt", "two.txt"]