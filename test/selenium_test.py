from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time
browser = webdriver.Chrome()
action = ActionChains(browser)


def visit_baidu():
    try:
        browser.get("https://www.baidu.com")
        input = browser.find_element_by_id("kw")
        input.send_keys("Python")
        input.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, "content_left")))
        print(browser.current_url)

        print(browser.page_source)
        print(browser.get_cookies())
        time.sleep(10)
    finally:
        browser.close()


def visit_taobao():
    browser.get("https://www.taobao.com")
    input = browser.find_element_by_id("q")
    input.send_keys("IPhone")
    input.send_keys(Keys.ENTER)
    time.sleep(2)
    #TODO 需要登录验证
    forget_pwd = browser.find_element_by_class_name("J_Quick2Static")
    forget_pwd.click()
    #账号密码
    """
    username = browser.find_element_by_id("TPL_username_1")
    password = browser.find_element_by_id("TPL_password_1")
    username.send_keys("")
    password.send_keys("")
    """
    #支付宝登录
    alipay_button = browser.find_element_by_class_name("alipay-login")
    alipay_button.click()
    show_login = browser.find_element_by_class_name("show_login")
    show_login.click()
    alipay_username = browser.find_element_by_id("J-input-user")
    alipay_password = browser.find_element_by_id("password_rsainput")
    alipay_username.send_keys("13760227355")
    alipay_password.send_keys("yh981114+")
    alipay_login = browser.find_element_by_id("J-login-btn")
    alipay_login.click()
    #滑动验证
    slide_button = browser.find_element_by_class_name("nc-lang-cnt")
    action.click_and_hold(slide_button).perform()
    action.move_by_offset(298,0)
    action.release().perform()
    #登录
    login_button = browser.find_element_by_id("J_SubmitStatic")
    login_button.click()
    button = browser.find_element_by_class_name("btn-search")
    button.click()
    time.sleep(10)
    browser.close()
def main():
    #visit_baidu()
    visit_taobao()



if __name__ == '__main__':
    main()
