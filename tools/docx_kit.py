#!/usr/bin/env python3
"""Shim. The real implementation lives in one place.

This file used to be a byte-for-byte copy of the same module in the sibling
asset repos, so a branding or layout fix applied in one repo silently missed the
others. The implementation now lives once, at

    /Users/dfreriks/Documents/SAP/sap_doc_kit/sap_docx_kit.py

and each repo keeps this shim so existing call sites (`from docx_kit import h1,
table, ...`) continue to work unchanged.

Add nothing here. Edit the shared module instead.
"""
import pathlib
import sys

_SHARED = pathlib.Path("/Users/dfreriks/Documents/SAP/sap_doc_kit")
if not (_SHARED / "sap_docx_kit.py").exists():  # fail loudly, not silently
    raise ImportError(
        f"shared docx kit not found at {_SHARED}/sap_docx_kit.py — "
        "the Word deliverables cannot be built without it"
    )
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

from sap_docx_kit import *  # noqa: F401,F403  (re-export)
from sap_docx_kit import (  # noqa: F401  explicit, so linters and IDEs resolve them
    AMBER,
    BLUE_HEX,
    GREEN,
    GREY,
    LIGHT_HEX,
    NAVY_HEX,
    RED,
    SAP_NAVY,
    SNOW_BLUE,
    body,
    bullet,
    callout,
    fixed,
    h1,
    h2,
    money,
    no_split,
    rich,
    setup_page,
    shade,
    table,
)
