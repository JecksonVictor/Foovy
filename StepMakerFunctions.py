import sys

#adiciona bibliotecas
def add_biblioteca(_file):
    with open("library/header", "r") as header_file:
        for line in header_file:
            _file.write(line)

#verifica sem a linha contem ":" no final
def verificaLinha(line):
	if line:
		if ":" in line[-1]:
			line = line[:-1]
	return line

#função para remover caracteres acentuados e tradução
def clear(dirty_string):
    dirty_string = dirty_string.replace('é', 'e')
    dirty_string = dirty_string.replace('ê', 'e')
    dirty_string = dirty_string.replace('á', 'a')
    dirty_string = dirty_string.replace('à', 'a')
    dirty_string = dirty_string.replace('ã', 'a')
    dirty_string = dirty_string.replace('ó', 'o')
    dirty_string = dirty_string.replace('í', 'i')
    dirty_string = dirty_string.replace('ú', 'u')
    dirty_string = dirty_string.replace("Dado", "given")
    dirty_string = dirty_string.replace("Quando", "when")
    dirty_string = dirty_string.replace("Entao", "then")
    dirty_string = dirty_string.replace("<", "{")
    dirty_string = dirty_string.replace(">", "}")
    return dirty_string

def criar_steps(): 
    #para cada linha do arquivo de entrada:
    for line in input_file:
        variavel = ""
        #remove identação e permite caracteres especiais
        line = line.strip().encode('latin-1').decode('utf-8')
        #da um clear na linha
        line = clear(line)
        #verifica a primeira palavra da linha
        first_word = line.split(' ', 1)[0]
        #verifica se tem alguma variavel e pega o nome
        if(line.find("<") != -1):
            posicao1 = line.find("<")
            posicao2 = line.find(">")
            variavel = line[posicao1 + 1:posicao2]
        #remove a primeira palavra da linha
        new_line = line[len(first_word)+1:]
        #remove ':' no fim da linha
        new_line = verificaLinha(new_line)
        output_file.write("@" + first_word + '("' + new_line + '")' + '\n')
        #se nao possuir nenhuma variavel
        if(variavel == ""):
            output_file.write("def step_impl(context):" + '\n\n\n')
        else:
            output_file.write("def step_impl(context, " + variavel + "):" + '\n\n\n')
        

#def das palavras reservadas
palavrasReservadas = ["E", "Quando", "Dado", "Então", "Entao"]
tipoStep = ""
#ler arquivo
#def ler_arquivo():
nomeArquivo = input("Digite o nome do arquivo : ") + ".feature"
input_file = open(nomeArquivo, "r")
nomeArquivo = nomeArquivo.split(".")
output_file = open(nomeArquivo[0] + ".py", "w")

add_biblioteca(output_file)
criar_steps()

input_file.close()
output_file.close()