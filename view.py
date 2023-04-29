import pygame

class CharacterView:

    def __init__(self, model, screen):
        self._model = model
        if model.SPRITE_NAMES_MOVING is None:
            self._sprites = [pygame.image.load(model.SPRITE_NAME_IDLE), pygame.image.load(model.SPRITE_NAME_IDLE)]
        else:
            self._sprites = [pygame.transform.flip(pygame.image.load(x), True, False) for x in model.SPRITE_NAMES_MOVING]

        self._sprite_index = 0
        self._counter = 0
        self._screen = screen

    @property
    def rect(self):
        rect = self.sprite.get_rect()
        rect.x = self._model.x
        rect.y = self._model.y
        return rect

    @property
    def sprite(self):
        self._counter += 1
        if self._counter > 20:
            self._counter = 0
            if self._sprite_index == 0:
                self._sprite_index = 1
            elif self._sprite_index == 1:
                self._sprite_index = 0
        return  self._sprites[self._sprite_index]


    def blit(self):
        self._screen.blit(self.sprite, self.rect)
    

    def touches(self, other):
        return self.rect.colliderect(other.rect)