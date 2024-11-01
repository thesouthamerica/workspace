#criando uma pilha:
pilha = []

#adcionando elementos a pilha (empilhado):
for n in range(5):
    pilha.append(f"prato {n+1}")

#remover ultimo prato da pilha:

x = pilha.pop(4)

#pilha apos remoção:
print("O prato removido da pilha foi o",x )