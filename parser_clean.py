#!/usr/bin/python3
"""
## Judgment Criteria
- Beauty of the code (beauty lies in the eyes of the beholder)
- Testing strategies
- Basic Engineering principles
## Parse fixed width file
- Generate a fixed width file using the provided spec.
- Implement a parser that can parse the fixed width file and generate a csv file.
- DO NOT use pre built python libraries like pandas for parsing. You can use a library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding
## Sample spec file (json file)
{
    "ColumnNames":"f1, f2, f3, f4, f5, f6, f7, f8, f9, f10",
    "Offsets":"3,12,3,2,13,1,10,13,3,13",
    "InputEncoding":"windows-1252",
    "IncludeHeader":"True",
    "OutputEncoding":"utf-8"
}
"""

import json
import csv
import logging
import argparse

class Parser:
    def __init__(self, spec_file):
        self.spec_file = spec_file
        self.column_names = []
        self.offsets = []
        self.include_header = False
        self.fixed_width_encoding = 'utf-8'
        self.delimited_encoding = 'utf-8'
        self._load_specification(spec_file)

    def _load_specification(self, spec_file):
        """Load and parse the JSON specification."""
        column_names = []
        offsets = []
        include_header = False
        fixed_width_encoding = None
        delimited_encoding = None

        try:
            # Read JSON specification
            with open(spec_file, 'r') as f:
                spec = json.load(f)
            
            self.column_names = spec["ColumnNames"]
            self.offsets = list(map(int, spec["Offsets"]))
            self.fixed_width_encoding = spec["FixedWidthEncoding"]
            self.include_header = spec["IncludeHeader"] == "True"
            self.delimited_encoding = spec["DelimitedEncoding"]

            return (
                self.column_names,
                self.offsets,
                self.include_header,
                self.fixed_width_encoding,
                self.delimited_encoding,
            )

        except Exception as err:
            logging.error('Cannot parse the spec')
            logging.error(err)


    def parse_fixed_width_file(self, spec, input_file):
        """Parse the fixed-width file into a list of records."""

        self.column_names, self.offsets, self.include_header, self.fixed_width_encoding, self.delimited_encoding = self._load_specification(spec)

        records = []
        try:
            with open(input_file, 'r', encoding=self.fixed_width_encoding) as file:
                for line in file:
                    record = []
                    pos = 0
                    for width in self.offsets:
                        record.append(line[pos:pos + width].strip())
                        pos += width
                    records.append(record)
        except Exception as e:
            logging.error('Error reading fixed-width file')
            logging.error(e)
            raise
        return records

    def write_csv(self, records, output_file):
        """Write records to a CSV file."""
        try:
            with open(output_file, 'w', newline='', encoding=self.delimited_encoding) as csvfile:
                writer = csv.writer(csvfile)
                if self.include_header:
                    writer.writerow(self.column_names)
                writer.writerows(records)
        except Exception as e:
            logging.error('Error writing CSV file')
            logging.error(e)
            raise

    def convert(self, spec, input_file, output_file):
        """Convert the fixed-width file to a CSV file."""
        records = self.parse_fixed_width_file(spec, input_file)
        self.write_csv(records, output_file)

    @staticmethod
    def main():
        """Command-line interface for the parser."""
        parser = argparse.ArgumentParser(description='Convert a fixed-width file to CSV.')
        parser.add_argument('spec', metavar='SPEC', type=str, help='Path to the specification JSON file.')
        parser.add_argument('input_file', metavar='INPUT', type=str, help='Path to the fixed-width input file.')
        parser.add_argument('output_file', metavar='OUTPUT', type=str, help='Path to the output CSV file.')
        args = parser.parse_args()

        # Create a Parser instance and perform the conversion
        try:
            parser = Parser(args.spec)
            parser.convert(args.spec, args.input_file, args.output_file)
        except Exception as e:
            logging.error('Conversion failed')
            logging.error(e)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    Parser.main()
