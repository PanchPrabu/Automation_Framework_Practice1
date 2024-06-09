import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser",action ="store", default="chrome")

@pytest.fixture(scope="class")
def test_setup(request):
    browser=request.config.getoption("--browser")
    if browser == 'chrome':
        driver =webdriver.Chrome()
    elif browser =='edge':
        driver= webdriver.ChromiumEdge()
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")
