import os

# Criando a pasta 'mod' se ela não existir
if not os.path.exists('mod'):
    os.makedirs('mod')

def processar_arquivo_lab(nome_arquivo):
    linhas_modificadas = []
    comeco, final, fonema = None, None, None
    vogal_anterior = None

    with open(nome_arquivo, 'r', encoding="utf8") as arquivo:
        for linha in arquivo:
            partes = linha.split()
            if len(partes) == 3:
                comeco, final, fonema = partes
                if fonema in ['a', 'e', 'i', 'o', 'u', 'an', 'en', 'in', 'on', 'un', 'eh', 'oh', 'ax', 'ae']:
                    if fonema == vogal_anterior:
                        final_vogal = final
                    else:
                        if vogal_anterior:
                            linhas_modificadas.append(f'{comeco_vogal} {final_vogal} {fonema_vogal}\n')
                        comeco_vogal = comeco
                        final_vogal = final
                        fonema_vogal = fonema
                    vogal_anterior = fonema
                else:
                    if vogal_anterior:
                        linhas_modificadas.append(f'{comeco_vogal} {final_vogal} {fonema_vogal}\n')
                        vogal_anterior = None
                    linhas_modificadas.append(linha)
            else:
                if vogal_anterior:
                    linhas_modificadas.append(f'{comeco_vogal} {final_vogal} {fonema_vogal}\n')
                    vogal_anterior = None
                linhas_modificadas.append(linha)

        if vogal_anterior:
            linhas_modificadas.append(f'{comeco_vogal} {final_vogal} {fonema_vogal}\n')

    return linhas_modificadas

def salvar_arquivo_modificado(nome_arquivo, linhas_modificadas):
    caminho_mod = os.path.join('mod', nome_arquivo)
    with open(caminho_mod, 'w', encoding="utf8") as arquivo_modificado:
        arquivo_modificado.writelines(linhas_modificadas)

def processar_e_salvar_arquivo(nome_arquivo):
    linhas_modificadas = processar_arquivo_lab(nome_arquivo)
    if linhas_modificadas:
        salvar_arquivo_modificado(nome_arquivo, linhas_modificadas)

# Listando e processando os arquivos na pasta atual
for arquivo in os.listdir('.'):
    if arquivo.endswith('.lab'):
        processar_e_salvar_arquivo(arquivo)
