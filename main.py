import random


while True:
    user_input = input("Se voce deseja gerar um nome, digite 'gerar', caso queira sair, digite 'sair': ").lower().strip()
    if user_input == "sair":
        print('Até logo, tenha um ótimo dia!')
        break
    elif user_input == "gerar":
        p1 = ["ra", "re", "ri", "ro", "ru", "riyu", "sari", "yuna", "hana", "kira", "ran", "yara", "sharan", "koyara", "wu", "ryuri", "ka", "mi", "ra", "shi", "yu", "ba", "be", "bi", "bo", "bu", "ka",  "kato", "ryu", ]
        p2 = ["ra", "re", "ri", "ro", "ru", "riyu", "sari", "yuna", "hana", "kira", "ran", "yara", "sharan", "koyara", "wu", "ryuri", "ka", "mi", "ra", "shi", "yu", "ba", "be", "bi", "bo", "bu", "ka",  "kato", "ryu", ]

        full_name = random.choice(p1) + random.choice(p2)
        print("Nome gerado:", full_name.capitalize())
    else:
        print("Opção inválida. Por favor, digite 'gerar' ou 'sair'.")