import re
from pathlib import Path

def clean_sequence(file_path):
    sequence_path = Path(__file__).resolve().parent / file_path
    with open(sequence_path, 'r') as file:
        code = file.read()

    sequence = re.sub(r'[^a-z]', '', code)
    return sequence

if __name__ == "__main__":
    clean_sequence('preproinsulin-seq.txt')





