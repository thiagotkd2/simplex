import numpy as np

def simplex(tipo_problema:int, numero_variaveis:int, numero_restricoes:int, funcao_objetivo:list, restricoes:list):
    tamanho_coluna=numero_restricoes+numero_variaveis+1
    tamanho_linha = numero_restricoes+1
    

    matriz = np.zeros((tamanho_linha, tamanho_coluna))
            
    if(tipo_problema==-1):
        #min
        print("asd")
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
        


        print(matriz)

        # for i in range(tamanho_linha):
        #     for j in range(tamanho_coluna):
        
        



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

simplex(int(tipo_problema), int(numero_variaveis), int(numero_restricoes), funcao_objetivo, lista_restricoes)