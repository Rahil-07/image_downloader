from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

X_path = """//div[@class='isv-r PNCib MSM1fd BUooTd']"""
URL = "https://www.google.com/search?q=bathroom&tbm=isch&ved=2ahUKEwiRgd7Q6f6AAxVzoekKHRcxDcQQ2-cCegQIABAA&oq=bathroom&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMgsIABCABBCxAxCDATIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQNQAFgAYLwGaABwAHgAgAF2iAF2kgEDMC4xmAEAqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=9kvsZJGuFPPCpgeX4rSgDA&bih=628&biw=1242&rlz=1C1RXQR_enIN1009IN1009"
show_more_results_X_path = """//input[@class='LZ4I']"""
img_x_path = """//img[@class='r48jcc pT0Scc iPVvYb']"""

driver=webdriver.Chrome()
driver.get(URL) 

img_elements = []

try:
    img_elements.extend(driver.find_elements(By.XPATH, X_path))
    print("--> ",len(img_elements)," found ")
    time.sleep(2)

    while len(img_elements) < 48:
            
        print("scrolling")
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        img_elements.extend(driver.find_elements(By.XPATH, X_path))
        print("--> ",len(img_elements)," found ")
        time.sleep(2)

        try:
            show_more_results = driver.find_element(By.XPATH, show_more_results_X_path).is_displayed()
        except Exception as e:
            print("Button problem")

        if show_more_results :
            show_more_results.click()
            time.sleep(2)

    print("total ",len(img_elements)," founds : ")

    link_container = []

    for img_element in img_elements:
        img_element.click()
        time.sleep(2)
        # driver.switch_to.window(driver.window_handles[0])
        try:
            tag = driver.find_element(By.XPATH,img_x_path)
            print(tag.get_attribute("src"))
            link_container.append(tag.get_attribute("src"))
            time.sleep(2)
        except Exception as e:
            print("link extraction problem")
    print(link_container)  




    
    # for div_element in div_elements:
    #     # Click on the div element
    #     div_element.click()
    #     i += 1
    #     print(i)
        # driver.switch_to.window(driver.window_handles[-1])

        # link
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser window
    driver.quit()