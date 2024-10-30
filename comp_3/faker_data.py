from faker import Faker

def gerar_dados(quantidade):
   fake = Faker()
   dados = []

   for i in range(quantidade):
      pessoa = {
         "nome": fake.name(),
         "endereco": fake.address(),
         "email": fake.email(),
         "telefone": fake.phone_number()
      }
      dados.append(pessoa)

    #salvar os dados em um arquivo de texto com formatação personalizada
   with open('dados_falsos.txt', 'w', encoding='utf-8') as arquivo:
      for pessoa in dados:
         arquivo.write(f'nome={pessoa["nome"]}\n')
         arquivo.write(f'endereco={pessoa["endereco"]}\n')
         arquivo.write(f'email={pessoa["email"]}\n')
         arquivo.write(f'telefone={pessoa["telefone"]}\n')
         arquivo.write('---\n')
   print(f' {quantidade} registros gerados e salvos em dados "dados_falsos.txt".')

#executa a geração de dados com a quantidade desejada
if __name__=="__main__":
   gerar_dados(10)

         
