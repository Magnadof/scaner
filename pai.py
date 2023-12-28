import subprocess
def salvar_caminhos_em_arquivo(entry, exit, rir, nome_arquivo_saida):
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        arquivo_saida.write(f'entry: {entry}\n')
        arquivo_saida.write(f'exit: {exit}\n')
        arquivo_saida.write(f'rir: {rir}\n')

    print(f'Os caminhos foram salvos no arquivo: {nome_arquivo_saida}')

# Exemplo de uso
entry = input('\033[93mCopy and paste the input path of the files:\n\n\033[0m')
exit = input('\033[93mAdd to Output Folder:\n\n\033[0m')
rir = input('\033[93mCopy and paste the path of the RIR folder:\n\n\033[0m')
nome_arquivo_saida = 'paths'

salvar_caminhos_em_arquivo(entry, exit, rir, nome_arquivo_saida)
subprocess.run(['python', 'filho.py'])

