# Ao longo deste projeto a notação utilizada na nomeação de variáveis 
# consiste na especificação do tipo da variável, representado pela sua
# letra inicial, seguido do seu nome. A título ilustrativo, uma variável
# "nome" do tipo string seria "sNome" e uma variável "profissoes" do tipo
# lista seria "lProfissoes".

# 1. Correção da documentação

# 1.2.1 Função corrigir_palavra

    # Função auxiliar elimina_surto, evita duplicação de código na função corrigir_palavra

def elimina_surto(lCadCarateres, i1, i2):
    """ corrigir_palavra: lista × inteiro × inteiro → booleano
    Esta função recebe uma lista e dois indices e avalia se o "surto de letras"
    se verifica, eliminando-o se isso acontecer.
    """
    bMudou = 0
    if lCadCarateres[i1].lower() == lCadCarateres[i2].lower() and lCadCarateres[i1] != lCadCarateres[i2]:
        lCadCarateres[i1] = 0
        lCadCarateres[i2] = 0
        bMudou = True

    return bMudou

    # Função corrigir_palavra

def corrigir_palavra(sCadCarateres):
    """ corrigir_palavra: cad. carateres → cad. carateres
    Esta função recebe uma palavra e elimina o "surto de letras" caso este exista
    """
    lCadCarateres = list(sCadCarateres)
    bMudou = True
    # A variavel bMudou e criada porque cada vez que eliminamos um par de letras correspondente
    # a um "surto" podemos ter criado outros pares, portanto é necessário rever a string mais uma vez.
    sCadCorrigida = ""
    while bMudou:
        bMudou = False
        for i in range(len(sCadCarateres) - 1):  
            if lCadCarateres[i] != 0 and lCadCarateres[i+1] != 0:
                iVerificaMudou = elimina_surto(lCadCarateres, i, i+1)
                if not iVerificaMudou == 0:
                    bMudou = iVerificaMudou
            elif lCadCarateres[i] != 0 and lCadCarateres[i+1] == 0:
                for j in range(i+2, len(sCadCarateres)):
                    if lCadCarateres[j] != 0:
                        iVerificaMudou = elimina_surto(lCadCarateres, i, j)
                        if not iVerificaMudou == 0:
                            bMudou = iVerificaMudou
                        break
   
    for i in range(len(sCadCarateres)):
        if lCadCarateres[i] != 0:
            sCadCorrigida += lCadCarateres[i]
    
    return sCadCorrigida

# 1.2.2 Função eh_anagrama

def eh_anagrama(sCadCarateres1, sCadCarateres2):
    """ eh_anagrama: cad. carateres × cad. carateres → booleano
    Esta função recebe duas palavras e verifica se são anagramas uma da outra
    """
    lCadCarateres1 = []
    lCadCarateres2 = []

    for char in sCadCarateres1:
        lCadCarateres1 += char.lower()
    for char in sCadCarateres2:
        lCadCarateres2 += char.lower()

    if sorted(lCadCarateres1) == sorted(lCadCarateres2):
        return True
    
    return False

# 1.2.3 Função corrigir_doc

def corrigir_doc(sCadCarateres):
    """ corrigir_doc: cad. carateres → cad. carateres
    Esta função recebe um texto, corrige as suas palavras e elimina 
    os anagramas que correspondem a palavras diferentes. Também verifica
    a validade do seu argumento.
    """
    sAuxiliar = ""
    sDocCorrigido = ""
    lCadCarateres = []
    lAnagramasVerificados = []
    # Como quando eliminamos os anagramas deixamos no texto as palavras
    # iguais, esta lista armazena os anagramas já verificados, para
    # evitar que a função tente eliminar anagramas de uma palavra cujos anagramas
    # já tenham sido removidos. Permite evitar repetição desnecessária.

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
                    if eh_anagrama(lCadCarateres[i], lCadCarateres[j]) and lCadCarateres[i].lower() != lCadCarateres[j].lower():
                        lCadCarateres[j] = 0
            lAnagramasVerificados.append(lCadCarateres[i])

    for e in lCadCarateres:
        if e != 0:
            sDocCorrigido += e
            sDocCorrigido += " "

    return sDocCorrigido.rstrip()

# 2. Descoberta do PIN

# 2.2.1 Função obter_posicao

