#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color, material):
        self.brand = brand
        self.size = size
        self.color = color
        self.material = material

    def get_size(self):
        return self._size

    def set_size(self, value):
        if isinstance(value, (int, float)):
            self._size = value
        else:
            print("size must be a number")

    size = property(get_size, set_size)

    def get_material(self):
        return self._material

    def set_material(self, value):
        self._material = value

    material = property(get_material, set_material)

    def cobble(self):
        print("Your shoe is as good as new!")
