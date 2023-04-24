#!/usr/bin/python3
"""
This module provides functions to read and write CSV files.

Functions:
    read_csv: Read data from a CSV file.
    write_csv: Write data to a CSV file.
"""
import csv

def read_csv(filename):
    """
    Read data from a CSV file and return a list of dictionaries.
    
    Args:
        filename (str): Name of the CSV file to read.
    
    Returns:
        list: List of dictionaries where each dictionary represents a row of data.
    """
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def write_csv(filename, data):
    """
    Write data to a CSV file.
    
    Args:
        filename (str): Name of the CSV file to write.
        data (list): List of dictionaries where each dictionary represents a row of data.
    """
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
