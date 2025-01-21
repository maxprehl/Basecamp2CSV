#! python3

from selectolax.parser import HTMLParser
from glob import glob
import re

html = b""
path = "../Basecamp-export-SapphireK12-04-12-2024/it-dr-transition-29508434/card-table-columns/cards/access-gitolite-6593844999.html"
files = glob("../Basecamp-export-SapphireK12-04-12-2024/it-dr-transition-29508434/card-table-columns/cards/*.html")
outfile = "outfile.csv"

with open(outfile, "w") as out_file:

    for file in files:
        # print("\n",file)
        id = re.search('-(\d*).html',file).group(1)
        # print(id)

        with open(file, "rb") as in_file:
            html = in_file.read()

        tree = HTMLParser(html)

        nodes = tree.css('ul.list--unbulleted.push_half--ends li span.content')
        text = ""
        for i in nodes:
            line = i.text().strip()
            line = re.sub("\n","",line)
            text += line + "\n"
        text = text.strip().replace('"','')
        # print(text)

        csvline = '"' + id + '"' + "," + '"' +  text + '"\n'

        # print(csvline)
        out_file.write(csvline)
