import urllib
import getpass

#----------------------------------------- DEFINIR FUNCOES -----------------------------------------

def substituir(file): #SUBSTITUI CARACTERES ESPECIAIS E ALGUNS COMANDOS
    #caracteres especiais
    str_out = file.replace("&Aacute;","\xc3\x81")
    str_out = str_out.replace("&aacute;","\xc3\xa1")
    str_out = str_out.replace("&Acirc;","\xc3\x82")
    str_out = str_out.replace("&acirc;","\xc3\xa2")
    str_out = str_out.replace("&Agrave;","\xc3\x80")
    str_out = str_out.replace("&agrave;","\xc3\xa0")
    str_out = str_out.replace("&Aring;","\xc3\x85")
    str_out = str_out.replace("&aring;","\xc3\xa5")
    str_out = str_out.replace("&Atilde;","\xc3\x83")
    str_out = str_out.replace("&atilde;","\xc3\xa3")
    str_out = str_out.replace("&Auml;","\xc3\x84")
    str_out = str_out.replace("&auml;","\xc3\xa4")
    str_out = str_out.replace("&AElig;","\xc3\x86")
    str_out = str_out.replace("&aelig;","\xc3\xa6")
    str_out = str_out.replace("&Eacute;","\xc3\x89")
    str_out = str_out.replace("&eacute;","\xc3\xa9")
    str_out = str_out.replace("&Ecirc;","\xc3\x8a")
    str_out = str_out.replace("&ecirc;","\xc3\xaa")
    str_out = str_out.replace("&Egrave;","\xc3\x88")
    str_out = str_out.replace("&egrave;","\xc3\xa8")
    str_out = str_out.replace("&Euml;","\xc3\x8b")
    str_out = str_out.replace("&euml;","\xc3\xab")
    str_out = str_out.replace("&ETH;","\xc3\x90")
    str_out = str_out.replace("&eth;","\xc3\xb0")
    str_out = str_out.replace("&Iacute;","\xc3\x8d")
    str_out = str_out.replace("&iacute;","\xc3\xad")
    str_out = str_out.replace("&Icirc;","\xc3\x8e")
    str_out = str_out.replace("&icirc;","\xc3\xae")
    str_out = str_out.replace("&Igrave;","\xc3\x8c")
    str_out = str_out.replace("&igrave;","\xc3\xac")
    str_out = str_out.replace("&Iuml;","\xc3\x8f")
    str_out = str_out.replace("&iuml;","\xc3\xaf")
    str_out = str_out.replace("&Oacute;","\xc3\x93")
    str_out = str_out.replace("&oacute;","\xc3\xb3")
    str_out = str_out.replace("&Ocirc;","\xc3\x94")
    str_out = str_out.replace("&ocirc;","\xc3\xb4")
    str_out = str_out.replace("&Ograve;","\xc3\x92")
    str_out = str_out.replace("&ograve;","\xc3\xb2")
    str_out = str_out.replace("&Oslash;","\xc3\x98")
    str_out = str_out.replace("&oslash;","\xc3\xb8")
    str_out = str_out.replace("&Otilde;","\xc3\x95")
    str_out = str_out.replace("&otilde;","\xc3\xb5")
    str_out = str_out.replace("&Ouml;","\xc3\x96")
    str_out = str_out.replace("&ouml;","\xc3\xb6")
    str_out = str_out.replace("&Uacute;","\xc3\x9a")
    str_out = str_out.replace("&uacute;","\xc3\xba")
    str_out = str_out.replace("&Ucirc;","\xc3\x9b")
    str_out = str_out.replace("&ucirc;","\xc3\xbb")
    str_out = str_out.replace("&Ugrave;","\xc3\x99")
    str_out = str_out.replace("&ugrave;","\xc3\xb9")
    str_out = str_out.replace("&Uuml;","\xc3\x9c")
    str_out = str_out.replace("&uuml;","\xc3\xbc")
    str_out = str_out.replace("&Ccedil;","\xc3\x87")
    str_out = str_out.replace("&ccedil;","\xc3\xa7")
    str_out = str_out.replace("&Ntilde;","\xc3\x91")
    str_out = str_out.replace("&ntilde;","\xc3\xb1")
    str_out = str_out.replace("&lt;","<")
    str_out = str_out.replace("&gt;",">")
    str_out = str_out.replace("&amp;","&")
    str_out = str_out.replace("&quot;","\xca\xba")
    str_out = str_out.replace("&reg;","\xc2\xae")
    str_out = str_out.replace("&copy;","\xc2\xa9")
    str_out = str_out.replace("&Yacute;","\xc3\x9d")
    str_out = str_out.replace("&yacute;","\xc3\xbd")
    str_out = str_out.replace("&THORN;","\xc3\x9e")
    str_out = str_out.replace("&thorn;","\xc3\xbe")
    str_out = str_out.replace("&szlig;","\xc3\x9f")
    str_out = str_out.replace("&ldquo;","\xca\xba")
    str_out = str_out.replace("&rdquo;","\xca\xba")
    str_out = str_out.replace("&lsquo;","'")
    str_out = str_out.replace("&rsquo;","'")
    str_out = str_out.replace("&ndash;","-")
    str_out = str_out.replace("&mdash;","-")
    str_out = str_out.replace("&nbsp;","")
    str_out = str_out.replace("&deg;","\xc2\xb0")
    str_out = str_out.replace("&sup3;","\xc2\xb3")
    str_out = str_out.replace("&sup2;","\xc2\xb2")    

    #comandos
    str_out = str_out.replace("<br />","")
    str_out = str_out.replace("\r\n","")
    str_out = str_out.replace("\t"," ")
    str_out = str_out.replace("<strong>","")
    str_out = str_out.replace("</strong>","")
    str_out = str_out.replace("</a>","")

    return str_out

