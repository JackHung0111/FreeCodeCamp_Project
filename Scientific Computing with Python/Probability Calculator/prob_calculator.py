# https://replit.com/@JackHung0111/boilerplate-probability-calculator

import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for k in kwargs:
            for i in range(kwargs[k]):
                self.contents.append(k)
    def draw(self, num):
        result = []
        if num >= len(self.contents):
            return self.contents
        else:
            for i in range(num):
                result.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
            return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    hat1 = copy.deepcopy(hat)
    for i in range(num_experiments):
        hat = copy.deepcopy(hat1)
        result = hat.draw(num_balls_drawn)
        success = True
        for k in expected_balls:
            if result.count(k) < expected_balls[k]:
                success = False
        m += 1 if success else 0
    return m/num_experiments