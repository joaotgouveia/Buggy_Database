# Ao longo deste projeto a notação utilizada diverge ligeiramente 
# da convencionada pelo PEP 8
# Mudei anagrama e criei registo de anagrama para nao repetir operacoes sem sentido

# 1. Correção da documentação

# 1.2.1 Função corrigir_palavra

# bChanged = True
# def elimina_surto(lCadCarateres, i1, i2):
#     global bChanged
#     if lCadCarateres[i1].lower() == lCadCarateres[i2].lower():
#         if lCadCarateres[i1].islower() and lCadCarateres[i2].isupper():
#             lCadCarateres[i1] = 0
#             lCadCarateres[i2] = 0
#             bChanged = True
#         elif lCadCarateres[i1].islower() and lCadCarateres[i2].isupper():
#             lCadCarateres[i1] = 0
#             lCadCarateres[i2] = 0
#             bChanged = True
#         else:
#             bChanged = False
#     else:
#         bChanged = False
    

def corrigir_palavra(sCadCarateres):
    lCadCarateres = list(sCadCarateres)
    bChanged = True
    sCadCorrigida = ""
    while bChanged:
        bChanged = False

        for i in range(len(sCadCarateres) - 1):  
            if lCadCarateres[i] != 0 and lCadCarateres[i+1] != 0:
                if lCadCarateres[i].lower() == lCadCarateres[i+1].lower():
                    if lCadCarateres[i].islower() and lCadCarateres[i+1].isupper():
                        lCadCarateres[i] = 0
                        lCadCarateres[i+1] = 0
                        bChanged = True
                    elif lCadCarateres[i+1].islower() and lCadCarateres[i].isupper():
                        lCadCarateres[i] = 0
                        lCadCarateres[i+1] = 0
                        bChanged = True
            elif lCadCarateres[i] != 0 and lCadCarateres[i+1] == 0:
                for j in range(i+2, len(sCadCarateres)):
                    if lCadCarateres[j] != 0:
                        if lCadCarateres[i].lower() == lCadCarateres[j].lower():
                            if lCadCarateres[i].islower() and lCadCarateres[j].isupper():
                                lCadCarateres[i] = 0
                                lCadCarateres[j] = 0
                                bChanged = True
                            elif lCadCarateres[j].islower() and lCadCarateres[i].isupper():
                                lCadCarateres[i] = 0
                                lCadCarateres[j] = 0
                                bChanged = True
                        break
   
    for i in range(len(sCadCarateres)):
        if lCadCarateres[i] != 0:
            sCadCorrigida += lCadCarateres[i]
    
    return sCadCorrigida

# 1.2.2 Função eh_anagrama

def eh_anagrama(sCadCarateres1, sCadCarateres2):
    lCadCarateres1 = []
    lCadCarateres2 = []
    # bAnagrama = True

    for char in sCadCarateres1:
        lCadCarateres1 += char.lower()
    for char in sCadCarateres2:
        lCadCarateres2 += char.lower()

    if sorted(lCadCarateres1) == sorted(lCadCarateres2):
        return True
    
    return False
    # for i in range(len(lCadCarateres1)):
    #     for j in range(len(lCadCarateres2)):
    #         if lCadCarateres1[i] == lCadCarateres2[j] and lCadCarateres2[j] != 0:
    #             lCadCarateres1[i] = 0
    #             lCadCarateres2[j] = 0
    #             break
    
    # for i in range(len(sCadCarateres1)):
    #     if lCadCarateres1[i] != 0:
    #         bAnagrama = False
    # for i in range(len(sCadCarateres2)):
    #     if lCadCarateres2[i] != 0:
    #         bAnagrama = False

    # return bAnagrama

# 1.2.3 Função corrigir_doc

def corrigir_doc(sCadCarateres):
    sAuxiliar = ""
    sDocCorrigido = ""
    lCadCarateres = []
    lAnagramasVerificados = []

    if type(sCadCarateres) != str:
        raise ValueError("corrigir_doc: argumento invalido")
    if sCadCarateres == "":
        raise ValueError("corrigir_doc: argumento invalido")
    for i in range(len(sCadCarateres)):
        if not sCadCarateres[i].isalpha():
            if i != len(sCadCarateres) - 1:
                if sCadCarateres[i] == " " and sCadCarateres[i + 1] == " ":
                    raise ValueError("corrigir_doc: argumento invalido")
            if sCadCarateres[i] != " ":
                raise ValueError("corrigir_doc: argumento invalido")
            else:
                lCadCarateres.append(sAuxiliar)
                sAuxiliar = ""
        else:
            sAuxiliar += sCadCarateres[i]
    lCadCarateres.append(sAuxiliar)

    for i in range(len(lCadCarateres)):
        lCadCarateres[i] = corrigir_palavra(lCadCarateres[i])
    for i in range(len(lCadCarateres)):
        if not lCadCarateres[i] in lAnagramasVerificados and lCadCarateres[i] != 0:
            for j in range(i + 1, len(lCadCarateres)):
                if lCadCarateres[j] != 0:
                    if eh_anagrama(lCadCarateres[i], lCadCarateres[j]) and lCadCarateres[i] != lCadCarateres[j]:
                        lCadCarateres[j] = 0
            lAnagramasVerificados.append(lCadCarateres[i])

    for e in lCadCarateres:
        if e != 0:
            sDocCorrigido += e
            sDocCorrigido += " "

    return sDocCorrigido.rstrip()

