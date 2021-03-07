import sys
import pygame

import settings

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self, settings): # initialize 初始化
        """初始化游戏并且创建游戏资源"""
        pygame.init() # 初始化pygame，初始化之后才能用pygame

        self.settings = settings
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption('外星人入侵')

    def run_game(self):
        """开始游戏主循环"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.background_color)
            # 让最近绘制的屏幕可见
            pygame.display.flip()   

# 表示程序从这里开始执行
if __name__ == "__main__":
    s = settings.load("lesson12/settings.json")
    ai = AlienInvasion(s)
    ai.run_game()