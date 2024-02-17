# boss enemy class

# After a certain amount of time/kills, a boss enemy appears
# The boss will have more health than regular enemies and will have special abilities

class BossEnemy:
    def __init__(self, start_x, start_y, radius = 50, max_health = 200):
        self.pos = [start_x, start_y]
        self.speed = 2
        self.radius = radius
        self.max_health = max_health
        self.current_health = max_health