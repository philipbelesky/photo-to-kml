from utils import dms_to_decimal


def extract_gps(exif_info):

    try:
        lat_dms = exif_info['GPS GPSLatitude'].values
        long_dms = exif_info['GPS GPSLongitude'].values
    except KeyError:
        return None

    latitude = dms_to_decimal(lat_dms[0].num, lat_dms[0].den,
                              lat_dms[1].num, lat_dms[1].den,
                              lat_dms[2].num, lat_dms[2].den)
    longitude = dms_to_decimal(long_dms[0].num, long_dms[0].den,
                               long_dms[1].num, long_dms[1].den,
                               long_dms[2].num, long_dms[2].den)
    if exif_info['GPS GPSLatitudeRef'].printable == 'S':
        latitude *= -1
    if exif_info['GPS GPSLongitudeRef'].printable == 'W':
        longitude *= -1
    altitude = None

    try:
        alt = exif_info['GPS GPSAltitude'].values[0]
        altitude = alt.num/alt.den
        if exif_info['GPS GPSAltitudeRef'] == 1:
            altitude *= -1
    except KeyError:
        altitude = 0

    return latitude, longitude, altitude