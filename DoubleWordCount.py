# Import the necessary libraries
import sys
import os

# Define the map function
def map(line):
    # Split the line into words
    words = line.strip().split()
    
    # Emit word bigrams as key-value pairs
    for i in range(len(words) - 1):
        bigram = f"{words[i]},{words[i + 1]}"
        yield (bigram, 1)

# Define the reduce function
def reduce(key, values):
    # Sum the counts for each bigram
    yield (key, sum(values))

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

# Construct the full input file path using the provided directory path
input_file_path = os.path.join("C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2", "C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2\\p3_input.txt")

# Construct the full output file path using the provided directory path
output_file_path = os.path.join("C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2", "C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2\\p3_output.txt")

# Initialize a dictionary to store the intermediate results
intermediate_data = {}

# Read input from the input file
with open("C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2\\p3_input.txt", 'r') as input_file:
    for line in input_file:
        # Call the map function for each line in the input file
        for bigram, count in map(line):
            if bigram not in intermediate_data:
                intermediate_data[bigram] = []
            intermediate_data[bigram].append(count)

# Initialize a dictionary to store the final results
final_data = {}

# Call the reduce function for each key-value pair in the intermediate data
for key, values in intermediate_data.items():
    for bigram, count in reduce(key, values):
        final_data[bigram] = count

# Output the final results to the specified output file
with open("C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2\\p3_output.txt", 'w') as output_file:
    for bigram, count in final_data.items():
        output_file.write(f'"{bigram}" {count}\n')

print(f"Results saved.")
