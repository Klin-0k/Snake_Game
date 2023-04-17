from pyglet import text
from pyglet.window import key
from pyglet.sprite import Sprite
from pyglet import image
from pyglet import clock
import random
import datetime
import Global_definitions


class Game:
    def __init__(self, parent):
        self._parent = parent
        self.score_label = text.Label("Score: {}".format(self.score), font_size=16, x=10, y=parent.height - 20)
        clock.schedule_interval(self.update, 1 / 10)
        parent.push_handlers(self, self.on_key_press, self.on_draw)
        self.reset()

    def rand_place_on_grid(self):
        return (random.randint(0, (self._field_size - 1)),
                random.randint(0, (self._field_size - 1)))

    def draw_image(self, image_to_draw, target_size, target_pos, angle=0):
        spr = Sprite(image_to_draw)
        spr.scale_x = target_size[0] / image_to_draw.width
        spr.scale_y = target_size[1] / image_to_draw.height
        spr.rotation = angle
        if len(target_pos) == 3:
            spr.position = (target_pos[0], target_pos[1], target_pos[2])
        else:
            spr.position = (target_pos[0], target_pos[1], 0)
        if angle == 90:
            spr.position = (spr.position[0], spr.position[1] + spr.height, spr.position[2])
        if angle == -90:
            spr.position = (spr.position[0] + spr.width, spr.position[1], spr.position[2])
        elif angle == 180:
            spr.position = (spr.position[0] + spr.width, spr.position[1] + spr.height, spr.position[2])
        spr.position = (spr.position[0] * self.grid_size[0], spr.position[1] * self.grid_size[1], spr.position[2])
        spr.draw()
        del spr

    def update(self, dt):
        if self.enable:
            new_head = (self.snake[-1][0] + self.direction[0], self.snake[-1][1] + self.direction[1])
            if new_head[0] < 0:
                new_head = (new_head[0] + self._field_size, new_head[1])
            if new_head[0] >= self._field_size:
                new_head = (new_head[0] - self._field_size, new_head[1])
            if new_head[1] < 0:
                new_head = (new_head[0], new_head[1] + self._field_size)
            if new_head[1] >=self._field_size:
                new_head = (new_head[0], new_head[1] - self._field_size)
            if new_head in self.snake[1:]:
                self.enable = False
                Global_definitions.stage = 'open_game_over_menu'
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_result = f"{time}\t{self.player_name}\t{self._field_size}\t{self.score}\n"
                with open("Resources/Records.txt", "a") as f:
                    f.write(new_result)
            self.snake.append(new_head)
            if self.apple is not None and new_head == self.apple:
                self.apple = None
                self.score += 1
                self.score_label.text = "Score: {}".format(self.score)
            else:
                self.snake.pop(0)
            if self.apple is None:
                self.apple = self.rand_place_on_grid()
                while self.apple in self.snake:
                    self.apple = self.rand_place_on_grid()
            self.csd = True

    def on_key_press(self, symbol, modifiers):
        if self.enable:
            if (symbol == key.LEFT or symbol == key.A) and (
                    self.direction != (1, 0) or len(self.snake) < 3) and self.csd:
                self.direction = (-1, 0)
            elif (symbol == key.RIGHT or symbol == key.D) and (
                    self.direction != (-1, 0) or len(self.snake) < 3) and self.csd:
                self.direction = (1, 0)
            elif (symbol == key.UP or symbol == key.W) and (
                    self.direction != (0, -1) or len(self.snake) < 3) and self.csd:
                self.direction = (0, 1)
            elif (symbol == key.DOWN or symbol == key.S) and (
                    self.direction != (0, 1) or len(self.snake) < 3) and self.csd:
                self.direction = (0, -1)
            self.csd = False
        if symbol == key.ESCAPE:
            if self.enable:
                self.enable = False
                Global_definitions.stage = 'open_in_game_menu'
            elif self.visible:
                Global_definitions.stage = 'close_in_game_menu'
            return True

    def on_draw(self):
        if self.visible:
            self._parent.clear()
            self.draw_image(self._Fon, self._parent.get_size(), (0, 0))
            if self._snake_style == 'classic':
                self.draw_image(self.head_image, self.grid_size, self.snake[-1])
                for i in reversed(self.snake[:-1]):
                    self.draw_image(self.body_image, self.grid_size, i)
            elif self._snake_style == 'rainbow':
                c = -1
                for i in reversed(self.snake):
                    c += 1
                    if c % 7 == 0:
                        self.draw_image(self.red_image, self.grid_size, i)
                    if c % 7 == 1:
                        self.draw_image(self.orange_image, self.grid_size, i)
                    if c % 7 == 2:
                        self.draw_image(self.yellow_image, self.grid_size, i)
                    if c % 7 == 3:
                        self.draw_image(self.green_image, self.grid_size, i)
                    if c % 7 == 4:
                        self.draw_image(self.blue_image, self.grid_size, i)
                    if c % 7 == 5:
                        self.draw_image(self.dark_blue_image, self.grid_size, i)
                    if c % 7 == 6:
                        self.draw_image(self.purple_image, self.grid_size, i)
            elif self._snake_style == 'rainbow2.0':
                c = -1
                for i in reversed(self.snake[:len(self.snake) // 2]):
                    if len(self.snake) // 2 > 1:
                        c += 1
                        current_image = image.SolidColorImagePattern(((255 * c) // (len(self.snake) // 2 - 1),
                                                                      255 - (255 * c) // (len(self.snake) // 2 - 1), 0,
                                                                      255)).create_image(1, 1)
                        self.draw_image(current_image, self.grid_size, i)
                        del current_image
                    else:
                        self.draw_image(self.red_image, self.grid_size, i)
                c = -1
                for i in reversed(self.snake[len(self.snake) // 2:]):
                    if len(self.snake) - len(self.snake) // 2 > 1:
                        c += 1
                        current_image = image.SolidColorImagePattern((0,
                        (255 * c) // (len(self.snake) - len(self.snake) // 2 - 1),
                        255 - (255 * c) // (len(self.snake) - len(self.snake) // 2 - 1), 255)).create_image(1, 1)
                        self.draw_image(current_image, self.grid_size, i)
                        del current_image
                    else:
                        self.draw_image(self.blue_image, self.grid_size, i)
            elif self._snake_style[:9] == 'textured_':
                angle = 0
                if self.direction == (self.grid_size[0], 0):
                    angle = 90
                elif self.direction == (0, -self.grid_size[1]):
                    angle = 180
                elif self.direction == (-self.grid_size[0], 0):
                    angle = -90
                self.draw_image(self.head_image, self.grid_size, self.snake[-1], angle)
                loc_dir = self.direction
                loc_pos = self.snake[-1]
                for i in reversed(self.snake[:-1]):
                    new_loc_dir = (loc_pos[0] - i[0], loc_pos[1] - i[1])
                    if new_loc_dir == loc_dir:
                        angle = 0
                        if loc_dir == (self.grid_size[0], 0):
                            angle = 90
                        elif loc_dir == (0, -self.grid_size[1]):
                            angle = 180
                        elif loc_dir == (-self.grid_size[0], 0):
                            angle = -90
                        self.draw_image(self.body_image, self.grid_size, i, angle)
                        # loc_dir = new_loc_dir
                        loc_pos = i
                    elif i == self.snake[-2]:
                        self.draw_image(self.red_image, self.grid_size, i)
                    else:
                        self.draw_image(self.red_image, self.grid_size, i)
            if self.apple is not None:
                self.draw_image(self.apple_image, self.grid_size, self.apple)
            if self.syringe is not None:
                self.draw_image(self.syringe_image, self.grid_size, self.syringe)
            if self.tablet is not None:
                self.draw_image(self.tablet_image, self.grid_size, self.tablet)
            if self.knife is not None:
                self.draw_image(self.knife_image, self.grid_size, self.knife)
            self.score_label.draw()

    def on_resize(self, width, height):
        ...
        # global grid_size
        # global direction
        # global snake
        # global food
        # grid_size = (window.get_size()[0] / 10, window.get_size()[1] / 10)
        # direction = (direction[0] // grid_size[0] * grid_size[0], direction[1] // grid_size[1] * grid_size[1])
        # if food is not None:
        #     food = (food[0] // grid_size[0] * grid_size[0], food[1] // grid_size[1] * grid_size[1])
        # for i in range(0, len(snake), 1):
        #     snake[i] = (snake[i][0] // grid_size[0] * grid_size[0], snake[i][1] // grid_size[1] * grid_size[1])

    @property
    def visible(self):
        return self._Visible

    @visible.setter
    def visible(self, val: bool):
        self._Visible = val
        # self._parent.clear()
        if self._Enable and not self._Visible:
            self.enable = False

    @property
    def enable(self):
        return self._Enable

    @enable.setter
    def enable(self, val: bool):
        self._Enable = val
        if self._Enable and not self._Visible:
            self.visible = True

    @property
    def game_mode(self):
        return self._game_mode

    @game_mode.setter
    def game_mode(self, val):
        if val == 'classic' or val == 'upgrade_classic' or val == 'casual' or (len(val) >= 6 and val[:6] == 'level_'):
            self._game_mode = val

    @property
    def snake_style(self):
        return self._snake_style

    @snake_style.setter
    def snake_style(self, val):
        if val == 'red':
            self.head_image = self.red_image
            self.body_image = self.red_image
            self._snake_style = 'classic'
        elif val == 'orange':
            self.head_image = self.orange_image
            self.body_image = self.orange_image
            self._snake_style = 'classic'
        elif val == 'yellow':
            self.head_image = self.yellow_image
            self.body_image = self.yellow_image
            self._snake_style = 'classic'
        elif val == 'green':
            self.head_image = self.green_image
            self.body_image = self.green_image
            self._snake_style = 'classic'
        elif val == 'blue':
            self.head_image = self.blue_image
            self.body_image = self.blue_image
            self._snake_style = 'classic'
        elif val == 'dark_blue':
            self.head_image = self.dark_blue_image
            self.body_image = self.dark_blue_image
            self._snake_style = 'classic'
        elif val == 'purple':
            self.head_image = self.purple_image
            self.body_image = self.purple_image
            self._snake_style = 'classic'
        elif val[:9] == 'textured_':
            self.head_image = image.load('Resources/head_' + val[9:] + '.png')
            self.body_image = image.load('Resources/body_' + val[9:] + '.png')
            self.body_angle_image = image.load('Resources/body_angle_' + val[9:] + '.png')
            self._snake_style = val
        else:
            self._snake_style = val

    @property
    def fon_style(self):
        return self._fon_style

    @fon_style.setter
    def fon_style(self, val):
        if val == 'black':
            self._Fon = self.black_image
        elif val == 'white':
            self._Fon = self.white_image
        elif val == 'red':
            self._Fon = self.red_image
        elif val == 'orange':
            self._Fon = self.orange_image
        elif val == 'yellow':
            self._Fon = self.yellow_image
        elif val == 'green':
            self._Fon = self.green_image
        elif val == 'blue':
            self._Fon = self.blue_image
        elif val == 'dark_blue':
            self._Fon = self.dark_blue_image
        elif val == 'purple':
            self._Fon = self.purple_image
        elif val == 'textured':
            self._Fon = image.load('Resources/game_fon.png')
        self._fon_style = val

    def reset(self):
        settings_file = open("Resources/Settings.txt")
        settings_ = []
        for i in settings_file:
            settings_.append(i.rstrip())
        self.snake_style = settings_[0]
        self.fon_style = settings_[1]
        self._field_size = int(settings_[2])
        settings_file.close()
        self.grid_size = (self._parent.get_size()[0] / self._field_size, self._parent.get_size()[1] / self._field_size)
        self.snake = [(0, 0)]
        self.apple = None
        self.syringe = None
        self.tablet = None
        self.knife = None
        self.score = 0
        self.csd = False
        self._Enable = False
        self._Visible = False
        self.direction = (1, 0)
        self.score_label = text.Label("Score: {}".format(self.score), font_size=16, x=10, y=self._parent.height - 20)
    _parent = None
    grid_size = None
    snake = [(0, 0)]
    direction = None
    apple = None
    syringe = None
    tablet = None
    knife = None
    score = 0
    score_label = None
    csd = False
    player_name = 'unknown'
    _game_mode = 'upgrade_classic'
    _snake_style = 'rainbow'
    apple_image = image.load('Resources/apple.png')
    syringe_image = image.load('Resources/syringe.png')
    tablet_image = image.load('Resources/tablet.png')
    knife_image = image.load('Resources/knife.png')
    red_image = image.SolidColorImagePattern((255, 0, 0, 255)).create_image(100, 100)
    orange_image = image.SolidColorImagePattern((255, 165, 0, 255)).create_image(100, 100)
    yellow_image = image.SolidColorImagePattern((255, 255, 0, 255)).create_image(100, 100)
    green_image = image.SolidColorImagePattern((0, 128, 0, 255)).create_image(100, 100)
    blue_image = image.SolidColorImagePattern((0, 0, 255, 255)).create_image(100, 100)
    dark_blue_image = image.SolidColorImagePattern((0, 0, 139, 255)).create_image(100, 100)
    purple_image = image.SolidColorImagePattern((128, 0, 128, 255)).create_image(100, 100)
    black_image = image.SolidColorImagePattern((0, 0, 0, 255)).create_image(100, 100)
    white_image = image.SolidColorImagePattern((255, 255, 255, 255)).create_image(100, 100)
    head_image = image.load('Resources/head_1.png')
    body_image = image.load('Resources/body_2.png')
    body_angle_image = image.load('Resources/body_angle_2.png')
    _Fon = image.load('Resources/game_fon.png')
    _field_size = 20
    _fon_style = 'black'
    _Enable = False
    _Visible = False
