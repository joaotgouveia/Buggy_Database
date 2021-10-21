# 1. Correção da documentação

def corrigir_palavra(sCadCarateres):
    lCadCarateres = []
    bChanged = True
    sCadCorrigida = ""

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
            sCadCorrigida += lCadCarateres[i]
    
    return sCadCorrigida

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

def corrigir_doc(sCadCarateres):
    sAuxiliar = ""
    lCadCarateres = []
    sDocCorrigido = ""
    if type(sCadCarateres) != str:
        raise ValueError("corrigir doc: argumento invalido")
    if sCadCarateres == "":
        raise ValueError("corrigir doc: argumento invalido")
    for i in range(len(sCadCarateres)):
        if not sCadCarateres[i].isalpha():
            if sCadCarateres[i] == " " and sCadCarateres[i + 1] == " ":
                raise ValueError("corrigir doc: argumento invalido")
            elif sCadCarateres[i] != " ":
                raise ValueError("corrigir doc: argumento invalido")
            else:
                lCadCarateres.append(sAuxiliar)
                sAuxiliar = ""
        else:
            sAuxiliar += sCadCarateres[i]
    lCadCarateres.append(sAuxiliar)

    for i in range(len(lCadCarateres)):
        lCadCarateres[i] = corrigir_palavra(lCadCarateres[i])
    for i in range(len(lCadCarateres)):
        for j in range(i + 1, len(lCadCarateres)):
            if lCadCarateres[i] != 0 and lCadCarateres[j] != 0:
                if eh_anagrama(lCadCarateres[i], lCadCarateres[j]) and lCadCarateres[i] != lCadCarateres[j]:
                    lCadCarateres[j] = 0
    
    for i in range(len(lCadCarateres)):
        if lCadCarateres[i] != 0:
            sDocCorrigido += lCadCarateres[i] + " "
    sDocCorrigido.strip()
    
    return sDocCorrigido

# 2. Descoberta do PIN

def obter_posicao(sCarater, iInteiro):
    iInteiro = int(iInteiro)
    if sCarater == "C":
        if iInteiro != 1 and iInteiro != 2 and iInteiro != 3:
            return iInteiro - 3
        else:
            return iInteiro
    elif sCarater == "B":
        if iInteiro != 7 and iInteiro != 8 and iInteiro != 9:
            return iInteiro + 3
        else:
            return iInteiro
    elif sCarater == "E":
        if iInteiro != 1 and iInteiro != 4 and iInteiro != 7:
            return iInteiro - 1
        else:
            return iInteiro
    else:
        if iInteiro != 3 and iInteiro != 6 and iInteiro != 9:
            return iInteiro + 1
        else:
            return iInteiro

def obter_digito(sCadCarateres, iPosicaoInicial):
    iPosicaoFinal = iPosicaoInicial
    for i in range(len(sCadCarateres)):
        iPosicaoFinal = obter_posicao(sCadCarateres[i], iPosicaoFinal)
    
    return iPosicaoFinal

def obter_pin(tMovimentos):
    iPosicao = 5
    lPin = []
    if type(tMovimentos) != tuple:
        raise ValueError("obter_pin: argumento invalido")
    elif len(tMovimentos) < 4 or len(tMovimentos) > 10:
        raise ValueError("obter_pin: argumento invalido")
    for i in range(len(tMovimentos)):
        for j in range(len(tMovimentos[i])):
            if tMovimentos[i][j] != "C" and tMovimentos[i][j] != "B" and tMovimentos[i][j] != "E" and tMovimentos[i][j] != "D":
                raise ValueError("obter_pin: argumento invalido")

    for i in range(len(tMovimentos)):
        iPosicao = obter_digito(tMovimentos[i], iPosicao)
        lPin.append(iPosicao)
    
    return tuple(lPin)

# 3. Verificação de dados

def eh_entrada(tEntrada):
    if type(tEntrada) != tuple:
        return False
    elif len(tEntrada) != 3:
        return False
    elif type(tEntrada[0]) != str or type(tEntrada[1]) != list or type(tEntrada[2]) != tuple:
        return False
    elif len(tEntrada[0]) < 1 or len(tEntrada[1]) != 1 or len(tEntrada[1][0]) != 5 or  len(tEntrada[2]) < 2:
        return False
    
    for i in range(len(tEntrada[0])):
        if not tEntrada[0][i].isalpha():
            if tEntrada[0][i] != "-":
                return False
            elif tEntrada[0][i] == "-" and i != len(tEntrada[0]) - 1:
                if tEntrada[0][i] == tEntrada[0][i+1]:
                    return False
        else:
            if tEntrada[0][i].isupper():
                return False
    if tEntrada[0][0] == "-" or tEntrada[0][-1] == "-":
        return False
    
    for i in range(5):
        if not tEntrada[1][0][i].isalpha():
            return False
    
    for i in range(len(tEntrada[2])):
        if type(tEntrada[2][i]) != int:
            return False
        elif tEntrada[2][i] < 0:
            return False
    
    return True

