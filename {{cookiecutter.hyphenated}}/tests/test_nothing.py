""" testing code which doesn't test anything """

import pytest


def test_nothing() -> None:
    """doesn't test anything"""
    pytest.skip("This doesn't test anything!")
