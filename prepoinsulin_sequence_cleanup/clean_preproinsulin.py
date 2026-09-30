import re

def clean_sequence(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    sequence = re.sub(r'[^a-z]', '', code)
    print(f'Recuperação da sequência proteica da pré-proinsulina humana\n')
    print(f'Dados formatados: {sequence}')
    print(f'Quantidade de caracters: {len(sequence)}')

clean_sequence('preproinsulin-seq.txt')





