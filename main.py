import math
import random
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
print(pygame.font.get_fonts())
while run:
    clock.tick(60)
    count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()
pygame.quit()