import Operations
from Operations import *
import folium
import os


class GolfCourse:
    def __init__(self, name, description, numholes, par):
        self.name = name
        self.description = description
        self.numholes = numholes
        self.par = par
        self.holes = []

    def add_hole(self, number, par, directory, centerX, centerY):
        new_hole = Hole(number, par, directory, centerX, centerY)
        self.holes.append(new_hole)
        return new_hole


class Hole:
    def __init__(self, number, par, directory, centerX, centerY):
        self.number = number
        self.par = par
        self.centre = []
        self.fairway = []
        self.treeline = []
        self.bunker = []
        self.zone = []
        self.teebox = []
        self.green = []
        self.directory = directory
        self.files = os.listdir(directory)
        self.map = folium.Map(location=[centerX, centerY], zoom_start=18)

    def create_zone(self):
        for name in self.files:
            path = os.path.join(self.directory, name)
            coords = Operations.kml_splitter(path)
            if 'fairway' in name.lower():
                self.fairway.append(coords)
            elif 'tree' in name.lower():
                self.treeline.append(coords)
            elif 'bunker' in name.lower():
                self.bunker.append(coords)
            elif 'zone' in name.lower():
                self.zone.append(coords)
            elif 'teebox' in name.lower():
                self.teebox.append(coords)
            elif 'green' in name.lower():
                self.green.append(coords)
            else:
                raise ValueError(f'{name} is an invalid .kml file name')

        #print(self.fairway)
        #print(self.treeline)
        #print(self.bunker)
        #print(self.zone)
        #print(self.teebox)
        #print(self.green)

    def print_map(self):

        for item in self.zone:
            folium.Polygon(
                locations=self.zone,
                color='blue',
                fill=True,
                fill_opacity=0.5,
                popup="Zone"
            ).add_to(self.map)

        for item in self.fairway:
            folium.Polygon(
                locations=item,
                color='green',
                fill=True,
                fill_opacity=0.5,
                popup="Fairway"
            ).add_to(self.map)

        for item in self.green:
            folium.Polygon(
                locations=item,
                color='lightgreen',
                fill=True,
                fill_opacity=0.5,
                popup="Green"
            ).add_to(self.map)

        for item in self.bunker:
            folium.Polygon(
                locations=item,
                color='yellow',
                fill=True,
                fill_opacity=0.5,
                popup="Bunker"
            ).add_to(self.map)

        for item in self.treeline:
            folium.Polygon(
                locations=item,
                fill_color='forestgreen',
                fill=True,
                fill_opacity=0.5,
                popup="Tree Line",
                color='brown'
            ).add_to(self.map)

        for item in self.teebox:
            folium.Polygon(
                locations=item,
                color='darkgreen',
                fill=True,
                fill_opacity=0.5,
                popup="Tee Box",
            ).add_to(self.map)

        self.map.save(str(self.number) + '.html')

    def __repr__(self):
        return f"Hole(number={self.number}, par={self.par}, zones={len(self.fairway)})"
