from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

TWITTER_LOGIN_PAGE="https://twitter.com/i/flow/login"
# enter below your email id
TWITTER_MAIL="your mailId or username"
SPEED_TEST_LINK= "https://www.speedtest.net/"
# please check your chrome browser version and download chrome driver for that specific version and paste it in the below given directory
CHROME_DRIVER_PATH= "C:\Development\chromedriver.exe"
# enter your password
TWITTER_PW="password"
# Enter the internet service provider promised upload speed
PROMISED_UPLOAD_SPEED=100
# Enter the internet service provider promised download speed
PROMISED_DOWNLOAD_SPEED=100
ISP="@rairtelxstream "

class  InternetSpeedTwitterBot:
    def __init__(self):
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.up=0
        self.down=0
    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_LINK)
        self.go_button=self.driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go_button.click()
        time.sleep(40)
        self.down=self.driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.down)
        self.up= self.driver.find_element(by=By.XPATH,value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(self.up)
    def tweet(self):
        self.driver.get(TWITTER_LOGIN_PAGE)
        time.sleep(5)
        self.mail_field = self.driver.find_element(by=By.XPATH,
                                         value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        self.mail_field.click()
        self.mail_field.send_keys(TWITTER_MAIL)
        time.sleep(5)
        self.next_button = self.driver.find_element(by=By.XPATH,
                                          value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span')
        self.next_button.click()
        time.sleep(5)
        self.password_field = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.password_field.send_keys(TWITTER_PW)
        self.login_button = self.driver.find_element(by=By.XPATH,
                                           value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        self.login_button.click()
        time.sleep(5)
        self.tweet_field = self.driver.find_element(by=By.XPATH,
                                          value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        self.tweet_field.click()
        self.tweet_field.send_keys(f"Hello {ISP} why is my internet speed is {self.down} Down/{self.up} Up ?, When i paid for {PROMISED_DOWNLOAD_SPEED} Down/{PROMISED_UPLOAD_SPEED} Up ")
        self.tweet_button = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        self.tweet_button.click()

    def close(self):
        self.driver.quit()


bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
upload_speed=float(bot.up)
download_speed=float(bot.down)

if upload_speed<PROMISED_UPLOAD_SPEED or download_speed<PROMISED_DOWNLOAD_SPEED:
    bot.tweet()
    time.sleep(10)
    bot.close()
else:
    bot.close()





