import pygame
import random
import sys
import os
import shutil
import tkinter as tk
from time import time

class TimerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("北欧圣战计时器")
        self.geometry("300x150")
        
        # 计时器状态变量
        self.start_time = 0
        self.running = False
        
        # 创建界面元素
        self.time_label = tk.Label(self, text="00:00:00.00", font=('Arial', 24))
        self.time_label.pack(pady=10)
        
        self.start_btn = tk.Button(self, text="开始", command=self.start_timer, width=10)
        self.start_btn.pack(side=tk.LEFT, padx=20)
        
        self.stop_btn = tk.Button(self, text="结束", command=self.stop_timer, width=10)
        self.stop_btn.pack(side=tk.RIGHT, padx=20)
    
    def start_timer(self):
        """启动计时器"""
        if not self.running:
            self.running = True
            self.start_time = time() - (self.start_time if self.start_time else 0)
            self.update_time()
    
    def stop_timer(self):
        """停止计时器"""
        self.running = False
    
    def update_time(self):
        """更新计时显示"""
        if self.running:
            elapsed = time() - self.start_time
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            milliseconds = int((elapsed % 1) * 100)
            self.time_label.config(
                text=f"{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
            )
            self.after(10, self.update_time)

if __name__ == "__main__":
    app = TimerApp()
    app.mainloop()

def move_images_to_graphic_folder():
    # 定义图片文件的扩展名
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
    
    # 获取当前目录
    current_directory = os.getcwd()
    
    # 创建 graphic 文件夹（如果不存在）
    graphic_folder = os.path.join(current_directory, 'graphic')
    if not os.path.exists(graphic_folder):
        os.makedirs(graphic_folder)
    
    # 遍历当前目录下的所有文件
    for filename in os.listdir(current_directory):
        # 获取文件扩展名
        _, ext = os.path.splitext(filename)
        
        # 检查文件是否为图片文件
        if ext.lower() in image_extensions:
            # 构建源文件路径和目标文件路径
            source_path = os.path.join(current_directory, filename)
            destination_path = os.path.join(graphic_folder, filename)
            
            # 移动文件
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename} to {graphic_folder}")

if __name__ == "__main__":
    move_images_to_graphic_folder()

# 初始化 Pygame
pygame.init()

# 设置窗口大小和标题
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Saint Seiya God Warrior War Game")

# 加载音乐文件
pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "saintseiya.mp3"))
pygame.mixer.music.play(-1)  # 循环播放音乐

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 定义关卡信息
levels = [
    {"enemy": "Thor", "enemy_icon": "enemy1.png", "background": "background1.png", "enemy_hp": 100},
    {"enemy": "Fenrir", "enemy_icon": "enemy2.png", "background": "background2.png", "enemy_hp": 200},
    {"enemy": "Hagen", "enemy_icon": "enemy3.png", "background": "background3.png", "enemy_hp": 400},
    {"enemy": "Mimir", "enemy_icon": "enemy4.png", "background": "background4.png", "enemy_hp": 700},
    {"enemy": "Alberich", "enemy_icon": "enemy5.png", "background": "background5.png", "enemy_hp": 1100},
    {"enemy": "Bud", "enemy_icon": "enemy6.png", "background": "background6.png", "enemy_hp": 1600},
    {"enemy": "Siegfried", "enemy_icon": "enemy7.png", "background": "background7.png", "enemy_hp": 2200},
    {"enemy": "QueenHilda", "enemy_icon": "enemy8.png", "background": "background8.png", "enemy_hp": 3000}
    # 其他关卡...
]

