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
        clock.schedule_interval(self.update, 1 / 100000000)
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
            spr.position = (spr.position[0], spr.position[1] + 1, spr.position[2])
        if angle == -90:
            spr.position = (spr.position[0] + 1, spr.position[1], spr.position[2])
        elif angle == 180:
            spr.position = (spr.position[0] + 1, spr.position[1] + 1, spr.position[2])
        spr.position = (spr.position[0] * self.grid_size[0], spr.position[1] * self.grid_size[1], spr.position[2])
        spr.draw()
        del spr

    def classic_update_logic(self):
        new_head = (self.snake[-1][0] + self.direction[0], self.snake[-1][1] + self.direction[1])
        if new_head[0] < 0:
            new_head = (new_head[0] + self._field_size, new_head[1])
        if new_head[0] >= self._field_size:
            new_head = (new_head[0] - self._field_size, new_head[1])
        if new_head[1] < 0:
            new_head = (new_head[0], new_head[1] + self._field_size)
        if new_head[1] >= self._field_size:
            new_head = (new_head[0], new_head[1] - self._field_size)
        if new_head in self.snake[1:]:
            self.enable = False
            Global_definitions.stage = 'open_game_over_menu'
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_result = f"{time}\t\t{self.player_name}\t\t{self.game_mode}\t\t{self._field_size}\t\t{self.score}\n"
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
            while self.apple in self.snake or self.apple == self.syringe or self.apple == self.tablet or self.apple == self.knife:
                self.apple = self.rand_place_on_grid()

    def upgraded_classic_update_logic(self):
        self.classic_update_logic()
        new_head = self.snake[-1]
        if self.syringe is not None and new_head == self.syringe:
            self.syringe = None
            self.time_interval /= 2
            self.score += 2
            self.score_label.text = "Score: {}".format(self.score)
        if self.syringe is None:
            if random.randint(1, 100) == 1:
                self.syringe = self.rand_place_on_grid()
                while self.syringe in self.snake or self.syringe == self.apple or self.syringe == self.tablet or self.syringe == self.knife:
                    self.syringe = self.rand_place_on_grid()
        if self.tablet is not None and new_head == self.tablet:
            self.tablet = None
            self.time_interval *= 2
        if self.tablet is None:
            if random.randint(1, 150) == 1:
                self.tablet = self.rand_place_on_grid()
                while self.tablet in self.snake or self.tablet == self.apple or self.tablet == self.syringe or self.tablet == self.knife:
                    self.tablet = self.rand_place_on_grid()
        if self.knife is not None and new_head == self.knife:
            self.knife = None
            self.snake = self.snake[len(self.snake) // 2:]
            self.score //= 2
            self.score_label.text = "Score: {}".format(self.score)
        if self.knife is None:
            if random.randint(1, 1000) == 1:
                self.knife = self.rand_place_on_grid()
                while self.knife in self.snake or self.knife == self.apple or self.knife == self.tablet or self.knife == self.syringe:
                    self.knife = self.rand_place_on_grid()

    def update(self, dt):
        dt *= 1000
        if self.enable:
            self.timer += dt
            while self.timer > self.time_interval:
                if self.game_mode == 'classic':
                    self.classic_update_logic()
                elif self.game_mode == 'upgraded_classic':
                    self.upgraded_classic_update_logic()
                self.csd = True
                self.timer -= self.time_interval
            if self._snake_style == 'rainbow2.0' and len(self.rainbow2_point_0_images) != len(self.snake):
                self.update_rainbow2_point_0_images()

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

    def draw_classic_snake(self):
        self.draw_image(self.head_image, self.grid_size, self.snake[-1])
        for i in reversed(self.snake[:-1]):
            self.draw_image(self.body_image, self.grid_size, i)

    def draw_rainbow_snake(self):
        c = -1
        for i in reversed(self.snake):
            c += 1
            self.draw_image(self.rainbow_images[c % len(self.rainbow_images)], self.grid_size, i)

    def update_rainbow2_point_0_images(self):
        self.rainbow2_point_0_images.clear()
        for i in range(len(self.snake[len(self.snake) // 2:])):
            if len(self.snake) - len(self.snake) // 2 > 1:
                current_image = image.SolidColorImagePattern((0,
                                                              (255 * i) // (len(self.snake) - len(
                                                                  self.snake) // 2 - 1),
                                                              255 - (255 * i) // (len(self.snake) - len(
                                                                  self.snake) // 2 - 1), 255)).create_image(1,
                                                                                                            1)
                self.rainbow2_point_0_images.append(current_image)
            else:
                if len(self.snake) != 1:
                    self.rainbow2_point_0_images.append(self.rainbow_images[4])
                else:
                    self.rainbow2_point_0_images.append(self.rainbow_images[0])
        for i in range(len(self.snake[:len(self.snake) // 2])):
            if len(self.snake) // 2 > 1:
                current_image = image.SolidColorImagePattern(((255 * i) // (len(self.snake) // 2 - 1),
                                                              255 - (255 * i) // (len(self.snake) // 2 - 1), 0,
                                                              255)).create_image(1, 1)
                self.rainbow2_point_0_images.append(current_image)
            else:
                self.rainbow2_point_0_images.append(self.rainbow_images[0])

    def draw_rainbow2_point_0_snake(self):
        for i in range(len(self.snake)):
            self.draw_image(self.rainbow2_point_0_images[i], self.grid_size, self.snake[i])

    def get_direction(self, current, previous):
        direction = (current[0] - previous[0], current[1] - previous[1])
        if direction[0] == self._field_size - 1:
            direction = (-1, direction[1])
        if direction[0] == 1 - self._field_size:
            direction = (1, direction[1])
        if direction[1] == self._field_size - 1:
            direction = (direction[0], -1)
        if direction[1] == 1 - self._field_size:
            direction = (direction[0], 1)
        return direction

    def draw_textured_snake(self):
        if len(self.snake) == 1:
            angle = 0
            if self.direction == (1, 0):
                angle = 90
            elif self.direction == (0, -1):
                angle = 180
            elif self.direction == (-1, 0):
                angle = -90
            self.draw_image(self.head_tail_image, self.grid_size, self.snake[-1], angle)
        if len(self.snake) != 1:
            current_loc_dir = self.get_direction(self.snake[-1], self.snake[-2])
            angle = 0
            if current_loc_dir == (1, 0):
                angle = 90
            elif current_loc_dir == (0, -1):
                angle = 180
            elif current_loc_dir == (-1, 0):
                angle = -90
            self.draw_image(self.head_image, self.grid_size, self.snake[-1], angle)
        for i in range(len(self.snake) - 2, 0, -1):
            current_loc_dir = self.get_direction(self.snake[i + 1], self.snake[i])
            next_loc_dir = self.get_direction(self.snake[i], self.snake[i - 1])
            if current_loc_dir == next_loc_dir:
                angle = 0
                if current_loc_dir == (1, 0):
                    angle = 90
                elif current_loc_dir == (0, -1):
                    angle = 180
                elif current_loc_dir == (-1, 0):
                    angle = -90
                self.draw_image(self.body_image, self.grid_size, self.snake[i], angle)
            else:
                angle = 0
                if (current_loc_dir == (0, -1) and next_loc_dir == (-1, 0)) or (current_loc_dir == (1, 0) and next_loc_dir == (0, 1)):
                    angle = 90
                if (current_loc_dir == (0, -1) and next_loc_dir == (1, 0)) or (current_loc_dir == (-1, 0) and next_loc_dir == (0, 1)):
                    angle = 180
                if (current_loc_dir == (0, 1) and next_loc_dir == (1, 0)) or (current_loc_dir == (-1, 0) and next_loc_dir == (0, -1)):
                    angle = -90
                self.draw_image(self.body_angle_image, self.grid_size, self.snake[i], angle)
        if len(self.snake) != 1:
            current_loc_dir = self.get_direction(self.snake[1], self.snake[0])
            angle = 0
            if current_loc_dir == (1, 0):
                angle = 90
            elif current_loc_dir == (0, -1):
                angle = 180
            elif current_loc_dir == (-1, 0):
                angle = -90
            self.draw_image(self.tail_image, self.grid_size, self.snake[0], angle)

    def on_draw(self):
        if self.visible:
            self._parent.clear()
            self.draw_image(self._Fon, self._parent.get_size(), (0, 0))
            if self._snake_style == 'classic':
                self.draw_classic_snake()
            elif self._snake_style == 'rainbow':
                self.draw_rainbow_snake()
            elif self._snake_style == 'rainbow2.0':
                self.draw_rainbow2_point_0_snake()
            elif self._snake_style[:9] == 'textured_':
                self.draw_textured_snake()
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
        if val == 'classic' or val == 'upgraded_classic':
            self._game_mode = val

    @property
    def snake_style(self):
        return self._snake_style

    @snake_style.setter
    def snake_style(self, val):
        self._snake_style = 'classic'
        if val == 'red':
            self.head_image = self.rainbow_images[0]
            self.body_image = self.rainbow_images[0]
        elif val == 'orange':
            self.head_image = self.rainbow_images[1]
            self.body_image = self.rainbow_images[1]
        elif val == 'yellow':
            self.head_image = self.rainbow_images[2]
            self.body_image = self.rainbow_images[2]
        elif val == 'green':
            self.head_image = self.rainbow_images[3]
            self.body_image = self.rainbow_images[3]
        elif val == 'blue':
            self.head_image = self.rainbow_images[4]
            self.body_image = self.rainbow_images[4]
        elif val == 'dark_blue':
            self.head_image = self.rainbow_images[5]
            self.body_image = self.rainbow_images[5]
        elif val == 'purple':
            self.head_image = self.rainbow_images[6]
            self.body_image = self.rainbow_images[6]
        elif val[:9] == 'textured_':
            self.head_image = image.load('Resources/Textures/head_' + val[9:] + '.png')
            self.body_image = image.load('Resources/Textures/body_' + val[9:] + '.png')
            self.body_angle_image = image.load('Resources/Textures/body_angle_' + val[9:] + '.png')
            self.tail_image = image.load('Resources/Textures/tail_' + val[9:] + '.png')
            self.head_tail_image = image.load('Resources/Textures/head_tail_' + val[9:] + '.png')
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
            self._Fon = self.rainbow_images[0]
        elif val == 'orange':
            self._Fon = self.rainbow_images[1]
        elif val == 'yellow':
            self._Fon = self.rainbow_images[2]
        elif val == 'green':
            self._Fon = self.rainbow_images[3]
        elif val == 'blue':
            self._Fon = self.rainbow_images[4]
        elif val == 'dark_blue':
            self._Fon = self.rainbow_images[5]
        elif val == 'purple':
            self._Fon = self.rainbow_images[6]
        elif val == 'textured':
            self._Fon = image.load('Resources/Fons/game_fon.png')
        self._fon_style = val

    def reset(self):
        settings_ = Global_definitions.get_settings()
        self.player_name = settings_[0]
        self.snake_style = settings_[1]
        self.fon_style = settings_[2]
        self._field_size = int(settings_[3])
        self.grid_size = (self._parent.get_size()[0] / self._field_size, self._parent.get_size()[1] / self._field_size)
        self.snake = [(0, 0)]
        self.apple = None
        self.syringe = None
        self.tablet = None
        self.knife = None
        self.score = 0
        self.csd = False
        self.rainbow2_point_0_images = [self.rainbow_images[0]]
        self._Enable = False
        self._Visible = False
        self.direction = (1, 0)
        self.score_label = text.Label("Score: {}".format(self.score), font_size=16, x=10, y=self._parent.height - 20)
        self.timer = 0
        self.time_interval = 80

    _parent = None
    grid_size = None
    snake = [(0, 0)]
    direction = None
    apple = None
    syringe = None
    tablet = None
    knife = None
    score = 0
    timer = 0
    score_label = None
    csd = False
    time_interval = 80
    player_name = 'unknown'
    _game_mode = 'classic'
    _snake_style = 'rainbow'
    apple_image = image.load('Resources/Textures/apple.png')
    syringe_image = image.load('Resources/Textures/syringe.png')
    tablet_image = image.load('Resources/Textures/tablet.png')
    knife_image = image.load('Resources/Textures/knife.png')
    black_image = image.SolidColorImagePattern((0, 0, 0, 255)).create_image(1, 1)
    white_image = image.SolidColorImagePattern((255, 255, 255, 255)).create_image(1, 1)
    rainbow_images = [image.SolidColorImagePattern((255, 0, 0, 255)).create_image(1, 1),
                      image.SolidColorImagePattern((255, 165, 0, 255)).create_image(1, 1),
                      image.SolidColorImagePattern((255, 255, 0, 255)).create_image(1, 1),
                      image.SolidColorImagePattern((0, 128, 0, 255)).create_image(1, 1),
                      image.SolidColorImagePattern((0, 0, 255, 255)).create_image(1, 1),
                      image.SolidColorImagePattern((0, 0, 139, 255)).create_image(1, 1),
                      image.SolidColorImagePattern((128, 0, 128, 255)).create_image(1, 1)]
    rainbow2_point_0_images = [rainbow_images[0]]
    head_image = image.load('Resources/Textures/head_1.png')
    body_image = image.load('Resources/Textures/body_1.png')
    body_angle_image = image.load('Resources/Textures/body_angle_1.png')
    tail_image = image.load('Resources/Textures/tail_1.png')
    head_tail_image = image.load('Resources/Textures/head_tail_1.png')
    _Fon = image.load('Resources/Fons/game_fon.png')
    _field_size = 20
    _fon_style = 'black'
    _Enable = False
    _Visible = False
