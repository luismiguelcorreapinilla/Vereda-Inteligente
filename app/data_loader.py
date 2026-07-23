"""
GeoJSON loader.

GeoSpatial Intelligence Lab
"""

import geopandas as gpd


def load_geojson(path):
    """
    Load a cadastral GeoJSON file.

    Parameters
    ----------
    path : str

    Returns
    -------
    GeoDataFrame
    str
        GeoJSON serialized as string.
    """

    print("Loading cadastral GeoJSON...")

    gdf = gpd.read_file(path)

    print(f"Properties loaded: {len(gdf)}")

    geojson = gdf.to_json()

    return gdf, geojson
