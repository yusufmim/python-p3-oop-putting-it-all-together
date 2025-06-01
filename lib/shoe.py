# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.color = None
        self.material = None
        self.condition = "New"

    def get_brand(self):
        return self._brand

    def set_brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            raise TypeError("Brand must be a string")

    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size

    def set_size(self, value):
        if isinstance(value, (int, float)):
            self._size = value
        else:
            raise TypeError("size must be a number")

    size = property(get_size, set_size)

    def get_color(self):
        return self._color

    def set_color(self, value):
        if isinstance(value, str):
            self._color = value
        else:
            raise TypeError("color must be a string")

    color = property(get_color, set_color)

    def get_material(self):
        return self._material

    def set_material(self, value):
        if isinstance(value, str):
            self._material = value
        else:
            raise TypeError("material must be a string")

    material = property(get_material, set_material)

    def get_condition(self):
        return self._condition

    def set_condition(self, value):
        if isinstance(value, str):
            self._condition = value
        else:
            raise TypeError("condition must be a string")

    condition = property(get_condition, set_condition)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
