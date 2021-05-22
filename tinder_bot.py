from selenium import webdriver
from time import sleep
from secrets import username, password
from random import randint


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    

    def login(self):
        self.driver.get('https://tinder.com') 

        sleep(2)


        btn_connexion = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        btn_connexion.click()

        sleep(2)

   
        btn_fb = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
        btn_fb.click()

        sleep(2)

        
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        sleep(2)

        btn_accept = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]') 
        btn_accept.click()

        sleep(2)

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        sleep(2)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)


        sleep(3)

        login_btn = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        login_btn.click()

        sleep(6)

        self.driver.switch_to_window(base_window)

        popup_1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        sleep(2)
        popup_2 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

        sleep(4)


    def like(self):
        like_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        sleep(1)
        while True:

            if (randint(0,10)<7):

                try:
                    self.like()
                except Exception:
                    try:
                        self.close_popup()
                    except Exception:
                        try:
                            self.close_popup2()
                        except Exception:    
                            self.close_match()

            else :
                try:
                    self.dislike()
                except Exception:
                    try:
                        self.close_popup()
                    except Exception:
                        try:
                            self.close_popup2()
                        except Exception:    
                            self.close_match()



    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="q930268116"]/div/div/button[2]')
        popup_3.click()

    def close_popup2(self):
       popup_4 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]')
       popup_4.click()
/html/body/div[2]/div/div/div[3]/button[1]
    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.login()
sleep(1)
bot.auto_swipe()
