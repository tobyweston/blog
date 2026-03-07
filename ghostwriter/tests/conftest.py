"""Pytest configuration for the ghostwriter test suite.

Globally patches openai.OpenAI so that any test that accidentally tries to
instantiate the real client will fail immediately with a clear error, rather
than making a live API call (which costs money and requires a key).
"""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture(autouse=True, scope="session")
def block_openai_client():
    """Raise if any code under test tries to create a real OpenAI client."""

    def _raise(*args, **kwargs):
        raise RuntimeError(
            "openai.OpenAI was instantiated during a test — this would make a "
            "real API call. Patch the client or the function under test instead."
        )

    with patch("openai.OpenAI", side_effect=_raise):
        yield

