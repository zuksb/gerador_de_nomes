import random

girl_name = ["Miyu", "Sari", "Yuna", "Hana", "Kira"]

alt_names1 = ["ka","mi","ra","shi","yu"]
alt_names2 = ["ran","yara","sharan","koyara","wu","Ryuri"]

boys_name = ["Toren", "Kato", "Guran", "Ryu", "Hanzo"]

name_place1 = ["Kan", "Sun", "Sen", "Par", "tarke", "koitsu", "Chin","saze"]
name_place2 = ["ka","rin","mi","ra","shi","yu"]

user_choice = str(input("Selecione o tipo de nome que voce quer(masculino, feminino, lugar ou alternativo ")).lower()

if user_choice == "feminino":
    name_chose_girl = random.choice(girl_name)
    print(name_chose_girl)

elif user_choice =="masculino":
    name_chose_boys = random.choice(boys_name)
    print(name_chose_boys)

elif user_choice == "lugar":
    place_name_chose = random.choice(name_place1) + random.choice(name_place2)
    print(place_name_chose)

elif user_choice == "alternativo":
    name_chose_alt = random.choice(alt_names1) + random.choice(alt_names2)
    print(name_chose_alt)

else:
    print("A opção não esta disponivel!")

