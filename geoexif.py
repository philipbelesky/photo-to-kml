#!/usr/bin/env python
import argparse

from exifread import process_file

from parsers import extract_gps
from utils import create_kml
from writers import write_overlay_node, write_camera_node, write_view_volume_node


# Arguments
description = "Convert geo-tagged photographs with EXIF data to a KML " \
              "PhotoOverlay."
parser = argparse.ArgumentParser(description=description)

parser.add_argument("filenames", type=argparse.FileType('rb'),
                    nargs='+', # Gather multiple CLI args into a list
                    help="The file path of the photo to parse")

parser.add_argument("--name", type=str, default="Photo Overlay", dest="name",
                    help="Name of the generated KML file")

parser.add_argument("--read-altitude", type=bool, default=False,
                    dest="read_altitude",
                    help="Use the altitude coordinates as specified by the " \
                         "photo's geotags (typically 0 as not recorded).")

parser.add_argument("--default-altitude", type=float, default=5.0,
                    dest="default_altitude",
                    help="Specifies the altitude to mark the overlays with " \
                         "(If not reading the altitude co-ordinates)")

args = parser.parse_args()


def add_photo_to_overlay(kml, photo_file, index, altitude):
    """Adds the specified photo to the KML file to be exported"""

    unique_id = "photo-" + str(index)
    exif_info = process_file(photo_file)
    coordinates = extract_gps(exif_info)
    if coordinates is None:
        print("File %s has no GPS Coordinates" % photo_file.name)
        return

    kml, overlay = write_overlay_node(kml, photo_file.name, unique_id)
    kml, overlay = write_camera_node(kml, overlay, exif_info, coordinates, altitude)
    kml, overlay = write_view_volume_node(kml, overlay, exif_info)

    e_point = kml.createElement('point')
    e_coordinates = kml.createElement('coordinates')
    e_coordinates.appendChild(kml.createTextNode('%s,%s,%s' %(coordinates[1],
                                                              coordinates[0],
                                                              coordinates[2])))
    e_point.appendChild(e_coordinates)
    overlay.appendChild(e_point)
    document = kml.getElementsByTagName('Document')[0]
    document.appendChild(overlay)


def main():
    kml_out = create_kml()

    if args.read_altitude:
        altitude = None # Don't specify and override
    else:
        altitude = args.default_altitude

    for i, file in enumerate(args.filenames):
        add_photo_to_overlay(kml_out, file, i, altitude)

    kml_name = args.name + ".kml"
    kml = open(kml_name, 'wb')
    kml_contents = kml_out.toprettyxml('  ', newl='\n', encoding='utf-8')
    kml.write(kml_contents)


if __name__ == '__main__':
    main()
