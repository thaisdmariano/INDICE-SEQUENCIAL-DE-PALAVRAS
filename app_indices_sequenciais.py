import streamlit as st
from rede_neural_indices import RedeNeuralIndices
import json
from typing import Dict

def processar_texto_para_indices(texto: str) -> Dict[str, str]:
    """
    Processa um texto em índices sequenciais com derivação
    Args:
        texto: Texto a ser processado
    Returns:
        Dicionário com os índices sequenciais e suas derivações
    """
    # Divide o texto em palavras
    palavras = texto.split()
    
    # Cria o dicionário de índices sequenciais
    indices = {}
    
    # Mantém um registro das sequências encontradas
    sequencias = {}
    
    # Processa o texto palavra por palavra
    for i, palavra in enumerate(palavras, 1):
        # Cria o índice base
        indice_base = f"0,{i}"
        
        # Verifica se já existe uma sequência similar
        sequencia_atual = " ".join(palavras[:i])
        
        # Se é a primeira ocorrência, usa índice base
        if sequencia_atual not in sequencias:
            indices[indice_base] = palavra
            sequencias[sequencia_atual] = [indice_base]
        else:
            # Se já existe, cria uma derivação
            ultima_sequencia = sequencias[sequencia_atual][-1]
            ultima_parte = ultima_sequencia.split(',')[-1]
            
            # Cria um índice derivado
            indice_derivado = f"0,{i}.{float(ultima_parte) + 0.1}"
            indices[indice_derivado] = palavra
            sequencias[sequencia_atual].append(indice_derivado)
    
    return indices

def processar_indices_para_teste(indices: Dict[str, str], texto_teste: str) -> Dict[str, str]:
    """
    Processa os índices para teste, mantendo a sequência e criando derivações baseadas no contexto
    Args:
        indices: Dicionário de índices sequenciais do treinamento
        texto_teste: Texto para teste
    Returns:
        Dicionário com os índices processados para teste
    """
    # Divide o texto de teste em palavras
    palavras_teste = texto_teste.split()
    
    # Cria o dicionário de índices para teste
    indices_teste = {}
    
    # Mantém um registro das palavras já vistas
    palavras_vistas = {}
    
    # Processa o texto de teste palavra por palavra
    for i, palavra in enumerate(palavras_teste, 1):
        # Cria o índice base
        indice_base = f"0,{i}"
        
        # Verifica se a palavra já foi vista
        if palavra in palavras_vistas:
            # Cria uma derivação baseada na ocorrência anterior
            ultima_ocorrencia = palavras_vistas[palavra]
            nova_ocorrencia = ultima_ocorrencia + 1
            palavras_vistas[palavra] = nova_ocorrencia
            
            # Cria o índice derivado
            indice_derivado = f"0,{i}.{nova_ocorrencia}"
            indices_teste[indice_derivado] = palavra
        else:
            # Primeira ocorrência da palavra
            palavras_vistas[palavra] = 1
            indices_teste[indice_base] = palavra
    
    return indices_teste
    
    return indices_teste

# Removendo a função duplicada

def processar_json_indices(json_str: str) -> Dict:
    """
    Processa o JSON de índices sequenciais
    Args:
        json_str: String com o JSON formatado
    Returns:
        Dicionário com os índices sequenciais
    """
    try:
        # Carrega o JSON
        dados = json.loads(json_str)
        
        # Verifica se tem todos os campos necessários
        campos_obrigatorios = ['índice', 'Nome', 'total_tokens', 'Tokens individuais']
        if not all(campo in dados for campo in campos_obrigatorios):
            raise ValueError("JSON incompleto. Verifique se todos os campos estão presentes.")
            
        # Retorna os tokens individuais
        return dados['Tokens individuais']
    except json.JSONDecodeError:
        raise ValueError("JSON inválido. Por favor, verifique o formato.")

