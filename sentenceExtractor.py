import csv
import os

def extract_and_export_sentences(tsv_file_path, output_file_path, num_sentences=15):
    """
    Reads a TSV file, extracts sentences from the second column (index 1),
    and writes the first 'num_sentences' into a new text file, line by line.

    Args:
        tsv_file_path (str): The path to the input TSV file.
        output_file_path (str): The path where the output text file will be saved.
        num_sentences (int): The maximum number of sentences to extract and write.
    """
    extracted_sentences = []

    try:
        with open(tsv_file_path, 'r', newline='', encoding='utf-8') as tsvfile:
            # Use csv.reader for TSV, specifying the delimiter as tab
            reader = csv.reader(tsvfile, delimiter='\t')
            
            # Iterate through each row in the TSV file
            for i, row in enumerate(reader):
                # Ensure the row has at least 2 columns (index 1 exists)
                if len(row) > 1:
                    sentence = row[1].strip() # Get the sentence from the second column and strip whitespace
                    extracted_sentences.append(sentence)
                    
                    # Stop if we have collected the desired number of sentences
                    if len(extracted_sentences) >= num_sentences:
                        break
                else:
                    print(f"Warning: Row {i+1} does not have enough columns to extract index 1. Skipping.")

        # Write the extracted sentences to the output text file
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            for sentence in extracted_sentences:
                outfile.write(sentence + '\n')

        print(f"Successfully extracted {len(extracted_sentences)} sentences from '{tsv_file_path}'")
        print(f"and saved them to '{output_file_path}'.")

    except FileNotFoundError:
        print(f"Error: The file '{tsv_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example Usage ---
if __name__ == "__main__":
    # Define the input TSV file path and output TXT file path
    input_tsv_file = "line_index_female.tsv"
    output_txt_file = "sentences.txt"

    # Call the function to extract and export sentences
    extract_and_export_sentences(input_tsv_file, output_txt_file, num_sentences=4500)

    # Clean up the dummy TSV file after execution (optional)
    # os.remove(input_tsv_file)
    # print(f"Removed dummy TSV file: '{input_tsv_file}'.")
