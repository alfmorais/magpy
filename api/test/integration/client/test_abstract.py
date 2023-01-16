from abc import ABC

from api.integrations.abstract_method import PyPiAbstract


def test_abstract_method_pypi():
    assert issubclass(PyPiAbstract, ABC)
