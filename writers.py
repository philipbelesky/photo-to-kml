

def write_overlay_node(kml_file, file_name, file_identifier):

    photo_overlay = kml_file.createElement('PhotoOverlay')
    photo_overlay.setAttribute('id', file_identifier)

    e_name = kml_file.createElement('name')
    e_name.appendChild(kml_file.createTextNode(file_name))

    description = kml_file.createElement('description')
    cdata_description = '<a href="#%s"> Click here to fly into photo</a>' % file_identifier
    description.appendChild(kml_file.createCDATASection(cdata_description))

    photo_overlay.appendChild(e_name)
    photo_overlay.appendChild(description)

    e_icon = kml_file.createElement('Icon')
    e_href = kml_file.createElement('href')
    e_href.appendChild(kml_file.createTextNode(file_name))
    e_icon.appendChild(e_href)
    photo_overlay.appendChild(e_icon)

    return kml_file, photo_overlay


def write_camera_node(kml_file, photo_overlay, exif_info, coordinates, altitude):

    e_longitude = kml_file.createElement('longitude')
    e_latitude = kml_file.createElement('latitude')
    e_altitude = kml_file.createElement('altitude')
    e_tilt = kml_file.createElement('tilt')

    e_longitude.appendChild(kml_file.createTextNode(str(coordinates[1])))
    e_latitude.appendChild(kml_file.createTextNode(str(coordinates[0])))

    # A None value for the altitude indicates it should be read from the exif
    if altitude is None:
        e_altitude.appendChild(kml_file.createTextNode(str(coordinates[2])))
    else:
        e_altitude.appendChild(kml_file.createTextNode(str(altitude)))

    e_tilt.appendChild(kml_file.createTextNode('90'))

    camera = kml_file.createElement('Camera')
    camera.appendChild(e_longitude)
    camera.appendChild(e_latitude)
    camera.appendChild(e_altitude)
    camera.appendChild(e_tilt)
    photo_overlay.appendChild(camera)

    return kml_file, photo_overlay


def write_view_volume_node(kml_file, photo_overlay, exif_info):

    # Determines the proportions of the image and uses them to set FOV.
    width = float(exif_info['EXIF ExifImageWidth'].printable)
    length = float(exif_info['EXIF ExifImageLength'].printable)
    lf = str(width/length * -20.0)
    rf = str(width/length * 20.0)

    e_viewvolume = kml_file.createElement('ViewVolume')
    e_leftfov = kml_file.createElement('leftFov')
    e_rightfov = kml_file.createElement('rightFov')
    e_bottomfov = kml_file.createElement('bottomFov')
    e_topfov = kml_file.createElement('topFov')
    e_near = kml_file.createElement('near')
    e_leftfov.appendChild(kml_file.createTextNode(lf))
    e_rightfov.appendChild(kml_file.createTextNode(rf))
    e_bottomfov.appendChild(kml_file.createTextNode('-20'))
    e_topfov.appendChild(kml_file.createTextNode('20'))
    e_near.appendChild(kml_file.createTextNode('10'))
    e_viewvolume.appendChild(e_leftfov)
    e_viewvolume.appendChild(e_rightfov)
    e_viewvolume.appendChild(e_bottomfov)
    e_viewvolume.appendChild(e_topfov)
    e_viewvolume.appendChild(e_near)

    photo_overlay.appendChild(e_viewvolume)

    return kml_file, photo_overlay
