import sys

def receber_dados():
    dados = {}

    while True:
        entrada = input('Digite um dado no formato "chave = valor" ou ("sair" para finalizar): ')
        #sys.stdin.flush()
        print(f'voce digitou {entrada}')

        if entrada.lower() == 'sair':
            break

        try: #separar chave e valor por "="
            chave,valor = entrada.split('=', 1)
            chave = chave.strip()
            valor = valor.strip()

            #adicionar ao dicionario
            dados[chave] = valor
        except ValueError:
            print('Entrada invalida! Por favor digite no formato "chave = valor".')
        
    return dados

def criar_json(dados):
    json_string = "{\n"
    for chave, valor in dados.items():
        #adicionar a chave e o valor no formato JSON, com aspas duplas de indentação
        json_string += f' "{chave}": "{valor}", \n'

    #remover a ultima virgula e adicionar o fechamento do objeto JSON
    json_string = json_string.rstrip(", \n") + "\n}"
    return json_string

def salvar_dados_json(json_string, caminho_arquivo):
    #salvar o JSON criado em um arquivo 
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(json_string)
    print(f"Dados salvos no arquivo {caminho_arquivo} com sucesso!")

dados_usuario = receber_dados()
if dados_usuario: 
    json_criado = criar_json(dados_usuario)
    salvar_dados_json(json_criado, 'dados.json')
else: 
    print('nenhum dado inserido')