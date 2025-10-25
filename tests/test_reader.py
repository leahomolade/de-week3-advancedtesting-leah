import sys
import os

# Ensure the parent directory (project root) is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import pytest
from order_pipeline.reader import Reader

def test_read_valid_file(tmp_path):
    # create a small JSON list file
    p = tmp_path / "sample.json"
    content = [
        {"order_id": "ORD1", "item": "A", "quantity": 1, "price": "$10", "total": "$10", "payment_status": "paid"}
    ]
    p.write_text(json.dumps(content), encoding="utf-8")

    r = Reader(str(p))
    data = r.read()
    assert isinstance(data, list)
    assert data[0]["order_id"] == "ORD1"

def test_read_unsupported_format(tmp_path):
    p = tmp_path / "sample.txt"
    p.write_text("not json")
    r = Reader(str(p))
    with pytest.raises(ValueError):
        r.read()

def test_read_missing_file(tmp_path):
    p = tmp_path / "does_not_exist.json"
    r = Reader(str(p))
    with pytest.raises(FileNotFoundError):
        r.read()

def test_read_empty_json(tmp_path):
    p = tmp_path / "empty.json"
    p.write_text("[]", encoding="utf-8")
    r = Reader(str(p))
    with pytest.raises(ValueError):
        r.read()

def test_read_invalid_json(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("{ invalid json }", encoding="utf-8")
    r = Reader(str(p))
    with pytest.raises(ValueError):
        r.read()
