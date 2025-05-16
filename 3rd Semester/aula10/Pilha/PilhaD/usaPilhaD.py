import PilhaD

def valida_parenteses(expressao):
    p = PilhaD.PilhaD()
    for i in range(len(expressao)):
        if expressao[i] == '(':
            p.push(i)
        if expressao[i] == ')':
            if p.esta_vazia():
                return False
            p.pop()
    return p.esta_vazia()

def verifica_palindromo(palavra):
    p = PilhaD.PilhaD()
    tam_palavra = len(palavra)
    for i in range(tam_palavra):
        p.push(palavra[i])
    for i in range(tam_palavra):
        if p.ver_topo() != palavra[i]:
            return False
        p.pop()
    return True

def calculadora_hp(expressao):
    p = PilhaD.PilhaD()
    for token in expressao.split():
        if token.isdigit():
            p.push(float(token))
        else:
            b = p.pop()
            a = p.pop()
            if token == '+':
                p.push(a + b)
            elif token == '-':
                p.push(a - b)
            elif token == '*':
                p.push(a * b)
            elif token == '/':
                p.push(a / b)
    return p.ver_topo()



t = "2 2 + 5 +"
print(calculadora_hp(t))

'''expressao = input(">>> ")
print(calculadora_hp(expressao))
l = expressao.split()
print(l)'''
