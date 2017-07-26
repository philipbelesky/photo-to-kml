# Photo to KML

A command line tool for converting photographs with geo-tags to a series of KML photo overlays suitable for opening in Google Earth. A work in progress.

## Attribution Notice

Most of the code here is heavily derivate of Mano Mark's code samples posted on the [Keyhole Markup Language documentation](https://developers.google.com/kml/articles/geotagsimple) page but has been adapted for Python 3.X with a few enhancements. From what I can tell his code is not hosted anywhere else (it was only provided as snippets) so this project replicates it from scratch rather than as a fork. All python files should be considered as modifications of the original source snippets.

## Setup

Developed on Python 3.6. Probably works with earlier versions of Python 3.

1. Create virtual environment (optional)
2. Install dependencies via pip:

        pip install -r requirements.txt

## Usage

Basic use:

    python geoexif.py <list of files>

Parsing multiple files:

    python geoexif.py /Path/to/file/A.jpg /Path/to/file/B.jpg

Parsing all files within a folder:

    python geoexif.py /Path/to/folder/*.jpg

## Flags

Filename for the resulting file (defaults to "Photo Overlay):

    --name <string>

Whether to assign altitude data from the EXIF tags. Most phones don't produce this an instead write "0" which can lead to photos clipped into the Google Earth terrain. Thus this defaults to false.

    --read-altitude <true/false>

## Roadmap

- The 'click to fly into photo' links only work in the sidebar
- Package up properly
- Document properly
- Find a better name

## License

This code (and the original code form which it is based) use the [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0).
