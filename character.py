class Character:
    def __init__(self, name, hp, attack, speed, techniques=None):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.speed = speed
        self.is_defending = False  # 防御中かどうかを管理
        self.previous_move = None  # 前回の技名を保存
        self.techniques = techniques if techniques else []  # 技のリストを追加

    def is_alive(self):
        """キャラクターが生存しているか確認"""
        return self.hp > 0

    def take_damage(self, damage):
        """ダメージを受ける処理"""
        if self.is_defending:
            damage //= 2  # 防御中はダメージを半減
        self.hp -= damage
        self.hp = max(self.hp, 0)  # HPが0未満にならないようにする

    def choose_move(self, move_name):
        """
        技や防御の選択処理
        - move_name: 選択された技名
        - 同じ技を連続使用できない制約を追加
        """
        if move_name != "防御" and move_name == self.previous_move:
            return False, "同じ技を連続で使用することはできません！"  # 同じ技の連続使用は禁止

        if move_name == "防御":
            self.is_defending = True
            self.previous_move = None  # 防御を選んだ場合、前回の技情報をリセット
        else:
            self.is_defending = False
            self.previous_move = move_name  # 選んだ技を記録
        return True, f"{self.name} は {move_name} を選択しました！"

    def get_hp_ratio(self):
        """HPの割合を計算"""
        return self.hp / self.max_hp
