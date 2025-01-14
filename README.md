# HW1 for ChemE 545 WI25 Class

This repository contains python files for the first Homework in ChemE 545: Data Science Methods for Molecular Science and Engineering.

# Index

- extract_parameter.py: Contains a function that takes a unit_operations_data dictionary and extracts the value of different parameters (passed as arguments to the function).
- calculate_solution_weights.py: Contains a function that takes a molecular_weights dictionary and a solutions_needed list and returns a modified solutions_needed list which included the weight of the compound in a 1 litre solution in grams.
- README.md: The file you're reading right now!
- .gitignore: File telling git to ignore some files

# Usage

In order to use the python files in this repository, you will first need to clone the repo:

```{shell}
git clone git@github.com:Braden-Griebel/CHEME545_WI25_HW1_Griebel_Braden.git
```

Then you can create a new python file in the directory, and import the files
in order to use the functions (or append the directory to the PYTHONPATH environment variable).

```{python}
from extract_parameter import extract_parameter
from calculate_solution_weights import calculate_solution_weights

# Testing
# Good Cases
print(extract_parameter("distillation_column", "temperature", 1))
print(extract_parameter("reactor", "pressure", 2))
# Error cases
print(extract_parameter("distillation_column", "entropy", 2)) # Invalid parameter_name
print(extract_parameter("reactor", "pressure", 5)) # Invalid index
print(extract_parameter("mixer", "pressure", 0)) # Invalid unit_name

# Define the molecular_weights dictionary
molecular_weights = {
    'NaCl': 58.44,
    'H2SO4': 98.079,
    'NaOH': 40.00,
    'KMnO4': 158.034,
    'CH3COOH': 60.052
}

# Define the solutions_needed list
solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']

calculate_solution_weights(molecular_weights= molecular_weights, solutions_needed= solutions_needed)
```

Another python file has been provided that does the above for the default values,
called test.py which can be run by calling

```{shell}
python test.py
```

```

```
