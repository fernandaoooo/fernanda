def hora(h):
    hora = h.split(':')
    hora[0] = int(hora[0])
    hora[1] = int(hora[1])
    if hora[0] > 1 and hora[1] > 1:
        return f'{hora[0]} horas e {hora[1]} minutos'
    elif hora[0] == 1 and hora[1] > 1:
        return f'{hora[0]} hora e {hora[1]} minutos'
    else:
        return f'{hora[0]} hora e {hora[1]} minuto'


print(hora('10:32'))