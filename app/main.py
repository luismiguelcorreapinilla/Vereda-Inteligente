"""
Main application for Vereda Inteligente.

GeoSpatial Intelligence Lab
"""

import webbrowser

from config import (
    HTML_OUTPUT,
    LOGO_PATH,
)

from data_loader import load_geojson

from html import build_html


def main():
    """
    Main application workflow.
    """

    print("=" * 50)
    print("VEREDA INTELIGENTE")
    print("GeoSpatial Intelligence Lab")
    print("=" * 50)

    # ----------------------------------
    # Load GeoJSON
    # ----------------------------------

    print("Loading cadastral data...")

    gdf, geojson_data = load_geojson()

    print(f"Parcels loaded: {len(gdf)}")

    # ----------------------------------
    # Build HTML
    # ----------------------------------

    print("Building HTML viewer...")

    html = build_html(
        geojson_data=geojson_data,
        logo_path=LOGO_PATH
    )

    # ----------------------------------
    # Save HTML
    # ----------------------------------

    with open(
        HTML_OUTPUT,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)

    print("Viewer generated successfully.")

    # ----------------------------------
    # Open Browser
    # ----------------------------------

    webbrowser.open(
        "file://" + HTML_OUTPUT
    )

    print("Viewer opened.")


if __name__ == "__main__":
    main()
