import spawn
from  finances import *
from zombie import *

screen = None

zombies = []

map = [(30,30),(400,30),(400, 250), (30, 250),(30, 440), (510, 440)]

def spawnZomb():
    zomb = zombie(screen, 3)
    zombies.append(zomb)
    print("spawn")

spawn.addAction(spawnZomb, 100)

def loop(screen, frame_duration):
    spawn.check(frame_duration)

    for zombie in zombies:
        zombie.loop(frame_duration)
        zombie.draw()

    i = 0
    while i < len(zombies):
        if zombies[i].delete:
            del zombies[i]
            finance.money += 20
            i -= 1
        i += 1

