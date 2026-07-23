"""
Build the final HTML page for Vereda Inteligente.

GeoSpatial Intelligence Lab
"""

from .template import HTML_TEMPLATE
from .styles import STYLES
from .javascript import JAVASCRIPT


def build_html(geojson_data: str, logo_path: str) -> str:
    """
    Builds the final HTML document by combining the template,
    styles, JavaScript, GeoJSON data and logo path.

    Parameters
    ----------
    geojson_data : str
        GeoJSON converted to string.

    logo_path : str
        Absolute path to the logo image.

    Returns
    -------
    str
        Complete HTML document.
    """

    html = HTML_TEMPLATE

    # Insert CSS
    html = html.replace(
        "{{STYLES}}",
        STYLES
    )

    # Insert JavaScript
    html = html.replace(
        "{{JAVASCRIPT}}",
        JAVASCRIPT
    )

    # Insert GeoJSON
    html = html.replace(
        "__GEOJSON__",
        geojson_data
    )

    # Insert Logo
    html = html.replace(
        "__LOGO__",
        "file:///" + logo_path.replace("\\", "/")
    )

    return html
