#verifica sem a linha contem ":" no final
def verifyLine(line):
	if line:
		if ":" in line[-1]:
			line = line[:-1]
	return line

#Def da função de remover caracteres acentuados
def clear(dirty_string):
    dirty_string = dirty_string.replace('é', 'e')
    dirty_string = dirty_string.replace('ê', 'e')
    dirty_string = dirty_string.replace('á', 'a')
    dirty_string = dirty_string.replace('à', 'a')
    dirty_string = dirty_string.replace('ã', 'a')
    dirty_string = dirty_string.replace('ó', 'o')
    dirty_string = dirty_string.replace('í', 'i')
    dirty_string = dirty_string.replace('ú', 'u')
    return dirty_string

#adiciona nome da classe
def placeClassName(_file, input_file_name):
    _file.write("public class " + input_file_name[:-8] + " {" + "\n")

#adiciona as bibliotecas pt
def placeHeader(_file):
    with open("library/header", "r") as header_file:
        for line in header_file:
            _file.write(line)

#def das palavras reservadas
def getReservedWords():
    return (["E", "Quando", "Dado", "Então", "Entao"])