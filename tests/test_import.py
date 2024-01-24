"""Test gitmoji-test."""

import gitmoji_test


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(gitmoji_test.__name__, str)
