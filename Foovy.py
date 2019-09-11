import sys

#def das palavras reservadas
library = ["E", "Quando", "Dado", "Então", "Entao"]

#Abrir arquivos
input_file_name = sys.argv[1]
input_file = open(input_file_name, "r")
output_file = open(input_file_name + ".groovy", "w")

#adiciona as bibliotecas pt
output_file.write("import cucumber.api.java.pt.E\n")
output_file.write("import cucumber.api.java.pt.Dado\n")
output_file.write("import cucumber.api.java.pt.Quando\n")
output_file.write("import cucumber.api.java.pt.Entao\n")
output_file.write("import internal.GlobalVariable\n\n")



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

#verifica sem a linha contem ":" no final
def verifyLine(line):
	if line:
		if ":" in line[-1]:
			line = line[:-1]
	return line

#para cada linha do arquivo de entrada:
for line in input_file:
    #remove identação e permite caracteres especiais
    line = line.strip().encode('latin-1').decode('utf-8')
    #verifica a primeira palavra da linha
    first_word = line.split(' ', 1)[0]
    
    #se a primeira palavra for um cenário, insira como comentário
    if first_word == "Cenário:":
        print ('/*' + line + '*/' + '\n')
    #senão, verifique se é uma palavra reservada
    else:
        #se primeira palavra é palavra reservada
        if first_word in library:            
            #remove a primeira palavra da linha
            new_line = line[len(first_word)+1:]
            #remove ':' no fim da linha
            new_line = verifyLine(new_line)
            #escreve a tag de identificação
            print ('@' + clear(first_word) + '("' + new_line + '")', end = '\n')
            output_file.write("@" + clear(first_word) + '("' + new_line + '")' + '\n')
            #escreve a assinatura da função e a abertura das chaves
            print ("def ", end = '')
            output_file.write("def ")
            word_list = new_line.split(' ')
            func_name = ''
            for s in word_list:
                func_name += clear(s) + '_'
            func_name = func_name[:len(func_name)-1]
            print (func_name + '()' + '{' + '\n' + '\n' + '}' + '\n')
            output_file.write(func_name + '()' + '{' + '\n' + '\n' + '}' + '\n')
        #caso contrário, nada a fazer
        else:
            pass

#fecha os arquivos abertos
input_file.close()
output_file.close()