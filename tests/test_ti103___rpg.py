#!/usr/bin/env python

"""Tests for `ti103___rpg` package."""

import pytest

from ti103___rpg import ti103___rpg


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_factorielle():

    assert ti103___rpg.factorielle(5) == 120
    assert False #si la condition est vrais ne fait rien si elle est fausse il s arrete immediatement et met une allarme
