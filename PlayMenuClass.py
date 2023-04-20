from pyglet import image
from pyglet.sprite import Sprite
from ButtonClass import Button
from TextEntryWindowClass import TextEntryWindow
import Global_definitions


class PlayMenu:
    def __init__(self, parent):
        self._Back = Button(0, 0, image.load('Resources/Buttons/Back_1.png'),
                            image.load('Resources/Buttons/Back_2.png'),
                            image.load('Resources/Buttons/Back_3.png'), parent)
        self._Classic = Button(0, 0, image.load('Resources/Buttons/Classic_1.png'),
                               image.load('Resources/Buttons/Classic_2.png'),
                               image.load('Resources/Buttons/Classic_3.png'), parent)
        self._UpgradeClassic = Button(0, 0, image.load('Resources/Buttons/Upgraded_Classic_1.png'),
                                      image.load('Resources/Buttons/Upgraded_Classic_2.png'),
                                      image.load('Resources/Buttons/Upgraded_Classic_3.png'), parent)
        self._Casual = Button(0, 0, image.load('Resources/Buttons/Casual_1.png'),
                              image.load('Resources/Buttons/Casual_2.png'),
                              image.load('Resources/Buttons/Casual_2.png'), parent)
        fon = image.load('Resources/Fons/fon_for_play_menu_1.jpeg')
        self._Fon = Sprite(fon)
        self._Fon.scale_x = parent.get_size()[0] / fon.width
        self._Fon.scale_y = parent.get_size()[1] / fon.height
        target_height = parent.get_size()[1] / 10
        self._Casual.scale = target_height / self._Casual.height
        self._Classic.scale = target_height / self._Classic.height
        self._UpgradeClassic.scale = target_height / self._UpgradeClassic.height
        target_height = parent.get_size()[1] / 8
        self._Back.scale = target_height / self._Back.height
        self._Name = TextEntryWindow('Enter your name:', image.load('Resources/Buttons/panel.png'), parent)
        self._Name.label_text = Global_definitions.get_settings()[0]
        self._Name.name_label_color = (0, 0, 0, 255)
        self._Name.height = parent.get_size()[1] / 10
        self._Name.width = parent.get_size()[1] / 2
        self._Name.position = ((parent.get_size()[0] - self._Name.width) / 2, parent.get_size()[1] * 8 / 10, 0)
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
        self._UpgradeClassic._pressed_event = self.upgraded_classic_event
        parent.push_handlers(self.on_draw)
        self._parent = parent

    def back_event(self):
        self.visible = False
        Global_definitions.stage = 'open_main_menu'
        settings_ = Global_definitions.get_settings()
        settings_[0] = self._Name.label_text if self._Name.label_text != '' else 'unknown'
        Global_definitions.set_settings(settings_)

    def classic_event(self):
        self.visible = False
        Global_definitions.stage = 'open_classic_snake'
        settings_ = Global_definitions.get_settings()
        settings_[0] = self._Name.label_text if self._Name.label_text != '' else 'unknown'
        Global_definitions.set_settings(settings_)

    def upgraded_classic_event(self):
        self.visible = False
        Global_definitions.stage = 'open_upgraded_classic_snake'
        settings_ = Global_definitions.get_settings()
        settings_[0] = self._Name.label_text if self._Name.label_text != '' else 'unknown'
        Global_definitions.set_settings(settings_)

    def on_draw(self):
        if self.visible:
            self._Fon.draw()
            self._Back.draw()
            self._Classic.draw()
            self._UpgradeClassic.draw()
            self._Casual.draw()
            self._Name.draw()

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
        self._Name.visible = val
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
        self._Name.enable = val
        if self.enable and not self.visible:
            self.visible = True

    _parent = None
    _Back = None
    _Classic = None
    _UpgradeClassic = None
    _Casual = None
    _Name = None
    _Enable = False
    _Visible = False
    _Fon = None
