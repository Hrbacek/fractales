import turtle as t
import time
from PIL import Image
from random import random
import io

class ScreenContext:
    def __init__(self):
        self.screen = t.Screen()
        self.screen.setup(height=1., width=1.)
        self.screen.tracer(0, 0)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        time.sleep(2)
        self.screen.bye()

    def _postscript(self):
        self.screen.update()
        eps = self.screen.getcanvas().postscript(colormode="color")
        return eps
    def screenshot(self):
        eps = self._postscript()
        eps_image = Image.open(io.BytesIO(eps.encode("utf-8")))
        eps_image.load(scale=1)
        name = f"{time.time()}_Screen"
        eps_image.save(f"results/{name}.png")


if __name__ == "__main__":
    with ScreenContext() as context:
        screen1 = context.screen
        print(screen1)
        t1 = t.Turtle()
        t2 = t.Turtle()
    
        screen1.bgcolor("lightgreen")
        for i in range(10):
            steps = int(random() * 100)
            angle = int(random() * 360)
            t1.right(angle)
            t1.fd(steps)
            t2.left(angle)
            t2.bk(steps)
        t1.hideturtle()
        t2.hideturtle()
        context.screenshot()
