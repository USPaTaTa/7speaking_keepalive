from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime


class KeepAlive:
    def __init__(self, email: str, password: str, headless: bool = True):
        self.email = email
        self.password = password
        self.headless = headless

    def login(self):
        print("Starting firefox...")
        self.options = webdriver.FirefoxOptions()
        if self.headless:
            self.options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.install_addon("./buster.xpi")
        print("Logging in...")
        self.driver.get("https://user.7speaking.com")
        self.driver.find_element(By.NAME, "username").send_keys(self.email)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/form/button"
        ).click()
        sleep(2)
        if self.driver.current_url == "https://user.7speaking.com/home":
            time_spent = self.driver.find_element(
                By.CSS_SELECTOR,
                "#root > div.LMS__globalWrapper > div > main > div.banner.home_page__banner.home_page__banner_items_3 > div.banner__dashboardWrapper > div > div:nth-child(3) > div.dashboard__moduleContent > h3",
            ).get_attribute("textContent")
            print(
                "Login successful at {}, time spent on 7speaking: {}".format(
                    datetime.now(), time_spent
                )
            )

    def logout(self):
        print("Logging out...")
        self.driver.find_element(
            By.CSS_SELECTOR,
            "#root > div.LMS__globalWrapper > div > header > div > div > div.appBar__rightContent > div.avatar-container.app_Bar__avatarContainer",
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR,
            "body > div.MuiPopover-root > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.profile__menu.MuiPaper-elevation2.MuiPaper-rounded > ul > li.MuiButtonBase-root.MuiListItem-root.MuiMenuItem-root.logout__container.MuiMenuItem-gutters.MuiListItem-gutters.MuiListItem-button",
        ).click()
        print("Logout successful at {}".format(datetime.now()))
        sleep(2)

    def __del__(self):
        self.driver.quit()