def obter_posicao(sCarater, iInteiro):
    """ obter_posicao: cad. carateres × inteiro → inteiro
    Esta função recebe um caráter que corresponde a um movimento
    e um inteiro que corresponde a uma posição e calcula a nova posição
    """
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
    """ obter_digito: cad. carateres × inteiro → inteiro
    Esta função recebe uma sequência de movimentos
    e um inteiro que corresponde a uma posição e calcula a nova posição
    """
    iPosicaoFinal = iPosicaoInicial
    for e in sCadCarateres:
        iPosicaoFinal = obter_posicao(e, iPosicaoFinal)
    
    return iPosicaoFinal

# 2.2.3 Função obter_pin

def obter_pin(tMovimentos):
    """ obter_pin: tuplo → tuplo
    Esta função recebe um conjunto de sequências de movimentos
    e calcula o pin a que estes correspondem. Também verifica a validade
    do seu arguento.
    """
    iPosicao = 5
    lPin = []
    if type(tMovimentos) != tuple:
        raise ValueError("obter_pin: argumento invalido")
    elif len(tMovimentos) < 4 or len(tMovimentos) > 10:
        raise ValueError("obter_pin: argumento invalido")
    for string in tMovimentos:
        if len(string) < 1:
            raise ValueError("obter_pin: argumento invalido")
        for char in string:
            if char != "C" and char != "B" and char != "E" and char != "D":
                raise ValueError("obter_pin: argumento invalido")

    for char in tMovimentos:
        iPosicao = obter_digito(char, iPosicao)
        lPin.append(iPosicao)
    
    return tuple(lPin)

# 3. Verificação de dados

# 3.2.1 Função eh_entrada

def eh_entrada(uEntrada):
    """ eh_entrada: universal → booleano
    Esta função verifica se o argumento dado corresponde a uma entrada da BDB.
    """
    if type(uEntrada) != tuple:
        return False
    elif len(uEntrada) != 3:
        return False
    elif type(uEntrada[0]) != str or type(uEntrada[1]) != str or type(uEntrada[2]) != tuple:
        return False
    elif uEntrada[0] == "" or len(uEntrada[1]) != 7 or  len(uEntrada[2]) < 2:
        return False
    
    for i in range(len(uEntrada[0])):
        if not uEntrada[0][i].isalpha():
            if uEntrada[0][i] != "-" or i == 0 or i == len(uEntrada[0]) - 1:
                return False
            elif uEntrada[0][i] == "-" and i != len(uEntrada[0]) - 1:
                if uEntrada[0][i] == uEntrada[0][i+1]:
                    return False
        else:
            if uEntrada[0][i].isupper():
                return False
    
    for i in range(1, len(uEntrada[1]) - 1):
        if not uEntrada[1][i].isalpha():
            return False
        if uEntrada[1][i].isupper():
            return False
    if uEntrada[1][0] != "[" or uEntrada[1][6] != "]":
        return False
    
    for num in uEntrada[2]:
        if type(num) != int:
            return False
        elif num <= 0:
            return False
    
    return True

# 3.2.2 Função validar_cifra

    # Função auxiliar ordem_alfabetica, contribui para a organização e clareza da função validar_cifra

def ordem_alfabetica(sChar1, sChar2):
    """ ordem_alfabetica: cad. carateres × cad. carateres → booleano
    Esta função recebe dois carateres e verifica se foram introduzidos
    por ordem alfabética.
    """
    lCadCarateres = [sChar1, sChar2]
    lAlfabetica = list(sorted(sChar1+sChar2))
    
    if lAlfabetica[0] == lCadCarateres[0]:
        return True
    
    return False

    # Função validar_cifra

