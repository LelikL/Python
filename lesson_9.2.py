class Road:

    # attribute object
    def __init__(self, length, width):
        self._length = length
        self._width = width

    # method
    def calc_mass(self, mass_1=25, depth=5):
        mass = (self._length * self._width * mass_1 * depth)/1000
        return mass

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width


road_1 = Road(5000, 20)
print(f'мвсса асфальта (в тоннах) для дороги длиной = {road_1.length} м и шириной = {road_1.width} м составит {road_1.calc_mass()} т')
