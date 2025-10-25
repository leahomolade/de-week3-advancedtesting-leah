import re
from datetime import datetime

class Transformer:
    def __init__(self, data):
        self.data = data

    def clean_currency(self, value):
        """Convert price strings like '$15.99', 'N2000', '45 dollars' → float"""
        if isinstance(value, (int, float)):
            return float(value)
        if not isinstance(value, str):
            return None

        value = value.lower().replace("usd", "").replace("dollars", "").replace("n", "").replace("$", "").strip()
        try:
            return float(value)
        except ValueError:
            return None

    def standardize_timestamp(self, ts):
        """Convert all timestamps into ISO format (YYYY-MM-DDTHH:MM:SSZ)"""
        formats = [
            "%Y-%m-%dT%H:%M:%SZ",
            "%Y-%m-%d %H:%M",
            "%d/%m/%Y %I:%M %p",
            "%Y/%m/%dT%H:%MZ"
        ]
        for fmt in formats:
            try:
                dt = datetime.strptime(ts, fmt)
                return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            except Exception:
                continue
        return None

    def transform(self):
        """Clean and standardize all data fields"""
        cleaned = []
        for record in self.data:
            item = record.get("item") or "Unknown Item"
            quantity = record.get("quantity")
            if isinstance(quantity, str):
                quantity = re.sub(r"\D", "", quantity)  # remove non-digit
            try:
                quantity = int(quantity)
            except Exception:
                quantity = None

            cleaned_record = {
                "order_id": record.get("order_id"),
                "timestamp": self.standardize_timestamp(record.get("timestamp", "")),
                "item": item.strip(),
                "quantity": quantity,
                "price": self.clean_currency(record.get("price")),
                "total": self.clean_currency(record.get("total")),
                "payment_status": record.get("payment_status", "").lower()
            }
            cleaned.append(cleaned_record)
        return cleaned
