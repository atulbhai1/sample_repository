from random import choice
from matplotlib import pyplot
class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice(list(range(0, 6)))
            x_step = x_distance * x_direction
            y_direction = choice([1, -1])
            y_distance = choice(list(range(0, 6)))
            y_step = y_distance * y_direction
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)
keep_running = 'yes'
while keep_running == 'yes':
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    pyplot.scatter(rw.x_values, rw.y_values, c=point_numbers,edgecolor='none', s=15)
    pyplot.show()
    keep_running = input('Want To Continue:')
