
# Class to hold pairs of co-ordinates (x,y) in a list.

class Coordinates():

    def __init__(self):

        self.coordinates = [ ]

    def add_coord(self, new_pair):

        self.coordinates.append(new_pair)

    def get_coord(self, point):

        if((point < 0) or (point > len(self.coordinates))):
            print("Index out of range! Returning (0,0)...")
            return [0.0, 0.0]

        return self.coordinates[point]

    def get_all_coordiante(self):

        return self.coordinates

    def get_x_values(self):

        return [x for [x,y] in self.coordinates]

    def get_y_values(self):

        return [y for [x,y] in self.coordinates]
