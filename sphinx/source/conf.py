# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ReDocparse'
copyright = '2023, Carl Best'
author = 'lapras'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.append(os.path.abspath("../../src"))

nitpicky = True

python_display_short_literal_types = True
python_use_unqualified_type_names = True
maximum_signature_line_length = 200

import sphinx.errors

def missing_reference(_app, _domain, node, _contnode):
    #print(node["reftarget"])
    if any([ignore in node["reftarget"] for ignore in ["ClassVar", "InitVar"]]):
        raise sphinx.errors.NoUri()

def setup(app):
    app.connect("missing-reference", missing_reference)

extensions = ["sphinx.ext.autodoc", "sphinx.ext.intersphinx"]

autodoc_type_aliases = {
    "AgentAssignment": "AgentAssignment"
}
autodoc_default_options = {
    "member-order": "bysource",
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
