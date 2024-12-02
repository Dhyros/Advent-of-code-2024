import timeit

def problem1(file_name: str) -> int:
    # Lists to store the left and right values
    left_values = []
    right_values = []
    
    # Open the file
    with open(file_name, 'r') as f:
        # Iterate through the file
        for line in f:
            # Left and right values of each line
            left, right = line.strip().split()
            
            # Append the left and right values to their respective lists
            left_values.append(int(left))
            right_values.append(int(right))
    
    # Order the lists
    left_values.sort()
    right_values.sort()
    
    # Calculations
    return sum(abs(l - r) for l, r in zip(left_values, right_values))

def problem2(file_name: str) -> int:
    # List to store the left values
    left_values = []
    
    # Dictionary to store the occurences of each number in the right list
    occurences = dict()
    
    # Open the file
    with open(file_name, 'r') as f:
        # Iterate through the file
        for line in f:
            # Left and right values of each line
            left, right = line.strip().split()
            
            # Append the left value to its list
            left_values.append(int(left))
            
            # If the right value is not in the dictionary, add it
            if int(right) not in occurences:
                occurences[int(right)] = 1
            else:
                occurences[int(right)] += 1
    
    score = 0
    # Iterate through the left list
    for number in left_values:
        # If the number is in the right list, calculate similarity
        if number in occurences:
            score += number * occurences[number]
    
    return score

#############################################################################

# Input files
input_file = 'input.txt'
test_file = 'input_reduced.txt'

# Problem 1
print('Solution to problem 1 test input:', problem1(test_file))
print('Solution to problem 2 test input:', problem2(test_file))

print('-' * 40)

# Problem 2
print('Solution to problem 1:', problem1(input_file))
print('Solution to problem 2:', problem2(input_file))
