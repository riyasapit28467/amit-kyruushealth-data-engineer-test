# Development Guide

Welcome to the project! This document provides guidelines for developers contributing to this project.

## Table of Contents

1. [Background](#background)
2. [Getting Started](#getting-started)
3. [Installation](#installation)
4. [Development Workflow](#development-workflow)
5. [Testing](#testing)


## Background

The National Security Administration publishes a list of the most popular baby names in the United States by year. This is provided to the public here.

This project is designed to analyze and visualize baby name data from various sources. It is built with Python and utilizes libraries.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/riyasapit28467/amit-kyruushealth-data-engineer-test
cd amit-kyruushealth-data-engineer-test


```
### Test solution1
```bash
cd solution1
python migration.txt
```

```bash 
cd solution1
python -m venv venv_name
venv_name\Scripts\activate (windows)
source venv_name/bin/activate (linux,mac)
pip3 install -r .\requirement.txt
python solution1.py
```

```test
curl "http://127.0.0.1:5000/getPopularNames?start_year=3000&end_year=2022"
````

Enter the start and end year

### Test solution2

```bash 
cd solution2
python names_by_business_unit.py

```
get the output.json in solution2 folder

### Test solution3

```bash 
cd solution3
python state_by_popular_names.py

```
get the output.json in solution3 folder