#############to be run in jupyter ipython notebook
import folium
import pandas as pd
import json

zipcode_geo = r'ny_zip_shapefile_new.json'
zipcode_values = r'zip_values.json'

with open(zipcode_geo) as data_file:
    shapedata = json.load(data_file)

d={"zipcodes":["10036","10011","10022","10023","10005","10017","10280"],"values":[7,6,5,4,3,2,1]}
data_frame=pd.DataFrame(d)

#Let Folium determine the scale
map = folium.Map(location=[40.7134,74.0055], zoom_start=2)
map.choropleth(geo_data=shapedata, data=data_frame,
             columns=['zipcodes', 'values'],
             key_on='feature.properties.postalCode',
             fill_color='BuPu', fill_opacity=0.9, line_opacity=0.9,
             legend_name='Market Rank')
map
