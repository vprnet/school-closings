#!/usr/bin/python
import json
import requests
import gspread
from PIL import Image
from PIL import ImageOps
import urllib
import os
import markdown
from bs4 import BeautifulSoup as Soup
from datetime import datetime
from cStringIO import StringIO
from config import NPR_API_KEY, ABSOLUTE_PATH
from oauth2client.client import SignedJwtAssertionCredentials

def convert_date(timestamp):
    """Converts API timestamp to publication-ready dateline"""

    day = timestamp[5:7]
    month = datetime.strptime(timestamp[8:11], '%b').strftime('%B')
    year = timestamp[12:16]
    date = month + ' ' + day + ", " + year
    return date
