import consts


class Snake:

    dx = {"UP": 0, "DOWN": 0, "LEFT": -1, "RIGHT": 1}
    dy = {"UP": -1, "DOWN": 1, "LEFT": 0, "RIGHT": 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        x, y = self.get_head()
        next_cell = (
            self.val(x + self.dx[self.direction]),
            self.val(y + self.dy[self.direction]),
        )
        if not self.game.get_cell(next_cell).color in [
            consts.back_color,
            consts.fruit_color,
        ]:
            self.game.kill(self)
        elif self.game.get_cell(next_cell).color == consts.fruit_color:
            self.cells.append(next_cell)
            self.game.get_cell(next_cell).set_color(self.color)
        else:
            self.game.get_cell(self.cells.pop(0)).set_color(consts.back_color)
            self.cells.append(next_cell)
            self.game.get_cell(next_cell).set_color(self.color)

    def handle(self, keys):
        for key in keys:
            if key in self.keys.keys() and self.keys[key] != self.direction:
                requested_direction = self.keys[key]
                if (
                    self.dx[requested_direction] != -self.dx[self.direction]
                    and self.dy[requested_direction] != -self.dy[self.direction]
                ):
                    self.direction = requested_direction
                    break
