import random
import pygame  # pip install pygame

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Color Game")

ansv_font = pygame.font.Font(None, 40)
font = pygame.font.Font(None, 70)
describing_font = pygame.font.Font(None, 24)

text_colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]

correct_answers = 0
wrong_answers = 0

def winner():
    screen.fill("green")
    screen.blit(font.render("ПОБЕДА!!!", True, "white"), (130, 150))
    pygame.display.update()

def loser():
    screen.fill("red")
    screen.blit(font.render("ПОРАЖЕНИЕ!!!", True, "white"), (80, 150))
    pygame.display.update()

def colorupdate():
    global text
    text = random.choice(["КРАСНЫЙ", "ЗЕЛЕНЫЙ", "СИНИЙ", "ЖЕЛТЫЙ", "ГОЛУБОЙ", "ПУРПУРНЫЙ"])
    global text_color
    text_color = random.choice(text_colors)

    text_surface = font.render(text, True, text_color)

    screen.fill((0, 0, 0))
    screen.blit(text_surface, (100, 130))

    screen.blit(ansv_font.render("Верно: "+str(correct_answers), True, "green"), (0, 0))
    screen.blit(ansv_font.render("Неверно: "+str(wrong_answers), True, "red"), (0, 30))
    screen.blit(describing_font.render("Нажимайте клавишу ВВЕРХ, если цвета совпадают.", True, "white"), (0, 330))
    screen.blit(describing_font.render("Клавишу ВНИЗ, если цвета НЕ совпадают.", True, "white"), (0, 350))
    screen.blit(describing_font.render("15 верных ответов - победа, 3 неверных - поражение.", True, "white"), (0, 370))

    pygame.display.update()

colorupdate()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if (text == "КРАСНЫЙ" and text_color == "red") or \
               (text == "ЗЕЛЕНЫЙ" and text_color == "green") or \
               (text == "СИНИЙ" and text_color == "blue") or \
               (text == "ЖЕЛТЫЙ" and text_color == "yellow") or \
               (text == "ГОЛУБОЙ" and text_color == "cyan") or \
               (text == "ПУРПУРНЫЙ" and text_color == "magenta"):
                if event.key == pygame.K_UP:
                    correct_answers += 1
                elif event.key == pygame.K_DOWN:
                    wrong_answers += 1
            else:
                if event.key == pygame.K_DOWN:
                    correct_answers += 1
                elif event.key == pygame.K_UP:
                    wrong_answers += 1
            colorupdate()

    if correct_answers >= 15:
        winner()
        pygame.time.wait(3*1000)
        break
    elif wrong_answers >= 3:
        loser()
        pygame.time.wait(3*1000)
        break

pygame.quit()