# 加载资源（假设资源文件在同一目录下）
try:
    tank_images = {name: pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', f"{name}.jpg")), (100, 100)) for name in ["Seiya", "Shiryu", "Ikki", "Hyoga", "Shun"]}
    enemy_images = {level["enemy"]: pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', level["enemy_icon"])), (100, 100)) for level in levels}  # 修改: 缩放敌人图标
    background_images = {level["background"]: pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', level["background"])), (SCREEN_WIDTH, SCREEN_HEIGHT)) for level in levels}  # 修改: 缩放背景图
    bullet_images = {
        "Seiya": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "bullet01.png")), (50, 50)),
        "Shiryu": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "bullet02.png")), (50, 50)),
        "Ikki": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "bullet03.png")), (50, 50)),
        "Hyoga": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "bullet04.png")), (50, 50)),
        "Shun": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "bullet05.png")), (50, 50))
    }
    enemy_bullet_images = {
        "enemy1": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "bullet1.png")), (50, 50)),
        "enemy2": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "bullet2.png")), (50, 50)),
        "enemy3": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "bullet3.png")), (50, 50)),
        "enemy4": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "bullet4.png")), (50, 50)),
        "enemy5": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "bullet5.png")), (50, 50)),
        "enemy6": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "bullet6.png")), (50, 50)),
        "enemy7": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "bullet7.png")), (50, 50)),
        "enemy8": pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "bullet8.png")), (50, 50))
    }
    # 新增背景图加载
    menu_background = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "start.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))  # 修改: 缩放菜单背景图
    ending_background = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'graphic', "ending.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))  # 新增: 加载通关画面背景图
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    sys.exit()

# 定义字体
font = pygame.font.Font(None, 36)

# 定义敌人的单词列表（使用牛津字典的一部分单词）
word_list = [
    "abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon",
    "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo",
    "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt",
    "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage",
    "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foist",
    "fopdoodle", "frivolous", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo",
    "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox",
    "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx",
    "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole",
    "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph",
    "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull",
    "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka",
    "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz",
    "rhubarb", "rhythm", "rickshaw", "schnauzer", "scratch", "shiv", "snazzy", "sphinx", "sprang", "squawk", "staff", "strength",
    "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz",
    "transcript", "transgress", "trivia", "twelfth", "twilight", "twinkle", "typhoon", "typewriter", "unknown", "unworthy",
    "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wavy", "waxy",
    "wellspring", "wheezy", "whiskey", "whizzing", "wimpy", "wristwatch", "wyrm", "xylophone", "yachtsman", "yippee", "yoked",
    "youthful", "yummy", "zephyr", "zigzag", "zilch", "zippy", "zombie"
]

# 初始化变量
score = 0
current_word = random.choice(word_list)
player_input = ""
enemy_x, enemy_y = random.randint(50, SCREEN_WIDTH - 50), 50
bullet_x, bullet_y = -100, -100  # 子弹初始位置
bullet_speed = 20
show_menu = True  # 是否显示菜单
difficulty = None  # 游戏难度
time_limit = 60  # 默认时间限制为60秒（easy难度）
word_timer = 0  # 单词计时器
consecutive_correct = 0  # 连续正确输入次数
used_words = set()  # 用于存储已使用的单词
current_level = 0  # 当前关卡
player = None  # 当前玩家角色
player_hp = 100  # 玩家初始生命值
player_attack = 10  # 玩家初始攻击力
enemy_hp = levels[current_level]['enemy_hp']  # 当前敌人生命值
attack_frame = 0  # 攻击动画帧

# 新增变量用于显示通关画面
show_ending = False

# 初始化 running 变量
running = True

# 初始化 clock 变量
clock = pygame.time.Clock()

def draw_menu():
    # 使用背景图填充屏幕
    screen.blit(menu_background, (0, 0))
    title_text = font.render("Saint Seiya God Warrior War Game", True, RED)
    start_text = font.render("Start", True, RED)
    settings_text = font.render("Settings", True, RED)
    quit_text = font.render("Quit", True, RED)
    
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, 200))
    screen.blit(settings_text, (SCREEN_WIDTH // 2 - settings_text.get_width() // 2, 300))
    screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 400))

