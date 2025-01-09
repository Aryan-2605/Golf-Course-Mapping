import xml.etree.ElementTree as ET


kml_file = ''
tree = ET.parse(kml_file)
root = tree.getroot()

namespace = {'kml': 'http://www.opengis.net/kml/2.2'}

coords_text = root.find(".//kml:coordinates", namespace).text.strip()

coords = [
    (float(lat), float(lon)) for lon, lat, _ in
    (coord.split(",") for coord in coords_text.split())
    ]

print(coords)

