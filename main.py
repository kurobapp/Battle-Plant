from charadeta import choose_random_character
from battle import BattleSystem
import random

# プレイヤーと敵をランダムに選択
player = choose_random_character()
enemy = choose_random_character()

# バトル開始
battle = BattleSystem(player, enemy)
print(f"プレイヤーのキャラクター: {player.name} (HP: {player.hp}, Speed: {player.speed})")
print(f"敵のキャラクター: {enemy.name} (HP: {enemy.hp}, Speed: {enemy.speed})")

# プレイヤーの最後に使用した技を記録
last_player_move = None

while player.hp > 0 and enemy.hp > 0:
    print(f"\nプレイヤーのHP: {player.hp}, 敵のHP: {enemy.hp}")
    print("\n選択してください:")
    for i, technique in enumerate(player.techniques, start=1):
        print(f"{i}: {technique.name}")  # 技の名前を表示
    print("4: 防御")

    try:
        choice = int(input("選択: "))
        if choice == 4:
            battle.defend(player)  # 防御を選んだ場合
            last_player_move = None  # 防御時は技の連続使用制限をリセット
            continue  # 防御選択時はターンを終了
        elif 1 <= choice <= 3:
            if last_player_move == choice:
                print("同じ技を連続で使用することはできません！ 別の技を選んでください。")
                continue
            battle.start_battle(choice)  # プレイヤーのターンに技を選択
            last_player_move = choice
        else:
            print("無効な選択です。もう一度選んでください。")
            continue
    except ValueError:
        print("無効な入力です。数字を入力してください。")
        continue

    # 敵が防御中なら防御解除
    enemy.is_defending = False  # 敵の防御状態を解除

    # プレイヤーの攻撃が終わった後に敵のダメージを計算
    if enemy.hp <= 0:
        print(f"{enemy.name} を倒した！ 勝利！")
        break

    # プレイヤーと敵のHPを表示
    print(f"\nプレイヤーのHP: {player.hp}, 敵のHP: {enemy.hp}")
    if player.hp <= 0:
        print(f"{player.name} は倒れた！ 敗北！")
        break
