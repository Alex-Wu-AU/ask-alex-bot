"""Pytest configuration ensuring project root is on sys.path.

Prevents ModuleNotFoundError for 'app' when tests are run with a
system Python or without proper working directory context.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))