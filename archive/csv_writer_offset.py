
import json
import csv

def convert_fixed_width_to_csv(json_spec_file, input_file, output_csv):
    # Read JSON specification
    with open(json_spec_file, 'r') as f:
        spec = json.load(f)
    
    column_names = spec["ColumnNames"]
    offsets = list(map(int, spec["Offsets"]))
    fixed_width_encoding = spec["FixedWidthEncoding"]
    include_header = spec["IncludeHeader"] == "True"
    delimited_encoding = spec["DelimitedEncoding"]
    
    # Read fixed-width file and parse data
    records = []
    with open(input_file, 'r', encoding=fixed_width_encoding) as file:
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

# Example usage
convert_fixed_width_to_csv('spec.json', 'fixed_width.txt', 'output.csv')
