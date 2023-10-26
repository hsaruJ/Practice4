import random


def computer_move(n):
    take_cnt = random.randint(1, min(n - 1, 3))
    print("Компьютер взял", take_cnt, ("камень" if take_cnt == 1 else "камня"),
          "из кучки.")

    return take_cnt


def player_move(n):
    print("Сколько камней вы хотите взять? ", end="")
    take_cnt = -1
    try:
        take_cnt = int(input())
    except ValueError:
        print("Ошибка. Число введено неверно."
              "Компьютер не смог вас понять и вы пропускаете ход.")
        return 0

    if not (1 <= take_cnt <= 3):
        print("Вы не можете взять число меньше 1 или больше 3.",
              "Вы ошиблись и пропускаете ход.", sep="\n")
        return 0

    if take_cnt > n - 1:
        print("Вы не можете взять столько же или больше, чем есть в кучке.",
              "Вы ошиблись и пропускаете ход.", sep="\n")
        return 0

    print("Вы взяли", take_cnt, ("камень" if take_cnt == 1 else "камня"),
          "из кучки.")
    return take_cnt


f_rules = open("bashe_output_rules.txt")
print(*f_rules.readlines(), sep="")

# random.seed(1)    #  information for debug
n = random.randint(4, 30)

# 0 - computer's move, 1 - player's move
move_order = random.randint(0, 1)

while n > 1:
    print(f"В кучке {n} камней.")
    if move_order == 0:
        n -= computer_move(n)
    else:
        n -= player_move(n)

    move_order = 1 - move_order
    
if (n == 1) and (move_order == 0):
    print("Поздравляю! Вы победили.")
else:
    print("Вы стали опытнее. Компьютер одержал победу.")