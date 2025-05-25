import streamlit as st
from indice_sequencial import IndiceSequencial
import os
from collections import defaultdict
import json
from typing import Optional

# Inicializa o índice e estados da sessão
if 'indice' not in st.session_state:
    st.session_state.indice = IndiceSequencial()
    st.session_state.editando = False
    st.session_state.historia_editando = None

    # Adiciona uma história de exemplo se for a primeira execução
    if not st.session_state.indice.historias:
        texto_exemplo = """Era uma vez um reino distante onde a magia era real e os dragões voavam pelos céus.
        Neste reino, vivia um jovem aprendiz de mago que sonhava em se tornar o maior feiticeiro de todos os tempos."""
        st.session_state.indice.adicionar_historia("O Aprendiz de Mago", texto_exemplo)

# Interface
st.set_page_config(page_title="Índice Sequencial de Palavras", page_icon="🔢", layout="wide")
st.title("🔢 Índice Sequencial de Palavras")


def mostrar_formulario_historia(titulo_form: str, titulo: str = "", texto: str = "", botao: str = "Salvar",
                                hist_id: str = None):
    """Mostra o formulário para adicionar/editar uma história"""
    with st.form(f"form_{hist_id if hist_id else 'nova'}"):
        st.subheader(titulo_form)
        novo_titulo = st.text_input("Título da História", value=titulo)
        novo_texto = st.text_area("Texto da História", value=texto, height=200,
                                  help="Use linhas em branco para separar parágrafos")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.form_submit_button(botao):
                if novo_titulo and novo_texto:
                    if hist_id:  # Editando
                        if st.session_state.indice.atualizar_historia(hist_id, novo_titulo, novo_texto):
                            st.success("História atualizada com sucesso!")
                            st.session_state.editando = False
                            st.session_state.historia_editando = None
                            st.rerun()
                        else:
                            st.error("Erro ao atualizar a história")
                    else:  # Nova história
                        hist_id = st.session_state.indice.adicionar_historia(novo_titulo, novo_texto)
                        st.success(f"História salva!")
                        st.rerun()
                else:
                    st.error("Preencha todos os campos")

        with col2:
            if st.form_submit_button("Cancelar"):
                st.session_state.editando = False
                st.session_state.historia_editando = None
                st.rerun()


# Sidebar para adicionar/editar histórias
if st.session_state.editando:
    hist = st.session_state.indice.obter_historia_para_edicao(st.session_state.historia_editando)
    if hist:
        mostrar_formulario_historia(
            "✏️ Editar História",
            hist['titulo'],
            hist['texto'],
            "Atualizar História",
            st.session_state.historia_editando
        )
else:
    with st.sidebar:
        with st.expander("➕ Adicionar Nova História", expanded=True):
            mostrar_formulario_historia("Nova História")

