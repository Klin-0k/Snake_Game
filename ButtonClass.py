from pyglet.sprite import Sprite


class Button(Sprite):
    def __init__(self, x, y, image1, image2, image3, parent):
        self._p1 = image1
        self._p2 = image2
        self._p3 = image3
        super().__init__(image1, x=x, y=y)
        parent.push_handlers(self, self.on_mouse_press, self.on_mouse_release, self.on_mouse_motion)
        self._parent = parent

    def on_mouse_press(self, x, y, button, modifiers):
        if self.enable:
            if self.check_collision(x, y):
                self._pressed = True
                self.assign(self._p3)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.enable:
            if self._pressed:
                if not self._under_mouse:
                    self.assign(self._p1)
                else:
                    self.assign(self._p2)
                    if self._pressed_event is not None:
                        self._pressed_event()
                if self is not None:
                    self._pressed = False

    def on_mouse_motion(self, x, y, dx, dy):
        if self.enable:
            if self._under_mouse and self.check_collision(x, y):
                if self._pressed:
                    self.assign(self._p3)
                else:
                    self.assign(self._p2)
            if self._under_mouse and not self.check_collision(x, y):
                if not self._pressed:
                    self.assign(self._p1)
                self._under_mouse = False
            if not self._under_mouse and self.check_collision(x, y):
                self._under_mouse = True
                self.assign(self._p2)

    def check_collision(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def assign(self, image):
        self.image = image

    def draw(self):
        if self.visible:
            super().draw()

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
    _p1 = None
    _p2 = None
    _p3 = None
    _under_mouse = False
    _pressed = False
    _pressed_event = None
    _Enable = False
    _Visible = False
