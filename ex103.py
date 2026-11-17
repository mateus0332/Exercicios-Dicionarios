import csv

print("programa que converte os valores de uma moeda")
print()

moedas = {}
with open("moedas.csv", encoding = "utf-8", newline = "") as arquivo:
    for codigo, nome_en, nome_pt, cotacao in csv.reader(arquivo):
        moedas[codigo.upper()] = {
            "nome": nome_pt,
            "cotacao": float(cotacao),
        }


valor = float(input("valor em R$: ").replace(",", "."))
codigo = input("Moeda de destino (ex.: USD): ").strip().upper()


if codigo in moedas:
    moeda = moedas[codigo]
    convercao = valor / moeda["cotacao"]
    print(f"{moeda['nome']}: {convercao:.2f}")
else:
    print("moeda nao encontrada")