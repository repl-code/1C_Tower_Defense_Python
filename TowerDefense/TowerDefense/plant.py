from Drawable import *
import game





class plant (drawable):

    def __init__(self, ImagePath, x, y):
        super().__init__(ImagePath)
        self.x = x
        self.y = y

    def loop(self, elapsed):
        self.time_since_reload += elapsed

        for enemy in game.zombies:
            change_x = enemy.x - self.x
            change_y = enemy.y - self.y



    def shoot():
        if math.hypot(change_x, change_y) < self.range:
  	        self.direction = math.degrees(math.atan2(change_y, change_x))

