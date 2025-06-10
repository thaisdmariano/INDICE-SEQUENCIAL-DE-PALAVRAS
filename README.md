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


## Mais sobre o Insepa:

# 📝 INSEPA - Índice Sequencial de Palavras

## INTRODUÇÃO

O **INSEPA**, criado em **2025** por **Lux Burnns**, é muito mais que um sistema de indexação. Ele se assemelha a um livro digital que une a **linguagem natural** (Português BR) à **matemática** para ordenar palavras e preservar o contexto de frases inseridas em parágrafos. Para isso, o sistema cria um **índice mãe** (que representa o título ou o bloco principal do conteúdo) e, a partir dele, gera identificadores únicos – os **índices filhos** – que são formados pela combinação do índice mãe com um atributo individualizador, garantindo que se preserve o contexto daquele trecho.

> **Exemplo:**  
> **O SOL E O MUNDO** (0 ÍNDICE MÃE)  
>  
> _O 0.1 sol0.2 é0.3 amarelo0.4 .0.5_  
>  
> Aqui, o ponto **0.5** determina o contexto: "Cor do Sol".  
>  
> Da mesma forma, cada ponto finalizador em determinadas sequências (como 0.11, 0.17, etc.) define o contexto daquela sequência.

---

## OS 6 FUNDAMENTOS DO INSEPA

O INSEPA se fundamenta em 6 princípios que auxiliam na extração e organização do contexto dos textos.

### 1. CHAVES DE ENTRADA  
- **Definição:** São sequências com estrutura idêntica, que se repetem em todos os parágrafos.  
- **Características:**  
  - Iniciam antes ou depois do ponto finalizador ([. ou !]).  
  - Podem vir acompanhadas de um ponto ativador (ex.: `,`, `...`, `?`, `:`, `•`, `;`).  
  - Sempre começam com maiúsculas e seguem com minúsculas.  
  - Servem como ponto de partida dominante para cada sequência.  
- **Exemplo Simplificado do Sol:**  
  ```plaintext
  "O 0.1 sol 0.2 é 0.3 amarelo 0.4 . 0.5
   O 0.6 sol 0.7 queima 0.8 a0.9 pele 0.10 . 0.11
   O 0.12 sol 0.13 é 0.14 brilhante 0.15 . 0.16"
  ```
  As chaves de entrada são, por exemplo, os conjuntos: **0.1, 0.2** da sequência 1; **0.6, 0.7** da sequência 2; **0.12, 0.13** da sequência 3 – que quando combinadas formam sempre "O Sol".

---

### 2. SUBCHAVES  
- **Definição:** São sequências menores que se repetem, porém menos frequentemente que as chaves de entrada – atuando em um papel secundário na hierarquia.  
- **Características:**  
  - Formadas pelo mesmo conjunto de índices iniciais (antes ou depois do ponto finalizador).  
  - Podem vir acompanhadas de um ponto ativador.
  - Sempre começam com maiúsculas, seguidas de minúsculas.
  - Servem de complemento à chave de entrada, mas com uma ocorrência menor (recessivas).
- **Exemplo no Sol:**  
  ```plaintext
  "O sol" – Ocorrência 1, 2 e 3 (Chave de Entrada dominante)  
  "O sol é" – Ocorrência 1 e 2 (Subchave, que se repete em menor quantidade)
  ```
  Assim, "O sol" aparece mais vezes, enquanto "O sol é" aparece apenas para complementar alguns contextos.

---

### 3. CHAVE FANTASMA  
- **Definição:** São sequências únicas que não se repetem ao longo do texto.  
- **Características:**  
  - Iniciam com letras ou palavras em maiúsculas e seguem com minúsculas (exceto nomes próprios).  
  - Surgem próximas de uma stopword.  
  - Respeitam a hierarquia, mas identificam conceitos únicos não encontrados em outras sequências.
- **Exemplo Complexo do Sol:**  
  ```plaintext
  Sequência 4: 0.18, 0.19  
  Sequência 5: 0.25, 0.26  
  Sequência 7: 0.35, 0.36  
  Sequência 8: 0.40, 0.41
  ```
  Essas combinações surgem apenas uma vez, formando um conjunto único.

---

## 4. FATORES

Os fatores definem as características adicionais de cada sequência e só podem ser ativados quando determinadas chaves (ou subchaves/chaves fantasmas) são "destrancadas".

### 4.1 FATOR DE ABERTURA  
- **Definição:** É o elemento que vem **imediatamente após** a **Chave de Entrada**.  
- **Exemplo Básico do Sol:**  
  ```plaintext
  [O 0.1 sol 0.2] (Chave de Entrada) → [é 0.3 amarelo 0.4] (Fator de Abertura)
  [O 0.6 sol 0.7] (Chave de Entrada) → [queima 0.8 a 0.9 pele] (Fator de Abertura)
  [O 0.12 Sol 0.13] (Chave de Entrada) → [é 0.14 brilhante 0.15] (Fator de Abertura)
  ```
- **Resumo das Características:**  
  - Sempre vêm depois da Chave de Entrada (sequência primária dominante).  
  - Podem ter um ponto ativador agregado à sequência.  
  - Geralmente começam com minúsculas e terminam com um ponto finalizador.  
  - Corresponderão à característica que define a essência da frase.

### 4.2 SUBFATOR  
- **Definição:** É o elemento que aparece **imediatamente após** a **Subchave** e é exclusivo dela.  
- **Exemplo:**  
  ```plaintext
  [O 0.1 sol 0.2 é 0.3] (Subchave) → [amarelo 0.4] (Subfator)
  [O 0.12 Sol 0.13 é 0.4] (Subchave) → [brilhante 0.15] (Subfator)
  ```
