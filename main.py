import unittest
from selenium import webdriver
import page

PATH = "C:\SeleniumDrivers\chromedriver.exe"

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.python.org/")

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

    def test_search_python(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
    
    def tearDown(self):
        self.driver.close

if __name__ == "__main__":
    unittest.main()