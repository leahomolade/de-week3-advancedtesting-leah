import pytest
from order_pipeline.validator import Validator

@pytest.fixture
def schema():
    return {"id": int, "customer": str, "amount": float}

@pytest.fixture
def valid_data():
    return [
        {"id": 1, "customer": "Alice", "amount": 200.0},
        {"id": 2, "customer": "Bob", "amount": 150.5},
    ]

def test_valid_data(schema, valid_data):
    validator = Validator(schema)
    assert validator.validate(valid_data) == True

def test_missing_field(schema):
    validator = Validator(schema)
    invalid_data = [{"id": 1, "customer": "Alice"}]
    with pytest.raises(ValueError, match="Missing required field"):
        validator.validate(invalid_data)

def test_wrong_type(schema):
    validator = Validator(schema)
    invalid_data = [{"id": "1", "customer": "Alice", "amount": 200.0}]
    with pytest.raises(TypeError, match="must be of type int"):
        validator.validate(invalid_data)
