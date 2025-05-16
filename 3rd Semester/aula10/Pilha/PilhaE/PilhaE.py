import PilhaE

p = PilhaE.PilhaE()
p.push('A')
p.push('B')
print(p.ver_topo())
p.pop()
print(p.ver_topo())
