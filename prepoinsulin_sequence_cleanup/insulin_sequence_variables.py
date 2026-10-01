from clean_preproinsulin import clean_sequence

# A sequência de pré-proinsulina humana
preproInsulin = clean_sequence('preproinsulin-seq.txt')

# Partes restantes da sequência.
isInsulin = preproInsulin[0:24]

# Primeira parte da sequência.
bInsulin = preproInsulin[24:54]

# Segunda parte da sequência.
aInsulin = preproInsulin[54:89]

# Terceira parte da sequência.
cInsulin = preproInsulin[89:110]

insulin = (bInsulin + aInsulin)

print(f'Exibição de sequências\n')

print(f'Sequência de pré-proinsulina humana: {preproInsulin}')
print(f'Sequência de insulina: {insulin}')
