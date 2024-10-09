import json
import xml.etree.cElementTree as ET #ET = ELEMENT TREE
import xml.dom.minidom

#deixa o xml criado menos feio (pra mim ele é feio pra caraio)
def indentar(elem):
    #retorna o xml formatado e indentado
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent=" ") 

#le e printa o arquivo json
with open("data.json",encoding='utf-8') as json_file:
    data = json.load(json_file)

print(data)

#sla oq isso faz mas ele gera o xml
root = ET.Element("root")
ET.SubElement(root, "nome").text = data["nome"]
ET.SubElement(root, "idade").text = str(data["idade"])
#ET.SubElement(root, "habilidades").text = data["habilidades"]
habilidades = ET.SubElement(root, "habilidades")

for i in data["habilidades"]:
    ET.SubElement(habilidades, "habilidades").text = i

#faz todo o resto
xml_string = indentar(root)
tree = ET.ElementTree(root)
tree.write("data.xml", encoding='utf-8', xml_declaration=True)
with open("data.xml","w",encoding='utf-8') as xml_file:
    xml_file.write(xml_string)

print("funcionou!")