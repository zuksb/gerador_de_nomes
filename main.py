import random


while True:
    user_input = input("Se voce deseja gerar um nome, digite 'gerar', caso queira sair, digite 'sair': ").lower().strip()
    if user_input == "sair":
        print('Até logo, tenha um ótimo dia!')
        break
    elif user_input == "gerar":
        p1 = ["ra", "re", "ri", "ro", "ru", "Miyu", "Sari", "Yuna", "Hana", "Kira", "ran", "yara", "sharan", "koyara", "wu", "Ryuri", "ka", "mi", "ra", "shi", "yu", "ba", "be", "bi", "bo", "bu","ka", "Toren", "Kato", "Guran", "Ryu", "Hanzo"]
        p2 = ["ra", "re", "ri", "ro", "ru", "Miyu", "Sari", "Yuna", "Hana", "Kira", "ran", "yara", "sharan", "koyara", "wu", "Ryuri", "ka", "mi", "ra", "shi", "yu", "ba", "be", "bi", "bo", "bu","ka", "Toren", "Kato", "Guran", "Ryu", "Hanzo"]

        full_name = random.choice(p1) + random.choice(p2)
        print("Nome gerado:", full_name)
    else:
        print("Opção inválida. Por favor, digite 'gerar' ou 'sair'.")