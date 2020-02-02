latitude=[]
longitude=[]
with open('/home/pawan/demo_cord.txt', 'r') as f:
    data = f.readlines()
for line in data:
    line_sequence = line.split()
    lat_point, long_point =float(line_sequence[0]), float(line_sequence[1])
    latitude.append(lat_point)
    longitude.append(long_point)

print(latitude)
print(longitude)
import geopandas as gpd
from shapely.geometry import Point

geometry = [Point(xy) for xy in zip(longitude,latitude)]
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
points = gpd.GeoDataFrame(index=list(range(0,len(latitude))) , crs=crs4, geometry=geometry)
points.to_file(filename='points.shp', driver="ESRI Shapefile")