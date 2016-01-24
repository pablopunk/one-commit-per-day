#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Pablo Varela 2016
#
# TODO: works fine on Mac/Linux,
# but sometimes wget/curl returns an empty page.
# If this happens, just run it again.
#

import os
import urlparse
import sys

downloaderURL = "http://youtubeinmp4.com/redirect.php?video="
myURL = ""
defaultFileName = "video"

if len(sys.argv) > 1:
    myURL = sys.argv[1]
else:
    print "Paste the youtube URL: ",
    myURL = raw_input()

url_data = urlparse.urlparse(myURL)
query = urlparse.parse_qs(url_data.query)
video = ""

try:
    video = query["v"][0]
except KeyError:
    print "This doesn't seem like a YouTube Vide URL :("
    exit(1)

url = downloaderURL+video

fileCount = 1
fileName = defaultFileName
currentDir = os.getcwd()
while os.path.isfile(currentDir+"/"+fileName+".mp4"):
    fileName = defaultFileName + str(fileCount)
    fileCount+=1

fileName+=".mp4"
wget = "wget %s -O %s" % (url,fileName)
curl = "curl %s -L -o %s" % (url,fileName)
download = "(%s) || (%s) " % (wget,curl)

if os.system(download):
    print "Download failed :("
    print "This script uses WGET or CURL,\nso be sure to have at least\none of those on your computer"
    exit(2)

print "Success! Video file:",fileName
