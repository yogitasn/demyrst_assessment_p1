Steps to run docker image
docker build -t parser_clean .
docker run --rm -v C:/demyrst_assessment_p1/spec.json:/app/spec.json -v C:/demyrst_assessment_p1/fixed_width.txt:/app/fixed_width.txt -v C:/demyrst_assessment_p1/output.csv:/app/output.csv parser_clean /app/spec.json /app/fixed_width.txt /app/output.csv
docker run -it --rm -v C:/demyrst_assessment_p1:/app python:3.9-slim /bin/bash
 
Fixed_width.txt
 
Output.csv
 
