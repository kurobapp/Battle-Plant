import random
from charadeta import Technique  # こちらを修正
from battle import BattleSystem  # バトルシステムをインポート

# ステージごとの敵キャラクターを設定
stage_1_enemies = [Technique.choose_stage1_enemy() for _ in range(3)]
stage_2_enemies = [Technique.choose_stage2_enemy() for _ in range(3)]
stage_3_enemies = [Technique.choose_stage3_enemy() for _ in range(2)]

# メインのゲーム処理
player = Technique.choose_player_character()

def start_stage(stage_enemies, stage_number):
    print(f"\n--- ステージ {stage_number} ---")
    print(f"{player.name} のHP: {player.hp}, スピード: {player.speed}")
    enemy = random.choice(stage_enemies)
    print(f"敵のクリーチャー: {enemy.name} (HP: {enemy.hp}, Speed: {enemy.speed})")

    battle = BattleSystem(player, enemy)
    player.reset_previous_move()
    while player.hp > 0 and enemy.hp > 0:
        print(f"\n{player.name}のHP: {player.hp}, {enemy.name}のHP: {enemy.hp}")
        print("\n選択してください:")
        for i, technique in enumerate(player.techniques, start=1):
            print(f"{i}: {technique.name}")

        try:
            choice = int(input("選択: "))
            if 1 <= choice <= len(player.techniques):  # 選択肢がリストの範囲内であることを確認
                valid_move, message = player.choose_move(player.techniques[choice - 1].name)
                if not valid_move:
                    print(message)
                    continue

                player_technique = player.techniques[choice - 1]
                enemy_choice = random.randint(1, 3)
                valid_enemy_move = False
                while not valid_enemy_move:
                    enemy_technique = enemy.techniques[enemy_choice - 1]
                    if enemy_technique.name != enemy.previous_move:  # 連続技を避ける
                        valid_enemy_move = True
                    else:
                        enemy_choice = random.randint(1, 3)
                print(f"プレイヤーの技: {player_technique.name} ({player_technique.attribute})")
                print(f"敵の技: {enemy_technique.name} ({enemy_technique.attribute})")

                # 属性判定
                result = battle.calculate_advantage(
                    player_technique.attribute, enemy_technique.attribute
                )

                if result == "attacker":
                    print("プレイヤーの属性が有利！")
                    battle.attack(player, enemy, player_technique)
                elif result == "defender":
                    print("敵の属性が有利！")
                    battle.attack(enemy, player, enemy_technique)
                else:  # 属性が同じ場合、速度で判定
                    print("属性は同じ！速度で勝負！")
                    if player.speed > enemy.speed:
                        battle.attack(player, enemy, player_technique)
                    elif player.speed < enemy.speed:
                        battle.attack(enemy, player, enemy_technique)
                    else:
                        print("速度も同じ！引き分け！")
            else:
                print("無効な選択です。もう一度選んでください。")
                continue
        except ValueError:
            print("無効な入力です。数字を入力してください。")
            continue

        # 勝敗判定
        if player.hp <= 0:
            print(f"{player.name} は倒れた！ 敗北！")
            break
        elif enemy.hp <= 0:
            print(f"{enemy.name} を倒した！ 勝利！")
            return True  # ステージクリア

    return False  # プレイヤー敗北

# ゲームの進行
stage_number = 1
while stage_number <= 3:
    if stage_number == 1:
        if start_stage(stage_1_enemies, stage_number):
            print(f"--- ステージ {stage_number} クリア ---")
            stage_number += 1
        else:
            print(f"{player.name}が敗北しました。ゲームオーバー！")
            break
    elif stage_number == 2:
        if start_stage(stage_2_enemies, stage_number):
            print(f"--- ステージ {stage_number} クリア ---")
            stage_number += 1
        else:
            print(f"{player.name}が敗北しました。ゲームオーバー！")
            break
    elif stage_number == 3:
        if start_stage(stage_3_enemies, stage_number):
            print("ゲームクリア！")
            break
        else:
            print(f"{player.name}が敗北しました。ゲームオーバー！")
            break
