import re

def clean_sequence(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    sequence = re.sub(r'[^a-z]', '', code)
    return sequence

if __name__ == "__main__":
    clean_sequence('preproinsulin-seq.txt')





