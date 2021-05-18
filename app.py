def get_file_xml(path_file): # Con esta función vamos a validar que exista algún archivo dentro de la carpeta xml.
    import os
    from get_xml import download_xml

    files = os.listdir(path_file) # In the variable, an array of length is obtained in how many files it finds in the directory.   

    if len(files) == 0: # If the length is equal to zero, it must return the value of false to indicate that there is no file.
        return download_xml(False)
    elif len(files) > 0: # 
        for f in files:
            valor = f.endswith(".xml")
            if valor:
                return download_xml(True)
            else:
                return download_xml(False)
               
            

if __name__ == "__main__":
    
    
    path_file = "/home/santiago/Projects/VisionAPI/xml/"
    get_file_xml(path_file)
