import xml.etree.ElementTree as ET
import os

list = os.listdir('HGC\Hole1')
print(list)
print(os.path.join('HGC\Hole1',list[3]))

def kml_splitter(directory):
    kml_file = directory
    tree = ET.parse(kml_file)
    root = tree.getroot()

    namespace = {'kml': 'http://www.opengis.net/kml/2.2'}

    coords_text = root.find(".//kml:coordinates", namespace).text.strip()

    coords = [
        (float(lat), float(lon)) for lon, lat, _ in
        (coord.split(",") for coord in coords_text.split())
    ]

    return coords
