from jsonFileHandler import readJsonFile

dados = readJsonFile('insulin.json')

if dados:
    weights = dados["weights"]
    bInsulin = dados["molecules"]["bInsulin"]
    aInsulin = dados["molecules"]["aInsulin"]
    molecularWeightInsulinActual = dados["molecularWeightInsulinActual"]
    insulin = aInsulin + bInsulin
    roughMolecularWeight = sum(weights[aminoAcid.upper()] for aminoAcid in insulin)
    percent = (roughMolecularWeight - molecularWeightInsulinActual) / molecularWeightInsulinActual * 100

    print(f"Contagem de aminoácidos: {len(insulin)}")
    print(f"Moléculas bInsulin: {bInsulin}")
    print(f"Moléculas aInsulin: {aInsulin}")
    print(f"Peso molecular real da insulina: {molecularWeightInsulinActual}")
    print(f"The rough molecular weight of insulin: {roughMolecularWeight:.2f}")
    print(f"Percent error: {percent:.2f}")
else:
    print("Não foi possível carregar os dados")