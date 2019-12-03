# McCarthyism
Designed for AIDA WDS Deep Leaning Training Wheel Protocol<br>
Copyright (C) HYPE Industries Military Defense Division - All Rights Reserved (HYPE-MMD) <hype-industries.com><br>
redistribution allowed under the MIT LICENSE<br>
Written by Evan Sellers <sellers.evan@hype-industries.com>, November 2019><br>


## What is McCarthyism?
McCarthyism is a simple python script that allows you to take multiple folders of images and combined them into one. While it does this it, also converts them all to jpg, with a consistent name and won't transfer duplicates of a picture.
 - merge folders
 - convert to `.jpg`
 - consistent naming conventions
 - prevent duplicated images

## Why would you ever use McCarthyism?
We designed McCarthyism, because when training our deep learning system, Training Wheels, for AIDA's Weapon Detection Software, we had hundreds and thousands of images. These image were all in different folders, with different formats, with similar names, and we had duplicated images sometimes. McCarthyism allows us to feed it multiple folder of random images, and it sorts it all into one folder, in one format, without duplicates.

## How to use?
Place a folder full of images in the `datasets` folder. You can't just place images in the `datasets` folder, the images must be inside a sub-directory, within `datasets`. McCarthyism, supports `PPM`, `PNG`, `JPEG`, `GIF`, `TIFF` and `BMP` image formats. It will just not move the image if it is an unsupported image. Once you place the folders of images in the `datasets`, just `cd` to the directory and run the python script with `python McCarthyism.py`.

## Config Options
