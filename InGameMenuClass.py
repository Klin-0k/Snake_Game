from pyglet import image
from pyglet.sprite import Sprite
from ButtonClass import Button
import Global_definitions


class InGameMenu:
    def __init__(self, parent):
        self._Continue = Button(0, 0, image.load('Resources/Buttons/Continue_1.png'),
                                image.load('Resources/Buttons/Continue_2.png'),
                                image.load('Resources/Buttons/Continue_3.png'), parent)
        self._Restart = Button(0, 0, image.load('Resources/Buttons/Restart_1.png'),
                               image.load('Resources/Buttons/Restart_2.png'),
                               image.load('Resources/Buttons/Restart_3.png'), parent)
        self._BackToMainMenu = Button(0, 0, image.load('Resources/Buttons/Main_Menu_1.png'),
                                      image.load('Resources/Buttons/Main_Menu_2.png'),
                                      image.load('Resources/Buttons/Main_Menu_3.png'), parent)
        fon = image.load('Resources/Fons/fon_for_in_game_menu_1.png')
        self._Fon = Sprite(fon)
        self._Fon.scale_x = parent.get_size()[0] / 2 / fon.width
        self._Fon.scale_y = parent.get_size()[1] / 2 / fon.height
        self._Fon.position = (parent.get_size()[0] / 4, parent.get_size()[0] / 4, 0)
        target_height = self._Fon.height / 6
        self._Continue.scale = target_height / self._Continue.height
        self._Restart.scale = target_height / self._Restart.height
        self._BackToMainMenu.scale = target_height / self._BackToMainMenu.height
        free_space = (self._Fon.height - (
                self._Continue.height + self._Restart.height + self._BackToMainMenu.height)) / 4
        self._BackToMainMenu.position = (self._Fon.position[0] + (self._Fon.width - self._BackToMainMenu.width) / 2, self._Fon.position[1] + free_space, 0)
        self._Restart.position = (self._Fon.position[0] + (self._Fon.width - self._Restart.width) / 2, self._BackToMainMenu.position[1] + self._BackToMainMenu.height + free_space, 0)
        self._Continue.position = (self._Fon.position[0] + (self._Fon.width - self._Continue.width) / 2, self._Restart.position[1] + self._Restart.height + free_space, 0)
        self._Continue._pressed_event = self.continue_event
        self._Restart._pressed_event = self.restart_event
        self._BackToMainMenu._pressed_event = self.back_to_main_menu_event
        parent.push_handlers(self.on_draw)
        self._parent = parent

    def back_to_main_menu_event(self):
        self.visible = False
        Global_definitions.stage = 'open_main_menu'

    def continue_event(self):
        self.visible = False
        Global_definitions.stage = 'close_in_game_menu'

    def restart_event(self):
        self.visible = False
        Global_definitions.stage = 'play_again'

    def on_draw(self):
        if self.visible:
            self._Fon.draw()
            self._Continue.draw()
            self._Restart.draw()
            self._BackToMainMenu.draw()

    @property
    def visible(self):
        return self._Visible

    @visible.setter
    def visible(self, val: bool):
        self._Visible = val
        self._Continue.visible = val
        self._Restart.visible = val
        self._BackToMainMenu.visible = val
        # self._parent.clear()
        if self.enable and not self.visible:
            self.enable = False

    @property
    def enable(self):
        return self._Enable

    @enable.setter
    def enable(self, val: bool):
        self._Enable = val
        self._Continue.enable = val
        self._Restart.enable = val
        self._BackToMainMenu.enable = val
        if self.enable and not self.visible:
            self.visible = True

    _parent = None
    _Continue = None
    _Restart = None
    _BackToMainMenu = None
    _Enable = False
    _Visible = False
    _Fon = None
