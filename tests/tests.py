import pytest
import requests
import json


def test_first_test():
    url = 'http://localhost:8000/employee'
    res = requests.get(url=url)
    a = json.loads(res.text)
    print(res)
    print(a)


def test_second_test():
    assert 1==2


def test_third_test():
    assert 1==1


def blabla():
    return 7

