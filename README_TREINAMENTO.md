# Interface de Treinamento de IA com Índices Sequenciais

Este projeto implementa uma interface para treinar uma IA usando um sistema inovador de numeração sequencial para palavras. Em vez de usar embeddings complexos ou pares de perguntas/respostas, o sistema utiliza uma abordagem única baseada em números sequenciais para ensinar IA.

## Características

- Interface Streamlit para treinamento e teste
- Sistema de numeração sequencial único
- Preservação natural do contexto através da ordem
- Diferenciação automática de ocorrências
- Treinamento baseado em sequências numéricas

## Como usar

1. **Instalação das dependências**:
```bash
pip install -r requirements.txt
```

2. **Executar a interface**:
```bash
streamlit run app_indices_sequenciais.py
```

3. **Formato de Treinamento**:
O sistema aceita dados no seguinte formato:
```json
{
    "índice": "0",
    "Nome": "Nome do Treinamento",
    "total_tokens": 37,
    "Tokens individuais": {
        "0,1": "Primeira palavra",
        "0,2": "Segunda palavra",
        ...
        "0,37": "Última palavra"
    }
}
```

## Preservação de Sequências

Durante o treinamento, o sistema mantém a sequência exata das palavras através dos índices numéricos:

1. **Exemplo de Preservação**:
   - Treinamento: "Era uma vez em um reino distante"
   - Sequências: 0,1 até 0,7
   - Cada palavra mantém sua posição exata na sequência

2. **Derivação de Sequências**:
   - Quando uma sequência é repetida, mantém-se a ordem base
   - Exemplo: "Era uma vez em um reino de magia e fadas"
   - Sequências: 0,8 até 0,17
   - A ordem "Era uma vez em um reino" é preservada (0,8 até 0,13)
   - O que vem depois muda (0,14 até 0,17)

## Benefícios

- A IA aprende através da sequência numérica
- O contexto vem naturalmente da ordem
- Não precisa de análise sintática complexa
- Sistema simples e eficiente
- Base sólida para treinamento de IA


## Requisitos

- Python 3.8+
- Streamlit
- NumPy
- Outras dependências listadas no requirements.txt

## Contribuição

Este projeto é uma colaboração entre:

- **Lux Burnns**: Criação do conceito, desenvolvimento inicial e coordenadora do projeto
- **Canvas**: Interface gráfica e experiência do usuário
- **Cascade**: Implementação da lógica de treinamento e rede neural


## Licença

[MIT License](LICENSE)
