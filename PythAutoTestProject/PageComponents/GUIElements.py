__author__ = 'admin'


from ToolsFile import Utility
from selenium import webdriver
import time

class MTGUI():


    b = webdriver.Chrome()
    #b.get('http://54.223.229.9:5202/CTPClient/app/login.html')
    # strUserLoginPageURL = 'http://54.223.229.9:5202/CTPWeb/app/login.html'
    # strUserLoginPageURL = 'https://ctp.360jincai.com/app/login.html'
    strUserLoginPageURL = 'https://ctp.360jincai.com/app/welcome.html'

    b.get(strUserLoginPageURL)

    # http://13.124.220.217:8010/Account/Login

    time.sleep(5)
    b.maximize_window()



    # def __init__(self):
    #
    #     print('==== in ====== ')
    #     b = webdriver.Chrome()
    #     b.get('http://13.124.220.217:8010/Account/Login')
    #     time.sleep(5)
    #     b.maximize_window()
    #     print('==== out ====== ')


    def txtBaiduSearch(self):
        txtBaiduSearch = MTGUI.b.find_element_by_xpath('//*[@id="kw"]')
        return txtBaiduSearch
    def btnBaiduSearch(self):
        btnBaiduSearch = MTGUI.b.find_element_by_xpath('//*[@id="su"]')
        return btnBaiduSearch
    def linkResOne(self,browser):

        linkResOne = browser.find_element_by_xpath('//*[@id="1"]')

        #linkResOne = MTGUI.b.find_element_by_xpath('//*[@id="1"]/*[contains(local-name(),"data-click")]')

        print(linkResOne.tag_name)


        return linkResOne


    def closeBrowser(self):
        MTGUI().b.close()
        return
# =========== Temp Using ========================
    def openNewTempPage():
        str_TemplPageURL = 'https://www.nypl.org/events/calendar'
        MTGUI.b.get(str_TemplPageURL)
    def cateGroup():
        grpURL = MTGUI.b.find_element_by_xpath('//*[@id="calendar-filter"]/form/div/div[4]/h5')
        return grpURL
# =========== Login Page & page elements ==========
    def switchUserLoginPage():
        str_switchUserLoginPage = 'https://ctp.360jincai.com/app/login.html'
        MTGUI.b.get(str_switchUserLoginPage)
# =========== Admin Login Page & page elements ==========
    def switchAdminPage():
        # str_AdminLoginPageURL = 'http://54.223.229.9:5202/CTPAdmin/app/login.html'
        str_AdminLoginPageURL = 'https://ctp.360jincai.com/CTPAdmin/app/login.html'


        MTGUI.b.get(str_AdminLoginPageURL)
    def txtAdminUserName():
        txtAdminUserName = MTGUI.b.find_element_by_xpath('//*[@id="username"]')
        return txtAdminUserName
    def txtAdminPwd():
        txtAdminUserName = MTGUI.b.find_element_by_xpath('//*[@id="password"]')
        return txtAdminUserName
# =========== 网站首页 及 登录 页面元素 ==========
    def linkLogin():
        # linkLogin = MTGUI.b.find_element_by_xpath('/html/body/div/ul/li/a[4]')
        linkLogin = MTGUI.b.find_element_by_xpath('//*[@id="loginStatus"]')
        return linkLogin

    def linkRegister():
        linkRegister = MTGUI.b.find_element_by_xpath('//*[@id="li_3"]/a')

        # /html/body/div[1]/div/div[2]/ul/li[6]/a
        # //*[@id="nav"]/ul/li/a[5]
        # //*[@id="LoginForm"]/div[4]/div/a
        return linkRegister

    def txtUserName():
        txtUserName = MTGUI.b.find_element_by_xpath('//*[@id="username"]')
        return txtUserName

    def txtPWD():
        txtPWD = MTGUI.b.find_element_by_xpath('//*[@id="password"]')
        return txtPWD

    def btnLogin():
        btnLogin = MTGUI.b.find_element_by_xpath('/html/body/div[2]/form/div[4]/button')
        return btnLogin

# =========== 用户个人管理中心 ==========
    def linkSysManage():
        linkSysManage = MTGUI.b.find_element_by_xpath('/html/body/div[4]/div[1]/div/ul/li[5]/a/span[1]')

        # //*[@id="leftsidebar"]/div[2]/div/ul/li[3]/a
        return linkSysManage
    def linkUserManage():
        linkUserManage =  MTGUI.b.find_element_by_xpath('/html/body/div[4]/div[1]/div/ul/li[5]/ul/li[3]/a')
        return linkUserManage
    def optionRowOne():
        optionRowOne = MTGUI.b.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[1]/label/span')
        return  optionRowOne
    def btnDelUserRow():
        btnDelUserRow = MTGUI.b.find_element_by_xpath('//*[@id="btn_delete"]')
        return btnDelUserRow
    def btnConfirmDelDialog():
        btnConfirmDelDialog = MTGUI.b.find_element_by_xpath('/html/body/div[6]/div[7]/div/button')
        return btnConfirmDelDialog
    def btnNotifyDialog():
        btnNotifyDialog = MTGUI.b.find_element_by_xpath('/html/body/div[6]/div[7]/div/button')
        return btnNotifyDialog

