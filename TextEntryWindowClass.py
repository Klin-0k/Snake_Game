from pyglet.sprite import Sprite
from pyglet import text
from pyglet.window import key
from pyglet.window import mouse
from pyglet import clock


class TextEntryWindow:
    def __init__(self, name, image, parent):
        self._fon = Sprite(image)
        self._name_label = text.Label(name, font_size=self._fon.height * 5 / 12,
                                      color=(255, 0, 0, 255),
                                      x=(self._fon.position[0] + self._fon.width / 2),
                                      y=(self._fon.position[1] + self._fon.height * 3 / 2),
                                      anchor_x='center',
                                      anchor_y='center')
        self._text_label = text.Label('',
                                      font_size=self._fon.height * 11 / 24,
                                      color=(0, 0, 0, 255),
                                      x=(self._fon.position[0] + self._fon.width / 2),
                                      y=(self._fon.position[1] + self._fon.height / 2),
                                      anchor_x='center',
                                      anchor_y='center')
        parent.push_handlers(self, self.on_mouse_press, self._key)
        clock.schedule_interval(self.update, 1 / 10)
        self._parent = parent

    def on_mouse_press(self, x, y, button, modifiers):
        if self.enable and button == mouse.LEFT:
            if self.check_collision(x, y):
                self._has_focus = True
            else:
                self._has_focus = False

    def on_text(self, input_text):
        if self.enable and self._has_focus and self._text_label.content_width < self._fon.width * 9 / 10:
            self._text_label.text += input_text

    def on_key_press(self, symbol, modifiers):
        if self.enable and self._has_focus:
            if symbol == key.BACKSPACE:
                self._text_label.text = self._text_label.text[:-1]
            elif symbol == key.ENTER:
                self._has_focus = False

    def update(self, dt):
        if self.enable and self._has_focus and self._key[key.BACKSPACE]:
            self._text_label.text = self._text_label.text[:-1]

    def check_collision(self, x, y):
        return self._fon.x <= x <= self._fon.x + self._fon.width and self._fon.y <= y <= self._fon.y + self._fon.height

    def draw(self):
        if self.visible:
            self._fon.draw()
            self._name_label.draw()
            self._text_label.draw()

    @property
    def name_label_text(self):
        return self._name_label.text

    @name_label_text.setter
    def name_label_text(self, val):
        self._name_label.text = val

    @property
    def label_text(self):
        return self._text_label.text

    @label_text.setter
    def label_text(self, val):
        self._text_label.text = val

    @property
    def name_label_color(self):
        return self._name_label.color

    @name_label_color.setter
    def name_label_color(self, val):
        self._name_label.color = val

    @property
    def label_color(self):
        return self._text_label.color

    @label_color.setter
    def label_color(self, val):
        self._text_label.color = val

    @property
    def height(self):
        return self._fon.height

    @height.setter
    def height(self, val):
        self._fon.scale_y *= val / self._fon.height
        self.position = self.position
        self._name_label.font_size = self._fon.height * 5 / 12
        self._text_label.font_size = self._fon.height * 11 / 24

    @property
    def width(self):
        return self._fon.width

    @width.setter
    def width(self, val):
        self._fon.scale_x *= val / self._fon.width
        self.position = self.position

    @property
    def position(self):
        return self._fon.position

    @position.setter
    def position(self, val):
        self._fon.position = val
        self._name_label.x = self._fon.position[0] + self._fon.width / 2
        self._name_label.y = self._fon.position[1] + self._fon.height * 3 / 2
        self._text_label.x = self._fon.position[0] + self._fon.width / 2
        self._text_label.y = self._fon.position[1] + self._fon.height / 2

    @property
    def visible(self):
        return self._Visible

    @visible.setter
    def visible(self, val: bool):
        self._Visible = val
        self._parent.clear()
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

    _parent = None
    _fon = None
    _name_label = None
    _text_label = None
    _has_focus = False
    _Enable = False
    _Visible = False
    _key = key.KeyStateHandler()
