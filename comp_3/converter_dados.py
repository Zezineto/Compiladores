def carregar_dados(arquivo):
    dados = []
    #registro_atual = {}

    with open(arquivo, 'r', encoding='utf-8') as file:
        pessoa = {}
        for linha in file:
            linha = linha.strip()
            if linha == "---": #indica o fim de um registro
                if pessoa: #adiciona pessoa apenas se houver dados    
                    dados.append(pessoa)
                    pessoa = {}
            else:
                try:
                    chave, valor = linha.split('=', 1)
                    pessoa[chave] = valor
                except ValueError:
                    print
                    (f"linha ignorada: {linha}")    
    
    return dados

def converter_json(dados):
    json_string = '[\n'
    for registro in dados:
        json_string += " {\n"
        for chave, valor in registro.items():
            json_string += f'  "{chave}": "{valor}",\n'
        json_string = json_string.rstrip(",\n") + "\n },\n"
    json_string = json_string.rstrip(",\n") + "\n]"
    return json_string

def converter_xml(dados):
    xml_string = "<root>\n"
    for resgistro in dados:
        xml_string += " <registro>\n"
        for chave, valor in resgistro.items():
            xml_string += f' <{chave}>{valor}</{chave}>\n'
        xml_string += " </registro>\n"
    xml_string += "</root>"
    return xml_string

def salvar_arquivo(conteudo, caminho):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
    print(f"arquivo salvo em {caminho}")

if __name__ == "__main__":
    dados = carregar_dados('dados_falsos.txt')
    if dados: 
        #converter e salver em json
        dados_json = converter_json(dados)
        salvar_arquivo(dados_json, 'dados_falsos_json.json')

        #converter e salver em xml
        dados_xml = converter_xml(dados)
        salvar_arquivo(dados_xml, 'dados_falsos_xml.xml')
    else:
        print("Nenhum dado encontrado para conversão.")
    