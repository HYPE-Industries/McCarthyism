# McCarthyism.py - combining multiple sub-directories, removing duplicate images, and converting to JPEG
# Designed for AIDA Weapon Detection Software training process
# Copyright (C) HYPE Industries Military Defense Division - All Rights Reserved (HYPE-MMD) <hype-industries.com>
# redistribution allowed under the MIT LICENSE
# Written by Evan Sellers <sellers.evan@hype-industries.com>, November 2019

import os
import imagehash
from PIL import Image, ImageMath
import imagehash
dataset_name = "AIDA_DS_" #name appended to the front of every file
diff_allowence = 5; # difference between each image; 0 = none; 2 = small; 5 = med; 20 = large

# Change Directory
if os.path.isdir( "datasets" ) == False:
    os.mkdir( "datasets" );
os.chdir( "datasets" );

# make output foler
if os.path.isdir( "output" ) == False:
    os.mkdir( "output" );

i = 0; #total images
s = 0; #saved images
hash_list = []; #hashed images
for dirpath, dirnames, filenames in os.walk( os.getcwd() ):
    for filename in [f for f in filenames]:
        file = os.path.join( dirpath, filename );

        if( os.path.isfile( file ) and file.lower().endswith( ( '.jfif' ) ) == False and dirpath != os.path.join( os.getcwd(), "output" ) ):
            i = i + 1;
            print( str( s ) + " of " + str( i ) + " : " + file );
            img = Image.open( file );

            # Convert Image Modes
            if img.mode in ('RGBA', 'LA'):
                background = Image.new(img.mode[:-1], img.size, "#000")
                background.paste(img, img.split()[-1])
                img = background
            elif img.mode == 'P':
                img = img.convert( "RGB" );

            # Check for Duplicated Images
            hash = imagehash.average_hash( img );
            _exists = False;
            for _h in hash_list:
                if abs( hash - _h ) <= diff_allowence:
                    _exists = True;

            if not _exists:
                hash_list.append( hash );
                s = s + 1;

                # attempt to rescale images
                # if img.width > 1028 or img.height > 1028:
                #     if img.height > img.width:
                #         factor = 1028 / img.height;
                #     else:
                #         factor =1028 / img.width;
                #     img = img.resize( ( int( img.width * factor ), int( img.height * factor ) ) );

                img.save( "output/" + dataset_name + str(s) + ".jpg", "JPEG", quality=60 ); # save images to output

            img.close(); # close image

# wrappup
print( "Total Images Passed: " + str( s ) );
print( "Lost Images        : " + str( i - s ) );
