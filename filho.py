import os
import pandas as pd
import requests
from io import BytesIO

def ler_caminhos_do_arquivo():
    caminhos = {}
    


    try:
        with open(f'paths', 'r') as arquivo_paths:
            linhas = arquivo_paths.readlines()

            for linha in linhas:
                chave, valor = linha.strip().split(': ')
                caminhos[chave] = valor

    except FileNotFoundError:
        print("O arquivo 'paths.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo 'paths.txt': {e}")

    return caminhos

def main():
    caminhos = ler_caminhos_do_arquivo()

    if caminhos:
        entry = caminhos.get('entry', '')
        exit = caminhos.get('exit', '')
        rir = caminhos.get('rir', '')
        return entry, exit, rir
        
    else:
        print("Não foi possível obter informações do arquivo 'paths.txt'.")
        print("Certifique-se de executar o script pai.py primeiro.")


entt, exitt, rirr =main()



def localizar_valor_em_coluna(x ):
    try:
        df = pd.read_excel(x, engine='openpyxl')

        # Convertendo a coluna 'rne' para o tipo de dados inteiro
        df['rne'] = pd.to_numeric(df['rne'], errors='coerce')
        df['rne'] = df['rne'].astype('Int64')  # Use 'Int64' para permitir valores nulos

        # Encontrar o último valor na coluna 'rne'
        ultimo_valor = df['rne'].iloc[-1]

        print(f"Último valor na coluna 'rne': {ultimo_valor +2}")
    except Exception as e:
        print(f"Erro ao processar a planilha: {e}")

    # Retorna None se o valor não for encontrado
    return None

# Exemplo de uso



localizar_valor_em_coluna(rirr)

if __name__ == "__main__":
    main()
