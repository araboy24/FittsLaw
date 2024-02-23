import math
import random
import time

import pygame
pygame.init()

sw = 1200
sh = 700

clock = pygame.time.Clock()
# gameOver = False
win = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Fitt's Law Test")
# bg = pygame.image.load("bg2.png")
bg_color = (1, 0, 29)
fg_color = (108, 176, 255)
black_color = (0,0,0)
ENUMS = ["HOME", "TEST", "TRIAL_COMPLETE", "TEST_COMPLETE"]
ENUM = "HOME"

def redrawGameWindow():
    if ENUM == "HOME":
        font = pygame.font.SysFont('segoeuiblack', 60)
        welcomeText = font.render("Welcome to the Fitt's Law Experiment", 1, fg_color)
        win.blit(welcomeText, (sw//2 - (welcomeText.get_width()//2), 50))
        pygame.draw.rect(win, fg_color, [372, 284, 455, 131])
        buttonText = font.render("Begin", 1, black_color)
        win.blit(buttonText, (sw // 2 - (buttonText.get_width() // 2), 307))
    else:
        # for i, f in enumerate(pygame.sysfont.get_fonts()):
        #     fon = pygame.font.SysFont(f, 25)
        #     welcomeText = fon.render(str(f), 1, fg_color)
        #     win.blit(welcomeText, (int(random.randint(0,1200)), i*12))
        pygame.draw.rect(win, bg_color, [0,0,sw,sh])
        pygame.draw.rect(win, fg_color, [200, 0, 100, sh])
        pygame.draw.rect(win, fg_color, [900, 0, 100, sh])
    # win.blit(bg, (0, 0))
    # player.draw(win)
    # for b in playerBullets:
    #     b.draw(win)
    # for a in alienBullets:
    #     a.draw(win)
    # for a in asteroids:
    #     a.draw(win)
    # for i in range(lives):
    #     win.blit(life, (10 + i * 60, 10))
    # for a in aliens:
    #     a.draw(win)
    # for s in stars:
    #     s.draw(win)
    #
    # #Rapid Fire time Gauge
    # if rapidFire:
    #     pygame.draw.rect(win, (0, 0, 0), [349, 19, 102, 22])
    #     pygame.draw.rect(win, (255, 255, 255), [350, 20, 100 - 100 * (count - rfStart)/500, 20])
    #
    # font = pygame.font.SysFont('arial', 30)
    # scoreText = font.render('Score : ' + str(score), 1, (255, 255, 255))
    # win.blit(scoreText, (sw - (scoreText.get_width()) - 20, 10))
    # hiScoreText = font.render('High Score : ' + str(highScore), 1, (255, 255, 255))
    # if highScore != 0:
    #     win.blit(hiScoreText, (sw - (hiScoreText.get_width()) - 20, 40))
    # if gameOver:
    #     goText = font.render('Game Over :( ', 1, (255, 255, 255))
    #     paText = font.render('Press Space to Play Again ', 1, (255, 255, 255))
    #     win.blit(goText, (sw//2 - (goText.get_width())//2, sh//2 - goText.get_height()//2 -30))
    #     win.blit(paText, (sw // 2 - (paText.get_width()) // 2, sh // 2 - paText.get_height() // 2 + 30))

    # pong.draw(win)
    pygame.display.update()

count = 0
run = True
trial_count = 0
print(pygame.sysfont.get_fonts())


while run:
    clock.tick(60)
    count += 1

    # if ENUM == "HOME":
    #     if

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if ENUM == "HOME":
                if 372 <= pos[0] <= 372 + 455 and 284 <= pos[1] <= 284 + 131:
                    ENUM = ENUM[1]
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()
pygame.quit()