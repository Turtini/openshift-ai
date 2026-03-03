from __future__ import annotations
from datetime import datetime
from turtini_sphinx_theme import get_theme_paths

project = "OpenShift AI"
author = "Turtini LLC"
copyright = f"{datetime.utcnow().year}, Turtini LLC"

extensions = ["myst_parser"]

source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
root_doc = "index"

html_theme = "sphinx_rtd_theme"
_paths = get_theme_paths()
templates_path = [_paths["templates"]]
html_static_path = [_paths["static"]]
html_css_files = ["turtini.css"]
