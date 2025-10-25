import json
import os

class Reader:
    """Simple JSON reader for the pipeline."""

    def __init__(self, filepath: str):
        self.filepath = filepath

    def read(self):
        # file exists?
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File not found: {self.filepath}")

        # only accept .json files
        if not self.filepath.lower().endswith(".json"):
            raise ValueError("Unsupported file format. Only .json is supported.")

        # read and parse
        with open(self.filepath, "r", encoding="utf-8") as fh:
            try:
                data = json.load(fh)
            except json.JSONDecodeError as exc:
                raise ValueError("Invalid JSON file.") from exc

        # empty data check
        if not data:
            raise ValueError("File is empty or contains no records.")

        # ensure it's a list of dicts
        if not isinstance(data, list):
            raise ValueError("Expected a JSON array (list) of records.")

        return data
