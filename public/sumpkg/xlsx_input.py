import glob
import io
import os
import webbrowser
import pandas as pd
from xlsx2html import xlsx2html

file_name = 'C:/Users/suetake/Python/web3_firebase/public/sample_file/test.xlsx'


out_stream = xlsx2html(file_name, 'testout.html')
out_stream.seek(0)
webbrowser.open("testout.html")