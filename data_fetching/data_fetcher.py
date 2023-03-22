from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


def data_fetcher(websites: dict):
    """Main function for the data fetching process."""

    for website in websites.keys():
        match website:
            case "Etuovi":
                fetch_data_etuovi(websites[website])
            case other:
                print(f"Unkown website {website} - {websites[website]}")


def fetch_data_etuovi(url: str):
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
        # Sleep for development
        sleep(2)

        # Input text and click search.
        # Collect search result urls.
        # Call individual urls.
        # Collect data from individual pages.
    finally:
        # Close browser.
        driver.quit()
