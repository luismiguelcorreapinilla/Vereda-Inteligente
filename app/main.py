"""
Vereda Inteligente

Main application.

GeoSpatial Intelligence Lab
"""

import webbrowser

from config import *
from data_loader import load_geojson

from html.page_builder import build_html


def main():

    gdf, geojson = load_geojson(GEOJSON_FILE)

    build_html(
        geojson=geojson,
        logo_path=LOGO_FILE,
        output_file=HTML_OUTPUT,
    )

    print("Interactive census generated.")

    webbrowser.open("file://" + HTML_OUTPUT)


if __name__ == "__main__":
    main()
