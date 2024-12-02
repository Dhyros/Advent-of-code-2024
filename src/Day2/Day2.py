from itertools import combinations


def is_safe(report: list[int]) -> bool:
    if len(report) < 2:
        return False
    
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are in range [1, 3] or [-3, -1]
    if all(1 <= d <= 3 for d in diffs):
        return True  # Strictly increasing with valid differences

    if all(-3 <= d <= -1 for d in diffs):
        return True  # Strictly decreasing with valid differences

    return False

def problem(file_name: str, *, max_bad_levels: int) -> int:

    # Open the file and read the levels
    with open(file_name, 'r') as file:
        # Initialize the score
        score = 0
        
        # Iterate through the file
        for line in file:
            report = list(map(int, line.split()))

            # Check if the report is safe without removing any levels
            if is_safe(report):
                score += 1
            else:
                # Check combinations of up to max_bad_levels to see if any reduced report is safe
                n = len(report)
                found_safe = False

                for k in range(1, max_bad_levels + 1):
                    # If a safe report is found, stop searching
                    if found_safe:
                        break

                    # Generate all combinations of bad levels
                    for bad_levels in combinations(range(n), k):
                        reduced_report = [report[i] for i in range(n) if i not in bad_levels]
                        
                        # If the reduced report is safe, stop searching
                        if is_safe(reduced_report):
                            found_safe = True
                            score += 1
                            break

    return score

#############################################################################

# Input files
input_file = 'input.txt'
test_file = 'input_reduced.txt'

# Problem 1
print('Solution to problem 1 test input:', problem(test_file, max_bad_levels=0))
print('Solution to problem 2 test input:', problem(test_file, max_bad_levels=1))

print('-' * 40)

# Problem 2
print('Solution to problem 1:', problem(input_file, max_bad_levels=0))
print('Solution to problem 2:', problem(input_file, max_bad_levels=1))