def draw_settings():
    screen.fill(BLACK)
    title_text = font.render("Settings", True, RED)
    easy_text = font.render("Easy", True, RED)
    medium_text = font.render("Medium", True, RED)
    hard_text = font.render("Hard", True, RED)
    hell_text = font.render("Hell", True, RED)
    back_text = font.render("Back", True, RED)
    
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
    screen.blit(easy_text, (SCREEN_WIDTH // 2 - easy_text.get_width() // 2, 200))
    screen.blit(medium_text, (SCREEN_WIDTH // 2 - medium_text.get_width() // 2, 300))
    screen.blit(hard_text, (SCREEN_WIDTH // 2 - hard_text.get_width() // 2, 400))
    screen.blit(hell_text, (SCREEN_WIDTH // 2 - hell_text.get_width() // 2, 500))
    screen.blit(back_text, (SCREEN_WIDTH // 2 - back_text.get_width() // 2, 600))

def draw_character_selection():
    screen.fill(BLACK)
    title_text = font.render("Select Your Character", True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
    for i, name in enumerate(tank_images.keys()):
        screen.blit(tank_images[name], (100 + i * 150, 200))

# 修改 draw_game 函数，增加通关判断
def draw_game():
    global current_level, enemy_x, enemy_y, player_input, enemy_hp, player_attack, consecutive_correct, attack_frame, player_hp, word_timer, used_words, current_word, score, difficulty, time_limit, show_menu, running, show_ending  # 修改: 添加 show_ending 到全局变量声明
    screen.blit(background_images[levels[current_level]["background"]], (0, 0))  # 绘制背景

    # 固定敌人图标在背景中间正上方
    enemy_x = SCREEN_WIDTH // 2 - enemy_images[levels[current_level]["enemy"]].get_width() // 2
    enemy_y = 100

    # 初始化攻击方向
    attack_direction = None  # 新增：初始化攻击方向

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_BACKSPACE:
                player_input = player_input[:-1]
            elif event.key == pygame.K_RETURN:
                if player_input == current_word:
                    enemy_hp -= player_attack + consecutive_correct * 10
                    consecutive_correct += 1
                    score += 10 + 10 * (consecutive_correct - 1)  # 修改: 更新分数计算逻辑
                    attack_frame = 60  # 触发攻击动画，持续2秒（60帧）
                    attack_direction = "player_to_enemy"  # 设置攻击方向
                    used_words.add(current_word)  # 将当前单词添加到已使用集合
                    if len(used_words) == len(word_list):
                        used_words.clear()  # 如果所有单词都已使用，清空集合
                    current_word = random.choice([word for word in word_list if word not in used_words])  # 从剩余单词中选择
                    player_input = ""
                    word_timer = 0  # 重置单词计时器
                else:
                    player_hp -= 10 + consecutive_correct * 10
                    consecutive_correct = 0
                    score -= 10  # 修改: 更新分数计算逻辑
                    attack_frame = 60  # 触发攻击动画，持续2秒（60帧）
                    attack_direction = "enemy_to_player"  # 设置攻击方向
            else:
                player_input += event.unicode

    # 更新单词计时器
    if time_limit > 0:
        word_timer += clock.get_time()
        if word_timer >= time_limit * 1000:
            player_hp -= 10 + (2 * consecutive_correct)
            consecutive_correct = 0
            score -= 10  # 修改: 更新分数计算逻辑
            attack_frame = 60  # 触发攻击动画，持续2秒（60帧）
            attack_direction = "enemy_to_player"  # 设置攻击方向
            used_words.add(current_word)  # 将当前单词添加到已使用集合
            if len(used_words) == len(word_list):
                used_words.clear()  # 如果所有单词都已使用，清空集合
            current_word = random.choice([word for word in word_list if word not in used_words])  # 从剩余单词中选择
            player_input = ""
            word_timer = 0

    # 更新敌人生命值
    if enemy_hp <= 0:
        current_level += 1
        if current_level < len(levels):
            enemy_hp = levels[current_level]["enemy_hp"]
            player_hp += 100
            player_attack += 10
            score += 50  # 修改: 过关奖励50分
        else:
            running = False  # 游戏结束
            show_ending = True  # 显示通关画面

    # 绘制玩家
    screen.blit(tank_images[player], (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 150))

    # 绘制敌人
    screen.blit(enemy_images[levels[current_level]["enemy"]], (enemy_x, enemy_y))  # 修改: 调整敌人绘制位置

    # 显示敌人生命值
    enemy_hp_text = font.render(f"HP: {enemy_hp}", True, RED)
    enemy_hp_text_rect = enemy_hp_text.get_rect(center=(enemy_x + enemy_images[levels[current_level]["enemy"]].get_width() // 2, enemy_y + enemy_images[levels[current_level]["enemy"]].get_height() + 30))
    screen.blit(enemy_hp_text, enemy_hp_text_rect)

    # 显示当前单词
    word_text = font.render(f"Type: {current_word}", True, RED)  # 修改: 使用红色显示字母
    screen.blit(word_text, (10, 10))

    # 显示玩家输入
    input_text = font.render(f"Input: {player_input}", True, RED)  # 修改: 使用红色显示字母
    screen.blit(input_text, (10, 50))

    # 显示得分
    score_text = font.render(f"Score: {score}", True, WHITE)
    score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 10))
    screen.blit(score_text, score_text_rect)

    # 显示玩家生命值
    hp_text = font.render(f"HP: {player_hp}", True, RED)
    hp_text_rect = hp_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 200))
    screen.blit(hp_text, hp_text_rect)

    # 显示玩家角色名称
    player_name_text = font.render(f"{player}", True, RED)
    player_name_text_rect = player_name_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 250))  # 修改: 调整玩家名称显示位置
    screen.blit(player_name_text, player_name_text_rect)

    # 显示敌人角色名称
    enemy_name_text = font.render(f"{levels[current_level]['enemy']}", True, RED)
    enemy_name_text_rect = enemy_name_text.get_rect(center=(enemy_x + enemy_images[levels[current_level]["enemy"]].get_width() // 2, enemy_y + enemy_images[levels[current_level]["enemy"]].get_height() + 60))  # 修改: 调整敌人名称显示位置
    screen.blit(enemy_name_text, enemy_name_text_rect)

    # 显示时间倒计时
    if time_limit > 0:
        time_left = max(0, time_limit - word_timer // 1000)
        time_text = font.render(f"Time: {time_left}", True, RED)
        screen.blit(time_text, (SCREEN_WIDTH - 150, 10))

    # 检查玩家生命值是否归0或低于0
    if player_hp <= 0:
        running = False  # 游戏结束
        show_menu = True  # 返回主界面

# 新增 draw_ending 函数
def draw_ending():
    screen.blit(ending_background, (0, 0))
    back_to_main_text = font.render("Back to Main", True, RED)
    screen.blit(back_to_main_text, (SCREEN_WIDTH // 2 - back_to_main_text.get_width() // 2, 400))

# 修改主循环，增加对通关画面的处理
while running:
    if show_menu:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 300 <= mouse_x <= 500 and 200 <= mouse_y <= 250:
                    show_menu = False  # 进入选人界面
                elif 300 <= mouse_x <= 500 and 300 <= mouse_y <= 350:
                    show_menu = False  # 进入设置界面
                    difficulty = "settings"
                elif 300 <= mouse_x <= 500 and 400 <= mouse_y <= 450:
                    running = False  # 退出游戏
    elif difficulty == "settings":
        draw_settings()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 300 <= mouse_x <= 500 and 200 <= mouse_y <= 250:
                    difficulty = "easy"
                    time_limit = 60
                elif 300 <= mouse_x <= 500 and 300 <= mouse_y <= 350:
                    difficulty = "medium"
                    time_limit = 30
                elif 300 <= mouse_x <= 500 and 400 <= mouse_y <= 450:
                    difficulty = "hard"
                    time_limit = 10
                elif 300 <= mouse_x <= 500 and 500 <= mouse_y <= 550:
                    difficulty = "hell"
                    time_limit = 3
                elif 300 <= mouse_x <= 500 and 600 <= mouse_y <= 650:
                    difficulty = None
                    show_menu = True
    elif player is None:
        draw_character_selection()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i, name in enumerate(tank_images.keys()):
                    if 100 + i * 150 <= mouse_x <= 200 + i * 150 and 200 <= mouse_y <= 300:
                        player = name
                        if difficulty is None:
                            difficulty = "easy"  # 默认设置为easy难度
    elif show_ending:
        draw_ending()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 300 <= mouse_x <= 500 and 400 <= mouse_y <= 450:
                    show_ending = False
                    show_menu = True
    else:
        draw_game()

    # 更新屏幕
    pygame.display.flip()
    clock.tick(30)

# 停止音乐播放
pygame.mixer.music.stop()

# 退出游戏
pygame.quit()
sys.exit()