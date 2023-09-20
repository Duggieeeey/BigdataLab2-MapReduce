# Import the necessary libraries
import sys
import os

# Define a set of stopwords
stopwords = set(["the", "and", "of", "a", "to", "in", "is", "it"])

# Define the map function
def map(key, value):
    words = key.split()
    for word in words:
        # Remove punctuation and convert to lowercase
        word = word.strip('.,!?()"\'').lower()
        # Check if the word is not in the stopwords set
        if word not in stopwords:
            yield (word, 1)

# Define the reduce function
def reduce(key, values):
    yield (key, sum(values))

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

# Construct the full input file path using the provided directory path
input_file_path = os.path.join("C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2", "C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2\\p2_input.txt")

# Construct the full output file path using the provided directory path
output_file_path = os.path.join("C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2", "C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2\\p2_output.txt")

# Initialize a dictionary to store the intermediate results
intermediate_data = {}

# Read input from the input file
with open("C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2\\p2_input.txt", 'r') as input_file:
    for line in input_file:
        # Call the map function for each line in the input file
        for word, count in map(line.strip(), None):
            if word not in intermediate_data:
                intermediate_data[word] = []
            intermediate_data[word].append(count)

# Sort the intermediate data by key (word)
sorted_data = sorted(intermediate_data.items())

# Initialize a dictionary to store the final results
final_data = {}

# Call the reduce function for each key-value pair in the sorted data
for key, values in sorted_data:
    for word, count in reduce(key, values):
        final_data[word] = count

# Sort the final data alphabetically by keys
final_data = dict(sorted(final_data.items()))

# Output the final results to the specified output file
with open("C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2\\p2_output.txt", 'w') as output_file:
    for word, count in final_data.items():
        output_file.write(f'"{word}" {count}\n')

print(f"Results saved.")
