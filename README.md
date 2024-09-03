# demyrst_assessment_p1

## Problem1: Parse fixed width file
- Generate a fixed width file using the provided spec.
- Implement a parser that can parse the fixed width file and generate a csv file.
- DO NOT use pre built python libraries like pandas for parsing. You can use a library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding

## Project Name
# Overview
This project involves using Docker to build and run a containerized application. Below are the steps to build the Docker image, run the container, and interact with it.

## Prerequisites
Docker installed on your machine
Basic understanding of Docker commands

## Steps to build Docker Image
# 1. Build the Docker Image

To build the Docker image for data parsing, use the following command:

``` docker build -t parser_clean . ```

This command builds the Docker image and tags it as parser_clean

## 2. Run the Docker Container for Data Parsing

After building the image, you can run the Docker container to perform the data parsing. Use the following command:

``` docker run --rm C:/demyrst_assessment_p1/spec.json:/app/spec.json C:/demyrst_assessment_p1/fixed_width.txt:/app/fixed_width.txt C:/demyrst_assessment_p1/output.csv:/app/output.csv parser_clean /app/spec.json /app/fixed_width.txt /app/output.csv ``` 

Here's what this command does:

* --rm: Automatically removes the container after it exits.
* -v C:/demyrst_assessment_p1/spec.json:/app/spec.json: Mounts the local spec.json file to the container.
* -v C:/demyrst_assessment_p1/fixed_width.txt:/app/fixed_width.txt: Mounts the local fixed_width.txt file to the container.
* -v C:/demyrst_assessment_p1/output.csv:/app/output.csv: Mounts the local output.csv file to the container.
parser_clean: Specifies the image to use.
/app/spec.json /app/fixed_width.txt /app/output.csv: Passes the arguments to the parser_clean command inside the container.


## 3. Access an Interactive Python Environment (Optional)

If you need to interact with the container or debug, you can start an interactive shell session:

``` docker run -it --rm C:/demyrst_assessment_p1:/app python:3.9-slim /bin/bash ```

This command does the following:

* -it: Runs the container in interactive mode with a terminal.
* --rm: Automatically removes the container after you exit.
* -v C:/demyrst_assessment_p1:/app: Mounts the local directory to the container.
* python:3.9-slim: Uses the official Python 3.9 slim image.
* /bin/bash: Starts a bash shell inside the container.

## Files Involved
* spec.json: Specification file for parsing.
* fixed_width.txt: Input data file.
* output.csv: Output file where the parsed data will be written.

## Notes
* Ensure Docker is installed and running on your machine before executing these commands.
* `output.csv` starts as an empty file. On a local machine, the Python script automatically creates and writes to this file. However, when running the script inside a Docker container, the file is not created automatically. Therefore, you need to manually create an empty `output.csv` file before running the script in the Docker container. The script will then write the results to this file as expected. Please refer to the screenshot for the output results in the file.
* Adjust file paths (C:/demyrst_assessment_p1/) according to your local setup.
* Using --rm ensures that the container is cleaned up after execution, which helps in managing disk space and container clutter.

## Troubleshooting
If you encounter issues, verify the following:

* Docker installation and configuration are correct.
* File paths are correct and accessible.
* The Docker image builds and runs without errors.


For further assistance, consult the Docker documentation or review the Dockerfile and any related scripts included in the project.