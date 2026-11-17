print("programa que coleta o nome e a idade de pessoas e apresent se sao maiores ou menores de idade")

pessoas = []
for i in range(10):
    nome = str(input(f"nome da pessoa {i + 1}: "))
    idade = int(input(f"idade de: {nome}"))
    pessoas.append({"nome": nome, "idade": idade})

menores = [p for p in pessoas if p["idade"] < 18]
maiores = [p for p in pessoas if p["idade"] >= 18]

print("menores de 18 anos: ")
for p in menores:
    print(f"{p['nome']} - {p['idade']} anos")

print("maiores de 18 anos: ")
for p in maiores:
    print(f"{p['nome']} - {p['idade']} anos")