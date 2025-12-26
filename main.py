import random

gn = ["Miyu", "Sari", "Yuna", "Hana", "Kira"]
bn = ["Toren", "Kato", "Guran", "Ryu", "Hanzo"]

uc = str(input("selecione o genero do seu nome, feminino ou masculino ")).lower()

if uc == "feminino":
    guc = random.choice(gn)
    print(guc)

elif uc =="masculino":
    buc = random.choice(bn)
    print(buc)

else:
    print("Digite feminino ou masculino!")

