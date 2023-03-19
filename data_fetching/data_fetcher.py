from selenium import webdriver
from selenium.webdriver.common.by import By


def data_fetcher(websites):
    """Main function for the data fetching process."""

    # Start Selenium session.
    driver = webdriver.Chrome()

    for url in websites:
        try:
            # Open browser with url.
            driver.get(url)
        finally:
            # Close browser.
            driver.quit()
