class analyzer:
    def __init__(self, data):
        self.data = data

    def compute_metrics(self):
        if not self.data:
            return {
                "total_revenue": 0,
                "average_revenue": 0,
                "status_counts": {}
            }

        total_revenue = 0
        paid_count = pending_count = refunded_count = 0

        for record in self.data:
            total = record.get("total", 0)
            total_revenue += total

            status = record.get("payment_status", "").lower()
            if status == "paid":
                paid_count += 1
            elif status == "pending":
                pending_count += 1
            elif status == "refunded":
                refunded_count += 1

        average_revenue = total_revenue / len(self.data)

        return {
            "total_revenue": round(total_revenue, 2),
            "average_revenue": round(average_revenue, 2),
            "status_counts": {
                "paid": paid_count,
                "pending": pending_count,
                "refunded": refunded_count
            }
        }
