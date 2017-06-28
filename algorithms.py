def string_calculator(string):
    string = string.replace(' ', '')
    string = string.replace('--', '+')
    while '++' in string:
        string = string.replace('++', '+')
    string = string.replace('+', ':+:')
    string = string.replace('-', ':-:')
    string = string.replace('/', ':/:')
    string = string.replace('*', ':*:')
    if string[0] == ':':
        string = string[1] + string[2:]
    if string[-1] == ':':
        string = string[:-1]
    string = string.replace('::', ':')
    calculation = [(i if i in '+-*/' else float(i)) for i in string.split(':')]
    i = 0
    n = len(calculation)
    while i < n:
        if calculation[i] == '-':
            calculation[i+1] = -calculation[i+1]
            del calculation[i]
            n -= 1
        elif calculation[i] == '+':
            del calculation[i]
            n -= 1
        else:
            i += 1
    i = 0
    n = len(calculation)
    while i < n:
        if calculation[i] == '*':
            calculation[i] = calculation[i+1]*calculation[i-1]
            del calculation[i-1]
            del calculation[i]
            n -= 2
        elif calculation[i] == '/':
            calculation[i] = calculation[i-1]/calculation[i+1]
            del calculation[i-1]
            del calculation[i]
            n -= 2
        else:
            i += 1
    answer = sum(calculation)
    return answer

