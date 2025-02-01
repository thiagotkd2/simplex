import numpy as np

def simplex(tipo_problema:int, numero_variaveis:int, numero_restricoes:int, funcao_objetivo:list, restricoes:list):
    tamanho_coluna=numero_restricoes+numero_variaveis+1
    tamanho_linha = numero_restricoes+1
    

    matriz = np.zeros((tamanho_linha, tamanho_coluna))
            
    if(tipo_problema==-1):
        #min
        f_obj_np=np.array(funcao_objetivo, dtype=float)
        funcao_restricoes=np.array(restricoes, dtype=float)
        for i in range(0,numero_variaveis):
            matriz[0][i]=f_obj_np[i]
        matriz[0][numero_variaveis::] = 0
        print(funcao_restricoes)
        for i in range(1,tamanho_linha):
            for j in range(0, numero_variaveis):
                matriz[i][j] = -funcao_restricoes[i-1][j]
        
        for i in range(1,tamanho_linha):
            matriz[i][tamanho_coluna-1] = -funcao_restricoes[i-1][numero_variaveis]

        for i in range(1,tamanho_linha):
            matriz[i][numero_variaveis+i-1]=1

        while(1):
            coluna_pivot = np.argmin(matriz[0])

            # linha_escolhida
            # matriz[i][tamanho_coluna]/matriz[i][coluna_pivot]
            razoes = np.zeros((tamanho_linha-1))
            for i in range(1, tamanho_linha):
                razoes[i-1]=matriz[i][tamanho_coluna-1]/matriz[i][coluna_pivot]
                razoes[i-1]= float('inf') if razoes[i-1]<0 else razoes[i-1] # se for negativo, definir como inf


            linha_pivot = np.argmin(razoes)+1
            print(linha_pivot)
            print(coluna_pivot)

            matriz[linha_pivot] = matriz[linha_pivot]/matriz[linha_pivot][coluna_pivot] # linha_pivot/elemento_pivot
            print(matriz)
            linha_ja_calculada=np.zeros(tamanho_linha)
            linha_ja_calculada[linha_pivot] = 1 # linha pivo já calculada
            print(linha_ja_calculada)

            # matriz[i] - (matriz[i][coluna_pivot])*matriz[linha_pivot]
            for i in range(0,tamanho_linha):
                if linha_ja_calculada[i]==0:
                    matriz[i]=matriz[i] - (matriz[i][coluna_pivot])*matriz[linha_pivot]
            print(matriz)
            # for i in range(tamanho_linha):
            #     for j in range(tamanho_coluna):
            if(not np.any(matriz[0]<0)):
                break
    else:
        #max
        f_obj_np=np.array(funcao_objetivo, dtype=float)*-1
        funcao_restricoes=np.array(restricoes, dtype=float)
        for i in range(0,numero_variaveis):
            matriz[0][i]=f_obj_np[i]
        matriz[0][numero_variaveis::] = 0
        print(funcao_restricoes)
        for i in range(1,tamanho_linha):
            for j in range(0, numero_variaveis):
                matriz[i][j] = funcao_restricoes[i-1][j]
        
        for i in range(1,tamanho_linha):
            matriz[i][tamanho_coluna-1] = funcao_restricoes[i-1][numero_variaveis]

        for i in range(1,tamanho_linha):
            matriz[i][numero_variaveis+i-1]=1

        while(1):
            coluna_pivot = np.argmin(matriz[0])

            # linha_escolhida
            # matriz[i][tamanho_coluna]/matriz[i][coluna_pivot]
            razoes = np.zeros((tamanho_linha-1))
            for i in range(1, tamanho_linha):
                razoes[i-1]=matriz[i][tamanho_coluna-1]/matriz[i][coluna_pivot]
                razoes[i-1]= float('inf') if razoes[i-1]<0 else razoes[i-1] # se for negativo, definir como inf


            linha_pivot = np.argmin(razoes)+1
            print(linha_pivot)
            print(coluna_pivot)

            matriz[linha_pivot] = matriz[linha_pivot]/matriz[linha_pivot][coluna_pivot] # linha_pivot/elemento_pivot
            print(matriz)
            linha_ja_calculada=np.zeros(tamanho_linha)
            linha_ja_calculada[linha_pivot] = 1 # linha pivo já calculada
            print(linha_ja_calculada)

            # matriz[i] - (matriz[i][coluna_pivot])*matriz[linha_pivot]
            for i in range(0,tamanho_linha):
                if linha_ja_calculada[i]==0:
                    matriz[i]=matriz[i] - (matriz[i][coluna_pivot])*matriz[linha_pivot]
            print(matriz)
            # for i in range(tamanho_linha):
            #     for j in range(tamanho_coluna):
            if(not np.any(matriz[0]<0)):
                break
    return matriz[0][tamanho_coluna-1]
        
        



f = open("txt\\entrada.txt")
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

#f_obj_np=np.array(funcao_objetivo)
#func_obj_neg = np.multiply(-1, f_obj_np)
#print(func_obj_neg)
print(tipo_problema)

print(simplex(int(tipo_problema), int(numero_variaveis), int(numero_restricoes), funcao_objetivo, lista_restricoes))