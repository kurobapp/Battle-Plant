import random  # random モジュールをインポート

class BattleSystem:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def calculate_advantage(self, attacker_attribute, defender_attribute):
        """属性相性を判定"""
        advantage_chart = {
            "炎": {"強い": "草", "弱い": "水"},
            "水": {"強い": "炎", "弱い": "草"},
            "草": {"強い": "水", "弱い": "炎"},
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

        # 属性の判定
        result = self.calculate_advantage(
            player_technique.attribute, enemy_technique.attribute
        )

        # プレイヤーが防御中ならダメージを半減
        if self.player.is_defending:
            print(f"{self.player.name} は防御中なので、ダメージが半減します！")
            damage = player_technique.damage // 2  # 半減
            self.enemy.hp -= damage
            if self.enemy.hp < 0:
                self.enemy.hp = 0
            print(f"{self.player.name} の {player_technique.name} が {self.enemy.name} に {damage} ダメージ！")
            print(f"{self.enemy.name} の残りHP: {self.enemy.hp}")
            return  # 攻撃後ターン終了

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
        """攻撃を処理"""
        damage = technique.damage
        if defender.is_defending:  # 防御中ならダメージを半減
            damage //= 2
            print(f"{defender.name} は防御中！ダメージが半減！")

        defender.hp -= damage
        if defender.hp < 0:
            defender.hp = 0

        print(f"{attacker.name} の {technique.name} が命中！ {defender.name} に {damage} ダメージ！")
        print(f"{defender.name} の残りHP: {defender.hp}")


    def defend(self, character):
        """防御の処理"""
        character.is_defending = True
        print(f"{character.name} は防御の体勢をとった！")
