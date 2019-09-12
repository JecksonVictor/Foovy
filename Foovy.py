import sys
from Functions import *

#Abrir arquivos
input_file_name = sys.argv[1]
input_file = open(input_file_name, "r")
output_file = open(input_file_name[:-8] + ".groovy", "w")

placeHeader(output_file)
placeClassName(output_file, input_file_name)

#para cada linha do arquivo de entrada:
for line in input_file:
        #remove identação e permite caracteres especiais
    line = line.strip()

    #verifica a primeira palavra da linha
    first_word = line.split(' ', 1)[0]
    
    #se a primeira palavra for um cenário, insira como comentário
    if first_word == "Cenário:" or first_word == "Esquema":
        output_file.write('\t' + '/*' + line + '*/' + '\n')
    #senão, verifique se é uma palavra reservada
    else:
        #se primeira palavra é palavra reservada
        if first_word in getReservedWords():            
            #remove a primeira palavra da linha
            new_line = line[len(first_word)+1:]

            #remove ':' no fim da linha
            new_line = verifyLine(new_line)

            #escreve a tag de identificação
            output_file.write('\t' + "@" + clear(first_word) + '("' + new_line + '")' + '\n')

            #escreve a assinatura da função e a abertura das chaves
            output_file.write('\t' + "def ")
            word_list = new_line.split(' ')
            func_name = ''
            for s in word_list:
                func_name += clear(s) + '_'
            func_name = func_name[:len(func_name)-1]
            output_file.write(func_name + '()' + '{' + '\n' + '\t' + '\t' + '\n' + '\t' + '}' + '\n' + '\n')

        #caso contrário, nada a fazer
        else:
            pass

#insere o final brace
output_file.write('}')

#fecha os arquivos abertos
input_file.close()
output_file.close()

#print outfile
with open(input_file_name[:-8] + ".groovy", "r") as outfile:
    for l in outfile:
        l = l.encode('latin-1').decode('utf-8')
        print(l, end = "")