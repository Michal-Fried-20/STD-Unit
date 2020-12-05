#name: michal frid
#class 2
# 27/04/2020



# import relevant modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, datetime

class ClassesGML: # define new test class

    def __init__(self):
        print('test_gmail_class test started')

    def writeToLog(self, fileName, textToWrite):
        logFileObj = open(fileName, 'a')  # opening file for adding text
        timeStamp = str(datetime.datetime.now())  # builtin function from datetime module to get current time
        logFileObj.write(timeStamp + " " + textToWrite + '\n')  # writing timestamp + text + \n in order to start a new line!
        logFileObj.close()  # Closing file

    def enterEmailUserName(self):
        self.fileName = "TestLog.txt"
        self.resultsFile = "TestResults.txt"
        self.errFlag = 0
        self.writeToLog(self.fileName,'Scenario#2 : enter gmail email with incorrect username')
        self.writeToLog(self.fileName, 'starting login to gmail with valid user name')
        self.writeToLog(self.resultsFile, 'Scenario#2 : enter gmail email with incorrect username')
        self.writeToLog(self.resultsFile, 'starting login to gmail with valid user name')
        try:
            self.driver = webdriver.Chrome('C:/Users/User/PycharmProjects/michal frid/draiver/chromedriver (1).exe')  # initiate chrome
            self.driver.get('http://www.gmail.com') # open browser with specific site
            time.sleep(2)
            self.driver.maximize_window()  # maximize window
            self.writeToLog(self.fileName, 'gmail home page was uploaded successfully')
        except:
            self.errFlag = 1
            self.writeToLog(self.fileName,'ERROR - error occurred during gmail home page upload')
        # locate email field and enter email
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'identifierId'))).clear()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'identifierId'))).send_keys('m12m@gmail.com')
            time.sleep(2)
            self.writeToLog(self.fileName, 'gmail address was loaded successfully')
        except:
            self.errFlag = 1
            self.writeToLog(self.fileName,'ERROR - invalid gmail address')
        # locate button_next and click it
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/span'))).click()
            time.sleep(2)
        except:
            self.errFlag = 1
            self.writeToLog(self.fileName,'ERROR - can not find next button to continue password' )
        time.sleep(5)
        # locate password field and enter password
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'password'))).clear()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'password'))).send_keys('XXXXX')
            time.sleep(3)
            self.writeToLog(self.fileName, 'gmail password was loaded successfully')
        except:
            self.errFlag = 1
            self.writeToLog(self.fileName,'ERROR - invalid password')
        # locate button_next_password and click it
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]/span'))).click()
            time.sleep(2)
        except:
            self.errFlag = 1
            self.writeToLog(self.fileName,'ERROR - can not find next button')
        self.driver.quit()
        if self.errFlag == 1:
            self.writeToLog(self.resultsFile, 'FAIL. see TestLog.txt')
        else:
            self.writeToLog(self.resultsFile, 'PASS. see TestLog.txt')




# Needed if you would like to run this plan within this file
if __name__=='__main__':
    ClassesGML().enterEmailUserName()
