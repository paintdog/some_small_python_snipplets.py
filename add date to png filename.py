# works with Windows (!)
import datetime
import os

pngs = [file for file in os.listdir() if file.endswith(".png")]

for png in pngs:
    
    st = os.stat(png)
    date = datetime.datetime.fromtimestamp(st.st_ctime).date()

    if not str(date.year) in png:
        dst = png.replace(".png", " -- {}.png".format(date))
        os.rename(png, dst)
    
