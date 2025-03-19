# amit-kyruushealth-data-engineer-test

# Python-interview

## Overview
Thank you for your interest and investing your time in working on this excercise. Our team appreciates it!

This assignment has 4 parts. Please only complete the parts you were asked to.

This assesment is meant to both get a view into your approach of solving problems as well as your technical skills that will be required on your
day to day job. It is meant to test knowledge of the following areas:

* development skills
* System design approach

In some cases instructions are purposefully short, so you may need to research how to do what is asked if you do not already know.

The code will be evaluated on the following criteria, in order of significance
* Correctness
* Readability and maintainability
* Software development best practices.
* Code documentation, clarity and ease of use
* Extensibility
* Performance

Candidates will be expected to talk to and explain their work in a follow up discussion.

## Dependencies Setup
It is assumed this excercise will be solved with the pyhton prograqmming languague, so you will need sdk installed.


## Project Setup

1. Clone the repo and setup your environment.
2. Document in the DEV.md file how the environment should be setup in order for us to run your solution.
3. Create a directory for each solution, ie solution1, solution2 etc.


## Exercises

Before starting the exercises create a new branch called `feature/exercises` 
and commit all subsequent code to that branch

For each exercise please make exactly 1 commit with a message describing the contents of the exercise. It is important to follow instructions
as we may run automated evaludation of your solution.

### Background
You are a recently hired engineer at a newly established StartUp: "TheBetterName". Our compmany provides name services to different organizations.

The National Security Administration publishes a list of the most popular baby names in the United States by year. This is provided to the public [here](https://www.ssa.gov/oact/babynames/limits.html).

Please navigate to that above link and study this dataset as we will be using it during our excercise.

### 1. Popular Name
Create a program that will produce the most popular baby name for a period.


The input is two arguments: ```<start-year> <end-year>```
Output: The most popular Male and Female baby names over this period (inclusive)
        The output should be just one line in the following format: "M: <name> F:<name>"

### 1.1 Popular Name SQL
Write a SQL query for the simple name prediction(question above). 
The query should take two arguments: ```<start-year> <end-year>```

### 2. Geo service
Our company is now working with a national insurance company called "InsureElite". The insurance company has business units that operate in different geographical areas.
In this task we want you to write a program that calculates the most popular name for each business unit.

The input is a path to a json file. This file is in the format:
```
{
  "input": [
    {
      "name": "Business Unit 1",
      "states": [
        "OH",
        "NY"
      ]
    },
    {
      "name": "Business Unit 2",
      "states": [
        "CA"
      ]
    }
  ]
}
```

The output: a json file, named `solution2.json` in this format:

```
{
  "output": [
    {
      "name": "Business Unit 1",
      "Male": "John",
      "Female": "Jane"
    },
    {
      "name": "Business Unit 2",
      "Male": "Johnny",
      "Female": "Gale"
    }
  ]
}
```

### 3. Overlap
Following our very succesful cooperation with "InsureElite" they have requested a more complex feature implemented from our system.
In this fictional scenario we are assuming a business unit will support a set of individuals. Those are individuals with specific names.
For this excercise we want to know for each given state which business unit can serve them best. That is by covering the largest number of customers.

Input: Path to a json file. The file will be in the format:

```
{
    [
        {
            "name": "Business Unit 1",
            "names": ["John", "Bob"]
        },
        {
            "name": "Business Unit 2",
            "names": ["Dave", "Brook"]
        }
    ]
}
```

Output: A path to a json file in the format:
```
{
    [
        {
            "name": "Business Unit 1",
            "states": ["OH", "NY"]
        },
        {
            "name": "Business Unit 2",
            "names": ["KS"]
        }
    ]
}
```

### 4. Naming system
This part of the excercise is a design portion and does not require writing code. If you choose to are free to provide code samples to show your design.
Our company has made a great progress and has become a national brand. We are now partnering with the SSA to get a daily feed of popular baby names.

This excercise has two parts (which are strongly coupled together):

1. Design and write a technical documentation for the SSA engineers to follow in order to provide the feed our company will need in order to know poular baby names in "Near Real Time"
2. Design a system in which our company knows the popular baby names in the population in "Near Real Time".

This design solution should outline the data ingestion, transformation, loading components and visualization as base requirement. Please add any other components that you see fit.

