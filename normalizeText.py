import os

def normalize_newlines(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split the content into sentences using any number of newlines
        sentences = [line.strip() for line in content.split('\n') if line.strip()]

        # Join sentences with exactly two newlines
        normalized_content = '\n\n'.join(sentences)

        # Create output filename
        base_name = os.path.basename(input_file)
        output_file = f"normalized_{base_name}"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(normalized_content)

        print(f"✅ Normalized content saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied when accessing '{input_file}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

#usage
input_path = './yoruba_alphabets.txt'
normalize_newlines(input_path)
