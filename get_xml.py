def handle_xml(xml_name):
    import xml.etree.ElementTree as ET
    from get_images import download_images

    tree = ET.parse("/home/santiago/Projects/VisionAPI/xml/" + xml_name)
    root = tree.getroot()

    images_urls = []

    for child in root.findall('{http://www.w3.org/2005/Atom}entry'):
        image = child.find('{http://base.google.com/ns/1.0}image_link')
        images_urls.append(image.text)

    path_img = "/home/santiago/Projects/VisionAPI/resources/images/tennis/"

    return download_images(images_urls, path_img)

def download_xml(validation_file):
    import wget
    import io, os

    path_file = "/home/santiago/Projects/VisionAPI/xml/tennis.xml"
    
    if validation_file is False:
        url = 'https://www.tennis.com.co/XMLData/adbid_facebook_junio.xml'
        file_xml = wget.download(url, path_file)
        f = io.open(path_file, 'rb')
        xml_name = os.path.basename(f.name)

        return handle_xml(xml_name)
    else:
        f = io.open(path_file, 'rb')
        xml_name = os.path.basename(f.name)
        
        return handle_xml(xml_name)
