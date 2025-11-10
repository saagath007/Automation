import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UpayaLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_login(self):
        driver = self.driver
        wait = self.wait        
        driver.get("https://qa-aircargo.upaya.com.np/login")
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "email")))
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))

        email_field.send_keys("saagath.shrestha@upaya.com.np")
        password_field.send_keys("password123")
        login_button.click()

    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main()
