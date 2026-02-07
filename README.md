# data-pipeline-python

This repository contains a simple example of a data pipeline built with Python.

## What it does
- Reads data from a CSV file (`dados.csv`)
- Filters records where the `valor` field is greater than 10
- Writes the filtered data to a new CSV file (`filtered_data.csv`)

## Technologies used
- Python
- Standard Python `csv` library

## How to run
1. Clone the repository:
   git clone https://github.com/lucascarvalho009/data-pipeline-python.git

2. Make sure the `data.csv` file is in the same directory (a sample file is included).

3. Run the script:
   python etl.py

After execution, a new file called `filtered_data.csv` will be generated with the filtered results.

## Purpose
This project demonstrates basic ETL concepts, data transformation, and automation using Python. It was created as a hands-on practice project.