# =========== 用户注册页页面元素 ==========

    def btnSendVerifyCode():
        btnSendVerifyCode = MTGUI.b.find_element_by_xpath('//*[@id="messageCode"]')
        return btnSendVerifyCode
    def txtPhoneNum():
        txtPhoneNum = MTGUI.b.find_element_by_xpath('//*[@id="phone"]')
        # //*[@id="RegisterForm"]/div[1]/div/div/div/input
        return txtPhoneNum
    def txtVerifyCode():
        txtVerifyCode = MTGUI.b.find_element_by_xpath('//*[@id="verification"]')
        # //*[@id="RegisterForm"]/div[2]/div[1]/div/div/input
        return txtVerifyCode
    def txtRegPWD():
        txtRegPWD = MTGUI.b.find_element_by_xpath('//*[@id="password"]')
        # //*[@id="RegisterForm"]/div[3]/div/div/div/input
        return txtRegPWD
    def txtRegSecondPWD():

        # txtRegSecondPWD = MTGUI.b.find_element_by_xpath('/html/body/div[2]/form/div[5]/div/input')
        txtRegSecondPWD = MTGUI.b.find_element_by_xpath('//*[@id="qpassword"]')


        # print(txtRegSecondPWD.tag_name)
        # print(txtRegSecondPWD.text)
        return txtRegSecondPWD
    def optionLink():
        optionLink = MTGUI.b.find_element_by_xpath('//*[@id="register-form"]/div[6]/div/div/ins')
        return optionLink
    def btnRegis():
        btnRegis = MTGUI.b.find_element_by_xpath('//*[@id="register-form"]/div[7]/button')
        return btnRegis
    def btnRegistSuccess():
        # btnRegistSuccess = MTGUI.b.find_element_by_xpath('/html/body/div[4]/div[7]/div/button')
        btnRegistSuccess = MTGUI.b.find_element_by_xpath('/html/body/div[5]/div[7]/div/button')

        return btnRegistSuccess
# ========
    def lblMTAccout(self):
        lblMTAccout = MTGUI.b.find_element_by_xpath('//*[@id="leftsidebar"]/div[2]/div/ul/li[3]/a/span')
        return lblMTAccout

    def lblCurrentUser(self):
        lblCurrentUser = MTGUI.b.find_element_by_id('HeaderCurrentUserName')
        # lblCurrentUser = MTGUI.b.find_element_by_xpath('//*[@id="HeaderCurrentUserName"]')
        return lblCurrentUser

    def lblRegisterSuccess(self):
        lblRegisterSuccess = MTGUI.b.find_element_by_xpath('/html/body/div/div[2]/div/h4')
        return lblRegisterSuccess
# ===================================== MT Link CTP Operation Actions =========================
    def linkMTAccount(self):

        linkMTAccount = MTGUI.b.find_element_by_xpath('//*[@id="leftsidebar"]/div[2]/div/ul/li[3]/a')
        return linkMTAccount

    def btnAddMTAccount(self):

        btnAddMTAccount = MTGUI.b.find_element_by_xpath('//*[@id="leftsidebar"]/div[2]/div/ul/li[3]/a/span')
        return btnAddMTAccount

    def btnAction(self):
        btnAction = MTGUI.b.find_element_by_xpath('/html/body/section[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td[9]/a')
        return btnAction

    def btnLink(self):
        btnLink = MTGUI.b.find_element_by_xpath('/html/body/section[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td[9]/ul/li[1]/a')
        return btnLink

    def btnSaveCTPLink(self):
        btnSaveCTPLink = MTGUI.b.find_element_by_xpath('//*[@id="MtAccountEditModal"]/div/div/div[3]/button[2]')
        return btnSaveCTPLink

    def lblCTPAccountLink(self):
        lblCTPAccountLink = MTGUI.b.find_element_by_xpath('/html/body/section[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td[5]')
        return lblCTPAccountLink
# ===================================== CTP Operation Actions =================================
    def linkCTPAccount(self):
        linkCTPAccount = MTGUI.b.find_element_by_xpath('//*[@id="leftsidebar"]/div[2]/div/ul/li[4]/a')
        #linkCTPAccount = myTestUtility.get_ele_times(MTGUI.b,50,lambda d:MTGUI.b.find_element_by_xpath('//*[@id="leftsidebar"]/div[2]/div/ul/li[4]/a'))
        return linkCTPAccount

    def btnAddCTP(self):
        btnAddCTP = MTGUI.b.find_element_by_xpath('/html/body/section[2]/div/div[1]/div/div/div[2]/button')

        return  btnAddCTP

    def txtInvsID(self):
        txtInvsID = MTGUI.b.find_element_by_xpath('//*[@id="create-ctpaccount-details"]/div[1]/div[1]/div/div/input')
        return txtInvsID
    def txtInvsPWD(self):
        txtInvsPWD = MTGUI.b.find_element_by_xpath('//*[@id="create-ctpaccount-details"]/div[1]/div[2]/div/div/input')
        return txtInvsPWD
    def txtFee(self):
        txtFee = MTGUI.b.find_element_by_xpath('//*[@id="create-ctpaccount-details"]/div[2]/div/div/div/input')
        return txtFee
    def btnSaveCTP(self):
        btnSaveCTP = MTGUI.b.find_element_by_xpath('//*[@id="CtpAccountCreateModal"]/div/div/div[2]/form/div[2]/button[2]')
        return btnSaveCTP
    def lblCTPAccount(self):
        lblCTPAccount = MTGUI.b.find_element_by_xpath('/html/body/section[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td[2]')
        return lblCTPAccount
