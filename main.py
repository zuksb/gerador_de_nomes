import random


girl_name = ["Miyu", "Sari", "Yuna", "Hana", "Kira"]
alt_names1 = ["ka", "mi", "ra", "shi", "yu"]
alt_names2 = ["ran", "yara", "sharan", "koyara", "wu", "Ryuri"]
boys_name = ["Toren", "Kato", "Guran", "Ryu", "Hanzo"]
name_place1 = ["Kan", "Sun", "Sen", "Par", "tarke", "koitsu", "Chin", "saze"]
name_place2 = ["ka", "rin", "mi", "ra", "shi", "yu"]

while True:
    
    print("Seja Bem vindo, suas opções são: Masculino, feminino, lugar, ou alternativo, selecione a opção que desejar, caso queira sair, digite 'sair', e caso nao queira escolher, digite 'opcao aleatoria'")
    user_choice = input("Selecione qual opção voce quer gerar: ").lower().strip()
    
    random_option = random.choice(["masculino", "feminino", "lugar", "alternativo"])

    if user_choice == "opcao aleatoria":
        opcao_final = random_option
    else:
        opcao_final = user_choice
    
    if opcao_final == "sair":
        print('Até logo, tenha um ótimo dia!')
        break  
    
    elif opcao_final == "opcao aleatoria":
        random_option = random.choice(["masculino", "feminino", "lugar", "alternativo"])

    
    elif opcao_final == "feminino":
        name_chose_girl = random.choice(girl_name)
        print(f"Nome gerado: {name_chose_girl}")
    
    elif opcao_final == "masculino":
        name_chose_boys = random.choice(boys_name)
        print(f"Nome gerado: {name_chose_boys}")
    
    elif opcao_final == "lugar":
        place_name_chose = random.choice(name_place1) + random.choice(name_place2)
        print(f"Nome gerado: {place_name_chose}")
    
    elif opcao_final == "alternativo":
        name_chose_alt = random.choice(alt_names1) + random.choice(alt_names2)
        print(f"Nome gerado: {name_chose_alt}")
    
    else:
        print("A opção não está disponível!")
        print("Opções válidas: masculino, feminino, lugar, alternativo ou sair")
    
    print()  