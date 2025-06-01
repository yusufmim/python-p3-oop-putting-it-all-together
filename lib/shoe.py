

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        

    def get_brand(self):
        return self._brand

    def set_brand(self, value):
        self._brand = value

    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size

    def set_size(self, value):
        if type(value) in (int, float):
            self._size = value
        else:
            print("size must be a number")

    size = property(get_size, set_size)

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value

    color = property(get_color, set_color)

    def get_material(self):
        return self._material

    def set_material(self, value):
        self._material = value

    material = property(get_material, set_material)

    def get_condition(self):
        return self._condition

    def set_condition(self, value):
        self._condition = value

    condition = property(get_condition, set_condition)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
