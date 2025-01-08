import folium


class Hole:
    def __init__(self, number, par):
        self.number = number
        self.par = par
        self.centre = []
        self.fairway = []
        self.treeline = []
        self.bunker = []
        self.zone = []
        self.teebox = []
        self.green = []

    def add_fairway(self, coordinates):
        for item in coordinates:
            self.fairway.append(item)

    def add_treeline(self, coordinates):
        for item in coordinates:
            self.treeline.append(item)

    def add_bunker(self, coordinates):
        for item in coordinates:
            self.bunker.append(item)

    def add_zone(self, coordinates):
        self.zone.append(coordinates)

    def add_teebox(self, coordinates):
        for item in coordinates:
            self.teebox.append(item)


    def add_green(self, coordinates):
        for item in coordinates:
            self.green.append(item)

    def add_centre(self, coordinate1, coordinate2):
        self.centre.append(coordinate1)
        self.centre.append(coordinate2)

    def print_map(self):
        hole = folium.Map(location=[self.centre[0], self.centre[1]], zoom_start=18)
        folium.Polygon(
            locations=self.zone,
            color='blue',
            fill = True,
            fill_opacity=0.5,
            popup="Zone"
        ).add_to(hole)
        for item in self.fairway:
            folium.Polygon(
                locations=item,
                color='green',
                fill=True,
                fill_opacity=0.5,
                popup="Fairway"
            ).add_to(hole)
        for item in self.green:
            folium.Polygon(
                locations=item,
                color='lightgreen',
                fill=True,
                fill_opacity=0.5,
                popup="Green"
            ).add_to(hole)
        for item in self.bunker:
            folium.Polygon(
                locations=item,
                color='yellow',
                fill=True,
                fill_opacity=0.5,
                popup="Bunker"
            ).add_to(hole)
        for item in self.treeline:
            folium.Polygon(
                locations=item,
                fill_color='forestgreen',
                fill=True,
                fill_opacity=0.5,
                popup="Tree Line",
                color='brown'
            ).add_to(hole)
        for item in self.teebox:
            folium.Polygon(
                locations=item,
                color='darkgreen',
                fill=True,
                fill_opacity=0.5,
                popup="Tee Box",
            ).add_to(hole)

        hole.save(str(self.number) + '.html')


    def __repr__(self):
        return f"Hole(number={self.number}, par={self.par}, zones={len(self.fairway)})"
