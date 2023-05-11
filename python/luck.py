from random import randint

def coin():
    return randint(0, 999) % 2 == 0

class Dice:
    def __init__(self, **kwargs):
        self.sides = [n for n in range(1, kwargs["sides"] + 1)] if kwargs.get("sides") else [1 , 2 , 3 , 4 , 5 , 6]

    def roll(self):
        return self.sides[randint(0, len(self.sides) - 1)]

    def customize_sides(self, arr):
        self.sides = arr


class BallMachine:
    def __init__(self, balls):
        self.balls = [num for num in range(balls)]
        self.available = {ball: True for ball in self.balls}
        self.used = {"all": []}

    def show_balls(self):
        print(self.balls)

    def is_available(self, ball):
        return True if self.available.get(ball) else False

    def has_been_used(self, ball):
        return True if self.used.get(ball) else False

    def show_all_used(self):
        print(self.used["all"])

    def shuffle(self):
        bucket = []
        while self.balls:
            i = randint(0, len(self.balls) - 1)
            bucket.append(self.balls.pop(i))
        self.balls = bucket

    def get_ball(self):
        if self.balls:
            self.shuffle()
            i = randint(0, len(self.balls) - 1)
            ball = self.balls.pop(i)
            self.used["all"].append(ball)
            self.used[ball] = len(self.used["all"]) - 1
            del self.available[ball]
            print(ball)
            return ball
        print("The Machine is empty. Reset or add balls")

    def draw(self, num):
        if num <= len(self.balls):
            return [self.get_ball() for i in range(num)]
        print(f"There are fewer than {num} balls available.")

    def insert_ball(self, ball):
        self.available[ball] = True
        self.balls.append(ball)
        self.shuffle()

    def return_ball(self, ball):
        if not self.used.get(ball):
            if not self.available[ball]:
                print(f"{ball} not in game.")
            print(f"{ball} hasn't been used")
            return
        i = self.used[ball]
        for key in self.used:
            if key != "all" and self.used[key] > i:
                self.used[key] -= 1
        self.used["all"].pop(self.used[ball])
        del self.used[ball]
        self.available[ball] = True
        self.balls.append(ball)
        self.shuffle()

    def return_last(self):
        if not self.used["all"]:
            print("No balls have been used yet")
            return
        ball = self.used["all"].pop(-1)
        del self.used[ball]
        self.available[ball] = True
        self.balls.append(ball)
        self.shuffle()





