# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv

#import folium
CONSTANT = "html/map/file/Data.html"

    # map1 = folium.Map(location=(35.61, -82.44), zoom_start=50)
    #map1.save('Data/map1.html')
if __name__ == '__main__':
    fv = open("data/volcanoes.tsv", "r")
    dialect= csv.Sniffer().sniff(fv.read())
    fv.seek(0)
    reader = csv.DictReader(fv, dialect=dialect)
    rows = []
    for row in reader:
        rows.append(row)
    print("dude")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
