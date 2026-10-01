from clean_preproinsulin import clean_sequence

# A sequência de pré-proinsulina humana
preproInsulin = clean_sequence('preproinsulin-seq.txt')

# Primeira parte da sequência.
lsInsulin = preproInsulin[0:24]

# Segunda parte da sequência.
bInsulin = preproInsulin[24:54]

# Terceira parte da sequência.
cInsulin = preproInsulin[54:89]

# Quarta parte da sequência.
aInsulin = preproInsulin[89:110]

insulin = (bInsulin + aInsulin)

print(f'Exibição de sequências\n')

print(f'Sequência de pré-proinsulina humana: {preproInsulin}\n')
print(f'Sequência de insulina: {insulin}\n')

# Pesos moleculares dos aminoácidos, em g/mol.
aaWeights = {
	'A': 89.09,
	'C': 121.16,
	'D': 133.10,
	'E': 147.13,
	'F': 165.19,
	'G': 75.07,
	'H': 155.16,
	'I': 131.17,
	'K': 146.19,
	'L': 131.17,
	'M': 149.21,
	'N': 132.12,
	'P': 115.13,
	'Q': 146.15,
	'R': 174.20,
	'S': 105.09,
	'T': 119.12,
	'V': 117.15,
	'W': 204.23,
	'Y': 181.19,
}

# Conta quantas vezes cada aminoácido aparece na sequência.
aaCountInsulin = {
	aminoAcid: (insulin).upper().count(aminoAcid)
	for aminoAcid in aaWeights
}

# Soma a contribuição de cada aminoácido para o peso molecular.
molecularWeightInsulin = sum(
	aaWeights[aminoAcid] * aaCountInsulin[aminoAcid]
	for aminoAcid in aaWeights
)

print(f'Peso molecular aproximado da insulina: {molecularWeightInsulin:.2f}\n')

acceptedMolecularWeightInsulin = 5807.63
percentErrorInsulin = (
	abs(molecularWeightInsulin - acceptedMolecularWeightInsulin)
	/ acceptedMolecularWeightInsulin
) * 100

print('Percentual de erro: \n' + f'{percentErrorInsulin:.2f}%')
