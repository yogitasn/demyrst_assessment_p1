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


def split_line_by_fixed_widths(textline = '', offsets = []):
    line = textline
 
    record = []
    pos = 0
    for width in offsets:
        record.append(line[pos:pos + width].strip())
        pos += width
   
    print(record)
    return record


def parse_spec(spec):
    column_names = []
    offsets = []
    include_header = False
    input_encoding = None
    output_encoding = None

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



def run(spec, inputfile):

    column_names, offsets, include_header, fixed_width_encoding, delimited_encoding = parse_spec(spec)

    try:
        with open('result.csv', 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')

             # Read fixed-width file and parse data
            records = []
 
            with open(inputfile, 'r', encoding=fixed_width_encoding) as file:
                for line_index, line in enumerate(f.readlines()):

                    if line_index == 1 or len(line) == 0:
                        continue

                    splitted_line = split_line_by_fixed_widths(line, offsets)
                    records.append(splitted_line)
                    print(splitted_line)
                    writer.writerow(splitted_line)

            # Write to CSV file
            with open('output_csv', 'w', newline='', encoding=delimited_encoding) as csvfile:
                writer = csv.writer(csvfile)
                if include_header:
                    writer.writerow(column_names)
                writer.writerows(records)

    
        csv_file.close()
    except Exception as err:
        logging.error('File IO error')
        logging.error(err)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Text to csv')
    parser.add_argument('spec', metavar='F', type=str, help='spec')
    parser.add_argument('file', metavar='F', type=str, help='textfile')
    args = parser.parse_args()
    spec = args.spec
    file = args.file
    run(spec, file)

    
# parser_test.py
import unittest
from parser import *


class MyTest(unittest.TestCase):

    def test_split_line(self):
        
        line = "abcd efgh 1123"
        offsets = [4, 9, 14]
        expected = ['abcd', 'efgh', '1123']
        print("Start Test 1")
        print(split_line_by_fixed_widths(line, offsets))
        self.assertEqual(split_line_by_fixed_widths(line, offsets), expected)

    def test_split_line_with_empty_value(self):
        line = "abcd efgh 1123   "
        offsets = [4, 9, 14, 17]
        expected = ['abcd', 'efgh', '1123', '_']
        print("Start Test 2")
        print(split_line_by_fixed_widths(line, offsets))
        self.assertEqual(split_line_by_fixed_widths(line, offsets), expected)

        line = "abcd efgh    1123"
        offsets = [4, 9, 12, 17]
        expected = ['abcd', 'efgh', '_', '1123']
        print("Start Test 3")
        print(split_line_by_fixed_widths(line, offsets))
        self.assertEqual(split_line_by_fixed_widths(line, offsets), expected)


if __name__ == '__main__':
    unittest.main()