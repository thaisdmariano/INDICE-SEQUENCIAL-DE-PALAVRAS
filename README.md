# Índice Sequencial de Palavras

Este projeto revoluciona o treinamento de IA através de um sistema inovador de numeração sequencial para palavras em textos. Em vez de usar embeddings complexos ou pares de perguntas/respostas, o sistema utiliza uma abordagem única baseada em números sequenciais para ensinar IA.

## Por que é Revolucionário?

1. **Aprendizado Natural**
   - A IA aprende tal como um humano aprende a ler
   - Não precisa de rótulos artificiais ou embeddings complexos
   - Aprende através da ordem natural das palavras

2. **Contexto Implícito**
   - Cada número representa uma posição única
   - A sequência numérica (0,1, 0,2, etc.) já estabelece relações
   - A IA aprende o contexto através da ordem

3. **Diferenciação Automática**
   - Mesma palavra em diferentes contextos recebe números diferentes
   - Exemplo: "O"=0,0 e "O"=0,4 são tratados como diferentes ocorrências
   - A IA entende que palavras com números diferentes têm contextos diferentes

4. **Eficiência e Escalabilidade**
   - Sistema simples e eficiente
   - Fácil de implementar e entender
   - Base sólida para treinamento de IA

## Por que Numeração Sequencial?

A numeração sequencial é fundamental para o treinamento de IA porque:

1. **Contexto Implícito**
   - Cada número representa uma posição única no texto
   - A sequência numérica (0,1, 0,2, etc.) já estabelece relações entre palavras
   - A IA aprende através da ordem natural das palavras

2.  **Simplicidade e Eficiência**
   - Não precisa de análise sintática complexa
   - Não requer embeddings multidimensionais
   - O sistema é direto e objetivo

## Características

- Numeração sequencial única para cada palavra
- Preservação natural do contexto através da ordem
- Diferenciação automática de ocorrências
- Sistema simples e eficiente

## Como usar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o exemplo:
```bash
python indice_sequencial.py
```

## Exemplo

Para o texto: "O Sol é amarelo."
- "O" recebe 0.1
- "sol" recebe 0.2
- "é" recebe 0.3
- "amarelo" recebe 0.4

Para o parágrafo: "O Sol é Amarelo. O Sol queima a pele. O Sol é brilhante."
- "O" recebe 0.1, 0.5, 0.10
- "sol" recebe 0.2, 0.6, 0.11
- "é" recebe 0.3, 0.12
- "amarelo" recebe 0.4
- "queima" recebe 0.7
- "a" recebe 0.8
- "pele" recebe 0.9
- "brilhante" recebe 0.12

O quê pode ser representado como:
- O
0.1
Sol
0.2
é
0.3
amarelo
0.4
O
0.5
Sol
0.6
queima
0.7
a
0.8
pele
0.9
O
0.10
Sol
0.11
é
0.12
brilhante.

Assim a máquina consegue fazer as diferenciações de contexto, sem o uso de cálculos vetoriais como aqueles presentes nos Embbendings.

## Benefícios

- Contexto implícito através da numeração
- Diferenciação automática de ocorrências
- Sistema simples e eficiente
- Fácil de implementar e entender
- Base sólida para treinamento de IA



## Site oficial:

https://tokenizador666.my.canva.site/indicesequencialdepalavras

#Aplicativo:

https://indice-sequencial-de-palavras-da-lux.streamlit.app/

## Requisitos

- Python 3.8+
- Streamlit
- NumPy
- Outras dependências listadas no requirements.txt

## Contribuição

Este projeto é uma colaboração entre:

- **Lux Burnns (Thaís D' Mariano)**: Criação do conceito, desenvolvimento inicial e coordenadora do projeto
- **Canvas**: Interface gráfica e experiência do usuário
- **Cascade**: Implementação da lógica de treinamento e rede neural

## Licença

[MIT License](LICENSE)



