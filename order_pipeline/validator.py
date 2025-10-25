import json

class Validator:
    def __init__(self, schema):
        self.schema = schema

    def validate(self, data):
        """Validate that data conforms to the schema."""
        if not isinstance(data, list):
            raise ValueError("Data must be a list of records")

        for record in data:
            for field, field_type in self.schema.items():
                if field not in record:
                    raise ValueError(f"Missing required field: {field}")
                if not isinstance(record[field], field_type):
                    raise TypeError(f"Field {field} must be of type {field_type.__name__}")
        return True
