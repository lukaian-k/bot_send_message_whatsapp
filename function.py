import pywhatkit as pwk


def send_message(hora, lista_numeros_site, mensagem_site, lista_numeros_outros_servicos, mensagem_outros_servicos):
    if hora[0] > 23:
        hora[0] = 0

    if lista_numeros_site:
        for i in lista_numeros_site:
            if hora[1] >= 59:
                if hora[0] >= 23:
                    hora[0] = 0
                else:
                    hora[0] += 1
                hora[1] == 0
            else:
                hora[1] += 1

            pwk.sendwhatmsg(i, mensagem_site, hora[0], hora[1], 10, True, 13)

    if lista_numeros_outros_servicos:
        for i in lista_numeros_outros_servicos:
            if hora[1] >= 59:
                if hora[0] >= 23:
                    hora[0] = 0
                else:
                    hora[0] += 1
                hora[1] == 0
            else:
                hora[1] += 1

            pwk.sendwhatmsg(i, mensagem_outros_servicos, hora[0], hora[1], 10, True, 13)