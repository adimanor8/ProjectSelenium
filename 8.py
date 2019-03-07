from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.keys import Keys
class text:
    def  url():
        file = open("C:/Users/Owner2-pc/Downloads/url_website.txt", "r+")
        x = file.readline()
        file.close()
        return x



class Chrome(text):
    def __init__():
        driver=webdriver.Chrome(executable_path='/Users/Owner2-pc/Downloads/chromedriver_win32/chromedriver.exe')
        driver.get(text.url())
        driver.find_element_by_class_name("seperator-link").click()
        driver.find_element_by_class_name("text-btn").click()
        #driver.find_element_by_class_name("rtl").send_keys("a")
        driver.find_element_by_id("ember1011").send_keys("המאסטר2")
        driver.find_element_by_id("ember1013").send_keys("adi.manor.8979@gmail.com")
        driver.find_element_by_id("valPass").send_keys("D@arrow2")
        driver.find_element_by_id("ember1017").send_keys("D@arrow2")
        driver.find_element_by_id("ember1018-id").send_keys(Keys.SPACE)
        try:
            driver.find_element_by_class_name("ui-btn").click()
            driver.find_element_by_class_name("sv-title")
            print("Cool!test Registration was completed without issues")
        except NoSuchElementException:
            print("the test has failed")

        finally:
            print("test was completed")

class Home(text):
    def __init__():
        driver = webdriver.Chrome(executable_path='/Users/Owner2-pc/Downloads/chromedriver_win32/chromedriver.exe')
        driver.get(text.url())

        # #driver.find_element_by_class_name("chosen-single").click()
        #driver.find_element_by_xpath('//span[contains(@text(),"סכום")]').encode('utf8')

        driver.find_element_by_class_name("seperator-link").click()
        driver.find_element_by_id("ember997").send_keys("adi.manor.8979@gmail.com")
        driver.find_element_by_id("ember999").send_keys("D@arrow2")
        driver.find_element_by_class_name("ui-btn").click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ember662_chosen"]/a/span').click()
        driver.find_element_by_xpath('//*[@id="ember662_chosen"]/div/ul/li[2]').click()
        driver.find_element_by_xpath('//*[@id="ember677_chosen"]/a/span').click()
        driver.find_element_by_xpath('//*[@id="ember677_chosen"]/div/ul/li[2]').click()
        driver.find_element_by_xpath('//*[@id="ember686_chosen"]/a/span').click()
        driver.find_element_by_xpath('//*[@id="ember686_chosen"]/div/ul/li[2]').click()
        try:
            driver.find_element_by_class_name("ui-btn").click()
            print("test Home Screen finished without issues")
        except NoSuchElementException:
            print("test failed")
        finally:
            print("the test was finished")
class Business(text):
    def __init__():
        driver = webdriver.Chrome(executable_path='/Users/Owner2-pc/Downloads/chromedriver_win32/chromedriver.exe')
        driver.get("https://buyme.co.il/express/#/?numberOfEmployees=50")
        driver.find_element_by_id("ember285").click()
        driver.find_element_by_class_name("selectedName").click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@data="6130759"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ember300"]/div').click()
        #driver.find_element_by_class_name("field select")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@data="27708"]').click()
        time.sleep(50)

class SR(text):
    def __init__():
        driver = webdriver.Chrome(executable_path='/Users/Owner2-pc/Downloads/chromedriver_win32/chromedriver.exe')
        driver.get("https://buyme.co.il/money/20620")
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="ember824"]').send_keys("50")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@type="submit"]').click()
        time.sleep(5)
        driver.find_element_by_id("ember994").send_keys("adi")
        driver.find_element_by_id("ember996").send_keys("moran")
        driver.find_element_by_xpath('//*[@id="ember1012"]/textarea').send_keys("מזל טוב")
        driver.find_element_by_id("ember1021").send_keys("C:/Users/Owner2-pc/Downloads/jpg/1.jpg")


class payment(text):
    driver = webdriver.Chrome(executable_path='/Users/Owner2-pc/Downloads/chromedriver_win32/chromedriver.exe')
    driver.get("https://buyme.co.il/money/20620")
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="ember824"]').send_keys("50")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@type="submit"]').click()
    time.sleep(5)
    driver.find_element_by_id("ember994").send_keys("adi")
    driver.find_element_by_id("ember996").send_keys("moran")
    driver.find_element_by_xpath('//*[@id="ember1012"]/textarea').send_keys("מזל טוב")
    driver.find_element_by_class_name("icon-print").click()
    driver.find_element_by_xpath('//button[contains(text(),"אוקיי")]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@type="submit"]').click()
    time.sleep(5)
    driver.find_element_by_id("ember1471").send_keys("adi.manor.8979@gmail.com")
    driver.find_element_by_id("ember1473").send_keys("D@arrow2")
    driver.find_element_by_class_name("ui-btn").click()
    time.sleep(15)
    driver.find_element_by_class_name("icon-print").click()
    driver.find_element_by_xpath('//button[contains(text(),"אוקיי")]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@type="submit"]').click()
    time.sleep(10)





    #driver.find_element_by_xpath('//*[@type="submit""]').click()




    # driver.get("https://buyme.co.il/payment/7519823")
    # driver.find_element_by_id("ember1014").send_keys("adi.manor.8979@gmail.com")
    # driver.find_element_by_id("ember1016").send_keys("D@arrow2")
    # driver.find_element_by_class_name("ui-btn").click()



























































# ao=Chrome
# ao.__init__()
# ao2=Home
# ao2.__init__()
# ao3=Business
# ao3.__init__()
ao4=SR
ao4.__init__()
#ao5=payment
#ao5.__init__()



