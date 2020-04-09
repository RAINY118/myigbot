from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import tqdm
class Insta123456`1234:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.Base_Url = "https://www.facebook.com/"
    def Close(self):
        self.driver.close()
    def Login(self):
        self.driver.get(self.Base_Url)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(self.password)

        self.driver.find_elements_by_xpath('//*[@id="u_0_b"]')[0].click()

        #self.driver.find_elements_by_xpath("//button[contains(text(),'Not Now')]")[0].click()
        print(" ==== Your Get Login ====")
    def nav_user(self,user):
        self.driver.get(f"{self.Base_Url}{user}")
        time.sleep(3)

    def follow_user(self,user):
        self.nav_user(user)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")[0].click()

    def unfollow_user(self,user):
        self.nav_user(user)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Following')]")[0].click()
        time.sleep(1)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Unfollow')]")[0].click()

    def davidbeckham(self,user):
        self.nav_user(user)

        self.driver.find_elements_by_xpath("//*[text()=' following']")[0].click()
        mybutton =self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")[0]
        mybutton.click()

f = open("top.txt", "r")
mylist =[]
for data in f:
    mylist.append(data)

Myig = Insta("billy_warchag","Billkyz131")
Myig.Login()
for i in mylist:
    time.sleep(1)
    print(f"=== your ger follow = {i}")
    Myig.follow_user(i)
