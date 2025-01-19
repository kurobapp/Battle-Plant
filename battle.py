import random

class BattleSystem:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    def calculate_advantage(self, attacker_attribute, defender_attribute):
        """属性相性を判定（防御技の場合の処理を追加）"""
        if attacker_attribute == "防御":
            return "defender"  # 防御技を選択した場合、必ず負ける
        elif defender_attribute == "防御":
            return "attacker"  # 相手が防御技を選択した場合、必ず勝つ

        advantage_chart = {
        "炎": {"強い": "水", "弱い": "草"},  # 炎は草に強く、水に弱い
        "水": {"強い": "草", "弱い": "炎"},  # 水は炎に強く、草に弱い
        "草": {"強い": "炎", "弱い": "水"},  # 草は水に強く、炎に弱い
        }

        if defender_attribute == advantage_chart[attacker_attribute]["弱い"]:
            return "attacker"
        elif defender_attribute == advantage_chart[attacker_attribute]["強い"]:
            return "defender"
        else:
            return "same"

    def start_battle(self, player_choice):
        """バトルを開始"""
        player_technique = self.player.techniques[player_choice - 1]
        enemy_choice = random.randint(1, 3)
        enemy_technique = self.enemy.techniques[enemy_choice - 1]

        print(f"プレイヤーの技: {player_technique.name} ({player_technique.attribute})")
        print(f"敵の技: {enemy_technique.name} ({enemy_technique.attribute})")

        # 属性判定
        if player_choice == 4:  # 防御を選択した場合
            self.player.is_defending = True
            print(f"{self.player.name} は防御を選択しました！")
            print(f"{self.player.name} は相手の技を受けます。防御中なので、ダメージは半減されます。")
            return

        # 通常のバトル処理
        result = self.calculate_advantage(
            player_technique.attribute, enemy_technique.attribute
        )

        # 属性有利判定
        if result == "attacker":
            print("プレイヤーの属性が有利！")
            self.attack(self.player, self.enemy, player_technique)
        elif result == "defender":
            print("敵の属性が有利！")
            self.attack(self.enemy, self.player, enemy_technique)
        else:  # 属性が同じ場合、速度で判定
            print("属性は同じ！速度で勝負！")
            if self.player.speed > self.enemy.speed:
                print("プレイヤーの速度が速い！")
                self.attack(self.player, self.enemy, player_technique)
            elif self.player.speed < self.enemy.speed:
                print("敵の速度が速い！")
                self.attack(self.enemy, self.player, enemy_technique)
            else:
                print("速度も同じ！引き分け！")

    def attack(self, attacker, defender, technique):
        """攻撃処理"""
        damage = technique.damage  # ここでダメージを計算
        print(f"{attacker.name} の攻撃: {technique.name} ({damage}ダメージ)")
        defender.take_damage(damage)  # ダメージを与える