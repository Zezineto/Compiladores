import ast

def ler_dados_do_txt(arquivo_txt):
    dados = []

    with open(arquivo_txt, 'r', encoding='utf-8') as arquivo:
        cliente = {}
        for linha in arquivo:
            linha = linha.strip()
            if linha == '---':  # Registro completo
                if cliente:  # Adiciona cliente se houver dados
                    dados.append(cliente)
                    cliente = {}
            else:
                try:
                    chave, valor = linha.split('=', 1)  # Divide a linha em chave e valor
                    # Converte o valor para o tipo apropriado (número, lista, dicionário etc.)
                    try:
                        valor = ast.literal_eval(valor)
                    except (ValueError, SyntaxError):
                        pass  # Mantém o valor como string se não for um tipo reconhecido
                    cliente[chave] = valor
                except ValueError:
                    print(f"Linha ignorada: {linha}")  # Ignora linhas malformadas

        # Adiciona o último cliente se houver dados
        if cliente:
            dados.append(cliente)

    return dados

def converter_para_json(dados):
    json_string = "[\n"
    for cliente in dados:
        json_string += "  {\n"
        for chave, valor in cliente.items():
            if isinstance(valor, str):
                json_string += f'    "{chave}": "{valor}",\n'
            else:
                json_string += f'    "{chave}": {valor},\n'
        json_string = json_string.rstrip(",\n") + "\n  },\n"
    json_string = json_string.rstrip(",\n") + "\n]\n"

    with open("dados.json", "w", encoding="utf-8") as arquivo_json:
        arquivo_json.write(json_string)

def converter_para_xml(dados):
    xml_string = "<clientes>\n"
    for cliente in dados:
        xml_string += "  <cliente>\n"
        for chave, valor in cliente.items():
            xml_string += f'    <{chave}>{valor}</{chave}>\n'
        xml_string += "  </cliente>\n"
    xml_string += "</clientes>\n"

    with open("dados.xml", "w", encoding="utf-8") as arquivo_xml:
        arquivo_xml.write(xml_string)

def converter_dados(arquivo_txt):
    # Lê os dados do arquivo .txt
    dados = ler_dados_do_txt(arquivo_txt)

    # Converte para JSON e XML
    converter_para_json(dados)
    converter_para_xml(dados)

    print("Conversão concluída. Os arquivos 'dados.json' e 'dados.xml' foram gerados.")

# Executa a função de conversão
if __name__ == "__main__":
    converter_dados("dados.txt")
