import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SPRING_AHEAD_URL = 'https://my.springahead.com/go/Account/Logon'
COPY_BUTTON='Copy Previous'
OK_BUTTON="/html/body/div[6]/div[2]/div[2]/input"
SUBMIT_BUTTON='//*[@id="submitall"]'
DEFAULT_DATE=time.strftime('%m/%d/%Y', time.localtime(time.time()))
DEFAULT_HOURS={'m': 8, 't': 8, 'w': 8, 'r': 8, 'f': 8}
VERIFICATION_SECONDS=30

class Client:
    def __init__(self, config):
        self.driver = webdriver.Chrome()
        self.config = config

    def copy_last_week(self, date = DEFAULT_DATE):
        self.__setup(date)

        self.driver.find_element(By.LINK_TEXT, COPY_BUTTON).click()
        self.driver.find_element(By.XPATH, OK_BUTTON).click()
        self.driver.find_element(By.XPATH, SUBMIT_BUTTON).click()

        self.__teardown()

    def submit_week(self, date = DEFAULT_DATE, hours =  DEFAULT_HOURS):
        self.__setup(date)

        for key, value in hours.items():
            self.add_hours(key, value)
        self.driver.find_element(By.XPATH, SUBMIT_BUTTON).click()

        self.__teardown()

    def add_hours(self, day, number):
        fields = {
                'm': '//*[@id="timelines"]/tr[1]/td[4]/input',
                't': '//*[@id="timelines"]/tr[1]/td[5]/input',
                'w': '//*[@id="timelines"]/tr[1]/td[6]/input',
                'r': '//*[@id="timelines"]/tr[1]/td[7]/input',
                'f': '//*[@id="timelines"]/tr[1]/td[8]/input'
        }
        self.driver.find_element(By.XPATH, fields[day]).send_keys(number)

    def login(self):
        self.driver.get(SPRING_AHEAD_URL)

        company_login = self.driver.find_element(By.NAME, 'CompanyLogin')
        company_login.send_keys(self.config["COMPANY"])

        username = self.driver.find_element(By.NAME, 'UserName')
        username.send_keys(self.config["USERNAME"])

        password = self.driver.find_element(By.NAME, 'Password')
        password.send_keys(self.config["PASSWORD"])

        submit = self.driver.find_element(By.ID, 'submit')
        submit.click()

    def open_calendar(self):
        calendar = self.driver.find_element(By.LINK_TEXT, "Time")
        calendar.click()

    def open_timecard(self, date):
        params = self.__get_params()
        url = self.__timecard_url(params["userid"], date)
        self.driver.get(url)

    def __setup(self, date):
        self.login()
        self.open_calendar()
        self.open_timecard(date)

    def __teardown(self):
        time.sleep(VERIFICATION_SECONDS)
        self.driver.quit()

    def __get_params(self):
        url = self.driver.current_url
        _params = url.split('?')[1]
        params = { p.split('=')[0]: p.split('=')[1] for p in [p for p in _params.split('&')][1:]}
        return params

    def __timecard_url(self, userid, date):
        return f'https://my.springahead.com/vt/go?Timecard&tokenid=vte&userid={userid}&startDate={date}'
