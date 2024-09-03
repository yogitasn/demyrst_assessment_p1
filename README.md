# demyrst_assessment_p1

## Project Name
# Overview
This project involves using Docker to build and run a containerized application. Below are the steps to build the Docker image, run the container, and interact with it.

## Prerequisites
Docker installed on your machine
Basic understanding of Docker commands

## Building the Docker Image
# Build the Docker Image

To build the Docker image, use the following command:
``` docker build -t parser_clean . ```

This command builds the Docker image and tags it as parser_clean

## Running the Docker Container
# Run the Container with Volume Mounts

To run the container and mount local files into it, use:

``` docker run --rm C:/demyrst_assessment_p1/spec.json:/app/spec.json C:/demyrst_assessment_p1/fixed_width.txt:/app/fixed_width.txt C:/demyrst_assessment_p1/output.csv:/app/output.csv parser_clean /app/spec.json /app/fixed_width.txt /app/output.csv ``` 

This command mounts the spec.json, fixed_width.txt, and output.csv files from your local machine into the /app directory in the container and then executes the parser_clean script with these files as arguments.

Here's what this command does:

--rm: Automatically removes the container after it exits.
-v C:/demyrst_assessment_p1/spec.json:/app/spec.json: Mounts the local spec.json file to the container.
-v C:/demyrst_assessment_p1/fixed_width.txt:/app/fixed_width.txt: Mounts the local fixed_width.txt file to the container.
-v C:/demyrst_assessment_p1/output.csv:/app/output.csv: Mounts the local output.csv file to the container.
parser_clean: Specifies the image to use.
/app/spec.json /app/fixed_width.txt /app/output.csv: Passes the arguments to the parser_clean command inside the container.


## Run the Container in Interactive Mode

If you need to interact with the container or debug, you can start an interactive shell session:

``` docker run -it --rm C:/demyrst_assessment_p1:/app python:3.9-slim /bin/bash ```his command does the following:

-it: Runs the container in interactive mode with a terminal.
--rm: Automatically removes the container after you exit.
-v C:/demyrst_assessment_p1:/app: Mounts the local directory to the container.
python:3.9-slim: Uses the official Python 3.9 slim image.
/bin/bash: Starts a bash shell inside the container.

## Files Involved
spec.json: Specification file for parsing.
fixed_width.txt: Input data file.
output.csv: Output file where the parsed data will be written.

## Notes
Ensure Docker is installed and running on your machine before executing these commands.
Adjust file paths (C:/demyrst_assessment_p1/) according to your local setup.
Using --rm ensures that the container is cleaned up after execution, which helps in managing disk space and container clutter.
Troubleshooting
If you encounter issues, verify the following:

## Docker installation and configuration are correct.
File paths are correct and accessible.
The Docker image builds and runs without errors.
For further assistance, consult the Docker documentation or review the Dockerfile and any related scripts included in the project.