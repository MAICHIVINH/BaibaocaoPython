import pygame
import time
import random

pygame.init()

# Thiết lập màn hình
width = 600
height = 400
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rắn Săn Mồi')

# Thiết lập màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Thiết lập kích thước rắn và mồi
snake_block = 10
snake_speed = 9

# Thiết lập font chữ
font = pygame.font.SysFont(None, 25)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(gameDisplay, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    gameDisplay.blit(mesg, [width / 6, height / 3])

def gameLoop():    
    game_over = False
    game_close = False

    while not game_over:
        # Khởi tạo vị trí và độ dài ban đầu của rắn
        lead_x = width / 2
        lead_y = height / 2
        lead_x_change = 0
        lead_y_change = 0

        snake_list = []
        length_of_snake = 1

        # Tạo vị trí ngẫu nhiên cho mồi
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

        # Điểm
        score = 0

        while not game_close:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        lead_x_change = -snake_block
                        lead_y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        lead_x_change = snake_block
                        lead_y_change = 0
                    elif event.key == pygame.K_UP:
                        lead_y_change = -snake_block
                        lead_x_change = 0
                    elif event.key == pygame.K_DOWN:
                        lead_y_change = snake_block
                        lead_x_change = 0

            # Kiểm tra va chạm với tường
            if lead_x >= width:
                lead_x = 0
            elif lead_x < 0:
                lead_x = width - snake_block
            elif lead_y >= height:
                lead_y = 0
            elif lead_y < 0:
                lead_y = height - snake_block

            lead_x += lead_x_change
            lead_y += lead_y_change
            gameDisplay.fill(white)
            pygame.draw.rect(gameDisplay, red, [foodx, foody, snake_block, snake_block])

            snake_head = []
            snake_head.append(lead_x)
            snake_head.append(lead_y)
            snake_list.append(snake_head)

            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            our_snake(snake_block, snake_list)

            # Kiểm tra rắn có ăn mồi không
            if lead_x == foodx and lead_y == foody:
                foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                length_of_snake += 1
                score += 1

            # Hiển thị điểm
            pygame.display.set_caption('Rắn Săn Mồi - Điểm: {}'.format(score))

            # Điều chỉnh tốc độ của rắn
            pygame.time.Clock().tick(snake_speed)

            pygame.display.update()

            # Hiển thị thông báo khi chết
        gameDisplay.fill(white)
        message("Ban thua! Nhan C de choi lai hoac Q de thoat.", red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                elif event.key == pygame.K_c:
                    gameLoop()

    pygame.quit()
    quit()

gameLoop()
