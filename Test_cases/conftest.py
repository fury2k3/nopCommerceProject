import pytest
from selenium import webdriver
#lahne isir el configuration mte3 les browsers ...
from pytest_metadata.plugin import metadata_key

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",help="Specify the browser: chrome or firefox or edge")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



@pytest.fixture()
def setup_driver(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser =="firefox":
        driver = webdriver.Firefox()
    elif browser =="edge":
        driver = webdriver.Edge()
    else:
         raise ValueError("unsupported browser")

    return driver

#*******for pytest html reports ***********
#****Hook for adding environment info in html reports
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'Ecommerce Project, nopcommerce'
    config.stash[metadata_key]['Test Module Name'] = 'Test_Admin_Login'
    config.stash[metadata_key]['Tester Name'] = 'Issaoui Mohamed Aziz'
#******Hook for deleting/modifying environment info in html reports

pytest.hookimpl(optionalhook=True)

def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
