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
dark_fg_color = (45, 44, 81)
black_color = (0, 0, 0)
ENUMS = ["HOME", "TEST", "TRIAL_COMPLETE", "TEST_COMPLETE"]
ENUM = "HOME"
trial_count = 0


class Trial:
    def __init__(self, distance, bar_width, id, trial_number):
        self.distance = distance
        self.bar_width = bar_width
        self.x1 = sw//2 - (self.distance + 2 * self.bar_width)//2
        self.x2 = self.x1 + self.bar_width + self.distance
        self.id = id
        self.trial_number = trial_number
        self.y = sh//2-self.bar_width//2
        self.height = self.bar_width
        self.is_left = True
        self.click_count = 0
        self.times = []
        self.t1 = 0
        self.t2 = 0

    def get_distance(self):
        return self.distance

    def get_average_time(self):
        return sum(self.times)/len(self.times)

    def reset(self):
        self.is_left = True
        self.click_count = 0
        self.times = []
        self.t1 = 0
        self.t2 = 0
    def clicked(self, x, y):
        if self.is_left:
            if self.x1 <= x <= self.x1 + self.bar_width and self.y <= y < self.y+self.height:
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
            if self.x2 <= x <= self.x2 + self.bar_width and self.y <= y < self.y+self.height:
                self.t1 = self.t2
                self.t2 = time.time()
                self.times.append(self.t2 - self.t1)
                # print(self.times)
                self.is_left = not self.is_left
                self.click_count += 1

    def get_clicks(self):
        return self.click_count

    def draw(self, win):
        if self.click_count == 0:
            font = pygame.font.SysFont('segoeuiblack', 60)
            welcomeText = font.render("Click the Left Square to Begin", 1, fg_color)
            win.blit(welcomeText, (sw // 2 - (welcomeText.get_width() // 2), 50))
        if self.is_left:
            pygame.draw.rect(win, fg_color, [self.x1, self.y, self.bar_width, self.height])
            pygame.draw.rect(win, dark_fg_color, [self.x2, self.y, self.bar_width, self.height])
        else:
            pygame.draw.rect(win, fg_color, [self.x2, self.y, self.bar_width, self.height])
            pygame.draw.rect(win, dark_fg_color, [self.x1, self.y, self.bar_width, self.height])


def create_trials():
    t1 = Trial(300, 100, 2, 1)
    t2 = Trial(600, 200, 2, 2)
    t3 = Trial(450, 150, 2, 3)

    t4 = Trial(700, 100, 3, 4)
    t5 = Trial(525, 75, 3, 5)
    t6 = Trial(350, 50, 3, 6)

    t7 = Trial(750, 50, 4, 7)
    t8 = Trial(375, 25, 4, 8)
    t9 = Trial(225, 15, 4, 9)

    t10 = Trial(775, 25, 5, 10)
    t11 = Trial(465, 15, 5, 11)
    t12 = Trial(310, 10, 5, 12)

    t13 = Trial(945, 15, 6, 13)
    t14 = Trial(630, 10, 6, 14)
    t15 = Trial(315, 5, 6, 15)
    trials_list = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15]
    return trials_list

trials = create_trials()

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




def write_output():
    with open("results.csv", "w") as f:
        f.write("Trial Number, Square Width, Distance, ID, Average Time, Time 1, Time 2, Time 3, Time 4, Time 5,")
        f.write("Time 6, Time 7, Time 8, Time 9, Time 10\n")
        for t in trials:
            f.write(f"{t.trial_number}, {t.bar_width}, {t.get_distance()}, {t.id}, {t.get_average_time()}")
            print(f"{t.trial_number}, {t.bar_width}, {t.get_distance()}, {t.id}, {t.get_average_time()}", end='')
            for time in t.times:
                f.write(f", {time}")
                print(f", {time}", end='')
            f.write("\n")
            print('')



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
                write_output()
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
