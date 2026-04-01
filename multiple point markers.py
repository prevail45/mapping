import folium
map=folium.Map(location=[38.58,-99.09], zoom_start=6, tile_layer="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

map.add_child(folium.Marker(location=[38.2,-99.1], popup="I AM AMERIGO", icon=folium.Icon(color="green")))
map.add_child(folium.Marker(location=[37.2,-97.1], popup="I AM AMERIGO", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("map.html")