def remove_link(file): #REMOVE LINKS DO TEXTO
    str_out = str(file)
    while True:
        start_index = 0
        start_index = str_out.find("<a")
        stop_index = str_out.find(">", start_index)+1
        stri = str_out[start_index:stop_index]
        str_out = str_out.replace(stri, "")
        if start_index == -1:
            break
    return str_out

def remove_span(file): #REMOVE TAG <SPAN> DO TEXTO
    str_out = str(file)
    while True:
        start_index = 0
        start_index = str_out.find("<span")
        stop_index = str_out.find("/span", start_index)+5
        stri = str_out[start_index:stop_index]
        str_out = str_out.replace(stri, "")
        if start_index == -1:
            break
    return str_out

def write_json_from_url(json_name, url): #FUNCAO QUE REALIZA O PROCESSAMENTO DA URL E GRAVA NO ARQUIVO JSON
    
    #----------------------------------------- CRIAR VARIAVEIS AUXILIARES -----------------------------------------
    index = 0 #indice do arq de leitura
    first = True #primeira passagem
    old_op = 0 #opcao anterior da maq. de estados

    #----------------------------------------- ABRIR ARQUIVO DE LEITURA -----------------------------------------
    f = urllib.urlopen(url)
    file = f.read()
    
    #----------------------------------------- ABRIR ARQUIVO DE ESCRITA -----------------------------------------
    json_name = json_name + ".json"

    json_file = open(json_name, "w+")

    #----------------------------------------- ESCREVER "CABECALHO" -----------------------------------------
    json_file.writelines("{\n")

    index = file.find("<item>", index)

    #----------------------------------------- LER ARQUIVO DE LEITURA E EXTRAIR INFORMACOES -----------------------------------------
    while True:

        #----------------------------------------- ENCONTRAR O TIPO DE TAG QUE VIRA A SEGUIR -----------------------------------------
        op = 0 #opcao da maq. de estados

        a = file.find("<title>", index) #titulo
        b = file.find("<img alt", index) #imagem
        c = file.find("<p>", index) #texto
        d = file.find("<li>", index) #link

        if a == -1:
            a = 9223372036854775807
        if b == -1:
            b = 9223372036854775807
        if c == -1:
            c = 9223372036854775807
        if d == -1:
            d = 9223372036854775807

        if(a < b) and (a < c) and (a < d):
            op = 1
        elif(b < a) and (b < c) and (b < d):
            op = 2
        elif(c < a) and (c < b) and (c < d):
            op = 3
        elif(d < a) and (d < b) and (d < c):
            op = 4

        #----------------------------------------- MAQUINA DE ESTADOS -----------------------------------------
        #OP = 1, TITULO
        if op == 1: 
            if(old_op == 4):
                json_file.writelines("\t\t],\n")
                json_file.writelines("\t  },\n")
            if first == False:
                json_file.writelines("\t]\n")
            first = False
            index_start = file.find("<title>", index)+16
            index_stop = file.find("]", index_start)
            json_file.writelines("\t\"title\":\"")
            json_file.writelines(substituir(file[index_start:index_stop]))
            json_file.writelines("\",\n")
            #LINK DO TITULO
            index_start = file.find("<link>", index)+6
            index_stop = file.find("</link>", index)
            json_file.writelines("\t\"link\":\"")
            json_file.writelines(substituir(file[index_start:index_stop]))
            json_file.writelines("\",\n")
            json_file.writelines("\t\"content\":[\n")
            index = file.find("<title>", index)+1
            old_op = op

        #OP = 2, IMAGEM
        elif op == 2:
            if(old_op == 4):
                json_file.writelines("\t\t],\n")
                json_file.writelines("\t  },\n")
            json_file.writelines("\t  {\n")
            json_file.writelines("\t\t\"type\":\"image\",\n")
            if file.find("http", index) != -1:
                #LINK DA IMAGEM
                index_start = file.find("http", file.find("<img alt", index))
                index_stop = file.find("title", index_start)-2
                json_file.writelines("\t\t\"content\":\"")
                json_file.writelines(substituir(file[index_start:index_stop]))
                json_file.writelines("\",\n")
            json_file.writelines("\t  },\n")
            index = file.find("<img alt", index) + 1
            old_op = op

        #OP = 3, TEXTO
        elif op == 3:
            if str(file[file.find("<p>", index)+6]) != '&':
                if(old_op == 4):
                    json_file.writelines("\t\t],\n")
                    json_file.writelines("\t  },\n")
                index_start = file.find("<p>", index)+6
                index_stop = file.find("</p>", index_start)
                json_file.writelines("\t  {\n")
                json_file.writelines("\t\t\"type\":\"text\",\n")
                json_file.writelines("\t\t\"content\":\"")
                json_file.writelines(remove_link(remove_span(substituir(file[index_start:index_stop]))))
                json_file.writelines("\",\n")
                json_file.writelines("\t  },\n")
                old_op = op
            index = file.find("<p>", index) + 1

        #OP = 4, LINKS
        elif op == 4:
            index_start = file.find("http", index)
            index_stop = file.find("\">", index_start)
            if(old_op != 4):
                json_file.writelines("\t  {\n")
                json_file.writelines("\t\t\"type\":\"links\",\n")
                json_file.writelines("\t\t\"content\":[\n")
            json_file.writelines("\t\t\t")
            json_file.writelines(substituir(file[index_start:index_stop]))
            json_file.writelines("\",\n")
            index = file.find("<li>", index) + 1
            old_op = op
        
        #OP = 0, FIM DO ARQUIVO DE LEITURA
        else:
            print "JSON ESCRITO COM SUCESSO"
            json_file.writelines("\t\t],\n")
            json_file.writelines("\t  },\n")
            json_file.writelines("\t]\n}")
            break
            #FIM

def w_service(): #"WEBSERVICE"
    print " ------ APENAS USUARIOS CADASTRADOS PODEM ACESSAR ESTA FUNCAO ------"

    #input do console
    user = raw_input("User: ")
    password = getpass.getpass("Password: ")

    #exemplo de usuario/senha cadastrados, poderia ser uma list, poderia estar em outro local, etc...
    cad_user = 'guilherme' 
    cad_pass = 'ganzaroli'

    #checar se usuario/senha estao corretos
    if(user == cad_user) and (password == cad_pass):
        print "ACESSO PERMITIDO"
        return True

    else:
        print "ACESSO NEGADO - USUARIO/SENHA INCORRETO(A)"
        return False

#----------------------------------------- MAIN -----------------------------------------

if w_service():
    url = "https://revistaautoesporte.globo.com/rss/ultimas/feed.xml" #url fixa, mas poderia pedir uma no console se fosse interessante
    write_json_from_url("teste_ed_globo_guilherme_rossi_ganzaroli", url) #nome do arquivo fixo, mas poderia pedir um no console se fosse interessante