# Conteúdo principal
if st.session_state.indice.historias:
    # Mostra informações básicas
    st.sidebar.subheader("📊 Informações")
    total_historias = len(st.session_state.indice.historias)
    st.sidebar.write(f"📚 **Total de Histórias:** {total_historias}")

    # Contagem total de palavras em todas as histórias
    total_palavras = sum(len(hist['Tokens individuais']) for hist in st.session_state.indice.historias.values())
    st.sidebar.write(f"📝 **Total de Palavras:** {total_palavras}")

    # Contagem de palavras únicas
    todas_palavras = []
    for hist in st.session_state.indice.historias.values():
        todas_palavras.extend(hist['Tokens individuais'].values())

    palavras_unicas = len(set(todas_palavras))
    st.sidebar.write(f"🔤 **Palavras Únicas:** {palavras_unicas}")

    # Porcentagem de palavras únicas
    if total_palavras > 0:
        porcentagem_unicas = (palavras_unicas / total_palavras) * 100
        st.sidebar.write(f"📊 **Taxa de Palavras Únicas:** {porcentagem_unicas:.1f}%")

    # Mostra a lista de histórias
    st.sidebar.subheader("📚 Histórias")
    historias = list(st.session_state.indice.historias.items())

    for idx, (hist_id, hist) in enumerate(historias):
        col1, col2, col3 = st.sidebar.columns([3, 1, 1])
        with col1:
            if st.button(f"{hist['Nome']}", key=f"hist_{hist_id}", use_container_width=True):
                st.session_state.historia_selecionada = hist_id
        with col2:
            if st.button("✏️", key=f"edit_{hist_id}", help=f"Editar '{hist['Nome']}'", use_container_width=True):
                st.session_state.editando = True
                st.session_state.historia_editando = hist_id
                st.rerun()
        with col3:
            if st.button("🗑️", key=f"del_{hist_id}", help=f"Excluir '{hist['Nome']}'", type="secondary",
                         use_container_width=True):
                if st.session_state.indice.remover_historia(hist_id):
                    st.sidebar.success(f"História '{hist['Nome']}' removida!")
                    st.rerun()
                else:
                    st.sidebar.error("Erro ao remover a história")

    # Seleciona uma história para visualizar
    if st.session_state.indice.historias:
        hist_id = st.selectbox(
            "Selecione uma história para visualizar:",
            options=list(st.session_state.indice.historias.keys()),
            format_func=lambda x: f"{x}: {st.session_state.indice.historias[x]['Nome']}"
        )
    else:
        st.warning("Nenhuma história disponível.")
        st.stop()

    if hist_id:
        # Mostra o título da história com botão de exclusão
        col1, col2 = st.columns([10, 1])
        with col1:
            st.header(st.session_state.indice.historias[hist_id]['Nome'])
        with col2:
            if st.button("🗑️", key=f"del_hist_{hist_id}", help="Excluir esta história", type="secondary"):
                if st.session_state.indice.remover_historia(hist_id):
                    st.success(f"História removida com sucesso!")
                    st.rerun()
                else:
                    st.error("Erro ao remover a história")

        # Mostra o JSON formatado manualmente para manter a ordem correta
        historia = st.session_state.indice.historias[hist_id]
        json_str = '{\n'
        json_str += f'"índice":"{historia["índice"]}"\n'
        json_str += f'"Nome":"{historia["Nome"]}"\n'
        json_str += f'"total_tokens":{historia["total_tokens"]}\n'

        # Adiciona os tokens em ordem
        json_str += '"Tokens individuais":{\n'
        tokens = []
        for i in range(1, len(historia['Tokens individuais']) + 1):
            chave = f"{hist_id},{i}"
            if chave in historia['Tokens individuais']:
                tokens.append(f'"{chave}":"{historia["Tokens individuais"][chave]}"')

        json_str += '\n'.join(tokens)
        json_str += '\n}\n}'

        st.code(json_str, language='json')

        # Estatísticas da história atual
        st.subheader("📊 Estatísticas da História")
        historia = st.session_state.indice.historias[hist_id]
        tokens = list(historia['Tokens individuais'].values())
        total_palavras = len(tokens)
        palavras_unicas = len(set(tokens))
        palavras_repetidas = total_palavras - palavras_unicas

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de palavras", total_palavras)
        with col2:
            st.metric("Palavras únicas", palavras_unicas)
        with col3:
            st.metric("Palavras repetidas", palavras_repetidas)

        # Palavras mais comuns
        contagem_palavras = defaultdict(int)
        for palavra in tokens:
            contagem_palavras[palavra] += 1

        palavras_comuns = sorted(contagem_palavras.items(), key=lambda x: x[1], reverse=True)[:10]

        st.subheader("🔠 Palavras mais comuns")
        for palavra, contagem in palavras_comuns:
            st.write(f"- {palavra}: {contagem} ocorrência{'s' if contagem > 1 else ''}")

        # Estatísticas gerais de todas as histórias
        st.subheader("📊 Estatísticas Gerais")
        todas_as_palavras = []
        for hist in st.session_state.indice.historias.values():
            todas_as_palavras.extend(hist['Tokens individuais'].values())

        if len(st.session_state.indice.historias) > 1:
            total_geral = len(todas_as_palavras)
            unicas_geral = len(set(todas_as_palavras))
            repetidas_geral = total_geral - unicas_geral

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total geral de palavras", total_geral)
            with col2:
                st.metric("Palavras únicas totais", unicas_geral)
            with col3:
                st.metric("Palavras repetidas totais", repetidas_geral)

            # Palavras mais comuns em todas as histórias
            contagem_geral = defaultdict(int)
            for palavra in todas_as_palavras:
                contagem_geral[palavra] += 1

            palavras_comuns_geral = sorted(contagem_geral.items(), key=lambda x: x[1], reverse=True)[:10]

            st.subheader("🔠 Palavras mais comuns (todas as histórias)")
            for palavra, contagem in palavras_comuns_geral:
                st.write(f"- {palavra}: {contagem} ocorrência{'s' if contagem > 1 else ''}")

        # Botão para exportar os dados
        st.download_button(
            label="📥 Exportar Dados",
            data=json.dumps(st.session_state.indice.historias, ensure_ascii=False, indent=2),
            file_name=f"indice_historias_{hist_id}.json",
            mime="application/json"
        )
else:
    st.info("Nenhuma história disponível. Adicione uma história usando o painel lateral.")

