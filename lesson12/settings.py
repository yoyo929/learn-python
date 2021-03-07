class Settings:
    """存储外星人入侵游戏中所有设置的类"""

    def __init__(self, screen_size=(300, 200), background_color=(255, 182, 193)):
        """初始化设置"""

        self.screen_size = screen_size
        self.background_color = background_color

import json

def load(path):
    with open(path) as sf:
        s = json.load(sf)

    screen = s['screen']
    screen_size = (screen['width'], screen['height'])

    bg = s['background']
    background_color = (bg['R'], bg['G'], bg['B'])

    return Settings(screen_size, background_color)
