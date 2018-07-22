
try:
    import time
    import pyautogui
    from pathlib import Path
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait    
    import socket
    import pickle

except ImportError:
    raise ImportError("Pyautogui or selenium not installed")
finally:
    class automation:
        @staticmethod
        def is_connected():
            try:
                # connect to the host -- tells us if the host is actually
                # reachable
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                pass
            return False

        def __init__(self):
            self.username=None
            self.password=None
            self.semester=None
            self.month=None
            self.year=None
            self.date=None
    
        def saveData(self):
            with open('user_data.pkl', 'wb') as output:
                pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)

        @staticmethod
        def loadData_file():
            f=open("user_data.pkl","rb")
            obj = pickle.load(f)
            return obj


        def loadData(self,uname,passwd,evenOrodd,sem,year):
            self.username=uname
            self.password=passwd
            self.year=year
            self.semester=sem
            if(evenOrodd=="Even Semester"):
                self.month="January"
                self.date="ctl00_ContentPlaceHolder1_wdcFromDate_DrpPnl1_DP_CAL_ID_1_d1"  # ID to click on 1
            else:
                self.month="August"
                self.date="ctl00_ContentPlaceHolder1_wdcFromDate_DrpPnl1_DP_CAL_ID_1_d3"  # ID to click on 1
            # automation.OpenURL(self)
            automation.saveData(self)
        def findTheEdgeDriver(self):
            try:
                DriverFile = Path("MicrosoftWebDriver.exe") # Find the Edge Driver
                return True
            except Exception as ex:
                print("Unable to find the Edge Driver") # Edge driver not found
                return False
        def OpenURL(self):
            # ----------------------- Login Start -----------------------------------

            br = webdriver.Edge(executable_path=r"MicrosoftWebDriver.exe") # Object of the Driver
            
            br.get('https://nucleus.niituniversity.in/') # URL of the Unoversity's ERP portal
            
            email = br.find_element_by_id('SchSel_txtUserName') # Find the Username field
            
            email.send_keys(self.username) # Enter the username 
            
            pas = br.find_element_by_id('SchSel_txtPassword') # Find the Username field
            
            pas.send_keys(self.password) # Enter the Password
            
            # submit = br.find_element_by_id('SchSel_btnLogin') # Find the Submit button
            
            # To bypass the security to run script directly random clicks at different places 
            pyautogui.click(80,80) 
            pyautogui.click(50,80)
            pyautogui.click(30,80)
            # ---End----
            
            time.sleep(1) # Time to update the onChnage() script on the website 
            
            br.execute_script("document.getElementById('SchSel_btnLogin').click()") # JS to click the submit Button

            # -----------------------------  End Login --------------------------------------------

            # -----------------------------  Attendance Page --------------------------------------
            # time.sleep(3)
            br.get('https://nucleus.niituniversity.in/WebApp/StudParentDashBoard/Attendance.aspx')  # Redirect to the Attendance page

            time.sleep(1)
            br.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlSession']/option[text()='"+self.year+"']").click() # Select the year from the Drop down Menu
            
            time.sleep(1) # Time to update the onChnage() script on the website 
            print(self.semester)
            br.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlPattern']/option[text()='"+str(self.semester)+"']").click() # Select semester from the Drop down Menu
            
            time.sleep(1) # Time to update the onChnage() script on the website 
            
            br.find_element_by_id('ctl00_ContentPlaceHolder1_wdcFromDate_img').click()  # Open the Date picker menu
            
            time.sleep(1) # Time to update the onChnage() script on the website 
            
            br.find_element_by_xpath("//select[@id='ctl00_ContentPlaceHolder1_wdcFromDate_DrpPnl1_DP_CAL_ID_1_504']/option[text()='"+self.month+"']").click() # Select the month from the Drop down Menu
            
            time.sleep(1) # Time to update the onChnage() script on the website 
            
            br.find_element_by_id(self.date).click()  # Select the date from the Date picker Menu
            
            time.sleep(1) # Time to update the onChnage() script on the website 
            
            # br.find_element_by_id('ctl00_ContentPlaceHolder1_Button1').click() # Submit the details 
            # find the customer table
            # table = br.find_element_by_xpath("//div[@id='ctl00_ContentPlaceHolder1_wdcFromDate_DrpPnl1']/table")

            # # find the row
            # br.execute_script('document.getElementById("ctl00_ContentPlaceHolder1_wdcFromDate_input").value = "01-Jan-2018"')
            # print("JS ")

            # pyautogui.click(80,80) 
            # pyautogui.click(20,80)
            # pyautogui.click(30,80)

            br.find_element_by_id('ctl00_ContentPlaceHolder1_Button1').click()

