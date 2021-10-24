import requests
import os
from pesquisa import pesquisara

banner = '''
   _______ __            __       _______             __ 
  |   _   |  |_.--.--.--|  .--.--|       .-----.-----|  |
  |   1___|   _|  |  |  _  |  |  |.|   | |  _  |  _  |  |
  |____   |____|_____|_____|___  `-|.  |-|_____|_____|__|
  |:  1   |                |_____| |:  |
  |::.. . |  By Legumii            |::.|
  `-------'                        `---'
  '''
buscas = ''' 
Escolha um
1 - Calculadora 
2 - Pesquisar Conteudo
0 - Sair
'''
def Menu():
    print(banner)
    print(buscas)
    inputt = input('~=>')
    if inputt == '0':
        exit()
    if inputt == '1':
        print('')
        calc()
        Menu()
    if inputt == '2':
        print('')
        pesquisa()
        Menu()
    else:
        os.system('clear')
        Menu()
def calc():
    operacao = input("Digite a operacao desejada (soma, sub, mult, div): ")
    numero1 = input("Digite o primeiro número: ")
    numero2 = input("Digite o segundo número: ")

    if operacao == "soma":
        resultado = int(numero1) + int(numero2)
    elif operacao == "sub":
        resultado = int(numero1) - int(numero2)
    elif operacao == "mult":
        resultado = int(numero1) * int(numero2)
    elif operacao == "div":
        resultado = int(numero1) / int(numero2)
    else:
        resultado = "Operação não suportada"
    
    os.system('clear')
    
    print("O resultado da operação é: " + str(resultado))
def pesquisa():
		palavra = input('Fale oque deseja pesquisar \n>>')
		tete = requests.get(f'https://kgsearch.googleapis.com/v1/entities:search?query={palavra}&key=AIzaSyAkSdDu4hAB8I0hH9ub6w05JSLUY6l94Gw&limit=1&indent=True&languages=pt').json() # Puxando os dados apartir da API
		try:
				jo = tete['itemListElement'][0]['result'] # Facilitando a escrita
		except:
				pass
		os.system('clear')
		# resultados
		print("-== Wikipédia ==-")
		pesquisara(palavra)
		print("-== Google ==-")
		try:
				print('Nome:', jo['name'])
				print('Detalhes:', jo['detailedDescription']['articleBody'])
				print('Sobre:',jo['description'])
				print('Links', jo['detailedDescription']['url'])
				print('Tipo da resposta(Em inglês):')
				print(jo['@type'][0])
		except:
			Menu()

os.system('clear')
Menu()