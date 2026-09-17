from pathlib import Path


def file_exists(path: str) -> bool:
    """Return True if the given file exists."""
    return Path(path).is_file()


def read_file(path: str) -> str:
    """Read and return the content of a text file."""
    return Path(path).read_text(encoding="utf-8")


def write_file(path: str, content: str) -> str:
    """Write content to a text file."""
    Path(path).write_text(content, encoding="utf-8")
    return f"File written successfully: {path}"


def list_files(path: str) -> list[str]:
    """Return the files contained in a directory."""
    directory = Path(path)

    return [
        item.name
        for item in directory.iterdir()
        if item.is_file()
    ]