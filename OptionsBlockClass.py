from ButtonClass import Button
from pyglet import image
from pyglet import text
from pyglet.sprite import Sprite
import Global_definitions


class OptionsBlock:
    def __init__(self, name, options: list, parent, option_fon_image, images_for_arrows: list):
        self._left_arrow = Button.construct_by_list(0, 0, images_for_arrows[:3], parent)
        self._right_arrow = Button.construct_by_list(0, 0, images_for_arrows[3:], parent)
        self._options = options
        self._option_fon = Sprite(option_fon_image)
        self._left_arrow._pressed_event = self.left_arrow_event
        self._right_arrow._pressed_event = self.right_arrow_event
        self._parent = parent
        self._option_name_label = text.Label(name, font_size=self._option_fon.height * 5 / 12,
                                             color=(255, 0, 0, 255),
                                             x=(self._option_fon.position[0] + self._option_fon.width / 2),
                                             y=(self._option_fon.position[1] + self._option_fon.height * 3 / 2),
                                             anchor_x='center',
                                             anchor_y='center')
        self._option_label = text.Label(self._options[self._current_option],
                                        font_size=self._option_fon.height * 11 / 24,
                                        color=(0, 0, 0, 255),
                                        x=(self._option_fon.position[0] + self._option_fon.width / 2),
                                        y=(self._option_fon.position[1] + self._option_fon.height / 2),
                                        anchor_x='center',
                                        anchor_y='center')

    @classmethod
    def construct_using_basic_arrows(cls, option_name, options, parent, option_fon_image):
        images_for_arrows = []
        for i in cls._paths_to_basic_images_for_arrows:
            images_for_arrows.append(image.load(Global_definitions.path(i)))
        return cls(option_name, options, parent, option_fon_image, images_for_arrows)

    @classmethod
    def construct_using_basic_fon(cls, option_name, options, parent, images_for_arrows):
        return cls(option_name, options, parent, cls._basic_option_fon_image, images_for_arrows)

    @classmethod
    def construct_using_basic_values(cls, option_name_label: str, options: list, parent):
        return cls.construct_using_basic_arrows(option_name_label, options, parent, cls._basic_option_fon_image)

    def left_arrow_event(self):
        self._current_option -= 1
        self._current_option %= len(self._options)
        self._option_label.text = self._options[self._current_option]

    def right_arrow_event(self):
        self._current_option += 1
        self._current_option %= len(self._options)
        self._option_label.text = self._options[self._current_option]

    def draw(self):
        self._option_fon.draw()
        self._option_name_label.draw()
        self._option_label.draw()
        self._left_arrow.draw()
        self._right_arrow.draw()

    @property
    def current_option_index(self):
        return self._current_option

    @current_option_index.setter
    def current_option_index(self, val):
        self._current_option = val
        self._option_label.text = self.current_option

    @property
    def current_option(self):
        return self._options[self.current_option_index]

    @current_option.setter
    def current_option(self, val):
        try:
            self.current_option_index = self._options.index(val)
        except ValueError:
            self.current_option_index = 0
        self._option_label.text = self.current_option

    @property
    def name_label_color(self):
        return self._option_name_label.color

    @name_label_color.setter
    def name_label_color(self, val):
        self._option_name_label.color = val

    @property
    def label_color(self):
        return self._option_label.color

    @label_color.setter
    def label_color(self, val):
        self._option_label.color = val

    @property
    def fon_height(self):
        return self._option_fon.height

    @fon_height.setter
    def fon_height(self, val):
        self._option_fon.scale_y *= val / self._option_fon.height
        self.position = self.position
        self._option_name_label.font_size = self._option_fon.height * 5 / 12
        self._option_label.font_size = self._option_fon.height * 11 / 24

    @property
    def fon_width(self):
        return self._option_fon.width

    @fon_width.setter
    def fon_width(self, val):
        self._option_fon.scale_x *= val / self._option_fon.width
        self.position = self.position

    @property
    def left_arrow_height(self):
        return self._left_arrow.height

    @left_arrow_height.setter
    def left_arrow_height(self, val):
        self._left_arrow.scale_y *= val / self._left_arrow.height
        self.position = self.position

    @property
    def left_arrow_width(self):
        return self._left_arrow.width

    @left_arrow_width.setter
    def left_arrow_width(self, val):
        self._left_arrow.scale_x *= val / self._left_arrow.width
        self.position = self.position

    @property
    def right_arrow_height(self):
        return self._right_arrow.height

    @right_arrow_height.setter
    def right_arrow_height(self, val):
        self._right_arrow.scale_y *= val / self._right_arrow.height
        self.position = self.position

    @property
    def right_arrow_width(self):
        return self._right_arrow.width

    @right_arrow_width.setter
    def right_arrow_width(self, val):
        self._right_arrow.scale_x *= val / self._right_arrow.width
        self.position = self.position

    @property
    def height(self):
        return max(self.fon_height, self.left_arrow_height, self.right_arrow_height)

    @height.setter
    def height(self, val):
        self.fon_height = val
        self.left_arrow_height = val
        self.right_arrow_height = val

    @property
    def width(self):
        return self.fon_width + self.left_arrow_width + self.right_arrow_width + \
               self.left_free_space + self.right_free_space

    @width.setter
    def width(self, val):
        true_width = val - (self.left_free_space + self.right_free_space)
        self.fon_width = true_width * 5 / 8
        self.left_arrow_width = true_width * 3 / 16
        self.right_arrow_width = true_width * 3 / 16

    @property
    def position(self):
        return self._option_fon.position[0] + self._option_fon.width / 2, self._option_fon.position[1] +\
               self._option_fon.height / 2, self._option_fon.position[2]

    @position.setter
    def position(self, val):
        self._option_fon.position = (val[0] - self._option_fon.width / 2, val[1] - self._option_fon.height / 2, val[2])
        self._left_arrow.position = (
            self._option_fon.position[0] - self._left_arrow.width - self._left_free_space,
            val[1] - self._left_arrow.height / 2, val[2])
        self._right_arrow.position = (
            self._option_fon.position[0] + self._option_fon.width + self._right_free_space,
            val[1] - self._right_arrow.height / 2, val[2])
        self._option_name_label.x = self._option_fon.position[0] + self._option_fon.width / 2
        self._option_name_label.y = self._option_fon.position[1] + self._option_fon.height * 3 / 2
        self._option_label.x = self._option_fon.position[0] + self._option_fon.width / 2
        self._option_label.y = self._option_fon.position[1] + self._option_fon.height / 2

    @property
    def left_free_space(self):
        return self._left_free_space

    @left_free_space.setter
    def left_free_space(self, val):
        self._left_free_space = val
        self._left_arrow.position = (
            self._option_fon.position[0] - self._left_arrow.width - self._left_free_space,
            self._left_arrow.position[1], self._left_arrow.position[2])

    @property
    def right_free_space(self):
        return self._right_free_space

    @right_free_space.setter
    def right_free_space(self, val):
        self._right_free_space = val
        self._right_arrow.position = (
            self._option_fon.position[0] + self._option_fon.position.width + self._right_free_space,
            self._right_arrow.position[1], self._right_arrow.position[2])

    def set_free_space(self, val):
        self.left_free_space = val
        self.right_free_space = val

    @property
    def visible(self):
        return self._Visible

    @visible.setter
    def visible(self, val: bool):
        self._Visible = val
        self._left_arrow.visible = val
        self._right_arrow.visible = val
        self._parent.clear()
        if self._Enable and not self._Visible:
            self.enable = False

    @property
    def enable(self):
        return self._Enable

    @enable.setter
    def enable(self, val: bool):
        self._Enable = val
        self._left_arrow.enable = val
        self._right_arrow.enable = val
        if self._Enable and not self._Visible:
            self.visible = True

    _parent = None
    _left_arrow = None
    _right_arrow = None
    _current_option = 0
    _options = list()
    _option_name_label = None
    _option_label = None
    _option_fon = None
    _left_free_space = 10
    _right_free_space = 10
    _paths_to_basic_images_for_arrows = ['Resources/Buttons/Left_Arrow_1.png', 'Resources/Buttons/Left_Arrow_2.png',
                                         'Resources/Buttons/Left_Arrow_3.png', 'Resources/Buttons/Right_Arrow_1.png',
                                         'Resources/Buttons/Right_Arrow_2.png', 'Resources/Buttons/Right_Arrow_3.png']
    _basic_option_fon_image = image.SolidColorImagePattern((0, 0, 255, 255)).create_image(100, 100)
    _Enable = False
    _Visible = False
