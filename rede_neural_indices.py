import numpy as np
from typing import Dict, List

class RedeNeuralIndices:
    def __init__(self, tamanho_sequencia: int = 100):
        """
        Inicializa a rede neural para aprender com índices sequenciais
        Args:
            tamanho_sequencia: Tamanho máximo das sequências
        """
        self.tamanho_sequencia = tamanho_sequencia
        
        # Inicializa pesos simples
        self.pesos = np.random.randn(tamanho_sequencia, 1) * 0.1
        
    def processar_sequencia(self, sequencia: Dict[str, str]) -> np.ndarray:
        """
        Processa uma sequência de índices sequenciais
        Args:
            sequencia: Dicionário com os índices sequenciais e palavras
        Returns:
            Array numpy com os índices numéricos ordenados
        """
        # Ordena os índices sequenciais
        def ordenar_indice(indice: str) -> tuple:
            # Separa o índice em partes
            partes = indice.split(',')
            # Converte cada parte para float, mantendo a derivação
            valores = []
            for parte in partes:
                try:
                    valor = float(parte)
                    valores.append(valor)
                except ValueError:
                    # Se tiver derivação (ex: 0.01), mantém como string
                    valores.append(parte)
            return tuple(valores)
        
        indices_ordenados = sorted(sequencia.keys(), key=ordenar_indice)
        
        # Converte para array numpy
        indices = np.array([
            float(x.replace(',', '.')) for x in indices_ordenados
        ])
        
        # Garante que a sequência tenha o tamanho correto
        if len(indices) < self.tamanho_sequencia:
            indices = np.pad(indices, (0, self.tamanho_sequencia - len(indices)), 'constant')
        elif len(indices) > self.tamanho_sequencia:
            indices = indices[:self.tamanho_sequencia]
        
        return indices
    
    def calcular_saida(self, entrada: np.ndarray) -> float:
        """
        Calcula a saída da rede para uma entrada
        Args:
            entrada: Array com os índices sequenciais
        Returns:
            Valor de saída da rede
        """
        # Usa a média dos índices como saída inicial
        saida = np.mean(entrada)
        return saida
    
    def treinar(self, sequencias: List[Dict[str, str]], epochs: int = 100):
        """
        Treina a rede neural
        Args:
            sequencias: Lista de sequências no formato correto
            epochs: Número de épocas de treinamento
        """
        print(f"Iniciando treinamento com {len(sequencias)} sequências")
        
        for epoch in range(epochs):
            erro_total = 0
            
            for sequencia in sequencias:
                # Processa a sequência
                entrada = self.processar_sequencia(sequencia['Tokens individuais'])
                
                # Calcula a saída
                saida = self.calcular_saida(entrada)
                
                # O erro é simplesmente a diferença entre a saída e a entrada
                erro = np.mean((saida - entrada) ** 2)
                erro_total += erro
                
                # Atualiza os pesos usando gradiente descendente simples
                # Simplificando para apenas ajustar um peso único
                self.pesos = np.mean(entrada)
            
            # Calcula o erro médio
            erro_medio = erro_total / len(sequencias)
            
            # Mostra o progresso
            print(f"\nÉpoca {epoch + 1}")
            print(f"Erro médio: {erro_medio:.6f}")
    
    def prever(self, sequencia: Dict[str, str]) -> float:
        """
        Faz uma previsão com base na sequência
        Args:
            sequencia: Dicionário com os índices sequenciais e palavras
        Returns:
            Valor de saída da rede
        """
        # Processa a sequência
        entrada = self.processar_sequencia(sequencia)
        
        # Calcula a saída
        saida = self.calcular_saida(entrada)
        
        return saida
