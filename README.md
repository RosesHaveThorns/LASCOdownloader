# LASCOdownloader
Download all LASCO coronagraph images for a given day

Images are collected from the LASCO CME Catalog dataset. Thanks to the Heliophysics Science Division at
NASA Goddard Space Flight Center for providing this data to the public.

Created by Rose Awen Brindle, 2022. Released under GNU GENERAL PUBLIC LICENSE Version 3.

For more information: contactme@rose-brindle.dev

## Usage
Call LASCO_imgdownload.py from the command line using the following command line arguments. Downloaded data is placed in the 'download' folder at LASCO_imgdownload.py's location. NOTE you may need to create this folder yourself before use.

Positional arguments:
- int                   year in yyyy format
- int                   month in mm format
- int                   day in dd format to be downloaded

Optional arguments:
- -h, --help            show this help message and exit
- -t str [str ...], --imgtype str [str ...]
                        type of image to retrieve, defaults to 2aia193, first digit denotes which LASCO coronagraph

### image types
- 2aia193: Instrument C2, 
- 2rdf: Instrument C2, 
- 2rdf_aia193rdf: Instrument C2, 
- 2rdf_cme: Instrument C2, 
- 3rdf: Instrument C3, 
- 3rdf_cme: Instrument C3, 