# parser.py
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

import io
import re
import argparse
import json
import csv
import logging
import unittest


def parse_spec(spec):
    column_names = []
    offsets = []
    include_header = False
    fixed_width_encoding = None
    delimited_encoding = None

    try:
        # Read JSON specification
        with open(spec, 'r') as f:
            spec = json.load(f)
        
        column_names = spec["ColumnNames"]
        offsets = list(map(int, spec["Offsets"]))
        fixed_width_encoding = spec["FixedWidthEncoding"]
        include_header = spec["IncludeHeader"] == "True"
        delimited_encoding = spec["DelimitedEncoding"]

        return (
            column_names,
            offsets,
            include_header,
            fixed_width_encoding,
            delimited_encoding,
        )

    except Exception as err:
        logging.error('Cannot parse the spec')
        logging.error(err)


def run(spec, inputfile, output_csv):

    column_names, offsets, include_header, fixed_width_encoding, delimited_encoding = parse_spec(spec)

    # Read fixed-width file and parse data
    try:
        records = []
        with open(inputfile, 'r', encoding=fixed_width_encoding) as file:
            for line in file:
                record = []
                pos = 0
                for width in offsets:
                    record.append(line[pos:pos + width].strip())
                    pos += width
                records.append(record)
        
        # Write to CSV file
        with open(output_csv, 'w', newline='', encoding=delimited_encoding) as csvfile:
            writer = csv.writer(csvfile)
            if include_header:
                writer.writerow(column_names)
            writer.writerows(records)
    
    except Exception as err:
        logging.error('File IO error')
        logging.error(err)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Text to csv')
    parser.add_argument('spec', metavar='F', type=str, help='spec')
    parser.add_argument('file', metavar='F', type=str, help='textfile')
    parser.add_argument('output_csv', metavar='F', type=str, help='output_csv')
    args = parser.parse_args()
    spec = args.spec
    file = args.file
    output_csv = args.output_csv
    run(spec, file,output_csv)

# Example usage
#convert_fixed_width_to_csv('spec.json', 'fixed_width.txt', 'output1.csv')
