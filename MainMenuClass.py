from pyglet import image
from pyglet.sprite import Sprite
from pyglet.app import exit
from ButtonClass import Button
import Global_definitions


class MainMenu:
    def __init__(self, parent):
        self._PlayButton = Button(0, 0, image.load('Resources/Buttons/Play_1.png'),
                                  image.load('Resources/Buttons/Play_2.png'),
                                  image.load('Resources/Buttons/Play_3.png'), parent)
        self._SettingsButton = Button(0, 0, image.load('Resources/Buttons/Settings_1.png'),
                                      image.load('Resources/Buttons/Settings_2.png'),
                                      image.load('Resources/Buttons/Settings_3.png'), parent)
        self._ExitButton = Button(0, 0, image.load('Resources/Buttons/Exit_1.png'),
                                  image.load('Resources/Buttons/Exit_2.png'),
                                  image.load('Resources/Buttons/Exit_3.png'), parent)
        fon = image.load('Resources/Fons/fon_for_main_menu.png')
        self._Fon = Sprite(fon)
        self._Fon.scale_x = parent.get_size()[0] / fon.width
        self._Fon.scale_y = parent.get_size()[1] / fon.height
        target_height = parent.get_size()[0] / 8
        self._PlayButton.scale = target_height / self._PlayButton.height
        self._SettingsButton.scale = target_height / self._SettingsButton.height
        self._ExitButton.scale = target_height / self._ExitButton.height
        free_space = (parent.get_size()[1] - (
                self._PlayButton.height + self._SettingsButton.height + self._ExitButton.height)) / 4
        self._ExitButton.position = ((parent.get_size()[0] - self._ExitButton.width) / 2, free_space, 0)
        self._SettingsButton.position = ((parent.get_size()[0] - self._SettingsButton.width) / 2,
                                         self._ExitButton.position[1] + self._ExitButton.height + free_space, 0)
        self._PlayButton.position = ((parent.get_size()[0] - self._PlayButton.width) / 2,
                                     self._SettingsButton.position[1] + self._SettingsButton.height + free_space, 0)
        self._PlayButton._pressed_event = self.play_event
        self._SettingsButton._pressed_event = self.settings_event
        self._ExitButton._pressed_event = self.exit_event
        parent.push_handlers(self.on_draw)
        self._parent = parent

    def play_event(self):
        self.visible = False
        Global_definitions.stage = 'open_play_menu'

    def settings_event(self):
        self.enable = False
        Global_definitions.stage = 'open_settings'

    @staticmethod
    def exit_event():
        exit()

    def on_draw(self):
        if self.visible:
            self._Fon.draw()
            self._PlayButton.draw()
            self._SettingsButton.draw()
            self._ExitButton.draw()

    @property
    def visible(self):
        return self._Visible

    @visible.setter
    def visible(self, val: bool):
        self._Visible = val
        self._PlayButton.visible = val
        self._SettingsButton.visible = val
        self._ExitButton.visible = val
        self._parent.clear()
        if self._Enable and not self._Visible:
            self.enable = False

    @property
    def enable(self):
        return self._Enable

    @enable.setter
    def enable(self, val: bool):
        self._Enable = val
        self._PlayButton._Enable = val
        self._SettingsButton._Enable = val
        self._ExitButton._Enable = val
        if self._Enable and not self._Visible:
            self.visible = True

    _parent = None
    _PlayButton = None
    _SettingsButton = None
    _ExitButton = None
    _Enable = False
    _Visible = False
    _Fon = None
