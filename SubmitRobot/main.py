'''
Created on 2022年3月23日

@author: ning_lin
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random
import config as conf
from get_chalendar import workday_flag

class FillOutRobot():
    def OpenChrome(self):
        self.driver = webdriver.Chrome(executable_path = conf.chrome_path)


    def LogIn(self):
        '''
        找到輸入框並進行登入
        輸入完成後提交表單
        sleep 3 秒避免網頁尚未加載就進行下一步
        '''
        self.driver.get(conf.target_url)
        user_id = self.driver.find_element_by_id("textUserId")
        user_id.send_keys(conf.user_id)
        user_pwd = self.driver.find_element_by_id("textPassword")
        user_pwd.send_keys(conf.user_pwd)
        self.driver.find_element_by_xpath("//*[@id='buttonLogin']").click()
    
        print('login successfully!')
        time.sleep(3)


    def FillOutTheForm(self):
        '''
        選擇下拉式選單選項
        清除原有欄位值重新填入
        提交表單後關閉所有視窗
        driver.close() - closes the browser active window.
        driver.quit() - closes all browser windows and ends driver's session/process.
        '''
        status = 'statusA'
        cell_selected = Select(self.driver.find_element_by_id('SelectedList'))
        cell_selected.select_by_value('N')
        self.driver.find_element_by_id('TextCell').clear()
        cell_text = self.driver.find_element_by_id('TextCell')
        cell_text.send_keys(status)
        self.driver.find_element_by_xpath("//*[@id='buttonSubmit']").click()
        self.driver.quit()
        print('fill out the form successfully!')


    def main(self):
        self.OpenChrome()
        self.LogIn()
        self.FillOutTheForm()

if __name__ == '__main__':
    time.sleep(random.randint(0, 100))
    FillOutRobot().main()