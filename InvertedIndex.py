# Import the necessary libraries
import sys
import os

# Define the map function
def map(line_number, line):
    # Split the line into words
    words = line.strip().split()
    
    # Emit word-document pairs as key-value pairs
    for word in words:
        yield (word, [line_number])

# Define the reduce function
def reduce(key, values):
    # Merge the lists of documents for each word
    documents = [doc for sublist in values for doc in sublist]
    
    # Remove duplicates by converting documents to a set
    unique_documents = list(set(documents))
    
    # Emit the word and the list of unique documents where it appears
    yield (key, unique_documents)

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

# Construct the full input file path using the provided directory path
input_file_path = os.path.join("C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2", "C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2\\p4_input.txt")

# Construct the full output file path using the provided directory path
output_file_path = os.path.join("C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2", "C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2\\p4_output.txt")

# Initialize a dictionary to store the intermediate results
intermediate_data = {}

# Read input from the input file
with open("C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2\\p4_input.txt", 'r') as input_file:
    for line_number, line in enumerate(input_file, start=1):
        # Call the map function for each line in the input file
        for word, documents in map(line_number, line):
            if word not in intermediate_data:
                intermediate_data[word] = []
            intermediate_data[word].append(documents)

# Initialize a dictionary to store the final results
final_data = {}

# Call the reduce function for each key-value pair in the intermediate data
for key, values in intermediate_data.items():
    for word, documents in reduce(key, values):
        final_data[word] = documents

# Output the final inverted index to the specified output file
with open("C:\\Users\\withm\\OneDrive\\Desktop\\DTSC 701\\lab2\\p4_output.txt", 'w') as output_file:
    for word, documents in final_data.items():
        output_file.write(f'"{word}", "Document {documents}"\n')

print(f"Inverted Index saved.")
