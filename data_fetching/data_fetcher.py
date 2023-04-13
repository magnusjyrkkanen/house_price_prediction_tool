from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from datetime import datetime


def data_fetcher(websites: dict):
    """Main function for the data fetching process."""

    # Variables for property location and type.
    location = "Rautalampi"
    type = "omakotitalo"

    # Date.
    now = datetime.now()
    year_month_day = now.strftime("%Y_%m_%d")

    for website in websites.keys():
        match website:
            case "Etuovi":
                fetch_data_etuovi(websites[website], location, type, year_month_day)
            case other:
                print(f"Unkown website {website} - {websites[website]}")


def fetch_data_etuovi(url: str, location: str, type: str, year_month_day):
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

        # Choose property type.
        type_box = driver.find_element(by=By.ID, value="mui-component-select-residentialType")
        delta_y = int(type_box.rect["y"] / 2)
        ActionChains(driver).scroll_by_amount(0, delta_y).perform()
        type_box.click()

        type_select = driver.find_element(by=By.XPATH, value='//*[@id="menu-residentialType"]/div[3]/ul/li[4]')
        ActionChains(driver).scroll_to_element(type_select).perform()
        type_select.click()
        ActionChains(driver).key_down(Keys.TAB).perform()

        # Input search terms and click search.
        location_box = driver.find_element(by=By.ID, value=":R5kopkp6mn:")
        # search_box = driver.find_element(by=By.ID, value=":rv:")
        location_box.send_keys(location)
        ActionChains(driver).key_down(Keys.ENTER).perform()
        search_button = driver.find_element(
            by=By.XPATH, value='//*[@id="frontpage"]/div[1]/div/div[2]/div/form/div/div[1]/div[3]/button')
        ActionChains(driver).scroll_to_element(search_button).perform()
        WebDriverWait(driver, timeout=3).until(element_to_be_clickable(search_button))
        search_button.click()

        # Results page.
        announcement_list = WebDriverWait(driver, timeout=3).until(
            lambda d: d.find_element(by=By.ID, value="announcement-list"))
        # ActionChains(driver).scroll_to_element(announcement_list).perform()
        announcement_list.screenshot(f"./data_fetching/results_{location}_{year_month_day}.png")

        # Sleep for development
        sleep(2)

        # Collect search result urls.
        # Call individual urls.
        # Collect data from individual pages.
    except ElementClickInterceptedException as ex:
        # Print the exception and take a screenshot from the situation.
        print(ex)
        driver.save_screenshot(f"./data_fetching/exception_click.png")
    except NoSuchElementException as ex:
        # Print the exception and take a screenshot from the situation.
        print(ex)
        driver.save_screenshot(f"./data_fetching/exception_element.png")
    finally:
        # Close browser.
        driver.quit()
