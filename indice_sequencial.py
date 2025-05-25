import json
import os
import re
from typing import Dict, List, Optional
from unidecode import unidecode

class IndiceSequencial:
    def __init__(self, arquivo_indice: str = 'indice_sequencial.json'):
        # Garante que o arquivo seja salvo em um local seguro
        self.arquivo_indice = os.path.join(os.path.dirname(os.path.abspath(__file__)), arquivo_indice)
        self.historias: Dict[str, dict] = {}
        self._carregar_indice()
    
    def adicionar_historia(self, titulo: str, texto: str) -> str:
        """Adiciona uma nova história ao índice"""
        # Gera um ID sequencial
        hist_id = str(len(self.historias))
        
        # Limpa o texto antes de tokenizar
        texto = self._limpar_texto(texto)
        
        # Tokeniza o texto
        resultado_tokenizacao = self._tokenizar_texto(texto, hist_id)
        
        # Cria o dicionário com a ordem correta dos campos
        self.historias[hist_id] = {
            'índice': hist_id,
            'Nome': titulo.strip(),
            'total_tokens': resultado_tokenizacao['total'],
            'Tokens individuais': resultado_tokenizacao['tokens']
        }
        
        # Salva a história
        self._salvar_indice()
        
        return hist_id
    
    def _limpar_texto(self, texto: str) -> str:
        """
        Limpa o texto mantendo apenas palavras e espaços
        """
        # Remove caracteres nulos e de controle
        texto = ''.join(c for c in texto if ord(c) > 31 or c in ['\n', '\r', '\t'])
        # Remove pontuações
        texto = re.sub(r'[.,!?;:\-"\']', ' ', texto)
        # Remove múltiplos espaços e quebras de linha
        texto = re.sub(r'[\s\n\r\t]+', ' ', texto)
        # Remove acentos usando unidecode
        texto = unidecode(texto)
        # Remove espaços extras no início e no fim
        return texto.strip()

    def _tokenizar_texto(self, texto, hist_id):
        """
        Divide o texto em palavras, mantendo pontuação como tokens separados
        e retorna um dicionário no formato solicitado, garantindo a ordem correta dos índices
        
        Args:
            texto: Texto a ser tokenizado
            hist_id: ID da história (obrigatório para gerar os índices)
            
        Returns:
            Dicionário com 'tokens' (dicionário formatado) e 'total' (quantidade de tokens)
        """
        import re
        # Limpa o texto mantendo pontuação
        texto = self._limpar_texto(texto)
        # Divide usando expressão regular para manter pontuação
        tokens = re.findall(r'\w+|[.,!?"]-', texto)
        
        # Cria o dicionário de tokens formatados
        tokens_formatados = {}
        
        # Garante que os índices estejam sempre em ordem sequencial
        for i, token in enumerate(tokens, 1):
            # Formato: "0,1", "0,2", etc.
            chave = f"{hist_id},{i}"
            tokens_formatados[chave] = token
            
        return {
            'tokens': tokens_formatados,
            'total': len(tokens_formatados)
        }
    
    def _salvar_indice(self):
        """Salva o índice no arquivo JSON usando json.dump"""
        try:
            # Garante que o diretório exista
            os.makedirs(os.path.dirname(self.arquivo_indice), exist_ok=True)
            
            with open(self.arquivo_indice, 'w', encoding='utf-8') as f:
                json.dump(self.historias, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Erro ao salvar índice: {str(e)}")
            return False
    
    
    def remover_historia(self, hist_id: str, reorganizar: bool = True) -> bool:
        """
        Remove uma história do índice
        
        Args:
            hist_id: ID da história a ser removida
            reorganizar: Se True, reorganiza os IDs após a remoção
            
        Returns:
            bool: True se a história foi removida, False caso contrário
        """
        if hist_id in self.historias:
            del self.historias[hist_id]
            
            # Reorganiza os IDs se necessário
            if reorganizar and self.historias:  # Só reorganiza se ainda houver histórias
                self._reorganizar_ids()
            else:
                self._salvar_indice()
                
            return True
        return False
    
    def _reorganizar_ids(self):
        """Reorganiza os IDs das histórias para serem sequenciais"""
        if not self.historias:
            return
            
        # Cria um novo dicionário com IDs sequenciais
        novas_historias = {}
        for novo_id, (_, hist) in enumerate(self.historias.items()):
            novas_historias[str(novo_id)] = hist
        
        self.historias = novas_historias
        self._salvar_indice()
        return self.historias
    
    def _carregar_indice(self):
        """Carrega o índice do arquivo JSON"""
        try:
            if os.path.exists(self.arquivo_indice):
                with open(self.arquivo_indice, 'r', encoding='utf-8') as f:
                    self.historias = json.load(f)
            else:
                self.historias = {}
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {str(e)}")
            self.historias = {}
        except Exception as e:
            print(f"Erro ao carregar índice: {str(e)}")
            self.historias = {}
    
    def obter_historia_formatada(self, hist_id: str) -> str:
        """
        Retorna a história formatada de forma legível
        
        Args:
            hist_id: ID da história a ser formatada
            
        Returns:
            str: Texto formatado da história
        """
        if hist_id not in self.historias:
            return "História não encontrada"
            
        historia = self.historias[hist_id]
        tokens = historia['Tokens individuais']
        
        # Ordena os tokens pelo índice
        tokens_ordenados = sorted(tokens.items(), key=lambda x: tuple(map(int, x[0].split(','))))
        
        # Junta as palavras em ordem
        texto = ' '.join(palavra for _, palavra in tokens_ordenados)
        
        # Remove espaços antes de pontuação para melhor formatação
        import re
        texto = re.sub(r'\s+([.,!?;:])', r'\1', texto)
        
        return texto
        
    def obter_historia_para_edicao(self, hist_id: str) -> dict:
        """
        Retorna os dados da história em um formato adequado para edição
        
        Args:
            hist_id: ID da história a ser editada
            
        Returns:
            dict: Dicionário com 'titulo' e 'texto' da história
        """
        if hist_id not in self.historias:
            return None
            
        historia = self.historias[hist_id]
        texto_formatado = self.obter_historia_formatada(hist_id)
        
        return {
            'titulo': historia['Nome'],
            'texto': texto_formatado
        }
    
    def atualizar_historia(self, hist_id: str, novo_titulo: str, novo_texto: str) -> bool:
        """
        Atualiza uma história existente garantindo a ordem correta dos índices (0,1, 0,2, 0,3, ...)
        
        Args:
            hist_id: ID da história a ser atualizada
            novo_titulo: Novo título da história
            novo_texto: Novo texto da história
            
        Returns:
            bool: True se a história foi atualizada com sucesso, False caso contrário
        """
        if hist_id not in self.historias:
            return False
            
        # Limpa o texto antes de tokenizar
        novo_texto = self._limpar_texto(novo_texto)
        
        # Remove a história para poder adicionar de volta
        self.remover_historia(hist_id, reorganizar=False)
        
        # Adiciona a história novamente para garantir a ordem correta dos índices
        resultado_tokenizacao = self._tokenizar_texto(novo_texto, hist_id)
        
        # Atualiza a história mantendo o ID original
        self.historias[hist_id] = {
            "índice": hist_id,
            "Nome": novo_titulo.strip(),
            "total_tokens": resultado_tokenizacao['total'],
            "Tokens individuais": resultado_tokenizacao['tokens']
        }
        
        self._salvar_indice()
        return True

# Exemplo de uso
if __name__ == "__main__":
    # Cria ou carrega o índice
    indice = IndiceSequencial()
    
    # Texto de exemplo
    texto = """Havia uma árvore muito especial em um jardim encantado. Ela era conhecida como a Árvore dos Desejos.
    Cada vez que alguém passava por ela e fazia um desejo sincero, a árvore fazia um milagre acontecer."""
    
    # Adiciona a história
    hist_id = indice.adicionar_historia("O segredo da Árvore Mágica", texto)
    
    # Mostra a história formatada
    print(indice.obter_historia_formatada(hist_id))
    
    # Mostra o JSON gerado
    print("\nVersão JSON:")
    print(json.dumps(indice.historias[hist_id], ensure_ascii=False, indent=2))
