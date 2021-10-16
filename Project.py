def corrigir_palavra(sCadCarateres):
    lCadCarateres = []
    bChanged = True
    sCorrected = ""
    for i in range(len(sCadCarateres)):
        lCadCarateres += sCadCarateres[i]
    while bChanged:
        bChanged = False
        for i in range(len(sCadCarateres) - 1):
            if lCadCarateres[i] != 0 and lCadCarateres[i+1] != 0:
                if lCadCarateres[i].lower() == lCadCarateres[i+1].lower() and ((lCadCarateres[i].islower() and lCadCarateres[i+1].isupper()) or (lCadCarateres[i+1].islower() and lCadCarateres[i].isupper())):
                    lCadCarateres[i] = 0
                    lCadCarateres[i+1] = 0
                    bChanged = True
            elif lCadCarateres[i] != 0 and lCadCarateres[i+1] == 0:
                for j in range(i+2, len(sCadCarateres)):
                    if lCadCarateres[j] != 0:
                        if lCadCarateres[i].lower() == lCadCarateres[j].lower() and ((lCadCarateres[i].islower() and lCadCarateres[j].isupper()) or (lCadCarateres[j].islower() and lCadCarateres[i].isupper())):
                            lCadCarateres[i] = 0
                            lCadCarateres[j] = 0
                            bChanged = True
                            break
    for i in range(len(sCadCarateres)):
        if lCadCarateres[i] != 0:
            sCorrected += lCadCarateres[i]
    return sCorrected
print(corrigir_palavra(input()))
