# Function definition, with type hints describing the inputs and the return type (not required but can be helpful)
def extract_parameter(unit_name: str, parameter_name: str, index: int) -> str:
    # Try, this will be the case when everything is found in the unit_operations_data
    try:
        # Extract the value, will raise IndexError if index is out of bounds, or KeyError if unit_name/parameter_name are not found
        value = unit_operations_data[unit_name][parameter_name][index]
        # Return the string with the format defined in the question
        return f"{unit_name}_{parameter_name}_{value}"
    # Catch the error with Index or Key not being found
    except (KeyError, IndexError):
        # Just return Invalid input as described in the question
        return "Invalid input"
