# 导入模块
import pygame
import random
import sys

# 初始化
pygame.init()   
screen = pygame.display.set_mode((800, 600))    # 窗口尺寸
pygame.display.set_caption("RandName for Class 49 by HQZ")  # 窗口标题
clock = pygame.time.Clock()
screen.fill((50,50,255))    # 填充背景色-深蓝色

# 设置基础资源
names = ["白绍鹏", "曹玛诗怡", "陈凡", "段善铧", "官韵涵", "韩年喻", "何峻熙", "贺雪阳", "侯俊宇", "胡瑾瑜", "胡洺涓", "黄锐洋", "黄馨怡", "贾云博", "蒋治恒", "敬一航", "李博", "李国强", "李昊珅", "李佳桐", "李睿扬", "李亚宁", "李玉菲", "廖麦荀", "刘柯辛", "刘瑞霖", "刘稹涵", "龙浩杰", "罗仕杰", "罗震宇", "彭茵茵", "任卓", "沈韦希", "谈华杰", "唐琪洲", "田家陈", "田之园", "宛彤", "王涵颍", "王沁喆", "翁梓轩", "吴思彤", "吴易达", "杨昊霖", "杨邱", "杨霆轩", "喻俊杰", "张恒瑞", "张宇鲲", "赵力松", "赵启峰", "赵子惟", "郑睿", "郑晓桐", "周鑫杰", "周宇凡", "左耘萌", "宋依竹"]
random.shuffle(names)   # 打乱名单
font1 = pygame.font.Font("C:/Windows/Fonts/方正粗黑宋简体.ttf", 80)    # 按键的字体
font2 = pygame.font.Font("C:/Windows/Fonts/方正粗黑宋简体.ttf", 120)    # 名字的字体
colors = [(random.randint(40, 250), random.randint(40, 250), random.randint(40, 180)) for x in range(6)]
start = False    # 是否开始播放名字
num = 0    # 记录播放到那个名字
color_names = (255, 255, 255)    # 用来显示名字的颜色
x = 770 / 2 + 15    # 名字的x坐标
y = 200 / 2 + 225    # 名字的y坐标
name = ""    # 屏幕上正在显示的名字
running = True    # 循环(程序)是否进行
FPS = 60    # 每秒渲染的帧数

while running:
    # 事件判断与反馈
    for event in pygame.event.get():
        # 判断是否人为关闭窗口退出
        if event.type == pygame.QUIT:
            running = False
        # 监听按键并反馈
        elif event.type == pygame.KEYDOWN:
            # 如果按W键，更改背景颜色
            if event.key == pygame.K_w:
                screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            # 如果按E键或者Esc键，退出(exit)
            if event.key == pygame.K_e:
                screen.fill((50,50,255))
                running = False
            if event.key == pygame.K_ESCAPE:
                screen.fill((50,50,255))
                running = False
            # 如果按空格键或者S键，切换播放状态
            if event.key == pygame.K_SPACE:
                start = not start
            if event.key == pygame.K_s:
                start = not start
            # 按下3键，切换到三十帧
            if event.key == pygame.K_3:
                FPS = 30
            # 按下6键，切换到六十帧
            if event.key == pygame.K_6:
                FPS = 60
        # 监听鼠标点击并反馈
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if 435<mouse_y<585:    # 下面一排
                if 15<mouse_x<395:    # “开始”键
                    start = True
                if 405<mouse_x<785:    # “停止”键
                    start = False
            if 35<mouse_y<195:    # 上面一排
                if 35<mouse_x<272:    # “30”键
                    FPS = 30
                if 282<mouse_x<517:    # “退出”键
                    screen.fill((50,50,255))
                    running = False
                if 527<mouse_x<764:    # “60”键
                    FPS = 60
    # 绘制背景矩形（一层）
    pygame.draw.rect(screen, colors[0], (15,15,770,200))
    pygame.draw.rect(screen, colors[1], (15,225,770,200))
    pygame.draw.rect(screen, colors[2], (15,435,380,150))
    pygame.draw.rect(screen, colors[3], (405,435,380,150))
    # 绘制背景矩形（二层）
    pygame.draw.rect(screen, colors[4], (35,35,237,160))
    pygame.draw.rect(screen, colors[5], (282,35,235,160))
    pygame.draw.rect(screen, colors[4], (527,35,237,160))
    # 渲染初始文本
    text_start = font1.render("开始", True, (240,240,240))
    text_start_rect = text_start.get_rect()
    text_start_rect.center = (380/2+15, 150/2+435)
    screen.blit(text_start, text_start_rect)
    text_stop = font1.render("停止", True, (240,240,240))
    text_stop_rect = text_stop.get_rect()
    text_stop_rect.center = (380/2+405, 150/2+435)
    screen.blit(text_stop, text_stop_rect)
    text_30 = font1.render("30", True, (240,240,240))
    text_30_rect = text_30.get_rect()
    text_30_rect.center = (237/2+35, 160/2+35)
    screen.blit(text_30, text_30_rect)
    text_60 = font1.render("60", True, (240,240,240))
    text_60_rect = text_60.get_rect()
    text_60_rect.center = (237/2+527, 160/2+35)
    screen.blit(text_60, text_60_rect)
    text_exit = font1.render("退出", True, (240,240,240))
    text_exit_rect = text_exit.get_rect()
    text_exit_rect.center = (235/2+282, 160/2+35)
    screen.blit(text_exit, text_exit_rect)
    # 更改num值
    num += 1
    if num >= len(names):
        num = 0
        random.shuffle(names)
    if start == True:
        # 定义变幻中的text_names位置(x, y)
        x = 770 / 2 + 15 + random.randint(-150, 150)
        y = 200 / 2 + 225 + random.randint(-20, 20)
        # 显示变幻中的名字
        color_names = ((255 + colors[1][0]) / 2, (255 + colors[1][1]) / 2, (255 + colors[1][2]) / 2)
        text_names = font2.render(names[num], True, color_names)
        name = names[num]
        text_names_rect = text_names.get_rect()
        text_names_rect.center = (x, y)
        screen.blit(text_names, text_names_rect)
    else:
        text_names = font2.render(name, True, (255, 255, 255))
        text_names_rect = text_names.get_rect()
        text_names_rect.center = (x, y)
        screen.blit(text_names, text_names_rect)
    # 更新显示
    pygame.display.flip()
    # 控制帧率
    clock.tick(FPS)

# 退出pygame
pygame.quit()
sys.exit()
