from pyglet import image
from pyglet.sprite import Sprite
from ButtonClass import Button
from OptionsBlockClass import OptionsBlock
import Global_definitions


class Settings:
    def __init__(self, parent):
        self._snake_style = OptionsBlock.construct_using_basic_arrows('Snake style', self._snake_styles, parent,
                                                                      image.load('Resources/Buttons/panel.png'))
        self._fon_style = OptionsBlock.construct_using_basic_arrows('Fon style', self._fon_styles, parent,
                                                                    image.load('Resources/Buttons/panel.png'))
        self._field_size = OptionsBlock.construct_using_basic_arrows('Field size', self._field_sizes, parent,
                                                                     image.load('Resources/Buttons/panel.png'))
        self._Back = Button(0, 0, image.load('Resources/Buttons/Back_1.png'),
                            image.load('Resources/Buttons/Back_2.png'),
                            image.load('Resources/Buttons/Back_3.png'), parent)
        settings_ = Global_definitions.get_settings()
        self._snake_style.current_option = settings_[1]
        self._fon_style.current_option = settings_[2]
        self._field_size.current_option = settings_[3] + 'x' + settings_[3]
        fon = image.load('Resources/Fons/fon_for_settings.png')
        self._Fon = Sprite(fon)
        self._Fon.scale_x = parent.get_size()[0] * 3 / 4 / fon.width
        self._Fon.scale_y = parent.get_size()[1] * 3 / 4 / fon.height
        self._Fon.position = (parent.get_size()[0] / 8, parent.get_size()[0] / 8, 0)
        self._snake_style.width = self._Fon.width * 5 / 8
        self._snake_style.height = self._Fon.height / 12
        self._fon_style.width = self._Fon.width * 5 / 8
        self._fon_style.height = self._Fon.height / 12
        self._field_size.width = self._Fon.width * 5 / 8
        self._field_size.height = self._Fon.height / 12
        self._Back.scale = self._Fon.height / 12 / self._Back.height
        free_space = (self._Fon.height -
                      (self._snake_style.height + self._fon_style.height + self._field_size.height +
                       self._Back.height)) / 5
        self._Back.position = (
            self._Fon.position[0] + (self._Fon.width - self._Back.width) / 2, self._Fon.position[1] + free_space, 0)
        self._field_size.position = (
            self._Fon.position[0] + self._Fon.width / 2,
            self._Back.position[1] + self._Back.height + free_space + self._field_size.height / 2, 0)
        self._fon_style.position = (
            self._Fon.position[0] + self._Fon.width / 2,
            self._field_size.position[1] + self._field_size.height / 2 + free_space + self._fon_style.height / 2, 0)
        self._snake_style.position = (
            self._Fon.position[0] + self._Fon.width / 2,
            self._fon_style.position[1] + self._fon_style.height / 2 + free_space + self._snake_style.height / 2, 0)
        self._Back._pressed_event = self.back_event
        parent.push_handlers(self.on_draw)
        self._parent = parent

    def back_event(self):
        self.visible = False
        settings_ = Global_definitions.get_settings()
        settings_[1] = self._snake_style.current_option
        settings_[2] = self._fon_style.current_option
        settings_[3] = self._field_size.current_option[:self._field_size.current_option.index('x')]
        Global_definitions.set_settings(settings_)
        Global_definitions.stage = 'open_main_menu'

    def on_draw(self):
        if self.visible:
            self._Fon.draw()
            self._snake_style.draw()
            self._field_size.draw()
            self._fon_style.draw()
            self._Back.draw()

    @property
    def visible(self):
        return self._Visible

    @visible.setter
    def visible(self, val: bool):
        self._Visible = val
        self._snake_style.visible = val
        self._field_size.visible = val
        self._fon_style.visible = val
        self._Back.visible = val
        if self.enable and not self.visible:
            self.enable = False

    @property
    def enable(self):
        return self._Enable

    @enable.setter
    def enable(self, val: bool):
        self._Enable = val
        self._snake_style.enable = val
        self._field_size.enable = val
        self._fon_style.enable = val
        self._Back.enable = val
        if self.enable and not self.visible:
            self.visible = True

    _parent = None
    _snake_style = None
    _snake_styles = ['red', 'yellow', 'orange', 'green', 'blue', 'dark_blue', 'purple', 'rainbow', 'rainbow2.0',
                     'textured_1', 'textured_2']
    _field_size = None
    _field_sizes = ['10x10', '20x20', '30x30', '40x40', '50x50', '60x60', '70x70', '70x70', '80x80', '90x90', '100x100']
    _fon_style = None
    _fon_styles = ['black', 'red', 'yellow', 'orange', 'green', 'blue', 'dark_blue', 'purple', 'textured']
    _Back = None
    _Enable = False
    _Visible = False
    _Fon = None