def validar_cifra(sCifra, sSeqControlo):
    """ validar_cifra: cad. carateres × cad. carateres → booleano
    Esta função recebe uma cifra e uma sequência de controlo
    e verifica se são coerentes.
    """
    lAlfabeto = ["a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
    "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lVerificacao = []
    lComparacao = []
    # Esta lista vai armazenar a frequência com que cada letra no alfabeto
    # consta na cifra. Serve para verificar se as letras que estão organizadas
    # na sequência de controlo são de facto as cinco mais frequentes na cifra.
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
    """ filtrar_bdb: lista → lista
    Esta função recebe entradas da BDB e identifica
    quais as entradas em que a sequência de controlo não é coerente
    com a cifra. Também verifica a validade do seu argumento.
    """
    lEntradas_Incorretas = []
    if type(lEntradas) != list:
        raise ValueError("filtrar_bdb: argumento invalido")
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
    """ obter_num_seguranca: tuplo → inteiro
    Esta função recebe uma sequência de números inteiros
    positivos e calcula o número de segurança.
    """
    lOrdenados = list(tSeqSeguranca)
    lOrdenados.sort(reverse = True)
    # Se a lista estiver organizada  por ordem decrescente,
    # apenas é necessário verificar a diferença entre números adjacentes.
    iNumSeguranca = lOrdenados[0] - lOrdenados[1]

    for i in range(1, len(lOrdenados)-1):
        if iNumSeguranca > lOrdenados[i] - lOrdenados[i+1] and lOrdenados[i] != lOrdenados[i+1]:
            iNumSeguranca = lOrdenados[i] - lOrdenados[i+1]
    
    return iNumSeguranca

# 4.2.3 Função decifrar_texto

    # Função auxiliar transformar_letra, contribui para a organização e clareza da função decifrar_texto

def transformar_letra(cLetra, iNumSeguranca, iPos):
    """ transformar_letra: cad. carateres × inteiro × inteiro → cad. carateres
    Esta função transforma uma letra de acordo com o valor
    do número de segurança e a sua posição no texto.
    """
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
    """ decifrar_texto: cad. carateres × inteiro → cad. carateres
    Esta função decifra uma cifra de acordo com o valor
    do número de segurança.
    """
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
    
    for char in lTextoDecifrado:
        sTextoDecifrado += char
    
    return sTextoDecifrado

# 4.2.4 Função decifrar_bdb

def decifrar_bdb(lEntradas):
    """ decifrar_bdb: lista → lista
    Esta função recebe entradas da BDB e decifra-as.
    Também verifica a validade do seu argumento.
    """
    lEntradasDecifradas = []

    if type(lEntradas) != list:
        raise ValueError("decifrar_bdb: argumento invalido")
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

def eh_utilizador(uUtilizador):
    """ eh_utilizador: universal → booleano
    Esta função verifica se o argumento corresponde a
    um utilizador da BDB.
    """
    if type(uUtilizador) != dict:
        return False
    if len(uUtilizador) != 3:
        return False
    if not "name" in uUtilizador.keys() or not "pass" in uUtilizador.keys() or not "rule" in uUtilizador.keys():
        return False
    if type(uUtilizador["name"]) != str or type(uUtilizador["pass"]) != str:
        return False
    if uUtilizador["name"] == "" or uUtilizador["pass"] == "":
        return False
    if type(uUtilizador["rule"]) != dict:
        return False
    if not "vals" in uUtilizador["rule"].keys() or not "char" in uUtilizador["rule"].keys():
        return False
    if type(uUtilizador["rule"]["vals"]) != tuple or type(uUtilizador["rule"]["char"]) != str:
        return False
    if len(uUtilizador["rule"]["vals"]) != 2 or len(uUtilizador["rule"]["char"]) != 1:
        return False
    if type(uUtilizador["rule"]["vals"][0]) != int or type(uUtilizador["rule"]["vals"][1]) != int:
        return False
    if uUtilizador["rule"]["vals"][0] < 1 or uUtilizador["rule"]["vals"][1] < 1:
        return False
    if  uUtilizador["rule"]["vals"][1] < uUtilizador["rule"]["vals"][0]:
        return False
    if not uUtilizador["rule"]["char"].isalpha():
        return False
    if uUtilizador["rule"]["char"].isupper():
        return False
    return True

# 5.2.2 Função eh_senha_valida

    # Função auxiliar valida_vogais, contribui para a organização e clareza da função eh_senha_valida

def valida_vogais(sSenha):
    """ valida_vogais: cad. carateres → booleano
    Esta função verifica se a senha contém pelo
    menos três vogais minúsculas.
    """
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
    """ valida_repeticoes: cad. carateres → booleano
    Esta função verifica se a senha contem pelo
    menos um caráter que apareça duas vezes consecutivas.
    """
    for i in range(len(sSenha)-1):
        if sSenha[i] == sSenha[i+1]:    
            return True
    
    return False

    # Função eh_senha_valida

def eh_senha_valida(sSenha, dRegras):
    """ eh_senha_valida: cad. carateres × dicionário → booleano
    Esta função verifica se a senha respeita as regras
    gerais e a regra individual.
    """
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
    """ filtrar_senhas: lista → lista
    Esta função recebe entradas da BDB e identifica
    quais as entradas em que a senha não respeita as regras.
    Também verifica a validade do seu argumento.
    """
    lUtilizadoresCorrompidos = []
    if type(lEntradas) != list:
        raise ValueError("filtrar_senhas: argumento invalido")
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
