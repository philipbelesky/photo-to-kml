#!/usr/bin/env python
import argparse

from exifread import process_file

# Arguments
description = "Convert geo-tagged photographs with EXIF data to a KML " \
              "PhotoOverlay."
parser = argparse.ArgumentParser(description=description)

parser.add_argument("filenames", type=argparse.FileType('rb'),
                    nargs='+', # Gather multiple CLI args into a list
                    help="The file path of the photo to parse")

args = parser.parse_args()

for file in args.filenames:

    exif = process_file(file)
    print(exif)