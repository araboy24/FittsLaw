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
black_color = (0, 0, 0)
ENUMS = ["HOME", "TEST", "TRIAL_COMPLETE", "TEST_COMPLETE"]
ENUM = "HOME"
trial_count = 0


class Trial:
    def __init__(self, x1, x2, bar_width, id, trial_number):
        self.x1 = x1
        self.x2 = x2
        self.bar_width = bar_width
        self.id = id
        self.trial_number = trial_number
        self.y = 0
        self.height = sh
        self.is_left = True
        self.click_count = 0
        self.times = []
        self.t1 = 0
        self.t2 = 0

    def reset(self):
        self.is_left = True
        self.click_count = 0
        self.times = []
        self.t1 = 0
        self.t2 = 0
    def clicked(self, x, y):
        if self.is_left:
            if self.x1 <= x <= self.x1 + self.bar_width and 0 < y < self.height:
                if self.click_count == 0:
                    self.t2 = time.time()
                else:
                    # temp = self.t1
                    self.t1 = self.t2
                    self.t2 = time.time()
                    self.times.append(self.t2-self.t1)
                    # print(self.times)
                self.is_left = not self.is_left
                self.click_count += 1
        else:
            if self.x2 <= x <= self.x2 + self.bar_width and 0 < y < self.height:
                self.t1 = self.t2
                self.t2 = time.time()
                self.times.append(self.t2 - self.t1)
                # print(self.times)
                self.is_left = not self.is_left
                self.click_count += 1

    def get_clicks(self):
        return self.click_count

    def draw(self, win):
        if self.is_left:
            pygame.draw.rect(win, fg_color, [self.x1, self.y, self.bar_width, self.height])
        else:
            pygame.draw.rect(win, fg_color, [self.x2, self.y, self.bar_width, self.height])

def reset_trials():
    for t in trials:
        t.reset()

def redrawGameWindow():
    if ENUM == "HOME":
        pygame.draw.rect(win, bg_color, [0, 0, sw, sh])
        font = pygame.font.SysFont('segoeuiblack', 60)
        welcomeText = font.render("Welcome to the Fitt's Law Experiment", 1, fg_color)
        win.blit(welcomeText, (sw // 2 - (welcomeText.get_width() // 2), 50))
        pygame.draw.rect(win, fg_color, [372, 284, 455, 131])
        buttonText = font.render("Begin", 1, black_color)
        win.blit(buttonText, (sw // 2 - (buttonText.get_width() // 2), 307))
    elif ENUM == "TEST":
        pygame.draw.rect(win, bg_color, [0, 0, sw, sh])
        trials[trial_count].draw(win)
    elif ENUM == ENUMS[2]:
        pygame.draw.rect(win, bg_color, [0, 0, sw, sh])
        font = pygame.font.SysFont('segoeuiblack', 60)
        completeText = font.render(f"Trial {trial_count} of 15 is Complete", 1, fg_color)
        win.blit(completeText, (sw // 2 - (completeText.get_width() // 2), 50))
        sfont = pygame.font.SysFont('segoeuiblack', 40)
        pygame.draw.rect(win, fg_color, [372, 284, 455, 131])
        buttonText = sfont.render("Click to Continue", 1, black_color)
        win.blit(buttonText, (sw // 2 - (buttonText.get_width() // 2), 320))
    elif ENUM == ENUMS[3]:
        pygame.draw.rect(win, bg_color, [0, 0, sw, sh])
        font = pygame.font.SysFont('segoeuiblack', 60)
        completeText = font.render(f"Test is Complete", 1, fg_color)
        win.blit(completeText, (sw // 2 - (completeText.get_width() // 2), 50))
        sfont = pygame.font.SysFont('segoeuiblack', 40)
        pygame.draw.rect(win, fg_color, [372, 284, 455, 131])
        buttonText = sfont.render("Click to Restart", 1, black_color)
        win.blit(buttonText, (sw // 2 - (buttonText.get_width() // 2), 320))
        # pygame.draw.rect(win, bg_color, [0,0,sw,sh])
        # pygame.draw.rect(win, fg_color, [200, 0, 100, sh])
        # pygame.draw.rect(win, fg_color, [900, 0, 100, sh])
    # win.blit(bg, (0, 0))
    # player.draw(win)

    pygame.display.update()


count = 0
run = True


def create_trials():
    t1 = Trial(100, 1000, 100, 3, 1)
    t2 = Trial(300, 800, 100, 2, 2)
    t3 = Trial(270, 920, 10, 6, 3)
    t4 = Trial(345, 840, 15, 5, 4)
    t5 = Trial(150, 1000, 50, 4, 5)
    t6 = Trial(350, 800, 50, 3, 6)
    t7 = Trial(175, 1000, 25, 5, 7)
    t8 = Trial(225, 900, 75, 3, 8)
    t9 = Trial(105, 1080, 15, 6, 9)
    t10 = Trial(510, 680, 10, 4, 10)
    t11 = Trial(375, 750, 75, 2, 11)
    t12 = Trial(435, 760, 10, 6, 12)
    t13 = Trial(430, 760, 10, 5, 13)
    t14 = Trial(375, 800, 25, 4, 14)
    t15 = Trial(150, 900, 150, 2, 15)
    trials_list = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15]
    return trials_list


trials = create_trials()
is_finished = False
while run:
    clock.tick(60)
    count += 1

    # if ENUM == "HOME":
    #     if
    if not is_finished:
        if trials[trial_count].get_clicks() == 11:
            print(trial_count, trials[trial_count].times)

            if trial_count == 14:
                ENUM = ENUMS[3]
                is_finished = True
            else:
                ENUM = ENUMS[2]
                trial_count += 1


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if ENUM == "HOME":
                if 372 <= pos[0] <= 372 + 455 and 284 <= pos[1] <= 284 + 131:
                    ENUM = ENUMS[1]
            if ENUM == "TEST":
                trials[trial_count].clicked(pos[0], pos[1])
            if ENUM == ENUMS[2]:
                if 372 <= pos[0] <= 372 + 455 and 284 <= pos[1] <= 284 + 131:
                    ENUM = ENUMS[1]
            if ENUM == ENUMS[3]:
                if 372 <= pos[0] <= 372 + 455 and 284 <= pos[1] <= 284 + 131:
                    ENUM = ENUMS[0]
                    trial_count = 0
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()
pygame.quit()
