import networkx as nx 
import matplotlib.pyplot as plt
from collections import deque
import os 

class Grafo: 
    def __init__(self, arquivo):
        self.matrizes_adjacencia = self.ler_matrizes_adjacencia(arquivo)
    
    def ler_matrizes_adjacencia(self, arquivo):
        matrizes=[]
        with open(arquivo, 'r') as file:
            linhas = file.readlines()
            matriz_atual = []
            for linha in linhas:
                if linha.strip():
                    valores = [int(x) for x in linha.split()]
                    matriz_atual.append(valores)
                else:
                    if matriz_atual:
                        matrizes.append(matriz_atual)
                        matriz_atual = []
            if matriz_atual:
                matrizes.append(matriz_atual)
        return matrizes
    
    
def exibir_menu():
    print("Escolha uma opção:")
    print("1. Verificar se o grafo é conexo")
    print("2. Aplicar Busca em Largura ")
    print("3. Encontrar Bipartição")
    print("0. Sair")
    
arquivo = 'grafos.txt'
grafo = Grafo(arquivo)

continuar = True

while continuar:
    os.system('clear') or None
    exibir_menu()
    opcao = input("Opção: ")
    
    if opcao == "1":
        for idx, matriz in enumerate(grafo.matrizes_adjacencia, start=1):
            print(f"Matriz {idx}")
        matricula_escolhida = int(input("Digite o número da matriz que deseja utilizar: "))
        if 1 <= matricula_escolhida <= len(grafo.matrizes_adjacencia):
            matriz = grafo.matrizes_adjacencia[matricula_escolhida - 1]
            print(f"Matriz selecionada:{matricula_escolhida}")
            if grafo.verificar_conexo(matriz):
                print("O grafo é conexo.")
            else:
                print("O grafo não é conexo")
            grafo.plotar_grafo(matriz)
        else:
            print("Numero de matriz invalido.")
        input("Aperte enter para continuar...")
        
    elif opcao == "2":
        for idx, matriz in enumerate(grafo.matrizes_adjacencia, start=1):
            print(f"Matriz {idx}")
        matricula_escolhida = int(input("Digite o número da matriz que deseja utilizar: "))
        if 1 <= matricula_escolhida <= len(grafo.matrizes_adjacencia):
            matriz = grafo.matrizes_adjacencia[matricula_escolhida - 1]
            print(f"Matriz selecionada: {matricula_escolhida}")
            vertice_inicial = int(input("Digite o vértice inicial: "))
            print("Caminho em largura:")
            grafo.buscar_largura(matriz, vertice_inicial)
            grafo.plotar_grafo(matriz)
        else:
            print("Número de matriz inválido.")
        input("Pressione Enter para continuar...")

    elif opcao == "3":
        for idx, matriz in enumerate(grafo.matrizes_adjacencia, start=1):
            print(f"Matriz {idx}")
        matricula_escolhida = int(input("Digite o número da matriz que deseja utilizar: "))
        if 1 <= matricula_escolhida <= len(grafo.matrizes_adjacencia):
            matriz = grafo.matrizes_adjacencia[matricula_escolhida - 1]
            print(f"Matriz selecionada: {matricula_escolhida}")
            print("Encontrar bipartição:")
            grafo.encontrar_biparticao(matriz)
            grafo.plotar_grafo(matriz)
        else:
            print("Número de matriz inválido.")
        input("Pressione Enter para continuar...")

    elif opcao == "0":
        continuar = False

    else:
        print("Opção inválida. Por favor, digite uma opção válida.")
        input("Pressione Enter para continuar...")

        
    