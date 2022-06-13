from appium import webdriver
from testdata import TestConfig


class Driver:
    """
    Class contains of a driver settings
    """

    def __init__(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "Tecno BB2",
            "appPackage": "com.google.android.keep",
            "appActivity": "com.google.android.apps.keep.ui.activities.BrowseActivity",
            "url": "http://127.0.0.1:4723",
            "noReset": True,
            "launchTimeout": "50000",
            "automationName": "UiAutomator2",
            "autoDismissAlerts": True
        }

        self.instance = webdriver.Remote(TestConfig.local_host, desired_cap)
        self.instance.implicitly_wait(15)
