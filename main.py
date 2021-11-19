# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import folium
CONSTANT = "html/map/file/Data.html"
    #map1.save('Data/map1.html')
if __name__ == '__main__':
    map1 = folium.Map(location=(35.61, -82.44), zoom_start=50)
    fv = open("data/volcanoes.tsv", "r")
    dialect= csv.Sniffer().sniff(fv.read())
    fv.seek(0)
    reader = csv.DictReader(fv, dialect=dialect)
    rows = []
    filename = 'map1.html'
    for row in reader:
        if row['Latitude']!= None and row['Longitude']!= None and row['Status']!= 'Historical' and row['Volcano Name'] !='unnamed' and '?' not in row['Type']:
            rows.append(row)
            print(f"{row['Volcano Name']}{row['Latitude']}{row['Longitude']}")
    for each_row in rows:
        icon_yellow = folium.Icon(color="white")
        marker = folium.Marker(location =(each_row['Latitude'], each_row['Longitude']), popup = each_row['Volcano Name'], icon = icon_yellow)
        map1.add_child(marker)
    map1.save('Data/'+filename)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
