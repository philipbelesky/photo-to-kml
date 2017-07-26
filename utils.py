import xml.dom.minidom


def create_kml():
    """Sets up the KML file to be exported."""

    kml_doc = xml.dom.minidom.Document()
    kml_element = kml_doc.createElementNS('http://www.opengis.net/kml/2.2', 'kml')
    kml_element.setAttribute('xmlns', 'http://www.opengis.net/kml/2.2')
    kml_element = kml_doc.appendChild(kml_element)
    document = kml_doc.createElement('Document')
    kml_element.appendChild(document)
    return kml_doc


def dms_to_decimal(degree_num, degree_den, minute_num, minute_den,
                   second_num, second_den):

    degree = float(degree_num)/float(degree_den)
    minute = float(minute_num)/float(minute_den)/60
    second = float(second_num)/float(second_den)/3600
    return degree + minute + second