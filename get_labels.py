def insert_db(list_label, file_name):
    from google.cloud import bigquery
    from google.oauth2 import service_account

    credentials = service_account.Credentials.from_service_account_file("/home/santiago/Projects/VisionAPI/vison--API-1cbf8599fbce.json")

    client = bigquery.Client(credentials=credentials)

    table_id = "vison-api-304615.seo_101.images"

    length_labels = len(list_label)
    quantity_labels = []
    for i in range(length_labels):
        quantity_labels.append("_"+str(i))

    attr_value = dict(zip(quantity_labels, list_label))
    rows_to_insert = [
        {
        u"image": file_name,
        u"image_attribute":
            [
                attr_value
            ], 
        }  
    ]

    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

    return ""


def translate_label(list_label, file_name, lang):
    import six
    from google.cloud import translate_v2 as translate
    from google.oauth2 import service_account

    credentials = service_account.Credentials.from_service_account_file("/home/santiago/Projects/VisionAPI/vison--API-1cbf8599fbce.json")
    translate_client = translate.Client(credentials=credentials)
    
    counter = 0
    kw_translate = []
    for label in list_label:
        result = translate_client.translate(label, target_language=lang)
        kw_translate.append(result['translatedText'])
        counter += 1
        
    insert_db(kw_translate, file_name)
    


def detect_labels(path):
    import io
    import os  
    from google.cloud import vision
    from google.oauth2 import service_account

    credentials = service_account.Credentials.from_service_account_file("/home/santiago/Projects/VisionAPI/vison--API-1cbf8599fbce.json")

    client = vision.ImageAnnotatorClient(credentials=credentials)
    files = os.listdir(path)
    counter = 0
    for file_ in files:
        image_path = path + str(files[counter])
        f = io.open(image_path, 'rb')
        file_name = os.path.basename(f.name)

        with f as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.label_detection(image=image, max_results=8)
        labels = response.label_annotations

        labels_list = []
        for label in labels:
            labels_list.append(label.description)
        lang = "es"
        translate_label(labels_list, file_name, lang)
        counter += 1

    

