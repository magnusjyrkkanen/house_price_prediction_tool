from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


def data_fetcher(websites: dict):
    """Main function for the data fetching process."""

    # Variables for property location and type.
    location = "Rautalampi"
    type = "omakotitalo"

    for website in websites.keys():
        match website:
            case "Etuovi":
                fetch_data_etuovi(websites[website], location, type)
            case other:
                print(f"Unkown website {website} - {websites[website]}")


def fetch_data_etuovi(url: str, location: str, type: str):
    """Fetch data from Etuovi."""

    # Start Selenium session.
    driver = webdriver.Chrome()

    try:
        # Open browser with url.
        driver.get(url)

        # Handle cookies modal.
        cookie_settings_button = WebDriverWait(driver, timeout=3).until(
            lambda d: d.find_element(by=By.ID, value="almacmp-modalSettingBtn"))
        cookie_settings_button.click()
        reject_cookies_button = WebDriverWait(driver, timeout=3).until(
            lambda d: d.find_element(by=By.ID, value="almacmp-reject-all-layer2"))
        reject_cookies_button.click()

        type_box = driver.find_element(by=By.ID, value="mui-component-select-residentialType")
        type_box.click()

        type_select = driver.find_element(by=By.XPATH, value='//*[@id="menu-residentialType"]/div[3]/ul/li[4]/div/span')
        type_select.click()
        ActionChains(driver).key_down(Keys.TAB).perform()

        # Input search terms and click search.
        location_box = driver.find_element(by=By.ID, value=":R5kopkp6mn:")
        # search_box = driver.find_element(by=By.ID, value=":rv:")
        location_box.send_keys(location)
        ActionChains(driver).key_down(Keys.ENTER).perform()
        search_button = driver.find_element(by=By.XPATH, value='//*[@id="frontpage"]/div[1]/div/div[2]/div/form/div/div[1]/div[3]/button')
        ActionChains(driver).scroll_to_element(search_button).perform()
        search_button.click()

        # Results page.
        announcement_list = WebDriverWait(driver, timeout=3).until(
            lambda d: d.find_element(by=By.ID, value="announcement-list"))
        # ActionChains(driver).scroll_to_element(announcement_list).perform()
        announcement_list.screenshot(f"./data_fetching/results_{location}.png")

        # Sleep for development
        sleep(2)

        # Collect search result urls.
        # Call individual urls.
        # Collect data from individual pages.
    except ElementClickInterceptedException:
        driver.save_screenshot(f"./data_fetching/exception.png")
    finally:
        # Close browser.
        driver.quit()
