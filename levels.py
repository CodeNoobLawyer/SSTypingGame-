class Level:
    def __init__(self, background, enemy, enemy_icon, bullet_icon, enemy_hp):
        self.background = background
        self.enemy = enemy
        self.enemy_icon = enemy_icon
        self.bullet_icon = bullet_icon
        self.enemy_hp = enemy_hp

levels = [
    Level("background1.png", "Thor", "enemy1.png", "bullet1.png", 100),
    Level("background2.png", "Fenrir", "enemy2.png", "bullet2.png", 200),
    Level("background3.png", "Hagen", "enemy3.png", "bullet3.png", 400),
    Level("background4.png", "Mimir", "enemy4.png", "bullet4.png", 700),
    Level("background5.png", "Alberich", "enemy5.png", "bullet5.png", 1100),
    Level("background6.png", "Bud", "enemy6.png", "bullet6.png", 1600),
    Level("background7.png", "Siegfried", "enemy7.png", "bullet7.png", 2200),
    Level("background8.png", "QueenHilda", "enemy8.png", "bullet8.png", 3000),
]