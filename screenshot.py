from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

screennwidth = 350
screenheight = 800

def getPostScreenshot(fileName, url):
    driver, wait = setUpDriver(url)
    driver.set_window_size(screennwidth, screenheight)
    driver.get(url)
    driver.save_screenshot(fileName)
    return fileName


def takeScreenshot(url, fileName):
    driver.set_window_size(screennwidth, screenheight)
    driver.get(url)
    driver.save_screenshot(fileName)
    return fileName

def setUpDriver(url: str):
    options = webdriver.ChromeOptions()
    options.headless = False
    options.enable_mobile = False
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    return driver, wait




def getScreenShot(url, commentId, filePath):
    print(filePath)
    handle = By.ID
    id = f"t3_{commentId}"
    driver, wait = setUpDriver(url)
    search = wait.until(EC.presence_of_element_located((handle, id)))
    screenShotName = filePath
    file = open(screenShotName, "wb")
    file.write(search.screenshot_as_png)
    file.close()
    return screenShotName

# driver = webdriver.Firefox()
# driver.get(url)
# wait = WebDriverWait(driver, 10)



