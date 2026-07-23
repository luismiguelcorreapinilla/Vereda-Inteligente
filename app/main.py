"""
Main application for Vereda Inteligente.

GeoSpatial Intelligence Lab
"""

import webbrowser

from config import (
    APP_NAME,
    VERSION,
    GEOJSON_FILE,
    HTML_OUTPUT,
    LOGO_PATH,
)

from data_loader import load_geojson

from html import build_html


def main():
    """
    Main application workflow.
    """

    print("=" * 60)
    print(APP_NAME)
    print(f"Version {VERSION}")
    print("GeoSpatial Intelligence Lab")
    print("=" * 60)

    # =====================================================
    # LOAD GEOJSON
    # =====================================================

    gdf, geojson_data = load_geojson(GEOJSON_FILE)

    # =====================================================
    # BUILD HTML
    # =====================================================

    print("Building HTML viewer...")

    html = build_html(
        geojson_data=geojson_data,
        logo_path=LOGO_PATH
    )

    # =====================================================
    # SAVE HTML
    # =====================================================

    with open(
        HTML_OUTPUT,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)

    print("HTML viewer generated successfully.")

    # =====================================================
    # OPEN BROWSER
    # =====================================================

    print("Opening browser...")

    webbrowser.open(
        "file://" + HTML_OUTPUT
    )

    print("Application finished successfully.")


if __name__ == "__main__":
    main()
