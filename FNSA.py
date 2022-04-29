import requests
import pprint
import pytest
import allure
import time
import allure


#@pytest.mark.parametrize("test_input",["Ukraine", "Spain", "Contry name", "1251251"])
#def test_get_req(test_input):
 #   base_url = "https://corona.lmao.ninja/v2/countries/" + test_input + "?yesterday=true&strict=true"
  #  r = requests.get(base_url)
   # print("\n ------json--------")
   # print(pprint.pprint(r.json())) #sss
   # item = r.json()
   # assert r.status_code == 200

@allure.story("test_story 1 ")
@allure.severity("Major")
@allure.testcase("testrail.com")
@allure.issue("Jira task 1")
def test_succes():
    """this test successed """
    time.sleep(4)
    assert True

@allure.severity("Trivial")
@allure.testcase("testrail.com")
@allure.issue("Jira task 2")
def test_fail():
    """this test failed """
    assert False

@allure.story("test_story 2 ")
@allure.severity("Blocker")
@allure.testcase("testrail.com")
@allure.issue("Jira task 3")
def test_skip():
    """this test skiped"""
    pytest.skip('skiped reason')

@allure.severity("Low")
@allure.testcase("testrail.com")
@allure.issue("Jira task 4")
def test_broken():
    raise Exception('broken')

@allure.severity("Trivial")
@allure.testcase("testrail.com")
@allure.issue("Jira task 2")
def test_fail():
    """this test failed """
    assert False

@allure.story("test_story 1 ")
@allure.severity("Major")
@allure.testcase("testrail.com")
@allure.issue("Jira task 1")
def test_succes():
    """this test successed """
    time.sleep(4)
    assert True

