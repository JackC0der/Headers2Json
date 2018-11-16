

caracteres = ",{}:'\n "

def help():
	print('''
####Todos os Espacos Serao Retidos####
#####Nao Esqueca de Arrumar Isso######
#############By J4CK_#################

'''
)

help()

#Abre o arquivo
texto = open(input("Nome do Arquivo txt Para Converter\n\n>>> "), "r+")

#Amazena o que esta dentro do arquivo em uma variavel
texto = texto.read()

#Retira espacos do texto
texto = texto.replace(' ','')

#Adiciona os caracteres "faceis"
texto = "{'"+texto+"'}"

texto = texto.replace(",","")

#Elimina quebras de linha
texto = texto.replace('\n',',\n')

#Coloca virgulas no texto
texto = texto.replace(" ",',')

#coloca aspa simples em cada ":"
texto = texto.replace(':',"':'")

#Tranforma o texto em list para facilitar a edicao
texto=list(texto)

#Coloca aspas simples no fim das plavras
for letra in range(len(texto)):
	if texto[letra - 1] == '\n' and texto[letra + 1] not in caracteres:
		texto[letra] = "'"+texto[letra]

#Coloca aspas simples no comeco das palavras
for letra in range(len(texto)):
	if texto[letra] == ',' and texto[letra - 1] not in caracteres:
		texto[letra] = "'"+texto[letra]

#Retira os caracteres de lista do texto
texto = "".join(texto)		

#Mostra o texto na tela
print('\n\n'+texto+'\n\n')