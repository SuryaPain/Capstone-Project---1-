from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Orange:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)

        sleep(3)
# Maximizing the window
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def DeletePIM(self):
        self.boot()
        sleep(3)
# Logging into the website
        username = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username.send_keys("Admin")
        password = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password.send_keys("admin123")
        loginbutton = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        loginbutton.click()
        sleep(3)
# Clicking on PIM module
        PIM = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        PIM.click()
        sleep(3)
# Passing employee name to search bar
        emp_name=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        emp_name.send_keys("Rathnavel Pandian")
        sleep(5)
        search=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
        search.click()
        sleep(5)
# Finding and deleting
        delete=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[9]/div/button[1]')
        sleep(5)
        delete.click()
        sleep(5)
# Confirming the deletion
        confirmdelete=self.driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
        confirmdelete.click()
        sleep(5)
        print("Deleted successfully !!!")
# Passing URL into the class Orange
obj = Orange("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# Deleting PIM
obj.DeletePIM()