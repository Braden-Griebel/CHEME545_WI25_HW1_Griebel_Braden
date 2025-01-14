# Import the functions from the other files
from extract_parameter import extract_parameter
from calculate_solution_weights import calculate_solution_weights

# Define the unit_operations_data nested dictionary
unit_operations_data = {
    "distillation_column": {
        "temperature": [150, 160, 170],
        "pressure": [2, 2.5, 3],
        "flow_rate": [100, 110, 120],
    },
    "reactor": {
        "temperature": [250, 260, 270],
        "pressure": [5, 5.5, 6],
        "residence_time": [10, 12, 14],
    },
    "heat_exchanger": {
        "temperature_in": [80, 90, 100],
        "temperature_out": [50, 60, 70],
        "flow_rate": [200, 210, 220],
    },
}

# Testing the unit_operations_data function
# Good Cases
print(extract_parameter("distillation_column", "temperature", 1))
print(extract_parameter("reactor", "pressure", 2))
# Error cases
print(extract_parameter("distillation_column", "entropy", 2))  # Invalid parameter_name
print(extract_parameter("reactor", "pressure", 5))  # Invalid index
print(extract_parameter("mixer", "pressure", 0))  # Invalid unit_name

# Define the molecular_weights dictionary
molecular_weights = {
    "NaCl": 58.44,
    "H2SO4": 98.079,
    "NaOH": 40.00,
    "KMnO4": 158.034,
    "CH3COOH": 60.052,
}

# Define the solutions_needed list
solutions_needed = ["NaCl-0.5M", "H2SO4-0.25M", "NaOH-1M", "KCl-0.1M", "CH3COOH-0.3M"]

# Test the calculate_solution_weights function
print(
    calculate_solution_weights(
        molecular_weights=molecular_weights, solutions_needed=solutions_needed
    )
)
