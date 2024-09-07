import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.parse import urljoin
from src.utils import search_url_in_file, write_url_to_file
load_dotenv()

reports_path = os.getenv("FILE_PATH")+'/ast_reports'
print("scrapping started")
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\Nishkarsh.Kumar\OneDrive - Everest Group\Desktop\Projects\Ast_reports\ast_reports",  # Set your desired download folder here
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

URL = "https://www2.everestgrp.com/Account/Login?ShowSsoLogin=False"
driver.get(URL)
driver.implicitly_wait(3)


try:
    time.sleep(5)
    username_field = driver.find_element(By.ID, "LoginForm_Username")
    password_field = driver.find_element(By.ID, "LoginForm_Password")

    # Enter the credentials
    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)

    # Click the submit button
    submit_button = driver.find_element(By.XPATH, "//input[@name='submit' and @type='submit']")
    submit_button.click()
    time.sleep(5)  # Wait for potential login response
    profile_link = driver.find_element(By.XPATH, "//a[@href='/User' and text()='My Profile']")
    if profile_link.is_displayed():
        print("Login was successful.")
    else:
        print("Login failed: No success indicator found.")
    
except Exception as e:
    print(f"An error occurred during the login process: {e}")
time.sleep(5)

URL = "https://www2.everestgrp.com/reports?cat0=1268"
driver.get(URL)
driver.implicitly_wait(5)
time.sleep(2)

# Get product links and iterate through them
product_links = driver.find_elements(By.CSS_SELECTOR, ".product-listing-title a")
index = 0
file_path = os.getenv("FILE_PATH")+"/src/product_links.txt"
while index < len(product_links):
    link_url = product_links[index].get_attribute("href")
    if search_url_in_file(file_path=file_path, target_url=link_url) != -1:
        index += 1
        continue
    try:
        driver.get(link_url)
        driver.implicitly_wait(5)
        time.sleep(2)

        try:
            download_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.js-download-button"))
            )
            download_link.click()
            print(f"Downloading from: {link_url}")
            write_url_to_file(file_path=file_path, url=link_url)
            time.sleep(5)  # Wait for the download to initiate
        except Exception as e:
            print(f"Failed to download from: {link_url}. Error: {e}")
    except Exception as e:
        print(f"Failed to navigate to: {link_url}. Error: {e}")

    # Refresh the product links list after each iteration
    driver.get(URL)
    driver.implicitly_wait(5)
    time.sleep(2)
    product_links = driver.find_elements(By.CSS_SELECTOR, ".product-listing-title a")
    index += 1

driver.quit()