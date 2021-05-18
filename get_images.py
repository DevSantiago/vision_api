def download_images(images_urls, path):
    import urllib.request
    import io
    from get_labels import detect_labels


    i = 0
    for image in images_urls:
        filename = 'tennis_' + str(i) + '.jpg'
        urllib.request.urlretrieve(image, path+filename)
        i += 1
        if i == 10:
            break

    return detect_labels(path)
