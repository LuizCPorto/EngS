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