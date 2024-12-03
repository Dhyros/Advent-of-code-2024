import re

def problem1(file_name: str) -> int:
    # List with tuples of numbers to multiply
    occurrences = []

    # Pattern to match the numbers    
    pattern = r"mul\((\d+),\s*(\d+)\)"

    # Open the file
    with open(file_name, 'r') as file:
        # Read the lines
        for line in file:
            # Append the coincidences to the list
            occurrences += re.findall(pattern, line)
    
    # Multiply the numbers and sum them
    return sum([int(num1) * int(num2) for num1, num2 in occurrences])

def problem2(file_name: str) -> int:
    # Regular expressions for instructions
    mul_pattern = r"mul\((\d+),\s*(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Initialize state
    mul_enabled = True
    total_sum = 0

    # Open the file
    with open(file_name, "r") as file:
        # Read the lines
        for line in file:
            # Split the input into tokens while preserving order
            tokens = re.split(r"(mul\(-?\d+,\s*-?\d+\)|do\(\)|don't\(\))", line)


            # Iterate over the tokens
            for token in tokens:
                # Check if the token is a multiplication
                if re.match(mul_pattern, token):
                    # Check if the multiplication is enabled
                    if mul_enabled:
                        # Extract the numbers
                        num1, num2 = re.match(mul_pattern, token).groups()
                        # Multiply the numbers and add them to the total sum
                        total_sum += int(num1) * int(num2)
                # Check if the token is a do
                elif re.match(do_pattern, token):
                    # Enable the multiplication
                    mul_enabled = True
                # Check if the token is a don't
                elif re.match(dont_pattern, token):
                    # Disable the multiplication
                    mul_enabled = False
    
    return total_sum

#############################################################################

# Input files
input_file = 'input.txt'
test_file1 = 'input_reduced1.txt'
test_file2 = 'input_reduced2.txt'

# Problem 1
print('Solution to problem 1 test input:', problem1(test_file1))
print('Solution to problem 2 test input:', problem2(test_file2))

print('-' * 40)

# Problem 2
print('Solution to problem 1:', problem1(input_file))
print('Solution to problem 2:', problem2(input_file))