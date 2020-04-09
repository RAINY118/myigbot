from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import tqdm
class Insta:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.Base_Url = "https://www.instagram.com/"
    def Login(self):
        self.driver.get(f"{self.Base_Url}accounts/login/")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()
        time.sleep(5)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Not Now')]")[0].click()
        print(" ==== Your Get Login ====")
    def nav_user(self,user):
        self.driver.get(f"{self.Base_Url}{user}")
        time.sleep(3)
    def follow_user(self,user):
        self.nav_user(user)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")[0].click()
    def unfodllow_user(self,user):
        self.nav_user(user)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Following')]")[0].click()
        time.sleep(1)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Unfollow')]")[0].click()

    def search_tag(self,hashtag):
        self.driver.get(f"{self.Base_Url}explore/tags/{hashtag}")
        print(f" ==== Your Get Searchs Tag by {hashtag} ====")

    def like_photo(self,count):
        self.driver.find_element_by_class_name('eLAPa').click() #click to show phoho
        i = 1
        while  i <= count:
            time.sleep(2)
            self.driver.find_element_by_class_name('wpO6b').click() #like button
            self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click() #nexphoto
            i += 1
            print("like" + str(i))
            x = self.driver.find_element_by_class_name('FFVAD').get_attribute("src")
            print(x)








#f = open("top.txt", "r")
#mylist =[]
#for data in f:
#    mylist.append(data)

Myig = Insta("warchag01","0959201930")
Myig.Login()

Myig.search_tag("chevrolet")
Myig.like_photo(2000)

#for i in mylist:
#    time.sleep(1)
#    print(f"=== your ger follow = {i}")
#    Myig.follow_user(i)
