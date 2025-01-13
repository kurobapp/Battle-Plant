from character import Character  # Character クラスをインポート

class Technique:
    """技のクラス"""
    def __init__(self, name, attribute, damage):
        self.name = name
        self.attribute = attribute
        self.damage = damage

def choose_random_character():
    """ランダムにキャラクターを選択"""
    # 技を定義
    water_techniques = [
        Technique("水鉄砲", "水", 20),
        Technique("波乗り", "水", 30),
        Technique("アクアリング", "水", 40),
    ]
    fire_techniques = [
        Technique("火炎放射", "炎", 25),
        Technique("炎の渦", "炎", 35),
        Technique("大文字", "炎", 50),
    ]
    grass_techniques = [
        Technique("つるのムチ", "草", 20),
        Technique("リーフブレード", "草", 30),
        Technique("ソーラービーム", "草", 40),
    ]

    # キャラクターを定義
    characters = [
        Character("水", hp=100, attack=20, speed=80, techniques=water_techniques),
        Character("炎", hp=100, attack=25, speed=70, techniques=fire_techniques),
        Character("草", hp=100, attack=15, speed=90, techniques=grass_techniques),
    ]

    import random
    return random.choice(characters)
