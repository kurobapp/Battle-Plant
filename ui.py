import pygame
from character import Character  # キャラクタークラスのインポート

# フォントの設定を行うクラス
class FontManager:
    def __init__(self, font_path="C:/Windows/Fonts/Meiryo.ttc", font_size=28):
        pygame.font.init()  # フォントを初期化
        self.font = pygame.font.Font(font_path, font_size)

    def render_text(self, text, color=(0, 0, 0)):
        """指定したテキストを描画できるSurfaceを返す"""
        return self.font.render(text, True, color)

class UI:
    def __init__(self):
        self.font_manager = FontManager()
        self.logs = []  # ログのリスト（テキストエリアに表示する内容）

    def add_log(self, message):
        """ログを追加し、最大5行までに制限"""
        self.logs.append(message)
        if len(self.logs) > 3:  # 表示行数を制限
            self.logs.pop(0)

    def draw_pokemon(self, screen, player, enemy):
        # プレイヤーと敵の描画（ブロック）
        pygame.draw.rect(screen, player.color, (150, 300, 50, 50))  # プレイヤー位置
        pygame.draw.rect(screen, enemy.color, (450, 250, 50, 50))  # 敵位置（下げた）

    def draw_hp(self, screen, player, enemy):
        # HPバーの描画（プレイヤー）
        pygame.draw.rect(screen, (255, 0, 0), (120, 290, 100, 10))  # 赤背景
        pygame.draw.rect(screen, (0, 255, 0), (120, 290, int(100 * player.get_hp_ratio()), 10))  # 緑バー

        # HPバーの描画（敵）
        pygame.draw.rect(screen, (255, 0, 0), (420, 230, 100, 10))  # 赤背景（下げた）
        pygame.draw.rect(screen, (0, 255, 0), (420, 230, int(100 * enemy.get_hp_ratio()), 10))  # 緑バー（下げた）

    def draw_ui(self, screen):
        # テキストエリアの背景
        pygame.draw.rect(screen, (220, 220, 220), (0, 0, 640, 100))  # 上部のテキストエリア

        # テキストエリアにログを表示
        for i, log in enumerate(self.logs):
            text_surface = self.font_manager.render_text(log, color=(0, 0, 0))
            screen.blit(text_surface, (10, 10 + i * 20))  # 各行を縦にずらして描画

        # コマンドメニューの描画（十字形）
        pygame.draw.rect(screen, (200, 200, 200), (0, 350, 640, 130))  # 背景

        # 攻撃のテキストを描画
        attack1_text = self.font_manager.render_text("1の攻撃")
        attack2_text = self.font_manager.render_text("2の攻撃")
        attack3_text = self.font_manager.render_text("3の攻撃")
        defend_text = self.font_manager.render_text("防御")
        swap_text = self.font_manager.render_text("入れ替え")

        # 十字配置：中央が防御、その上下左右が攻撃
        screen.blit(attack1_text, (50, 400))  # 上
        screen.blit(attack2_text, (150, 350))  # 左
        screen.blit(attack3_text, (250, 400))  # 右
        screen.blit(defend_text, (150, 450))  # 中央
        screen.blit(swap_text, (400, 400))  # 下
    
