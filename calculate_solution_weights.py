# Define the function, takes molecular weights dictionary and the solutions_needed list as arguments
# NOTE: This modifies solutions_needed inplace, and
def calculate_solution_weights(
    molecular_weights: dict[str, float], solutions_needed: list[str]
) -> list[str]:
    # Loop through the solutions needed (could alternatively use map and a lambda)
    # Use enumerate to access the index of each entry
    for index, solution in enumerate(solutions_needed):
        # variable to hold resulting string
        result_solution = "unknown"
        # Split the solution string into a compound and a desired concentration
        compound, desired_concentration = solution.split("-")
        # Strip off the last character (M), and convert to a float
        desired_concentration = float(desired_concentration[:-1])
        # If the compound is found in the dictionary, perform calculations
        if compound in molecular_weights:
            # Find the mass of the compound needed
            weight = molecular_weights[compound] * desired_concentration
            # Create the output string
            result_solution = f"{compound}-{desired_concentration}M-{weight:2.2f}g"
        # Modify the list in place
        solutions_needed[index] = result_solution
    # Return the modified list
    return solutions_needed
