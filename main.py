import random
from charadeta import choose_random_character  # キャラクターを選択する関数をインポート
from battle import BattleSystem  # バトルシステムをインポート

# メインのゲーム処理
player = choose_random_character()
enemy = choose_random_character()

battle = BattleSystem(player, enemy)
print(f"プレイヤーのキャラクター: {player.name} (HP: {player.hp}, Speed: {player.speed})")
print(f"敵のキャラクター: {enemy.name} (HP: {enemy.hp}, Speed: {enemy.speed})")

last_player_move = None

while player.hp > 0 and enemy.hp > 0:
    print(f"\nプレイヤーのHP: {player.hp}, 敵のHP: {enemy.hp}")
    print("\n選択してください:")
    for i, technique in enumerate(player.techniques, start=1):
        print(f"{i}: {technique.name}")
    print(f"4: 防御")

    try:
        choice = int(input("選択: "))
        
        if 1 <= choice <= 3:
            valid_move, message = player.choose_move(player.techniques[choice - 1].name)
            if not valid_move:
                print(message)
                continue

            player_technique = player.techniques[choice - 1]
            enemy_choice = random.randint(1, 3)
            enemy_technique = enemy.techniques[enemy_choice - 1]

            print(f"プレイヤーの技: {player_technique.name} ({player_technique.attribute})")
            print(f"敵の技: {enemy_technique.name} ({enemy_technique.attribute})")

            # 属性判定
            result = battle.calculate_advantage(
                player_technique.attribute, enemy_technique.attribute
            )

            if result == "attacker":
                print("プレイヤーの属性が有利！")
                # プレイヤーが攻撃、敵は反撃しない
                battle.attack(player, enemy, player_technique)
            elif result == "defender":
                print("敵の属性が有利！")
                # 敵が攻撃、プレイヤーは反撃しない
                battle.attack(enemy, player, enemy_technique)
            else:  # 属性が同じ場合、速度で判定
                print("属性は同じ！速度で勝負！")
                if player.speed > enemy.speed:
                    battle.attack(player, enemy, player_technique)
                elif player.speed < enemy.speed:
                    battle.attack(enemy, player, enemy_technique)
                else:
                    print("速度も同じ！引き分け！")

        elif choice == 4:  # 防御選択
            valid_move, message = player.choose_move("防御")
            if not valid_move:
                print(message)
                continue

            print(f"{player.name} は防御を選択しました！")

            # 敵の攻撃を軽減
            enemy_choice = random.randint(1, 3)
            enemy_technique = enemy.techniques[enemy_choice - 1]
            damage = battle.calculate_damage(enemy, player, enemy_technique, defender_is_defending=True)
            player.hp -= damage
            player.hp = max(player.hp, 0)  # HPが0未満にならないようにする

            print(f"敵の攻撃: {enemy_technique.name} ({enemy_technique.attribute})")
            print(f"防御の結果、{player.name} は {damage} ダメージを受けた！")
            print(f"{player.name} の残りHP: {player.hp}")
            continue  # 防御のターン終了

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
        break
