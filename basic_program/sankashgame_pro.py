import  random
#
def enter_choice():
    while True:
        print("Enter your choice from following:")
        for x, y in choice_dict.items():
            print(x, ':', y)
        z = input()
        if z in choice_dict.keys():
            break
        else:
            print('Wrong input, Try again !!!')
    return choice_dict[z]
    #     print("Enter your choice from following:")
    #     for x, y in choice_dict.items():
    #         print(x, ':', y)
    #     z = input()
    #     if z in choice_dict.keys():
    #         break
    #     else:
    #         print('Wrong input, Try again !!!')
    # return choice_dict[z]


choice_dict = {'1': 'Snake', '2': 'Water', '3': 'Gun'}
compu_score = 0
your_score = 0
i = 10
while i:
    compu_choice = random.choice(list(choice_dict.values()))
    your_choice = enter_choice()
    if compu_choice == your_choice:
        print(f'computer choice was {compu_choice} and it is tie in round {11-i}')
        i -= 1
        continue
    elif compu_choice == 'sanak' and your_choice == 'wsater':
        print(f'computer choice was {compu_choice} and computer won in round {11 - i}')
        compu_score += 1
    elif compu_choice == 'water' and your_choice == 'sanak':
        print(f'computer choice was {compu_choice} and you won in round {11 - i}')
        your_score += 1
    elif compu_choice == 'sanak' and your_choice == 'gun':
        print(f'computer choice was {compu_choice} and you won in round {11 - i}')
        your_score += 1
    elif compu_choice == 'gun' and your_choice == 'sanak':
        print(f'computer choice was {compu_choice} and computer won in round {11 - i}')
        compu_score += 1
    elif compu_choice == 'water' and your_choice == 'gun':
        print(f'computer choice was {compu_choice} and computer won in round {11 - i}')
        compu_score += 1
    elif compu_choice == 'gun' and your_choice == 'water':
        print(f'computer choice was {compu_choice} and you won in round {11 - i}')
        your_score += 1
    i -= 1
print('Game Over !!!')

if your_score > compu_score:
    print("you won finally ")
elif compu_score > your_score:
    print("computer won finally...")
else:
    print("It's is tie")

print(f'your score : {your_score} \ncomputer\'s score: {compu_score}')

#
# def enter_chhoose():
#     while True:
#         print("Enter your choise from following :")
#         for x, y in choose_dict.items():
#             print(x, ':', y)
#         z = input()
#         if z in choose_dict.keys():
#             break
#         else:
#             print("Input is wrong! try again..!")
#
#
#
# choose_dict={'1':'sanak','2':'water','3':'gun'}
# compu_score = 0
# you_score = 0
# i = 10
#
# while i:
#     compu_choice = random.choice(list(choose_dict.values()))
#     your_choice = enter_chhoose()
#
#     if compu_choice == your_choice:
#         print(f"computer choose is {compu_choice} and it is round of vlue {11-i}")
#         continue
#     elif compu_choice == "sanak" and your_choice == "water":
#         print(f"computer choose  is{compu_choice} and it is round of value {11-i}")
#         your_choice += 1
#     elif compu_choice == "water" and your_choice =="sanak":
#         print(f"computer choose is {compu_choice} and it is round of value {11-i}")
#         you_score +=1
#     elif compu_choice =="sanak" and your_choice =="gun":
#         print(f"computer choose is {compu_choice} and it is round of value {11-i}")
#         you_score +=1
#     elif compu_choice =="gun" and your_choice=="sanak":
#         print(f"computer choose is {compu_choice} and it is round of value {11-i}")
#         compu_score +=1
#     elif compu_choice =="gun" and your_choice =="water":
#         print(f"computer choose is {compu_choice} and it is round of value{11-i}")
#         compu_score +=1
#     elif compu_choice =="water" and your_choice=="gun":
#         print(f"computer choose is {compu_choice} and it is round of value {11-i}")
#         you_score +=1
#     i -=1
#     print("Game over !!!!!")
#
# if you_score > compu_score:
#     print(" yor are won the game!!!")
# elif compu_score > you_score:
#     print("you loose the game !")
# else:
#     print("It's is try again..!")
#
# print(f"you score {you_score} \n computer secore{compu_score}")
# print("Program End")
# print("thanksyou")