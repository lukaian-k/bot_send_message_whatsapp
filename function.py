import pywhatkit as pwk


def send_message(time, list_numbers, messages):
    print('Verificando os contatos que irão ser contactados...\n\n')
    if time['hour'] > 23:
        time['hour'] = 0

    print('Iniciando os envios das propostas para os contatos...')
    for key in list_numbers.keys():
        for number in list_numbers[key]:
            if time['minute'] >= 59:
                if time['hour'] >= 23:
                    time['hour'] = 0
                else:
                    time['hour'] += 1
                time['minute'] = 0
            else:
                time['minute'] += 1

            print(f'\nEnviado para o contato: {number} - horário: {time["hour"]}:{time["minute"]}')
            pwk.sendwhatmsg(number, messages[key], time['hour'], time['minute'], 10, True, 13)
    
    print('\nNão existe ou acabou os contatos para contactar.\n')