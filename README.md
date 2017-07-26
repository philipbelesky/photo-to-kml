## Introduction

Convert geo-tagged photographs to a KML overlay suitable for import into Google Earth.

## Setup

Developed on Python 3.6. Probably works with earlier versions of Python 3.

1. Create virtual environment (optional)
2. Install dependencies via pip:

    `pip install -r requirements.txt`

## Usage

Basic use:

   `python geoexif.py <list of files>`

Parsing multiple files:

   `python geoexif.py /Path/to/file/A.jpg /Path/to/file/B.jpg`

Parsing all files within a folder:

   `python geoexif.py /Path/to/folder/*.jpg`

## Flags

Filename for the resulting file (defaults to "Photo Overlay):

    `--name <string>`

Whether to assign altitude data from the EXIF tags. Most phones don't produce this an instead write "0" which can lead to photos clipped into the Google Earth terrain. Thus this defaults to false.

    `--read-altitude <true/false>`

## Attribution Notice

Most of the code here is heavily derivate of Mano Mark's code samples posted on the [Keyhole Markup Language documentation](https://developers.google.com/kml/articles/geotagsimple) page but has been adapted for Python 3.X versions with a few enhancements. From what I can tell this code is not hosted anywhere (it was only provided as snippets) so this project replicates it from scratch rather than as a fork. All python files should be considered as modifications of these source snippets.

## License

This code (and the original code form which it is based) use the [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0).
