# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#



import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))


# -- Project information -----------------------------------------------------

project = 'Control-M Python Client'
copyright = '2022, BMC Inc.'
author = 'BMC Inc.'
html_favicon = 'favicon.ico'

# The full version, including alpha/beta/rc tags
# release = '1.0.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'nbsphinx',
    'myst_parser'
    # 'sphinx_copybutton',
]
nbsphinx_allow_errors = True
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
# html_theme = "press"
# html_theme = "renku"
html_theme = "furo"
# html_theme = 'sphinxawesome_theme'
# html_theme = 'sphinx_material'
# html_theme = 'karma_sphinx_theme'
# html_theme = 'sphinx_pdj_theme'
# html_theme = 'sphinx_book_theme'
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# html_logo = 'iconbmc.png'
html_theme_options = {
    "light_css_variables": {
        "color-sidebar-background": "#F0F1F3",
        # "color-sidebar-caption-text": "white",
        # "color-sidebar-link-text--top-level": "#cccccc",
    },

    "dark_css_variables": {
        "color-sidebar-background": "#1A1C1E"
    }

}

nbsphinx_execute = 'never'