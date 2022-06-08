from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("************TestCase_001_Login***************")
        self.logger.info("************test_homePageTitle started ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            self.driver.close()
            assert True
            self.logger.info("************test_homePageTitle passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTile.png")
            self.driver.close()
            self.logger.info("************test_homePageTitle Failed ***************")
            assert False

    def test_login(self, setup):
        self.logger.info("************test_login started ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************test_login passed ***************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("************test_login Failed ***************")
            assert False
