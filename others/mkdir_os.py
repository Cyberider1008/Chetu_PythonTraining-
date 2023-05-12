#! usr/bin/python
from datetime import datetime
import os

today = datetime.now()

os.mkdir("/Desktop/chetu/" + today.strftime('%Y%m%d'))

