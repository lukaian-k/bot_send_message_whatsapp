from function import send_message
from datetime import datetime


name = 'Lucas José' #ENTER YOUR NAME HERE
waiting_minutes = 0 #SET HOW MANY MINUTES AFTER MESSAGES WILL BE SENT

print('\n<<<Programa Inicializado>>>\n')
file = open('contacts/offer_websites.txt', 'r+')
list_numbers = {'01_message': file.readlines()}; file.truncate(0), file.close()

file = open('contacts/offer_other_services.txt', 'r+')
list_numbers['02_message'] = file.readlines(); file.truncate(0), file.close()
print('Arquivos limpos!\n')

time = datetime.now(); time = {'hour': int(time.strftime('%H')), 'minute': int(time.strftime('%M'))+waiting_minutes}

messages = {
'01_message': f'Olá, bom dia, chamo-me {name} e sou colaborador da Include Jr. Após algumas pesquisas, notamos que vocês não possuem um site próprio. Devido a isso, gostaríamos de indicar os nossos serviços e de verificar a possibilidade de marcar uma reunião para apresentarmos uma proposta de estruturação do site.\n\n*Agradecemos pela atenção, e desejamos um ótimo dia.*',
'02_message': f'Olá, bom dia, chamo-me {name} e sou colaborador da Include Jr. Após algumas pesquisas, constatamos que vocês possuem um site próprio, e concluímos que a importância de fazer investimentos em soluções tecnológicas já é uma prática bastante difundida na organização. Por conseguinte, queremos auxiliá-los a ter um crescimento ainda maior do negócio através de outros tipos de tecnologias, desde sistemas informacionais a aplicativos mobile. Caso haja interesse em nossos serviços, gostaríamos de verificar a possibilidade de marcarmos uma reunião para discussão dos termos e definição de metas.\n\n*Agradecemos pela atenção, e desejamos um ótimo dia.*'
}

send_message(time, list_numbers, messages)