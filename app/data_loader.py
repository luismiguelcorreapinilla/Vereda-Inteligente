"""
GeoJSON loader.

GeoSpatial Intelligence Lab
"""

import geopandas as gpd


def load_geojson(path: str):
    """
    Load a cadastral GeoJSON file.

    Parameters
    ----------
    path : str
        Path to the GeoJSON file.

    Returns
    -------
    tuple
        (GeoDataFrame, GeoJSON string)
    """

    print("Loading cadastral GeoJSON...")

    gdf = gpd.read_file(path)

    print(f"Properties loaded: {len(gdf)}")

    geojson_data = gdf.to_json()

    return gdf, geojson_data
