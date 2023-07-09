# US State Population Lookup
Lets the user look up population data for US states.

## Overview
This program presents population data from the USDA to the user. The user has 3 ways to look up state population:
- Show states and population for a specific year, sorted by population
- Show states with positive or negative growth rate, sorted by state name
- Show whether there is a drop in state population between 2 years.

## Program Files
The program consists of the following files:
- This README file has general information
- `lab1.docx` contains the program specs and requirements
- `statesPop.csv` has [population data from the USDA](https://data.ers.usda.gov/reports.aspx?ID=17827)
- `states.py` has the back end code to access the data in the USDA file
- `ui.py` presents a menu to the user and displays the population data based on the user's choice.
Running the program creates an additional file:
- `logfile.txt` logs the back end function calls and results.

## Downloading Running the Program
The program requires that python already be installed on your local machine. If you do not have python installed, you can download the latest version from [python.org]((https://www.python.org/downloads/).

Download `us_state_pop_lookup.zip`, an archive of the entire repo for easy local installation. At the command line prompt, type `python ui.py` to launch the program. On some systems, you may instead need to type `python3 ui.py` at the command line prompt.

## Credits
- Lab 1 for CIS 41B, De Anza College, Spring 2023
- Professor: Clare Nguyen
- Author: Surajit A. Bose, copyright © 2023. 
