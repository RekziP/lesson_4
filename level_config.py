from level import *
from gamesingle import game
from constants import *

level_1 = Level()
level_1.set_back('cave.png')
level_1.set_hero(200, 350)
level_1.min_x = 0 
level_1.max_x = win_width * 15

level_1.add_enemy(0, 650, 300, 600, 750, 3)
level_1.add_enemy(0, 880, 130, 280, 1000, 0)
level_1.add_enemy(0, 1820, 0, 1600, 1950, 1)

level_1.add_enemy(1, 1250, 400, 1120, 1400, 4)
level_1.add_enemy(1, 1700, 100, 1600, 1950, 6)

level_1.add_enemy(1, 3000, 100, 2950, 3300, 8)

level_1.add_enemy(0, 2650, 0, 1600, 2950, 0)
# level_1.add_platform(20, 550, 300, 100, 15, 0, 0)
# level_1.add_platform(100, 50, 300, 250, 5, 0, -5)

# level_1.add_platform(100, 50, 300, 150, 5, 0, -3)
level_1.add_platform(100, 450, 300, 250, 5, 0, 0)

# level_1.add_platform(150, 50, 200, 500, 5, 1.8, 0)
# level_1.add_platform(150, 250, 300, 500, 5, 5, 0)
level_1.add_platform(300, 170, 300, 250, 5, 0, -3)
level_1.add_platform(300, 565, 300, 250, 7, 0, 0)

level_1.add_platform(550, 550, 300, 100, 15, 0, 0)
level_1.add_platform(700, 100, 300, 250, 5, 2, 0)
level_1.add_platform(900, 250, 300, 250, 5, 0, -3)
level_1.add_platform(1100, 550, 300, 100, 15, 0, 0)

level_1.add_platform(1650, 400, 300, 100, 15, 0, 0)
level_1.add_platform(2200, 550, 300, 100, 15, 0, 0)

level_1.add_platform(2620, 180, 300, 340, 5, 0, 4)
level_1.add_platform(2900, 350, 300, 100, 15, 0, 0)

level_1.set_goal(3600, 180)

game.levels.append(level_1)

#  ______________________________________________________________________________________
#  
#                                 ДАЛЬШЕ УРОВЕНЬ 2
#  ______________________________________________________________________________________


level_2 = Level()

level_2.set_back('I.jpeg')

level_2.set_hero(300, 350)
level_2.min_x = 0 
level_2.max_x = win_width * 15

level_2.add_platform(0, 550, 300, 100, 18, 0, 0)

level_2.add_enemy(0, 570, 445, 500, 1100, 0)
level_2.add_platform(550, 550, 300, 150, 4, 5, 0)

level_2.add_platform(540, 400, 300, 100, 5, 0, 0)

level_2.add_enemy(1, 820, 135, 800, 1000, 5)
level_2.add_platform(800, 250, 300, 170, 5, 0, 2)

level_2.add_enemy(0, 1250, 135, 1150, 1400, 5)
level_2.add_platform(1150, 250, 300, 170, 10, 0, 0)

level_2.add_platform(1520, 410, 300, 170, 3, 8, 0)
level_2.add_platform(1950, 200, 300, 170, 2, 0, 8)

level_2.add_enemy(1, 2200, 65, 2200, 2400, 0)
level_2.add_platform(2200, 180, 300, 170, 2, 0, 0)

level_2.add_enemy(0, 2500, 185, 2500, 2700, 10)
level_2.add_enemy(0, 2900, 185, 2720, 3000, 10)
level_2.add_platform(2500, 300, 300, 170, 18, 0, 0)

level_2.set_goal(3200, 80)

game.levels.append(level_2)
