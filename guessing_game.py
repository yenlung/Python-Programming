# coding: utf-8
from random import randint
def game():
    ans = randint(1, 100)
    guess = -1

    while guess != ans:
        guess = int(input("請輸入一個數字: "))

        if guess>ans:
            print("太大了!")
        elif guess<ans:
            print("太小了!")
        else:
            print("太神了!")
play = True

while play:
    game()
    print("ヽ(∀ﾟ )人(ﾟ∀ﾟ)人( ﾟ∀)人(∀ﾟ )ﾉ")
    again = input("再玩一次?")
    if again == 'no':
        play = False
