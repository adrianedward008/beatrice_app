
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.07, 1)

class HeartWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.redraw, pos=self.redraw)

    def redraw(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(0.1, 0.1, 0.14, 1)
            for x in range(0, int(self.width), 25):
                Line(points=[x, 0, x, self.height])
            for y in range(0, int(self.height), 25):
                Line(points=[0, y, self.width, y])

            Color(1, 0.16, 0.33, 1)

            cx = self.width / 2
            cy = self.height / 2 + 60
            size = 22

            pixels = [
                (-2,-3),(-1,-3),(1,-3),(2,-3),
                (-3,-2),(-2,-2),(-1,-2),(0,-2),(1,-2),(2,-2),(3,-2),
                (-3,-1),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(3,-1),
                (-3,0),(-2,0),(-1,0),(0,0),(1,0),(2,0),(3,0),
                (-2,1),(-1,1),(0,1),(1,1),(2,1),
                (-1,2),(0,2),(1,2),
                (0,3)
            ]

            for ox, oy in pixels:
                Rectangle(
                    pos=(cx + ox*size - size/2, cy + oy*size - size/2),
                    size=(size, size)
                )

class BeatriceApp(App):
    def build(self):
        return HeartWidget()

BeatriceApp().run()
