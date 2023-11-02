"""Context for saving screenshot
"""
import io
import time
import turtle as t

from PIL import Image

class ScreenContext:
    """Screen context for turtle
    """
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
        """Take screenshot for created figure
        """
        eps = self._postscript()
        eps_image = Image.open(io.BytesIO(eps.encode("utf-8")))
        eps_image.load(scale=1)
        # name = f"{time.time()}_Screen"
        # eps_image.save(f"results/{name}.png")
        return eps_image
