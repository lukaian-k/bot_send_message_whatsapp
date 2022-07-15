from function import send_message
from datetime import datetime


nome = 'Lucas José' #INSIRA SEU NOME AQUI

file = open('contatos/lista_numeros_site.txt', 'r')
lista_numeros_site = file.readlines(); file.close()

file = open('contatos/lista_numeros_site.txt', 'r')
lista_numeros_outros_servicos = file.readlines(); file.close()

horario = datetime.now(); hora = [int(horario.strftime('%H')), int(horario.strftime('%M'))]

mensagem_site = f'Olá, bom dia, chamo-me {nome} e sou colaborador da Include Jr. Após algumas pesquisas, notamos que vocês não possuem um site próprio. Devido a isso, gostaríamos de indicar os nossos serviços e de verificar a possibilidade de marcar uma reunião para apresentarmos uma proposta de estruturação do site.\n\n*Agradecemos pela atenção, e desejamos um ótimo dia.*'
mensagem_outros_servicos = f'Olá, bom dia, chamo-me {nome} e sou colaborador da Include Jr. Após algumas pesquisas, constatamos que vocês possuem um site próprio, e concluímos que a importância de fazer investimentos em soluções tecnológicas já é uma prática bastante difundida na organização. Por conseguinte, queremos auxiliá-los a ter um crescimento ainda maior do negócio através de outros tipos de tecnologias, desde sistemas informacionais a aplicativos mobile. Caso haja interesse em nossos serviços, gostaríamos de verificar a possibilidade de marcarmos uma reunião para discussão dos termos e definição de metas.\n\n*Agradecemos pela atenção, e desejamos um ótimo dia.*'

send_message(hora, lista_numeros_site, mensagem_site, lista_numeros_outros_servicos, mensagem_outros_servicos)