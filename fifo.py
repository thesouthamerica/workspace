#criando uma fila vazia:
fila = []

#adcionando elementos a fila:
for n in range(5):
    fila.append(f"pessoa {n + 1}")

print(fila)

saiu=fila.pop(0)
print("fila apos sair:", fila)
print("pessoa que saiu:", saiu)
