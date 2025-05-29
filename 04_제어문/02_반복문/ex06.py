# 가위바위보 게임
# : 컴퓨터랑 가위바위보 게임을 하여, 질 때까지 반복하는 게임을 완성하시오.

import random
choices = ["가위", "바위", "보"]
i = 1

while True:
    print("<{}경기>".format(i))
    you = input("가위, 바위, 보! : ")
    # random.choice(리스트) : 리스트 요소 중 하나를 랜덤으로 선택
    computer = random.choice(choices)
    print("당신 : {}".format(you))
    print("컴퓨터 : {}".format(computer))
    if you == "가위" and computer == "바위" or you == "바위" and computer == "보" or you == "보" and computer == "가위":
        print("당신은 졌습니다!")
        break
    elif you != computer:
        print("이겼습니다!")
    else:
        print("비겼습니다!")
    print()
    i += 1