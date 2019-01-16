import os
import csv


def search_files():
    # file_list = os.listdir(r'/Volumes/Public/Shared Pictures/')
    os.chdir(r'/Users/dcasanova/Desktop/')
    path = r'/Volumes/silvana'

    images_list = []

    for subdir, dirs, files in os.walk(path):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith((".png", ".jpg", ".jpeg")):
                images_list.append(filepath)
                if filepath.endswith((".mp4.jpeg", ".MPG.jpeg")):
                    images_list.remove(filepath)

    with open('/Users/dcasanova/Desktop/lista_silvana.csv', 'w', encoding='utf-8') as myfile:
        wr = csv.writer(myfile, dialect='excel', quoting=csv.QUOTE_ALL)
        for image_file in images_list:
            wr.writerow([image_file])
    # return images_list


# def write_csv( image_list ):





search_files()
# write_csv(search_files())
