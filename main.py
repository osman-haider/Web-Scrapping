import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
import time
from src.Last_Three_Months_Dates import last_three_months_dates_function
from src.Entity_Data_Values import entity_data_values
from src.Insert_in_Google_Sheet import inert_in_sheet
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
sheet_key = os.getenv('Sheet_ID')
# Initialize an empty DataFrame
df = pd.DataFrame()
def func(url):
    global df
    current_date = datetime.now()
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)  # Adjust the time according to your page load time

    # Locate the username and password fields
    username_field = driver.find_element(By.ID, value='username')  # The id for the username/email field
    password_field = driver.find_element(By.ID, value='password')  # The id for the password field

    # Enter login credentials
    username_field.send_keys(username)  # Replace with your actual username or email
    password_field.send_keys(password)  # Replace with your actual password

    # Locate and click the login button
    login_button = driver.find_element(By.XPATH,
                                       value="//button[@type='submit']")  # Locating the submit button by its type attribute
    login_button.click()
    # driver.get(url)
    print("Driver is Created...")
    date_picker = driver.find_element(By.XPATH, "//input[@type='date']")
    # date_picker.clear()
    last_three_months_dates = last_three_months_dates_function(current_date)
    for date in last_three_months_dates:

        # date_picker.send_keys(date + Keys.ENTER)
        driver.execute_script(f"arguments[0].value = '{date}';", date_picker)
        driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_picker)
        time.sleep(3)
        updated_html = driver.page_source
        soup = BeautifulSoup(updated_html, 'html.parser')
        th_tag = soup.find('thead').find_all('th')
        column_names = [th.get_text() for th in th_tag]
        entities_data = entity_data_values(soup, date)
        # Create DataFrame if it's empty
        if df.empty:
            df = pd.DataFrame(columns=column_names)
        if len(entities_data) != 1:

            # Select the relevant columns from entities data
            entities_data_selected = [entity[:len(column_names)] for entity in entities_data]
            # Append selected entities data to DataFrame
            df = pd.concat([df, pd.DataFrame(entities_data_selected, columns=column_names)], ignore_index=True)
    inert_in_sheet(df, current_date, sheet_key)


if __name__ == '__main__':
    url = "https://users.sentimentrader.com/users/screens/short_ideas/"
    func(url)