import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
SIMILAR_ACCOUNT = "NAME OF THE ACCOUNT SIMMILAR TO YOURS"
USER_NAME = "INSTAGRAM USER NAME"
PASSWORD = "YOUR INSTAGRAM PASSWORD"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get("https://www.instagram.com")

    def login(self):
        cookies = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/button[1]")
        cookies.click()
        time.sleep(3)
        login = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        login.send_keys(USER_NAME)
        password = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        saving_pass = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        saving_pass.click()

    def find_followers(self):
        search = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search.send_keys(SIMILAR_ACCOUNT)
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(3)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for i in range (10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
