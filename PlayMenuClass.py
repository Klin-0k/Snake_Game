from pyglet import image
from pyglet.sprite import Sprite
from ButtonClass import Button
import Global_definitions


class PlayMenu:
    def __init__(self, parent):
        self._Back = Button(0, 0, image.load('Resources/Buttons/Back_1.png'),
                            image.load('Resources/Buttons/Back_2.png'),
                            image.load('Resources/Buttons/Back_3.png'), parent)
        self._Classic = Button(0, 0, image.load('Resources/Buttons/Classic_1.png'),
                               image.load('Resources/Buttons/Classic_2.png'),
                               image.load('Resources/Buttons/Classic_3.png'), parent)
        self._UpgradeClassic = Button(0, 0, image.load('Resources/Buttons/Upgraded_classic_1.png'),
                                      image.load('Resources/Buttons/Upgraded_classic_2.png'),
                                      image.load('Resources/Buttons/Upgraded_classic_3.png'), parent)
        self._Casual = Button(0, 0, image.load('Resources/Buttons/Casual_1.png'),
                              image.load('Resources/Buttons/Casual_2.png'),
                              image.load('Resources/Buttons/Casual_2.png'), parent)
        fon = image.load('Resources/fon_for_play_menu_1.jpeg')
        self._Fon = Sprite(fon)
        self._Fon.scale_x = parent.get_size()[0] / fon.width
        self._Fon.scale_y = parent.get_size()[1] / fon.height
        target_height = parent.get_size()[0] / 10
        target_width = target_height * self._Casual.width / self._Casual.height
        self._Casual.scale_x = target_width / self._Casual.width
        self._Casual.scale_y = target_height / self._Casual.height
        target_width = target_height * self._Classic.width / self._Classic.height
        self._Classic.scale_x = target_width / self._Classic.width
        self._Classic.scale_y = target_height / self._Classic.height
        target_width = target_height * self._UpgradeClassic.width / self._UpgradeClassic.height
        self._UpgradeClassic.scale_x = target_width / self._UpgradeClassic.width
        self._UpgradeClassic.scale_y = target_height / self._UpgradeClassic.height
        target_height = parent.get_size()[0] / 8
        target_width = target_height * self._Back.width / self._Back.height
        self._Back.scale_x = target_width / self._Back.width
        self._Back.scale_y = target_height / self._Back.height
        free_space = (parent.get_size()[0] - (
                self._Casual.width + self._Classic.width + self._UpgradeClassic.width)) / 4
        self._Classic.position = (free_space, (parent.get_size()[1] - self._Classic.height) / 2, 0)
        self._UpgradeClassic.position = (self._Classic.position[0] + self._Classic.width + free_space,
                                         (parent.get_size()[1] - self._UpgradeClassic.height) / 2, 0)
        self._Casual.position = (self._UpgradeClassic.position[0] + self._UpgradeClassic.width + free_space,
                                 (parent.get_size()[1] - self._Casual.height) / 2, 0)
        self._Back.position = ((parent.get_size()[0] - self._Back.width) / 2, parent.get_size()[1] / 10, 0)
        self._Back._pressed_event = self.back_event
        self._Classic._pressed_event = self.classic_event
        parent.push_handlers(self.on_draw)
        self._parent = parent

    def back_event(self):
        self.visible = False
        Global_definitions.stage = 'open_main_menu'

    def classic_event(self):
        self.visible = False
        Global_definitions.stage = 'open_classic_snake'

    def on_draw(self):
        if self.visible:
            self._Fon.draw()
            self._Back.draw()
            self._Classic.draw()
            self._UpgradeClassic.draw()
            self._Casual.draw()

    @property
    def visible(self):
        return self._Visible

    @visible.setter
    def visible(self, val: bool):
        self._Visible = val
        self._Back.visible = val
        self._Classic.visible = val
        self._UpgradeClassic.visible = val
        self._Casual.visible = val
        # self._parent.clear()
        if self.enable and not self.visible:
            self.enable = False

    @property
    def enable(self):
        return self._Enable

    @enable.setter
    def enable(self, val: bool):
        self._Enable = val
        self._Back.enable = val
        self._Classic.enable = val
        self._UpgradeClassic.enable = val
        self._Casual.enable = val
        if self.enable and not self.visible:
            self.visible = True

    _parent = None
    _Back = None
    _Classic = None
    _UpgradeClassic = None
    _Casual = None
    _Enable = False
    _Visible = False
    _Fon = None
