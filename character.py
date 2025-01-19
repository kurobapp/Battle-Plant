class Character:
    def __init__(self, name, hp, speed, techniques=None):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.speed = speed
        self.previous_move = None  # 前回の技名を保存
        self.techniques = techniques if techniques else []  # 技のリストを追加
        self.defending = False  # 防御状態を管理するフラグ

    def is_alive(self):
        """キャラクターが生存しているか確認"""
        return self.hp > 0

    def take_damage(self, damage):
        """ダメージを受ける処理 (防御中はダメージ半減)"""
        if self.defending:
            damage /= 2  # 防御中はダメージを半減
            print(f"{self.name} は防御しているため、ダメージが半分になった！")
        self.hp -= int(damage)
        self.hp = max(self.hp, 0)  # HPが0未満にならないようにする

    def choose_move(self, move_name):
        if move_name == self.previous_move and move_name != "防御":
            return False, "同じ技を連続で使用することはできません！"  # 防御技以外は連続使用を禁止

        # 防御技が選ばれた場合はリセット
        if move_name == "防御":
            self.previous_move = "防御"  # 防御技を選んだときは前回の技を防御に更新
            self.defending = True  # 防御状態をオンにする
        else:
            self.previous_move = move_name  # 防御以外の技の場合は通常通り
            self.defending = False  # 防御状態をオフにする

        return True, f"{self.name} は {move_name} を選択しました！"

    def reset_previous_move(self):
        """前回の技をリセット"""
        self.previous_move = None  # 技のリセット
        self.defending = False  # 防御状態をリセット
