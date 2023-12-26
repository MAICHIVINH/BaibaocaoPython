import pygame
import time
import random

pygame.init()

# Thiết lập màn hình
width = 600
height = 400
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rắn Săn Mồi')

# Load ảnh nền
background_image = pygame.image.load("D:\Python\mau-background-dep.jpg")

# Thiết lập màu sắc
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Thiết lập kích thước rắn và mồi
snake_block = 20  # Kích thước của rắn
snake_speed = 7

# Thiết lập font chữ
font = pygame.font.SysFont(None, 30)

# Âm thanh
pygame.mixer.init()
pygame.mixer.music.load("D:\Python\game-music-loop-7-145285.mp3")
game_over_sound = pygame.mixer.Sound("game-over-31-179699.wav")
eat_sound = pygame.mixer.Sound("button-124476.wav")  # Replace with your actual sound file

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(gameDisplay, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color, y_displace=0):
    mesg = font.render(msg, True, color)
    gameDisplay.blit(mesg, [width / 6, height / 3 + y_displace])

def game_intro():
    intro = True
    pygame.mixer.music.play(-1)  # Play background music on loop
    while intro:
        gameDisplay.fill(white)
        gameDisplay.blit(background_image, (0, 0))  # Draw the background image
        message("Welcome to the game Snake Prey", green, -50)
        message("Red: Food        Green: Snake", white, 10)
        message("Press C to start or Q to exit", red, 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    gameLoop()

def gameLoop():
    game_over = False
    game_close = False

    # Khởi tạo vị trí và độ dài ban đầu của rắn
    lead_x = width / 2
    lead_y = height / 2
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    length_of_snake = 1

    # Tạo vị trí ngẫu nhiên cho mồi
    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    score = 0

    clock = pygame.time.Clock()  # Khởi tạo đối tượng Clock

    while not game_over:
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
        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            game_over_sound.play()
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        gameDisplay.blit(background_image, (0, 0))  # Draw the background image
        pygame.draw.rect(gameDisplay, red, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over_sound.play()
                game_close = True

        our_snake(snake_block, snake_list)

        # Kiểm tra rắn có ăn mồi không
        if lead_x == foodx and lead_y == foody:
            eat_sound.play()
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            length_of_snake += 1
            score += 1

            # Hiển thị điểm
            pygame.display.set_caption('Rắn Săn Mồi - Điểm: {}'.format(score))

        # Điều chỉnh tốc độ của rắn
        pygame.time.Clock().tick(snake_speed)

        pygame.display.update()

        # Hiển thị thông báo khi chết
        while game_close:
            gameDisplay.fill(white)
            gameDisplay.blit(background_image, (0, 0))  # Draw the background image
            message("You lose! Press C to play again or Q to exit.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()

            clock.tick(snake_speed)  # Sử dụng đối tượng Clock để điều chỉnh tốc độ

            pygame.display.update()

    pygame.mixer.music.stop()  # Stop the background music
    pygame.quit()
    quit()

game_intro()
