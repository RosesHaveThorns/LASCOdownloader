"""
 SOHO LASCO image downloader
-----------------------------
Download all LASCO coronagraph images for a given day.
Images are downloaded to the 'download' folder in the same location as this file.

Usage:
    positional arguments:
        int                   year in yyyy format
        int                   month in mm format
        int                   day in dd format to be downloaded

    optional arguments:
        -h, --help            show this help message and exit
        -t str [str ...], --imgtype str [str ...]
                            type of image to retrieve, defaults to 2aia193, first digit denotes which LASCO coronagraph

Made with love by ROSE, March 2022
"""

from fileinput import filename
import urllib.request as urllib2
import requests
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
from progressbar import *
import argparse

# downloads to the folder 'download' in the same location as this file

lascoURL = "https://cdaw.gsfc.nasa.gov/images/soho/lasco"
imgtypes = ["2aia193", "2rdf", "2rdf_aia193rdf", "2rdf_cme", "3rdf", "3rdf_cme", "2eit"]

def getDayImgs(y, m, d, type="2aia193"):
    """
    Downloads all of one type of images for a given day from LASCO Catalog

    Args:
        y: year
        m: month
        d: day
        type: defaults to 2_aia193, options are 2aia193, 2rdf, 2rdf_aia193rdf, 2rdf_cme, 3rdf, 3rdf_cme
    """

    if (not type in imgtypes):
        print("Unexpected image type request, defaulting")
        type = "2aia193"

    dayURL = lascoURL + "/" + str(y)  + "/" + f'{m:02d}'  + "/" + f'{d:02d}'
    
    # get image adresses
    page = requests.get(dayURL)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('a')
    print("Reading all imgs at: " + dayURL)
    print("Looking for image type lasc" + type)

    todownload = []

    for a in soup.find_all('a', href=True):
        search = type + ".png"
        if (search in a.text):
            todownload.append(dayURL + "/" + a.text)
        
    if (len(todownload) == 0):
        print("\nWARNING - No images found for this image type")
    else:
        print("Found " + str(len(todownload)) + " images, begining downloads")

    # download images

    for i in todownload:
        getImg(i)


def getImg(url):
    """
    Dowloads a single image from the web with a console progress bar

    Args:
        url: web url of image to be downloaded
    """
    file_name = "download/" + url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.get("Content-Length"))

    file_size_dl = 0
    block_sz = 8192
    start_progress(url)
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        progress(file_size_dl * 100. / file_size)

    end_progress()
    f.close()

if(__name__ == "__main__"):
    parser = argparse.ArgumentParser(description="Download all LASCO coronagraph images for a given day")
    parser.add_argument(
        'year', metavar='int', type=int, choices=range(9999),
         nargs='+', help='year in yyyy format')

    parser.add_argument(
        'month', metavar='int', type=int, choices=range(12),
         nargs='+', help='month in mm format')

    parser.add_argument(
        'day', metavar='int', type=int, choices=range(31),
         nargs='+', help='day in dd format to be downloaded')

    parser.add_argument(
        '-t', '--imgtype', metavar='str', type=str, choices=imgtypes,
         default="2aia193", const="2aia193", nargs='?', help='type of image to retrieve, defaults to 2aia193, first digit denotes which LASCO coronagraph')

    args = parser.parse_args()

    getDayImgs(args.year[0], args.month[0], args.day[0], type=args.imgtype)