import pygame

# 初始化 Pygame
pygame.init()

# 设置窗口大小
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("字体测试")

# 尝试加载字体
try:
    # 根据你的系统修改字体文件路径
    font_path = '/Library/Fonts/Microsoft/Microsoft YaHei.ttf'
    font = pygame.font.Font(font_path, 30)
except FileNotFoundError:
    print("未找到指定字体文件，将使用系统默认字体。")
    font = pygame.font.SysFont(None, 30)

# 渲染文本
text = font.render("得分: 100", True, (255, 255, 255))

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景色
    screen.fill((0, 0, 0))

    # 绘制文本
    screen.blit(text, (10, 10))

    # 更新显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()