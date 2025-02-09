import numpy as np

def simplex(tipo_problema:int, numero_variaveis:int, numero_restricoes:int, funcao_objetivo:list, restricoes:list):
    quantidade_colunas=numero_restricoes+numero_variaveis+1
    quantidade_linhas = numero_restricoes+1
    
    matriz = np.zeros((quantidade_linhas, quantidade_colunas))

    ##### BLOCO DE MONTAGEM DO ESTADO INICIAL DA TABELA
    funcao_objetivo_np=np.array(funcao_objetivo, dtype=float)*-1
    print(funcao_objetivo_np)
    funcao_restricoes=np.array(restricoes, dtype=float)

    # preenchendo a linha Z
    matriz[0][0:numero_variaveis]=funcao_objetivo_np[0:numero_variaveis]
    matriz[0][numero_variaveis::] = 0
    print(funcao_restricoes)

    # pega todas restrições de funcao_restricoes e as coloca na matriz
    matriz[1:quantidade_linhas, :numero_variaveis] = funcao_restricoes[:quantidade_linhas-1, :numero_variaveis]

    # Preenche o lado direito do tableau 
    matriz[1::, quantidade_colunas-1]= funcao_restricoes[::,numero_variaveis]

    # Monta a identidade
    for i in range(1,quantidade_linhas):
        matriz[i][numero_variaveis+i-1]=1   

    # Fim do bloco de construcao inicial
    print(matriz)
    while((np.any(matriz[0]<0) and tipo_problema==1) or (np.any(matriz[0]>0) and tipo_problema==-1)):
        coluna_pivot = np.argmin(matriz[0]) if tipo_problema ==1 else np.argmax(matriz[0])

        razoes = np.zeros((quantidade_linhas-1))
        # escolher menor razao positiva
        for i in range(1, quantidade_linhas):
            razoes[i-1]=matriz[i][quantidade_colunas-1]/matriz[i][coluna_pivot] if not matriz[i][coluna_pivot]==0 else float('inf')
            razoes[i-1]= float('inf') if razoes[i-1]<0 else razoes[i-1] 
            # se for negativo, definir como inf

        linha_pivot = np.argmin((razoes))+1
        print(linha_pivot)
        print(coluna_pivot)

        # calcular nova linha pivot
        matriz[linha_pivot] = matriz[linha_pivot]/matriz[linha_pivot][coluna_pivot] if not matriz[linha_pivot][coluna_pivot] == 0 else float('inf') # linha_pivot/elemento_pivot
        print(matriz)
        linha_ja_calculada=np.zeros(quantidade_linhas)
        linha_ja_calculada[linha_pivot] = 1 # linha pivo já calculada
        print(linha_ja_calculada)

        # calcular as linhas restantes
        for i in range(0,quantidade_linhas):
            if linha_ja_calculada[i]==0:
                matriz[i]=matriz[i] - (matriz[i][coluna_pivot])*matriz[linha_pivot]
        print(matriz)
    return matriz[0][quantidade_colunas-1]
              
f = open("txt/entrada.txt")
linhas = f.read().split('\n')

tipo_problema = linhas[0]

numero_variaveis = linhas[1]

numero_restricoes = linhas[2]

funcao_objetivo = linhas[3].split()

# aplicar slice nas restricoes
restricoes = linhas[4::]

# transforma em array 2d as restricoes, retirando espacos em branco
lista_restricoes = [e.split() for e in restricoes]

# ao final temos:
# tres variaveis com a descricao do problema 
# (tipo de problema, numero de variaveis do problema, numero de restricoes)
# a funcao objetivo
# e uma lista com todas restricoes
# a partir disso, é possivel criar a matriz e aplicar o simplex

# consideracoes: 
# numero de variaveis de folga = numero de restricoes
# numero de colunas = numero de variaveis + numero de variaveis de folga + 1
# numero de linhas = numero de variaveis de folga + 1 
# tablea[linha][coluna]

#funcao_objetivo_np=np.array(funcao_objetivo)
#func_obj_neg = np.multiply(-1, funcao_objetivo_np)
#print(func_obj_neg)
print("o tipo "+tipo_problema)

print(simplex(int(tipo_problema), int(numero_variaveis), int(numero_restricoes), funcao_objetivo, lista_restricoes))
