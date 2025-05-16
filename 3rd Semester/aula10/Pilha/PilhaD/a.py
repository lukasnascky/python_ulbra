import PilhaD

l=PilhaD.PilhaD()

p='53+*2'

op1=0
op2=0

for i in p:
    if i.isdigit():
        l.push(float(i))
    
        
    else:
        op2=l.ver_topo()
        l.pop()
        op1=l.ver_topo()
        l.pop()

        if i == '+':
            l.push(op1+op2)

        elif i == '-':
            l.push(op1-op2)

        elif i == '*':
            l.push(op1*op2)

        else:
            l.push(op1/op2)

print(l.ver_topo())