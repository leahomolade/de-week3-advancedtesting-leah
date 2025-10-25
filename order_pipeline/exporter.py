import json

class Exporter:
    def __init__(self, output_file):
        self.output_file = output_file

    def export_data(self, data):
        try:
            with open(self.output_file, 'w') as file:
                json.dump(data, file, indent=4)
            return True
        except Exception as e:
            print(f"Error exporting data: {e}")
            return False
