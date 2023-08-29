def substituir_caracteres(string, char_substituir, lista_substitutos):
    resultados = []
    for substituto in lista_substitutos:
        nova_string = string.replace(char_substituir, substituto)
        resultados.append(nova_string)
    return resultados

def main():
    string_original = input("Digite o texto ou o caminho para o arquivo .txt contendo a string original: ")
    if string_original.endswith('.txt'):
        with open(string_original, 'r') as file:
            string_original = file.read()

    char_substituir = input("Digite o caractere que precisa ser substituído: ")
    lista_substitutos = input("Digite a lista de caracteres separados por vírgula: ").split(',')

    resultados = substituir_caracteres(string_original, char_substituir, lista_substitutos)

    for resultado in resultados:
        print(resultado)

    # Salvar em um arquivo txt
    nome_arquivo = "resultados.txt"
    with open(nome_arquivo, "w") as arquivo:
        for resultado in resultados:
            arquivo.write(resultado + "\n")

if __name__ == "__main__":
    main()
