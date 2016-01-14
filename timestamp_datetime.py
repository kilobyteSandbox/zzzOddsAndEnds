#! python3

# timestamp_datetime.py
# Creates a timestamp in the format _yyyymmdd_hhmmss, and copies it to the clipboard.


import pyperclip
import time


pyperclip.copy(time.strftime("_%Y%m%d_%H%M%S"))