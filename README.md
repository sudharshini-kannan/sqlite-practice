# SQLite Practice – Bioinformatics Data Queries

## Overview
This repository contains structured SQL practice exercises focused on biological datasets. 
The project demonstrates database creation, data insertion, filtering, aggregation, grouping, and joining tables using SQLite.

## Technologies Used
- SQLite
- SQL
- Ubuntu (Linux Command Line)
- Git & GitHub

## Project Structure
- sql_practice.sql → Contains table creation, insert statements, and analytical queries
- .gitignore → Ignores database files (*.db)

## Concepts Practiced
- CREATE TABLE
- INSERT INTO
- SELECT
- WHERE filtering
- GROUP BY
- HAVING
- ORDER BY
- LIMIT
- JOIN operations
- Aggregate functions (COUNT, AVG)

## Sample Use Case
The dataset simulates gene metadata and experiment results. 
Queries were written to:
- Filter genes by species
- Calculate average gene length
- Compute GC content statistics
- Count genes per species
- Join gene and experiment tables

## Purpose
This project demonstrates foundational SQL skills relevant for bioinformatics, data analysis, and research roles.

Python Automation & Data Export

In addition to writing SQL queries manually in SQLite, this project demonstrates how to automate database analysis using Python.

Objective

To connect a SQLite database to Python, execute analytical queries, and export structured results for reporting.

Workflow

Connect to SQLite database (genes.db) using sqlite3

Execute SQL query inside Python

Load results into a pandas DataFrame

Export results as a CSV file for reporting

SQL Query Used
SELECT species, AVG(length) AS avg_length
FROM genes
GROUP BY species;

Result

The query calculates the average gene length for each species in the dataset.

