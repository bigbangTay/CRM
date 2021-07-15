# Solar
# handsome
from selenium import webdriver
import unittest
from time import sleep

class FangFa (unittest.TestCase) :

    options = webdriver.ChromeOptions ()
    options.add_argument ('--ignore-certificate-errors')
    options.add_argument ('--ignore-ssl-errors')
    driver = webdriver.Chrome (chrome_options = options)

    def setUp (self) -> None :
        self.driver.get ('http://localhost:8080/crm')
        self.driver.maximize_window ()
        self.driver.implicitly_wait (5)
        self.driver.find_element_by_name ('userNum').send_keys ('admin')
        self.driver.find_element_by_name ('userPw').send_keys ('123456')
        self.driver.find_element_by_css_selector ('[type = "submit"]').submit ()

    def tearDown (self) -> None :
        sleep (2)
        self.driver.quit ()

    def find (self,*args) :
        try :
            return self.driver.find_element (*args)
        except :
            print ('定位失败')

    def click (self,*args) :
        return self.find (*args).click ()

    def submit (self,*args) :
        return self.find (*args).submit ()

    def clear (self,*args) :
        return self.find (*args).clear ()

    def sendkey (self,*args,value) :
        return self.find (*args).send_keys (value)

    def scorll (self,move) :
        # window.scrollTo (x,y)
        return self.driver.execute_script (move)

    def url (self) :
        return self.driver.current_url

    def back (self) :
        return self.driver.back ()

    def forward (self) :
        return self.driver.forward ()

    def quit (self) :
        return self.driver.quit ()

    def frame (self,value) :
        return self.driver.switch_to.frame (value)