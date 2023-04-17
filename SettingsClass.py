from pyglet import image
from pyglet.sprite import Sprite
from ButtonClass import Button
from pyglet import text
import Global_definitions


class Settings:
    def __init__(self, parent):
        self._Change_snake_style_to_previous = Button(0, 0, image.load('Resources/Buttons/Left_Arrow_1.png'),
                                                      image.load('Resources/Buttons/Left_Arrow_2.png'),
                                                      image.load('Resources/Buttons/Left_Arrow_3.png'), parent)
        self._Change_snake_style_to_next = Button(0, 0, image.load('Resources/Buttons/Right_Arrow_1.png'),
                                                  image.load('Resources/Buttons/Right_Arrow_2.png'),
                                                  image.load('Resources/Buttons/Right_Arrow_3.png'), parent)
        self._Change_field_size_to_previous = Button(0, 0, image.load('Resources/Buttons/Left_Arrow_1.png'),
                                                     image.load('Resources/Buttons/Left_Arrow_2.png'),
                                                     image.load('Resources/Buttons/Left_Arrow_3.png'), parent)
        self._Change_field_size_to_next = Button(0, 0, image.load('Resources/Buttons/Right_Arrow_1.png'),
                                                 image.load('Resources/Buttons/Right_Arrow_2.png'),
                                                 image.load('Resources/Buttons/Right_Arrow_3.png'), parent)
        self._Change_fon_style_to_previous = Button(0, 0, image.load('Resources/Buttons/Left_Arrow_1.png'),
                                                    image.load('Resources/Buttons/Left_Arrow_2.png'),
                                                    image.load('Resources/Buttons/Left_Arrow_3.png'), parent)
        self._Change_fon_style_to_next = Button(0, 0, image.load('Resources/Buttons/Right_Arrow_1.png'),
                                                image.load('Resources/Buttons/Right_Arrow_2.png'),
                                                image.load('Resources/Buttons/Right_Arrow_3.png'), parent)
        self._Back = Button(0, 0, image.load('Resources/Buttons/Back_1.png'),
                            image.load('Resources/Buttons/Back_2.png'),
                            image.load('Resources/Buttons/Back_3.png'), parent)
        fon = image.load('Resources/fon_for_settings.png')
        self._Fon = Sprite(fon)
        self._Fon.scale_x = parent.get_size()[0] * 3 / 4 / fon.width
        self._Fon.scale_y = parent.get_size()[1] * 3 / 4 / fon.height
        self._Fon.position = (parent.get_size()[0] / 8, parent.get_size()[0] / 8, 0)
        fon_for_labels = image.SolidColorImagePattern((0, 0, 255, 255)).create_image(100, 100)
        self._snake_style_label_fon = Sprite(fon_for_labels)
        self._field_size_label_fon = Sprite(fon_for_labels)
        self._fon_style_label_fon = Sprite(fon_for_labels)
        self._snake_style_label_fon.scale_x = self._Fon.width / 3 / fon_for_labels.width
        self._snake_style_label_fon.scale_y = self._Fon.height / 12 / fon_for_labels.height
        self._field_size_label_fon.scale_x = self._Fon.width / 3 / fon_for_labels.width
        self._field_size_label_fon.scale_y = self._Fon.height / 12 / fon_for_labels.height
        self._fon_style_label_fon.scale_x = self._Fon.width / 3 / fon_for_labels.width
        self._fon_style_label_fon.scale_y = self._Fon.height / 12 / fon_for_labels.height
        self._Back.scale = self._Fon.height / 12 / self._Back.height
        free_space = (self._Fon.height -
                      (self._snake_style_label_fon.height +
                       self._field_size_label_fon.height + self._fon_style_label_fon.height + self._Back.height)) / 5
        self._Back.position = (self._Fon.position[0] + (self._Fon.width - self._Back.width) / 2, self._Fon.position[1] + free_space, 0)
        self._field_size_label_fon.position = (
            self._Fon.position[0] + (self._Fon.width - self._field_size_label_fon.width) / 2,
            self._Back.position[1] + self._Back.height + free_space, 0)
        self._fon_style_label_fon.position = (
            self._Fon.position[0] + (self._Fon.width - self._fon_style_label_fon.width) / 2,
            self._field_size_label_fon.position[1] + self._field_size_label_fon.height + free_space, 0)
        self._snake_style_label_fon.position = (
            self._Fon.position[0] + (self._Fon.width - self._snake_style_label_fon.width) / 2,
            self._fon_style_label_fon.position[1] + self._fon_style_label_fon.height + free_space, 0)
        target_height = self._Fon.height / 12
        target_width = target_height * self._Change_snake_style_to_previous.width / self._Change_snake_style_to_previous.height
        self._Change_snake_style_to_previous.scale_x = target_width / self._Change_snake_style_to_previous.width
        self._Change_snake_style_to_previous.scale_y = target_height / self._Change_snake_style_to_previous.height
        target_width = target_height * self._Change_snake_style_to_next.width / self._Change_snake_style_to_next.height
        self._Change_snake_style_to_next.scale_x = target_width / self._Change_snake_style_to_next.width
        self._Change_snake_style_to_next.scale_y = target_height / self._Change_snake_style_to_next.height
        target_width = target_height * self._Change_field_size_to_previous.width / self._Change_field_size_to_previous.height
        self._Change_field_size_to_previous.scale_x = target_width / self._Change_field_size_to_previous.width
        self._Change_field_size_to_previous.scale_y = target_height / self._Change_field_size_to_previous.height
        target_width = target_height * self._Change_field_size_to_next.width / self._Change_field_size_to_next.height
        self._Change_field_size_to_next.scale_x = target_width / self._Change_field_size_to_next.width
        self._Change_field_size_to_next.scale_y = target_height / self._Change_field_size_to_next.height
        target_width = target_height * self._Change_fon_style_to_previous.width / self._Change_fon_style_to_previous.height
        self._Change_fon_style_to_previous.scale_x = target_width / self._Change_fon_style_to_previous.width
        self._Change_fon_style_to_previous.scale_y = target_height / self._Change_fon_style_to_previous.height
        target_width = target_height * self._Change_fon_style_to_next.width / self._Change_fon_style_to_next.height
        self._Change_fon_style_to_next.scale_x = target_width / self._Change_fon_style_to_next.width
        self._Change_fon_style_to_next.scale_y = target_height / self._Change_fon_style_to_next.height

        self._Change_snake_style_to_previous.position = (
            self._snake_style_label_fon.position[0] - self._Change_snake_style_to_previous.width * 3 / 2,
            self._snake_style_label_fon.position[1], 0)
        self._Change_snake_style_to_next.position = (self._snake_style_label_fon.position[
                                                         0] + self._snake_style_label_fon.width + self._Change_snake_style_to_next.width / 2,
                                                     self._snake_style_label_fon.position[1],
                                                     0)
        self._Change_field_size_to_previous.position = (
            self._field_size_label_fon.position[0] - self._Change_field_size_to_previous.width * 3 / 2,
            self._field_size_label_fon.position[1], 0)
        self._Change_field_size_to_next.position = (self._field_size_label_fon.position[
                                                        0] + self._field_size_label_fon.width + self._Change_field_size_to_next.width / 2,
                                                    self._field_size_label_fon.position[1],
                                                    0)
        self._Change_fon_style_to_previous.position = (
            self._fon_style_label_fon.position[0] - self._Change_fon_style_to_previous.width * 3 / 2,
            self._fon_style_label_fon.position[1], 0)
        self._Change_fon_style_to_next.position = (self._fon_style_label_fon.position[
                                                       0] + self._fon_style_label_fon.width + self._Change_fon_style_to_next.width / 2,
                                                   self._fon_style_label_fon.position[1],
                                                   0)
        self._Back._pressed_event = self.back_event
        self._Change_snake_style_to_previous._pressed_event = self.change_snake_style_to_previous_event
        self._Change_snake_style_to_next._pressed_event = self.change_snake_style_to_next_event
        self._Change_field_size_to_previous._pressed_event = self.change_field_size_to_previous_event
        self._Change_field_size_to_next._pressed_event = self.change_field_size_to_next_event
        self._Change_fon_style_to_previous._pressed_event = self.change_fon_style_to_previous_event
        self._Change_fon_style_to_next._pressed_event = self.change_fon_style_to_next_event
        parent.push_handlers(self.on_draw)
        self._parent = parent

    def back_event(self):
        self.visible = False
        Global_definitions.stage = 'open_main_menu'

    def change_snake_style_to_previous_event(self):
        self._Current_snake_style -= 1
        self._Current_snake_style %= len(self._snake_styles)

    def change_snake_style_to_next_event(self):
        self._Current_snake_style += 1
        self._Current_snake_style %= len(self._snake_styles)

    def change_field_size_to_previous_event(self):
        self._Current_field_size -= 1
        self._Current_snake_style %= len(self._field_sizes)

    def change_field_size_to_next_event(self):
        self._Current_field_size += 1
        self._Current_snake_style %= len(self._field_sizes)

    def change_fon_style_to_previous_event(self):
        self._Current_fon_style -= 1
        self._Current_fon_style %= len(self._fon_styles)

    def change_fon_style_to_next_event(self):
        self._Current_fon_style += 1
        self._Current_fon_style %= len(self._fon_styles)

    def on_draw(self):
        if self.visible:
            self._Fon.draw()
            self._snake_style_label_fon.draw()
            # self._snake_style_label.draw()
            self._field_size_label_fon.draw()
            # self._field_size_label.draw()
            self._fon_style_label_fon.draw()
            # self._fon_style_label.draw()
            self._Change_snake_style_to_previous.draw()
            self._Change_snake_style_to_next.draw()
            self._Change_field_size_to_previous.draw()
            self._Change_field_size_to_next.draw()
            self._Change_fon_style_to_previous.draw()
            self._Change_fon_style_to_next.draw()
            self._Back.draw()

    @property
    def visible(self):
        return self._Visible

    @visible.setter
    def visible(self, val: bool):
        self._Visible = val
        self._Change_snake_style_to_previous.visible = val
        self._Change_snake_style_to_next.visible = val
        self._Change_field_size_to_previous.visible = val
        self._Change_field_size_to_next.visible = val
        self._Change_fon_style_to_previous.visible = val
        self._Change_fon_style_to_next.visible = val
        self._Back.visible = val
        # self._parent.clear()
        if self.enable and not self.visible:
            self.enable = False

    @property
    def enable(self):
        return self._Enable

    @enable.setter
    def enable(self, val: bool):
        self._Enable = val
        self._Change_snake_style_to_previous.enable = val
        self._Change_snake_style_to_next.enable = val
        self._Change_field_size_to_previous.enable = val
        self._Change_field_size_to_next.enable = val
        self._Change_fon_style_to_previous.enable = val
        self._Change_fon_style_to_next.enable = val
        self._Back.enable = val
        if self.enable and not self.visible:
            self.visible = True

    _parent = None
    _Change_snake_style_to_previous = None
    _Change_snake_style_to_next = None
    _Current_snake_style = 0
    _snake_styles = ['red', 'yellow', 'orange', 'green', 'blue', 'dark_blue', 'purple', 'rainbow', 'rainbow2.0',
                     'textured']
    _snake_style_label = None
    _snake_style_label_fon = None
    _Change_field_size_to_previous = None
    _Change_field_size_to_next = None
    _Current_field_size = 0
    _field_sizes = ['10x10', '20x20', '30x30', '40x40', '50x50', '60x60', '70x70', '70x70', '80x80', '90x90'  '100x100']
    _field_size_label = None
    _field_size_label_fon = None
    _Change_fon_style_to_previous = None
    _Change_fon_style_to_next = None
    _Current_fon_style = 0
    _fon_styles = ['black', 'red', 'yellow', 'orange', 'green', 'blue', 'dark_blue', 'purple', 'textured']
    _fon_style_label = None
    _fon_style_label_fon = None
    _Back = None
    _Enable = False
    _Visible = False
    _Fon = None
