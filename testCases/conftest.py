import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        ser_obj = Service(ChromeDriverManager().install())
        ops = Options()
        ops.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=ser_obj, options=ops)

    elif browser == "firefox":
        from webdriver_manager.firefox import GeckoDriverManager
        from selenium.webdriver.firefox.service import Service
        ser_obj = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=ser_obj)
    else:
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        ser_obj = Service(ChromeDriverManager().install())
        ops = Options()
        ops.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=ser_obj, options=ops)

    return driver


def pytest_addoption(parser):  # This will get the value from CLI/Hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to the setup method
    return request.config.getoption("--browser")


## Pytest HTML Report #########

# It is the hook adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Title'] = 'Amaresh'


# It is the hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
