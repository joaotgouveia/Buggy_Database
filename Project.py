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

def eh_anagrama(sCadCarateres1, sCadCarateres2):
    lCadCarateres1 = []
    lCadCarateres2 = []
    bAnagrama = True

    for i in range(len(sCadCarateres1)):
        lCadCarateres1 += sCadCarateres1[i].lower()
    for i in range(len(sCadCarateres2)):
        lCadCarateres2 += sCadCarateres2[i].lower()

    for i in range(len(lCadCarateres1)):
        for j in range(len(lCadCarateres2)):
            if lCadCarateres1[i] == lCadCarateres2[j] and lCadCarateres2[j] != 0:
                lCadCarateres1[i] = 0
                lCadCarateres2[j] = 0
                break
    
    for i in range(len(sCadCarateres1)):
        if lCadCarateres1[i] != 0:
            bAnagrama = False
    for i in range(len(sCadCarateres2)):
        if lCadCarateres2[i] != 0:
            bAnagrama = False

    return bAnagrama

print(eh_anagrama(input(), input()))