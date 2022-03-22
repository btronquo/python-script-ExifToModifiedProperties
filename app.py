# This program was made to correct a bad behavior of Infomaniak kDrive for photo wich consist to order the photo by modified date instead of looking for exif informations
# It will copy the date from the exif created date and put it in the 'modified to:' field of properties

import os, time
# we use the lib exif
from exif import Image

# The name of the directory that you have files in
dirname = 'input/'

# Only the specified type files
ext = ('.jpg', '.jpeg', '.JPG', '.JPEG')

# for each file in the directory
for filename in os.listdir(dirname):
    if filename.endswith(ext):

        # get the time on the exif
        with open(dirname + filename, 'rb') as image_file:
            my_image = Image(image_file)

        # Convert the exif data to a timestamp
        timestampToPut = time.mktime(time.strptime(my_image.datetime_original, '%Y:%m:%d %H:%M:%S'))
        # on firt tests I found that the timestamps was minus 1 hours. I didn't figure out why yet
        # so here the quick fix
        timestampToPut2 = timestampToPut - 3600000.0

        # set the date into the field "modified to"
        os.utime(dirname + filename,(timestampToPut, timestampToPut))

        print('processed: ' + filename)
        
    else:
        continue

print ("Finished. Enjoy !")
