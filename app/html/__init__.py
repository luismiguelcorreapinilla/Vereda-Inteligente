"""
HTML generation package for Vereda Inteligente.

GeoSpatial Intelligence Lab
"""

from .template import HTML_TEMPLATE
from .styles import STYLES
from .javascript import JAVASCRIPT
from .page_builder import build_html

__all__ = [
    "HTML_TEMPLATE",
    "STYLES",
    "JAVASCRIPT",
    "build_html",
]
