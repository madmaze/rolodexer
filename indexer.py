#!/usr/bin/env python
import Image
import PythonMagick
from pytesseract import image_to_string
import glob
import os
import argparse
import time

def main(args):
    raw_key_words={}
    for f in glob.glob(os.path.join(args.input_dir,"*.pdf")):
        print "Loading..",f
        s_time = time.time()
        PMimg = PythonMagick.Image()
        PMimg.density("500")
        
        PMimg.read(f)
        PMimg.depth = 8
        #PMimg.magick = "RGB"
        
        PMimg.write("temp.jpg")
        img = Image.open("temp.jpg")
        raw_key_words[f] = image_to_string(img, "eng")
        print "done. parse time:",time.time()-s_time
    return raw_key_words

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Indexes a folder")
    parser.add_argument("-i","--inputDir",dest="input_dir", default="./test", help="Directory to index")
    args = parser.parse_args()
    main(args)
