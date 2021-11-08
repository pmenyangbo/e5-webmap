# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import folium
CONSTANT = "html/map/file/Data.html"
if __name__ == '__main__':
    map1 = folium.Map(location=(35.61, -82.44), zoom_start=50)
    map1.save('Data/map1.html')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
