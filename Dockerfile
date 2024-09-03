# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script and any necessary files to the container
COPY parser_clean.py .
COPY fixed_width.txt /app/input_width.txt
COPY spec.json /app/spec.json
COPY output.csv /app/output.csv

# Copy the requirements file and install dependencies if you have one
# Uncomment the following lines if you have a requirements.txt file
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

## Make sure your script uses argparse or similar to handle command-line arguments
ENTRYPOINT ["python", "parser_clean.py"]

# Specify the default command
#CMD ["python", "parser_clean.py", "spec.json", "input_width.txt", "output.csv"]
