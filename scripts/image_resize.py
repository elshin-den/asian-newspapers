# -*- coding: utf-8 -*-

from wand.image import Image
import os

IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg']

for (dirpath, dirnames, filenames) in os.walk('/home/elshin/web/asian-newspapers'):
    for name in filenames:
	filename = os.path.join(dirpath, name)
	if name.split('.')[-1] in IMAGE_EXTENSIONS and os.stat(filename).st_size >= 500000:
            print filename, name.split('.')[-1], os.stat(filename).st_size
	    with Image(filename=filename) as img:
		quality = int(30000000.0 / os.stat(filename).st_size)
		img.compression_quality = quality
		img.save(filename=filename)
		print quality
	    print filename, name.split('.')[-1], os.stat(filename).st_size
	    print '\n'