- **Resumo:**  
  - Exclusivo de cada Subchave.  
  - Pode ter um ponto ativador e segue as mesmas regras de formatação da sequência (inicia com minúsculas, exceto nomes próprios, e finaliza com um marcador finalizador).

### 4.3 FATOR F  
- **Definição:** Como as **Chaves Fantasma** são únicas, elas exigem um fator próprio – o **Fator F**.  
- **Exemplo no Sol:**  
  ```plaintext
  Sequência 4: Fator F composto por 0.20, 0.21  
  Sequência 5: Fator F composto por 0.27, 0.28  
  Sequência 7: Fator F composto por 0.37, 0.38  
  Sequência 8: Fator F composto por 0.42, 0.43
  ```
- **Resumo:**  
  - Sempre segue uma Chave Fantasma, mantendo seu próprio contexto singular.  
  - Regras de formatação semelhantes (inicia com minúsculas, finaliza com a pontuação finalizadora).

---

## 5. PONTUAÇÃO FINALIZADORA X PONTUAÇÃO ATIVADORA

No INSEPA, a pontuação tem um papel essencial para estruturar o significado:

### 5.1 Pontuação Finalizadora  
- **Definição:** São os símbolos que indicam o **fim** de uma sequência, consolidando os fundamentos (Chave + Fator, Subchave + Subfator, ou Chave Fantasma + Fator F).  
- **Exemplos no Sol:**  
  - **0.5, 0.11, 0.17, 0.24, 0.29, 0.34, 0.39, 0.44** – cada um desses pontos determina o encerramento da respectiva sequência.  
- **Função:**  
  - Indicam ao leitor que “é aqui que a frase acaba, pode seguir para a próxima.”

### 5.2 Pontuação Ativadora  
- **Definição:** São símbolos que **expressam emoção, dúvida ou continuidade narrativa**, mas que **não finalizam** a sequência.  
- **Exemplos:**  
  - `?` em "O 0.1 sol 0.2 é 0.3 amarelo ? 0.4" – expressa intriga ou questionamento.  
  - `...` em "O 0.1 sol 0.2 é 0.3 amarelo...0.4" – remete a uma pausa narrativa ou nostalgia.  
- **Observação:**  
  - Diferente dos pontos finalizadores, a pontuação ativadora não recebe índices.

---

## 6. CONTEXTO

O contexto é formado pela integração dos diferentes componentes da sequência. Em outras palavras, a combinação:

- **Chave de Entrada + Fator de Abertura**,  
- **Subchave + Subfator**, ou  
- **Chave Fantasma + Fator F**

determina o significado inteiro do trecho.

**Exemplos:**

1.  
```plaintext
[O 0.1 sol 0.2] (Chave de Entrada)
[é 0.3 amarelo 0.4] (Fator de Abertura)
.0.5  → Contexto: "Cor do Sol"
```

2.  
```plaintext
[O 0.6 sol 0.7] (Chave de Entrada)
[queima 0.8 a0.9 pele 0.10] (Fator de Abertura)
.0.11  → Contexto: "Perigo ligado ao sol"
```

3.  
```plaintext
[O 0.12 sol 0.13] (Chave de Entrada)
[aquece 0.14 o0.15 mundo0.16] (Fator de Abertura)
.0.17  → Contexto: "Sol e mundo"
```

4.  
```plaintext
[O 0.18 mundo0.19] (Chave Fantasma)
[é 0.20 azul0.21 e0.22 verde0.23] (Fator F)
.0.24  → Contexto: "Cores do mundo"
```

E assim por diante para as demais sequências.

---

## RESUMO

- **O INSEPA** é mais do que um sistema de indexação – é um livro digital que une a **linguagem natural** à **matemática** para entender e preservar o contexto de um conteúdo.
- **Índices Mãe** são os títulos que nomeiam os conteúdos (ex.: "O Sol e o Mundo").
- **Índices Filhos** compõem o conteúdo e derivam do índice mãe (ex.: "O: 0.1, 0.6, 0.12, 0.18, 0.30").
- **Ordenadores** funcionam como editores, organizando a estrutura do documento de forma linear, garantindo uma leitura da esquerda para a direita e respeitando as pontuações.
- O INSEPA possui uma hierarquia de pares para identificar padrões:
  1. **Chave de Entrada + Fator de Abertura**
  2. **Subchave + Subfator**
  3. **Chave Fantasma + Fator F**
- **Chaves de Entrada** são sequências idênticas dominantes (repetidas em todos os parágrafos).
- **Subchaves** são sequências recessivas que se repetem menos vezes.
- **Chaves Fantasma** são únicas e não se repetem, distinguindo-se por não terem elementos idênticos em outras sequências.
- **Fatores de Abertura**, **Subfatores** e **Fatores F** definem as características das sequências e só podem ser ativados pelas respectivas chaves.
- **Pontuações Finalizadoras** indicam o encerramento de uma sequência, enquanto **Pontuações Ativadoras** expressam continuidade ou emoção sem finalizar o trecho.

---

🚀 **INSEPA - Preservando o significado das palavras, uma sequência de cada vez.**  



## Site oficial:

https://insepacode.my.canva.site/insepa

## Aplicativo:

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
- **Cascade e Copilot**: Implementação da lógica de treinamento e rede neural


## Licença

Este projeto está licenciado sob a GNU Affero General Public License (AGPL) versão 3.0.

A AGPL v3.0 oferece proteção adicional comparada à GPL, especialmente para aplicações web e serviços online:

- **Proteção Adicional**: Garante que qualquer modificação em serviços online seja compartilhada
- **Controle Total**: Você mantém o controle sobre o código e suas modificações
- **Proteção contra Serviços**: Impede que serviços online usem seu código sem compartilhar as modificações
- **Transparência**: Garante que qualquer alteração em serviços online seja disponibilizada ao público



