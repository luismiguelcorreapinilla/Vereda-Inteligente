from config import *
from data_loader import cargar_geojson
from html.page_builder import construir_html

def main():

    gdf, geojson = cargar_geojson(RUTA_GEOJSON)

    construir_html(
        geojson,
        RUTA_LOGO,
        RUTA_HTML
    )

    print("VISOR CENSO GENERADO")

if __name__ == "__main__":
    main()
