"""
Configuration settings for Vereda Inteligente.

GeoSpatial Intelligence Lab
"""

import os
import sys

# =====================================================
# APPLICATION
# =====================================================

APP_NAME = "Vereda Inteligente"
VERSION = "1.0.0"
AUTHOR = "GeoSpatial Intelligence Lab"

# =====================================================
# BASE DIRECTORY
# =====================================================

if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =====================================================
# FILE PATHS
# =====================================================

GEOJSON_FILE = os.path.join(
    BASE_DIR,
    "simijaca_completo.geojson"
)

HTML_OUTPUT = os.path.join(
    BASE_DIR,
    "visor_censo.html"
)

LOGO_PATH = os.path.join(
    BASE_DIR,
    "logo.png"
).replace("\\", "/")
