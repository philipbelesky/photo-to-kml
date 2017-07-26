

def write_overlay_node(kml_file, file_name, file_identifier):

    photo_overlay = kml_file.createElement('PhotoOverlay')
    photo_overlay.setAttribute('id', file_identifier)

    name = kml_file.createElement('name')
    name.appendChild(kml_file.createTextNode(file_name))

    description = kml_file.createElement('description')
    cdata_description = '<a href="#%s"> Click here to fly into photo</a>' % file_identifier
    description.appendChild(kml_file.createCDATASection(cdata_description))

    photo_overlay.appendChild(name)
    photo_overlay.appendChild(description)

    icon = kml_file.createElement('Icon')
    href = kml_file.createElement('href')
    href.appendChild(kml_file.createTextNode(file_name))
    icon.appendChild(href)
    photo_overlay.appendChild(icon)

    return kml_file, photo_overlay


def write_camera_node(kml_file, photo_overlay, exif_info, coordinates):

    longitude = kml_file.createElement('longitude')
    latitude = kml_file.createElement('latitude')
    altitude = kml_file.createElement('altitude')
    tilt = kml_file.createElement('tilt')

    longitude.appendChild(kml_file.createTextNode(str(coordinates[1])))
    latitude.appendChild(kml_file.createTextNode(str(coordinates[0])))
    altitude.appendChild(kml_file.createTextNode('10'))
    tilt.appendChild(kml_file.createTextNode('90'))

    camera = kml_file.createElement('Camera')
    camera.appendChild(longitude)
    camera.appendChild(latitude)
    camera.appendChild(altitude)
    camera.appendChild(tilt)
    photo_overlay.appendChild(camera)

    return kml_file, photo_overlay


def write_view_volume_node(kml_file, photo_overlay, exif_info):

    # Determines the proportions of the image and uses them to set FOV.
    width = float(exif_info['EXIF ExifImageWidth'].printable)
    length = float(exif_info['EXIF ExifImageLength'].printable)
    lf = str(width/length * -20.0)
    rf = str(width/length * 20.0)

    viewvolume = kml_file.createElement('ViewVolume')
    leftfov = kml_file.createElement('leftFov')
    rightfov = kml_file.createElement('rightFov')
    bottomfov = kml_file.createElement('bottomFov')
    topfov = kml_file.createElement('topFov')
    near = kml_file.createElement('near')
    leftfov.appendChild(kml_file.createTextNode(lf))
    rightfov.appendChild(kml_file.createTextNode(rf))
    bottomfov.appendChild(kml_file.createTextNode('-20'))
    topfov.appendChild(kml_file.createTextNode('20'))
    near.appendChild(kml_file.createTextNode('10'))
    viewvolume.appendChild(leftfov)
    viewvolume.appendChild(rightfov)
    viewvolume.appendChild(bottomfov)
    viewvolume.appendChild(topfov)
    viewvolume.appendChild(near)

    photo_overlay.appendChild(viewvolume)

    return kml_file, photo_overlay