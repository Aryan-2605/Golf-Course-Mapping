from Hole import *
class GolfCourse:
    def __init__(self, name, description, numholes, par):
        self.name = name
        self.description = description
        self.numholes = numholes
        self.par = par
        self.holes = []

    def add_hole(self, number, par):
        new_hole = Hole(number, par)
        self.holes.append(new_hole)
        return new_hole


