import os

def modificar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    for i in range(len(linhas)):
        linhas[i] = linhas[i].replace('pau', 'SP')
        linhas[i] = linhas[i].replace('br', 'AP')
    
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)

# Obtém o caminho do diretório onde o script está localizado
diretorio_atual = os.path.dirname(os.path.realpath(__file__))

# Obtém uma lista de todos os arquivos .lab no diretório
arquivos_lab = [f for f in os.listdir(diretorio_atual) if f.endswith('.lab')]

# Modifica cada arquivo .lab
for arquivo_lab in arquivos_lab:
    caminho_arquivo = os.path.join(diretorio_atual, arquivo_lab)
    modificar_arquivo(caminho_arquivo)

print("Modificações concluídas.")