doc = "BuAaXOoxiIKoOkggyrFfhHXxR duJjUTtaCcmMtaAGga eEMmtxXOjUuJQqQHhqoada JlLjbaoOsuUeYy cChgGvValLCwMmWBbclLsNn LyYlMmwmMrRrongTtoOkyYcCK daRfFKkLlhHrtZKqQkkvVKza"
print(corrigir_doc(doc))


# 2. Descoberta do PIN

# 2.2.1 Função obter_posicao

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

# 2.2.2 Função obter_digito

def obter_digito(sCadCarateres, iPosicaoInicial):
    iPosicaoFinal = iPosicaoInicial
    for i in range(len(sCadCarateres)):
        iPosicaoFinal = obter_posicao(sCadCarateres[i], iPosicaoFinal)
    
    return iPosicaoFinal

# 2.2.3 Função obter_pin

def obter_pin(tMovimentos):
    iPosicao = 5
    lPin = []
    if type(tMovimentos) != tuple:
        raise ValueError("obter_pin: argumento invalido")
    elif len(tMovimentos) < 4 or len(tMovimentos) > 10:
        raise ValueError("obter_pin: argumento invalido")
    for i in range(len(tMovimentos)):
        if len(tMovimentos[i]) < 1:
            raise ValueError("obter_pin: argumento invalido")
        for j in range(len(tMovimentos[i])):
            if tMovimentos[i][j] != "C" and tMovimentos[i][j] != "B" and tMovimentos[i][j] != "E" and tMovimentos[i][j] != "D":
                raise ValueError("obter_pin: argumento invalido")

    for i in range(len(tMovimentos)):
        iPosicao = obter_digito(tMovimentos[i], iPosicao)
        lPin.append(iPosicao)
    
    return tuple(lPin)

# 3. Verificação de dados

# 3.2.1 Função eh_entrada

def eh_entrada(tEntrada):
    if type(tEntrada) != tuple:
        return False
    elif len(tEntrada) != 3:
        return False
    elif type(tEntrada[0]) != str or type(tEntrada[1]) != str or type(tEntrada[2]) != tuple:
        return False
    elif tEntrada[0] == "" or len(tEntrada[1]) != 7 or  len(tEntrada[2]) < 2:
        return False
    
    for i in range(len(tEntrada[0])):
        if not tEntrada[0][i].isalpha():
            if tEntrada[0][i] != "-" or i == 0 or i == len(tEntrada[0]) - 1:
                return False
            elif tEntrada[0][i] == "-" and i != len(tEntrada[0]) - 1:
                if tEntrada[0][i] == tEntrada[0][i+1]:
                    return False
        else:
            if tEntrada[0][i].isupper():
                return False
    
    for i in range(1, len(tEntrada[1]) - 1):
        if not tEntrada[1][i].isalpha():
            return False
        if tEntrada[1][i].isupper():
            return False
    if tEntrada[1][0] != "[" or tEntrada[1][6] != "]":
        return False
    
    for i in range(len(tEntrada[2])):
        if type(tEntrada[2][i]) != int:
            return False
        elif tEntrada[2][i] <= 0:
            return False
    
    return True

# 3.2.2 Função validar_cifra

    # Função auxiliar ordem_alfabetica, contribui para a organização e clareza da função validar_cifra

def ordem_alfabetica(sChar1, sChar2):
    lCadCarateres = [sChar1, sChar2]
    lAlfabetica = list(sorted(sChar1+sChar2))
    
    if lAlfabetica[0] == lCadCarateres[0]:
        return True
    
    return False

    # Função validar_cifra

