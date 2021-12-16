def leiadinheiro():
    a = input(('Informe um preço R$ \n'))
    if isinstance(a, (float, int)) == True:
        return a    
    else:
        while True: 
            a = input('Valor inválido, digite números! \n')
            if isinstance(a, (float, int)) == True:
                break
        return a
    