from order_pipeline.reader import Reader
from order_pipeline.validator import Validator
from order_pipeline.analyzer import Analyzer
from order_pipeline.exporter import Exporter

class Pipeline:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def run(self):
        reader = Reader(self.input_file)
        data = reader.read()

        validator = Validator()
        if not validator.validate(data):
            print("Validation failed. Exiting pipeline.")
            return None

        analyzer = Analyzer(data)
        results = analyzer.compute_metrics()

        exporter = Exporter(self.output_file)
        exporter.export_data(results)

        print("Pipeline completed successfully.")
        return results