def validar_cifra(sCifra, sSeqControlo):
    lAlfabeto = ["a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
    "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lVerificacao = []
    lComparacao = []
    iContador = 0
    sSeqControlo = sSeqControlo[1:6]
    
    for char1 in sSeqControlo:
        for char2 in sCifra:
            if char1 == char2:
                iContador += 1
        lVerificacao.append(iContador)
        iContador = 0
    
    for char1 in lAlfabeto:
        for char2 in sCifra:
            if char1 == char2:
                iContador += 1
        lComparacao.append(iContador)
        iContador = 0

    for i in range(len(lVerificacao)):    
        if i != len(lVerificacao) - 1:
            if lVerificacao[i] == lVerificacao[i+1] and not ordem_alfabetica(sSeqControlo[i], sSeqControlo[i+1]):
                return False

    lComparacao.sort(reverse = True)
    if lVerificacao != lComparacao[:5]:
        return False

    return True

# 3.2.2 Função filtrar_bdb

def filtrar_bdb(lEntradas):
    lEntradas_Incorretas = []

    if lEntradas == []:
        raise ValueError("filtrar_bdb: argumento invalido")
    for entrada in lEntradas:
        if not eh_entrada(entrada):
            raise ValueError("filtrar_bdb: argumento invalido")

    for entrada in lEntradas:
        if not validar_cifra(entrada[0], entrada[1]):
            lEntradas_Incorretas.append(entrada)
    
    return lEntradas_Incorretas

# 4. Desencriptação de dados

# 4.2.2 Função obter_num_seguranca

def obter_num_seguranca(tSeqSeguranca):
    lOrdenados = list(tSeqSeguranca)
    lOrdenados.sort(reverse = True)
    iNumSeguranca = lOrdenados[0] - lOrdenados[1]

    for i in range(1, len(lOrdenados)-1):
        if iNumSeguranca > lOrdenados[i] - lOrdenados[i+1] and lOrdenados[i] != lOrdenados[i+1]:
            iNumSeguranca = lOrdenados[i] - lOrdenados[i+1]
    
    return iNumSeguranca

# 4.2.3 Função decifrar_texto

    # Função auxiliar transformar_letra, contribui para a organização e clareza da função decifrar_texto

def transformar_letra(cLetra, iNumSeguranca, iPos):
    lAlfabeto = ["a", "b", "c", "d", "e", "f", "g", 
    "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
    "r", "s", "t", "u", "v", "w", "x", "y", "z"]

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

    # Função decifrar_texto

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

# 4.2.4 Função decifrar_bdb

def decifrar_bdb(lEntradas):
    lEntradasDecifradas = []
    if lEntradas == []:
        raise ValueError("decifrar_bdb: argumento invalido")
    for tEntrada in lEntradas:
        if not eh_entrada(tEntrada):
            raise ValueError("decifrar_bdb: argumento invalido")
    
    for tEntrada in lEntradas:
        lEntradasDecifradas.append(decifrar_texto(tEntrada[0], obter_num_seguranca(tEntrada[2])))

    return lEntradasDecifradas

# 5. Depuração de senhas

# 5.2.1 Função eh_utilizador

def eh_utilizador(dUtilizador):
    if type(dUtilizador) != dict:
        return False
    if len(dUtilizador) != 3:
        return False
    if not "name" in dUtilizador.keys() or not "pass" in dUtilizador.keys() or not "rule" in dUtilizador.keys():
        return False
    if type(dUtilizador["name"]) != str or type(dUtilizador["pass"]) != str:
        return False
    if dUtilizador["name"] == "" or dUtilizador["pass"] == "":
        return False
    if type(dUtilizador["rule"]) != dict:
        return False
    if not "vals" in dUtilizador["rule"].keys() or not "char" in dUtilizador["rule"].keys():
        return False
    if type(dUtilizador["rule"]["vals"]) != tuple or type(dUtilizador["rule"]["char"]) != str:
        return False
    if len(dUtilizador["rule"]["vals"]) != 2:
        return False
    if type(dUtilizador["rule"]["vals"][0]) != int or type(dUtilizador["rule"]["vals"][1]) != int:
        return False
    if dUtilizador["rule"]["vals"][0] < 1 or dUtilizador["rule"]["vals"][1] < 1:
        return False
    if not dUtilizador["rule"]["vals"][1] >= dUtilizador["rule"]["vals"][0]:
        return False
    if not dUtilizador["rule"]["char"].isalpha():
        return False
    if dUtilizador["rule"]["char"].isupper():
        return False
    return True

# 5.2.2 Função eh_senha_valida

    # Função auxiliar valida_vogais, contribui para a organização e clareza da função eh_senha_valida

def valida_vogais(sSenha):
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
    
    if iVogais > 2:
        return True

    return False

    # Função auxiliar valida_repeticoes, contribui para a organização e clareza da função eh_senha_valida

def valida_repeticoes(sSenha):
    for i in range(len(sSenha)-1):
        if sSenha[i] == sSenha[i+1]:    
            return True
    
    return False

    # Função eh_senha_valida

def eh_senha_valida(sSenha, dRegras):
    iContaChar = 0
    if valida_repeticoes(sSenha) and valida_vogais(sSenha):
        for char in sSenha:
            if char == dRegras["char"]:
                iContaChar += 1
        if dRegras["vals"][0] <= iContaChar <= dRegras["vals"][1]:
            return True
    
    return False

# 5.2.2 Função filtrar_senhas

def filtrar_senhas(lEntradas):
    lUtilizadoresCorrompidos = []
    if lEntradas == []:
        raise ValueError("filtrar_senhas: argumento invalido")
    for entrada in lEntradas:
        if not eh_utilizador(entrada):
            raise ValueError("filtrar_senhas: argumento invalido")
    
    for entrada in lEntradas:
        if not eh_senha_valida(entrada["pass"], entrada["rule"]):
            lUtilizadoresCorrompidos.append(entrada["name"])
    lUtilizadoresCorrompidos.sort()
    return lUtilizadoresCorrompidos
