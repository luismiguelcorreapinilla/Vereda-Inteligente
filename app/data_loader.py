print("Cargando GeoJSON...")

gdf = gpd.read_file(...)

geojson = gdf.to_json()
