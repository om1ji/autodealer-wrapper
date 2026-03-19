import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "autodealer"
copyright = "2025, Om1ji"
author = "Om1ji"
release = "0.0.1"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}
napoleon_google_docstring = True
napoleon_include_init_with_doc = False

templates_path = ["_templates"]
exclude_patterns = []
language = "ru"

# -- Options for HTML output -------------------------------------------------

html_theme = "alabaster"
html_static_path = ["_static"]
html_theme_options = {
    "description": "Python ORM-обёртка для базы данных АвтоДилер (Firebird)",
    "github_user": "om1ji",
    "github_repo": "autodealer-wrapper",
}
