from pyglet import image
from pyglet.sprite import Sprite
from ButtonClass import Button
from pyglet import text
import Global_definitions


class GameOverMenu:
    def __init__(self, parent):
        self._PlayAgain = Button(0, 0, image.load('Resources/Buttons/restart01.png'),
                                 image.load('Resources/Buttons/restart02.png'),
                                 image.load('Resources/Buttons/restart01.png'), parent)
        self._BackToMainMenu = Button(0, 0, image.load('Resources/Buttons/home01.png'),
                                      image.load('Resources/Buttons/home02.png'),
                                      image.load('Resources/Buttons/home03.png'), parent)
        fon = image.load('Resources/Fons/fon_for_game_over_menu1.png')
        self._Fon = Sprite(fon)
        self._Fon.scale_x = parent.get_size()[0] / 2 / fon.width
        self._Fon.scale_y = parent.get_size()[1] / 2 / fon.height
        self._Fon.position = (parent.get_size()[0] / 4, parent.get_size()[0] / 4, 0)
        target_height = self._Fon.height / 6
        target_width = target_height * self._PlayAgain.width / self._PlayAgain.height
        self._PlayAgain.scale_x = target_width / self._PlayAgain.width
        self._PlayAgain.scale_y = target_height / self._PlayAgain.height
        target_width = target_height * self._BackToMainMenu.width / self._BackToMainMenu.height
        self._BackToMainMenu.scale_x = target_width / self._BackToMainMenu.width
        self._BackToMainMenu.scale_y = target_height / self._BackToMainMenu.height
        free_space = (self._Fon.width - (
                self._PlayAgain.width + self._BackToMainMenu.width)) / 3
        self._BackToMainMenu.position = (self._Fon.position[0] + free_space, self._Fon.position[1] * 4 / 3, 0)
        self._PlayAgain.position = (
            self._BackToMainMenu.position[0] + self._BackToMainMenu.width + free_space, self._Fon.position[1] * 4 / 3,
            0)
        self.game_over_label = text.Label('Game Over!', font_size=self._Fon.height / 8, color=(255, 0, 0, 255),
                                          x=(self._Fon.position[0] + self._Fon.width / 2),
                                          y=(self._Fon.position[1] + self._Fon.height * 3 / 4),
                                          anchor_x='center',
                                          anchor_y='center')
        self.result_label = text.Label('', font_size=self._Fon.height / 12, color=(255, 215, 0, 255),
                                       x=(self._Fon.position[0] + self._Fon.width / 2),
                                       y=(self._Fon.position[1] + self._Fon.height / 2),
                                       anchor_x='center',
                                       anchor_y='center')
        self._PlayAgain._pressed_event = self.play_again_event
        self._BackToMainMenu._pressed_event = self.back_to_main_menu_event
        parent.push_handlers(self.on_draw)
        self._parent = parent

    def back_to_main_menu_event(self):
        self.visible = False
        Global_definitions.stage = 'open_main_menu'

    def play_again_event(self):
        self.visible = False
        Global_definitions.stage = 'play_again'

    def on_draw(self):
        if self.visible:
            self._Fon.draw()
            self._PlayAgain.draw()
            self._BackToMainMenu.draw()
            self.result_label.draw()
            self.game_over_label.draw()

    @property
    def visible(self):
        return self._Visible

    @visible.setter
    def visible(self, val: bool):
        self._Visible = val
        self._PlayAgain.visible = val
        self._BackToMainMenu.visible = val
        # self._parent.clear()
        if self._Enable and not self._Visible:
            self.enable = False

    @property
    def enable(self):
        return self._Enable

    @enable.setter
    def enable(self, val: bool):
        self._Enable = val
        self._PlayAgain._Enable = val
        self._BackToMainMenu._Enable = val
        if self._Enable and not self._Visible:
            self.visible = True

    _parent = None
    _PlayAgain = None
    _BackToMainMenu = None
    _Enable = False
    _Visible = False
    _Fon = None
    result_label = None
    game_over_label = None
