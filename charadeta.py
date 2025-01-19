import random
from character import Character  # Character クラスをインポート

class Technique:
    """技のクラス"""
    def __init__(self, name, attribute, damage):
        self.name = name
        self.attribute = attribute
        self.damage = damage

    @staticmethod
    def choose_player_character():
        """プレイヤーキャラクターを選択"""
        water_techniques = [
            Technique("アクアビーム", "水", 70),
            Technique("フレア", "炎", 50),
            Technique("リーフアロー", "草", 50),
            Technique("防御", "防御", 0),
        ]
        fire_techniques = [
            Technique("ウォータースラッシュ", "水", 50),
            Technique("フレイムスラッシュ", "炎", 80),
            Technique("グラススラッシュ", "草", 20),
            Technique("防御", "防御", 0),
        ]
        grass_techniques = [
            Technique("水の波動", "水", 60),
            Technique("炎の刻印", "炎", 60),
            Technique("草の導き", "草", 65),
            Technique("防御", "防御", 0),
        ]

        # プレイヤーキャラクターを選ぶ
        characters = [
            Character("水の魔法使い", hp=random.randint(90, 110), speed=random.randint(115, 135), techniques=water_techniques),
            Character("炎の戦士", hp=random.randint(140, 160), speed=random.randint(65, 85), techniques=fire_techniques),
            Character("草の僧侶", hp=random.randint(65, 85), speed=random.randint(90, 110), techniques=grass_techniques),
        ]

        chosen_character = random.choice(characters)
        print(f"{chosen_character.name}キャラクターが選ばれました！")
        return chosen_character

    @staticmethod
    def choose_stage1_enemy():
        """ステージ1の敵キャラクターを選択（3キャラからランダム選択）"""
        water_techniques = [
            Technique("水鉄砲", "水", 50),
            Technique("突進", "水", 30),
            Technique("熱湯", "炎", 20),
        ]
        fire_techniques = [
            Technique("火の粉", "炎", 50),
            Technique("突進", "炎", 30),
            Technique("種植え", "草", 20),
        ]
        grass_techniques = [
            Technique("水やり", "水", 20),
            Technique("木の葉", "草", 50),
            Technique("突進", "草", 30),
        ]

        # ステージ1のキャラクター3体
        characters = [
            Character("水スライム", hp=random.randint(80, 80), speed=random.randint(100, 100), techniques=water_techniques),
            Character("炎スライム", hp=random.randint(120, 120), speed=random.randint(60, 60), techniques=fire_techniques),
            Character("草スライム", hp=random.randint(45, 45), speed=random.randint(80, 80), techniques=grass_techniques),
        ]
        
        chosen_enemy = random.choice(characters)
        return chosen_enemy

    @staticmethod
    def choose_stage2_enemy():
        """ステージ2の敵キャラクターを選択（3キャラからランダム選択）"""
        water_techniques = [
            Technique("アクアビーム", "水", 70),
            Technique("フレア", "炎", 50),
            Technique("リーフアロー", "草", 50),
        ]
        fire_techniques = [
            Technique("ウォータースラッシュ", "水", 50),
            Technique("フレイムスラッシュ", "炎", 80),
            Technique("グラススラッシュ", "草", 20),
        ]
        grass_techniques = [
            Technique("水の波動", "水", 60),
            Technique("炎の刻印", "炎", 60),
            Technique("草の導き", "草", 65),
        ]

        # ステージ2のキャラクター3体
        characters = [
            Character("水の魔法使い", hp=random.randint(90, 110), speed=random.randint(115, 135), techniques=water_techniques),
            Character("炎の戦士", hp=random.randint(140, 160), speed=random.randint(65, 85), techniques=fire_techniques),
            Character("草の僧侶", hp=random.randint(65, 85), speed=random.randint(90, 110), techniques=grass_techniques),
        ]

        chosen_enemy = random.choice(characters)
        return chosen_enemy

    @staticmethod
    def choose_stage3_enemy():
        """ステージ3の敵キャラクターを選択（2キャラからランダム選択）"""
        love_techniques = [
            Technique("ラブビーム", "水", 60),
            Technique("愛の鞭", "炎", 90),
            Technique("大母神", "草", 50),
        ]
        gold_techniques = [
            Technique("ジャックポット", "水", 80),
            Technique("ゴールドラッシュ", "炎", 80),
            Technique("コインベット", "草", 40),
        ]

        # ステージ3のキャラクター2体
        characters = [
            Character("愛の伝道師", hp=random.randint(250, 350), speed=random.randint(100, 150), techniques=love_techniques),
            Character("金の亡者", hp=random.randint(200, 250), speed=random.randint(210, 300), techniques=gold_techniques),
        ]

        chosen_enemy = random.choice(characters)
        return chosen_enemy
