x = []
y = []
import csv

with open("coords.csv") as g:
    reader = csv.reader(g, delimiter=',')
    for row in reader:
        x.append(row[0])
        y.append(row[1])

        print(x)
x = [float(i) for i in x]
y = [float(i) for i in y]

import geopandas as gpd
from shapely.geometry import Point

print(x, y)
geometry = [Point(xy) for xy in zip(x, y)]
print(geometry)
# crs1 = {'init': 'epsg:4326'}         # Does NOT work
crs2 = {'proj': 'longlat', 'ellps': 'WGS84', 'datum': 'WGS84', 'no_defs': True}  # Works
# crs3 = 'EPSG:4326'       # Does NOT work
crs4 = 'GEOGCS["WGS 84",DATUM["WGS_1984",' \
       'SPHEROID["WGS 84",6378137,298.257223563,' \
       'AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],' \
       'PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],' \
       'UNIT["degree",0.01745329251994328,' \
       'AUTHORITY["EPSG","9122"]],' \
       'AUTHORITY["EPSG","4326"]]'  # Works

points = gpd.GeoDataFrame(index=list(range(0,len(x))) , crs=crs4, geometry=geometry)
points.to_file(filename='points.shp', driver="ESRI Shapefile")
print('Done')