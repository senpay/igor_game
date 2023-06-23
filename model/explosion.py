from pgzero.actor import Actor
from pgzero.loaders import sounds

class Explosion(Actor):

    def __init__(self):
        super().__init__('explosion/img_0.png')
        self.images = [f"explosion/img_{num}.png" for num in range(35) ]
        self.image_index = 0.0
        self.pause = 60
        self.visible = False

    def show(self):
        if not self.visible:
            sounds.bang.play()
            self.visible = True
        
    def update(self):
        if self.visible:
            self.image_index += 0.3
            if int(self.image_index) >= len(self.images):
                self.image_index = 0.0
                self.visible = False
            self.image = self.images[int(self.image_index)]
        
    def draw(self):
        if self.visible:
            super().draw()