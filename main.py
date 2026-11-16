import random


while True:
    user_input = input("Se voce deseja gerar um nome, digite 'gerar', caso queira sair, digite 'sair': ").lower().strip()
    if user_input == "sair":
        print('Até logo, tenha um ótimo dia!')
        break
    elif user_input == "gerar":
        p1 = ["ra", "re", "ri", "ro", "ru", "riyu", "sari", "yuna", "hana", "kira", "ran", "yara", "sharan", "koyara", "wu", "ryuri", "ka", "mi", "ra", "shi", "yu", "ba", "be", "bi", "bo", "bu", "ka",  "kato", "ryu", ]
        p2 = ["ra", "re", "ri", "ro", "ru", "riyu", "sari", "yuna", "hana", "kira", "ran", "yara", "sharan", "koyara", "wu", "ryuri", "ka", "mi", "ra", "shi", "yu", "ba", "be", "bi", "bo", "bu", "ka",  "kato", "ryu", ]

        p1_name = random.choice(p1)
        p2_name = random.choice(p2)
        full_name = p1_name + p2_name
        print(f"Nome gerado: {full_name.capitalize()} (junção de {p1_name} e {p2_name})")
    else:
        print("Opção inválida. Por favor, digite 'gerar' ou 'sair'.")