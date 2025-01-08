import xml.etree.ElementTree as ET

kml_file = "HGC/Hole1/Tee Box.kml"
tree = ET.parse(kml_file)
root = tree.getroot()

namespace = {'kml': 'http://www.opengis.net/kml/2.2'}

# Extract coordinates text
coords_text = root.find(".//kml:coordinates", namespace).text.strip()

# Process coordinates into a list of (latitude, longitude) tuples
coords = [
    (float(lat), float(lon)) for lon, lat, _ in
    (coord.split(",") for coord in coords_text.split())
]

# Print the parsed coordinates
print(coords)