import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt

#create pandas dataframe from lon and lat values of South American Countries
df = pd.DataFrame({'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
     'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
     'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
     'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})
#pandas runs indexing as a dctionary. Observe the nested lists within the dictionary format. The Keys are City, Country, Lat, and Long
#Their values are within the nested lists. Each entry in the list is a new row in the index and the Keys are columns

#in order to create a plottable Geometry field we need to conver these coordinates into a shapely function. 
#Shapely is a package dependent to Geopandas and we will use the "points_from_xy()" program to conver the pandas lat and long into a shapely column

gdf = gp.GeoDataFrame(df, geometry=gp.points_from_xy(df.Longitude, df.Latitude))

#print header (first 5 rows)

print(gdf.head())

#now call in the geodatalayers available through geopandas and overlay the point lat-lon coordinates over top. 
#use matplotlib.pyplot to do this 

world = gp.read_file(gp.datasets.get_path('naturalearth_lowres')) #pull map of world (low res) to code

# We restrict to South America.
ax = world[world.continent == 'South America'].plot(
    color='white', edgecolor='black')

# We can now plot our ``GeoDataFrame``.
gdf.plot(ax=ax, color='red')

plt.show()