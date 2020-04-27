from selenium import webdriver
from common import config_value
from common.base_page import BasePage


def set_driver():
    driver = webdriver.Chrome(executable_path=config_value.config.chrome_path)
    base_page = BasePage(driver)
    driver.implicitly_wait(10)
    base_page.set_browser_max()
    url = config_value.config.zantao_url
    base_page.open_url(url)
    return driver


if __name__ == '__main__':
    set_driver()
