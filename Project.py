def corrigir_palavra(sCadCarateres):
    dCadCarateres = {}
    lKeys = []
    bChanged = True
    for i in range(len(sCadCarateres)):
        dCadCarateres[i] = sCadCarateres[i].lower()
    print(dCadCarateres)
    input()
    while bChanged:
        bChanged = False
        for i in range(len(dCadCarateres ) - 1):
            if dCadCarateres[i] == dCadCarateres[i + 1]:
                dCadCarateres.pop(i)
                dCadCarateres.pop(i+1)
                i += 1
                bChanged = True
    return dCadCarateres
while True:
    print(corrigir_palavra(input()))
