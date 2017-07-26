#!/usr/bin/env python
import argparse

# Arguments
description = "Convert geo-tagged photographs with EXIF data to a KML " \
              "PhotoOverlay."
parser = argparse.ArgumentParser(description=description)

parser.add_argument("filenames", type=argparse.FileType('rb', 0),
                    help="The file paths of the photos to parse")

args = parser.parse_args()

for file in args.filenames:
    print(file)