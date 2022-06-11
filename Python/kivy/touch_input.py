from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:

            Color(1, 0, 0, .5, mode='rgba')
            self.line = Line(points=(0,0))
            print(self.line.points)
            self.rect = Rectangle(pos=(100, 0), size=(50, 50))
            Color(1, 1, 0, .5, mode='rgba')
            self.rect = Rectangle(pos=(300, 200), size=(80, 50))

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        self.rect.pos = touch.pos
        # print("Mouse Down", touch)

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        self.line.points.append(int(touch.pos[0]))
        self.line.points.append(int(touch.pos[1]))
        #print("Mouse Move", touch)

    def on_touch_up(self, touch):
        with self.canvas:
            p = tuple(self.line.points)
            print(f"Angegebene Punkte: {p}")
            Line(points=p)
        # print("Mouse Up", touch)


class TouchApp(App):
    def build(self):
        return Touch()


if __name__ == '__main__':
    TouchApp().run()
