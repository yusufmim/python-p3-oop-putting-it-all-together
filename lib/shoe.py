# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # uses the property setter
        self._color = None
        self._material = None
        self._condition = "New"

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            print("Brand must be a string")

    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size

    def set_size(self, size):
        if isinstance(size, (int, float)):
            self._size = size
        else:
            print("size must be a number")

    size = property(get_size, set_size)

    def get_color(self):
        return self._color

    def set_color(self, color):
        if isinstance(color, str):
            self._color = color
        else:
            print("color must be a string")

    color = property(get_color, set_color)

    def get_material(self):
        return self._material

    def set_material(self, material):
        if isinstance(material, str):
            self._material = material
        else:
            print("material must be a string")

    material = property(get_material, set_material)

    def get_condition(self):
        return self._condition

    def set_condition(self, condition):
        if isinstance(condition, str):
            self._condition = condition
        else:
            print("condition must be a string")

    condition = property(get_condition, set_condition)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