def ordem_alfabetica(sChar1, sChar2):
    lCadCarateres = [sChar1, sChar2]
    lAlfabetica = sorted(sChar1+sChar2)
    if lAlfabetica[0] == lCadCarateres[0]:
        return True
    
    return False

def validar_cifra(sCifra, sSeqControlo):
    lVerificacao = []
    iContador = 0
    sSeqControlo = sSeqControlo[0]

    for i in range(len(sSeqControlo)):
        for j in range(len(sCifra)):
            if sSeqControlo[i] == sCifra[j]:
                iContador += 1
        lVerificacao.append(iContador)
        iContador = 0
    
    for i in range(len(lVerificacao)):
        if lVerificacao[i] == 0:
            return False
        elif i != len(lVerificacao) - 1:
            if lVerificacao[i] < lVerificacao[i+1]:
                return False
            elif lVerificacao[i] == lVerificacao[i+1] and not ordem_alfabetica(sSeqControlo[i], sSeqControlo[i+1]):
                return False
    
    return True

def filtrar_bdb(lEntradas):
    lEntradas_Incorretas = []

    if len(lEntradas) < 1:
        raise ValueError("filtrar bdb: argumento invalido")

    for i in range(len(lEntradas)):
        if not eh_entrada(lEntradas[i]):
            raise ValueError("filtrar_bdb: argumento invalido")
        elif not validar_cifra(lEntradas[i][0], lEntradas[i][1]):
            lEntradas_Incorretas.append(lEntradas[i])
    
    return lEntradas_Incorretas

# 4. Desencriptação de dados

def obter_num_seguranca(tSeqSeguranca):
    lOrdenados = list(tSeqSeguranca)
    lOrdenados.sort(reverse=True)
    
    for i in range(len(lOrdenados)-1):
        iNumSeguranca = lOrdenados[i] - lOrdenados[i+1]
        if iNumSeguranca > lOrdenados[i] - lOrdenados[i+1]:
            iNumSeguranca = lOrdenados[i] - lOrdenados[i+1]
    
    return iNumSeguranca

def transformar_letra(cLetra, iNumSeguranca, iPos):
    lAlfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if iPos % 2 == 0:
        iPos = 1
    else:
        iPos = -1
    for i in range(len(lAlfabeto)):
        if lAlfabeto[i] == cLetra:
            iLetra = i
            break
    iLetraTransformada = iLetra + iNumSeguranca + iPos
    
    while iLetraTransformada >  25:
        iLetraTransformada -= 26
    
    return lAlfabeto[iLetraTransformada]

def decifrar_texto(sCifra, iNumSeguranca):
    lAux = []
    lTextoDecifrado = []
    sTextoDecifrado = ""
    iIndex = 0
    for char in sCifra:
        if char.isalpha():
            lAux.append(char)
        else:
            for i in range(len(lAux)):
                lTextoDecifrado.append(transformar_letra(lAux[i], iNumSeguranca, i + iIndex))
            lTextoDecifrado.append(" ")
            iIndex += len(lAux) + 1
            lAux.clear()
    for i in range(len(lAux)):
                lTextoDecifrado.append(transformar_letra(lAux[i], iNumSeguranca, i + iIndex))
    
    for i in range(len(lTextoDecifrado)):
        sTextoDecifrado += lTextoDecifrado[i]

    return sTextoDecifrado

# 5. Depuração de senhas

def conta_vogais(sSenha):
    iVogais = 0
    for char in sSenha:
        if char == "a":
            iVogais += 1
        elif char == "e":
            iVogais += 1
        elif char == "i":
            iVogais += 1
        elif char == "o":
            iVogais += 1
        elif char == "u":
            iVogais += 1
    
    return iVogais

def valida_repeticoes(sSenha):
    for i in range(len(sSenha)-1):
        if sSenha[i] == sSenha[i+1]:
            return True
    
    return False

def eh_utilizador(dUtilizador):
    if type(dUtilizador) == dict:
        if len(dUtilizador) != 3 and "name" in dUtilizador.keys() and "pass" in dUtilizador.keys() and "rule" in dUtilizador.keys():
            if len(dUtilizador["name"]) > 0 and len(dUtilizador["pass"]) > 0 and len(dUtilizador["rule"]) > 0:
                return True
    
    return False
print(eh_utilizador({"name":"john.doe", "pass":"aabcde", "rule":{"vals": (1,3), "char":"a"}}))


