def main():
    st.title("Treinamento de I.A por meio de Índices Sequenciais de Palavras")
    
    # Explicação do sistema
    st.write("""
    Este sistema treina uma I.A. usando índices sequenciais de palavras. 
    Cada palavra recebe um índice único baseado em sua posição, permitindo 
    que a máquina aprenda o contexto através da ordem das palavras.
    """)
    
    # Área para inserir o JSON
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Treinamento")
        json_input = st.text_area(
            "Coloque seu índice formatado em JSON aqui:",
        """{
    \"índice\":\"0\",
    \"Nome\":\"O Aprendiz de Mago\",
    \"total_tokens\":37,
    \"Tokens individuais\":{
        \"0,1\":\"Era\",
        \"0,2\":\"uma\",
        \"0,3\":\"vez\",
        \"0,4\":\"um\",
        \"0,5\":\"reino\",
        \"0,6\":\"distante\",
        \"0,7\":\"onde\",
        \"0,8\":\"a\",
        \"0,9\":\"magia\",
        \"0,10\":\"era\",
        \"0,11\":\"real\",
        \"0,12\":\"e\",
        \"0,13\":\"os\",
        \"0,14\":\"dragoes\",
        \"0,15\":\"voavam\",
        \"0,16\":\"pelos\",
        \"0,17\":\"ceus\",
        \"0,18\":\"Neste\",
        \"0,19\":\"reino\",
        \"0,20\":\"vivia\",
        \"0,21\":\"um\",
        \"0,22\":\"jovem\",
        \"0,23\":\"aprendiz\",
        \"0,24\":\"de\",
        \"0,25\":\"mago\",
        \"0,26\":\"que\",
        \"0,27\":\"sonhava\",
        \"0,28\":\"em\",
        \"0,29\":\"se\",
        \"0,30\":\"tornar\",
        \"0,31\":\"o\",
        \"0,32\":\"maior\",
        \"0,33\":\"feiticeiro\",
        \"0,34\":\"de\",
        \"0,35\":\"todos\",
        \"0,36\":\"os\",
        \"0,37\":\"tempos\"
    }
}""",
        height=400
    )
    
    # Área de Teste
    with col2:
        st.header("Teste da IA")
        
        # Área para inserir texto de teste
        texto_teste = st.text_area(
            "Digite um texto para testar a IA:",
            "Era uma vez um reino...",
            height=200
        )
        
        # Botão para testar
        if st.button("Testar IA"):
            if 'rede_treinada' not in st.session_state:
                st.error("Por favor, treine uma rede primeiro!")
                return
            
            try:
                # Processa o texto de teste com derivação
                indices_teste = processar_indices_para_teste(
                    st.session_state['indices_treinamento'],
                    texto_teste
                )
                
                # Faz a previsão
                saida = st.session_state['rede_treinada'].prever(indices_teste)
                
                # Mostra o resultado
                st.write("\nResultado do teste:")
                st.write(f"Saída da IA: {saida}")
                
                # Mostra os índices processados
                st.write("\nÍndices processados:")
                for indice, palavra in sorted(indices_teste.items()):
                    st.write(f"Índice {indice}: {palavra}")
                
                # Mostra a sequência completa
                st.write("\nSequência completa:")
                for indice, palavra in sorted(indices_teste.items()):
                    st.write(palavra, end=" ")
                st.write()
                
                # Mostra a derivação dos índices
                st.write("\nDerivação dos índices:")
                for indice in sorted(indices_teste.keys()):
                    if '.' in indice:
                        base, derivacao = indice.split('.')
                        st.write(f"Índice {indice} é derivação de {base}")
            except Exception as e:
                st.error(f"Erro ao processar o teste: {str(e)}")
        
    # Botão para processar
    if st.button("Treinar Rede"):
        try:
            # Processa o JSON
            indices = processar_json_indices(json_input)
            
            # Cria a sequência no formato correto
            sequencia = {
                "índice": "0",  # Índice pai do "livro"
                "Nome": "Sequência Carregada",
                "total_tokens": len(indices),
                "Tokens individuais": indices
            }
            
            # Salva os índices do treinamento
            st.session_state['indices_treinamento'] = indices
            
            # Cria a rede neural
            rede = RedeNeuralIndices(tamanho_sequencia=100)
            
            # Treina com a sequência
            st.write("\nIniciando treinamento...")
            rede.treinar([sequencia], epochs=10)
            
            # Mostra os índices processados
            st.write("\nÍndices Processados:")
            for indice, palavra in sorted(indices.items()):
                st.write(f"Índice {indice}: {palavra}")
            
            # Faz uma previsão
            st.write("\nFazendo previsão...")
            saida = rede.prever(indices)
            st.write(f"Saída da rede: {saida}")
            
            # Salva a rede treinada
            st.session_state['rede_treinada'] = rede
            st.success("Rede treinada com sucesso!")
        except ValueError as e:
            st.error(f"Erro ao processar JSON: {str(e)}")
            return
            
            # Mostra os índices processados
            st.write("\nÍndices Processados:")
            for indice, palavra in sorted(indices.items()):
                st.write(f"Índice {indice}: {palavra}")
            
            # Cria a rede neural
            rede = RedeNeuralIndices(tamanho_sequencia=100)
            
            # Treina com a sequência
            st.write("\nIniciando treinamento...")
            rede.treinar([sequencia], epochs=10)
            
            # Faz uma previsão
            st.write("\nFazendo previsão...")
            saida = rede.prever(indices)
            st.write(f"Saída da rede: {saida}")
            
            # Salva a rede treinada
            st.session_state['rede_treinada'] = rede
            st.success("Rede treinada com sucesso!")
        
        # Mostra os índices processados
        st.write("\nÍndices Processados:")
        for indice, palavra in sorted(indices.items()):
            st.write(f"Índice {indice}: {palavra}")
        
        # Cria a rede neural
        rede = RedeNeuralIndices(tamanho_sequencia=100)
        
        # Treina com a sequência
        st.write("\nIniciando treinamento...")
        rede.treinar([sequencia], epochs=10)
        
        # Faz uma previsão
        st.write("\nFazendo previsão...")
        saida = rede.prever(indices)
        st.write(f"Saída da rede: {saida}")
        
        # Cria a rede neural
        rede = RedeNeuralIndices(tamanho_sequencia=100)
        
        # Treina com a sequência
        st.write("\nIniciando treinamento...")
        rede.treinar([sequencia], epochs=10)
        
        # Mostra os índices processados
        st.write("\nÍndices Processados:")
        for indice, palavra in indices.items():
            st.write(f"Índice {indice}: {palavra}")
        
        # Faz uma previsão
        st.write("\nFazendo previsão...")
        saida = rede.prever(indices)
        st.write(f"Saída da rede: {saida}")

if __name__ == "__main__":
    main()
