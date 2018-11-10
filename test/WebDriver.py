from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image


IMAGE_DIR = "E:\WorkSpeace\image\\"

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com/')
    # 获取页面名为wrapper的id标签的文本内容
    data = browser.find_element_by_id("wrapper").text
    print(data)

    # 打印页面标题 "百度一下，你就知道"
    print(browser.title)

    # 生成当前页面快照并保存
    browser.save_screenshot(IMAGE_DIR+"baidu.png")

    #显示图片
    # hiq_img = Image.open(IMAGE_DIR+"baidu.png")
    # hiq_img.show()

    # 关闭浏览器
    browser.quit()



if __name__ == '__main__':
    main()