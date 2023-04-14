from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
import os


# set up the webdriver
driver = webdriver.Chrome("C:/Users/jmowo/Downloads/chromedriver_win32/chromedriver")

# navigate to the website
# URL for Queensu-Secure
url = "http://10.216.7.209"
driver.get(url)


# clear the file contents
open('accelerations.csv', 'w').close()

with open('accelerations.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(
        ['Time (s)', 'Linear Acceleration x (m/s^2)', 'Linear Acceleration y (m/s^2)',
         'Linear Acceleration z (m/s^2)',
         'Absolute acceleration (m/s^2)'])


# set start time
start_time = time.time()

# initialize previous value numbers
prev_value_numbers = None

# set a flag to indicate if there are valid acceleration values
valid_acceleration = False

while True:
    # wait for the page to fully load
    driver.implicitly_wait(10)

    # get the page source after the JavaScript has executed
    page_source = driver.page_source

    # parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")

    # extract the valueNumber elements
    value_numbers = [span.text for span in soup.find_all("span", class_="valueNumber")]

    # check if there are at least three elements in the value_numbers list
    if len(value_numbers) >= 3:

        # check if the current values are different from the previous values
        if value_numbers != prev_value_numbers:
            # calculate elapsed time
            elapsed_time = time.time() - start_time

            # check if there are valid acceleration values
            if any(value_numbers[1:]):
                # set the flag to indicate that there are valid acceleration values
                valid_acceleration = True

                # calculate absolute acceleration
                x_accel = float(value_numbers[0])
                y_accel = float(value_numbers[1])
                z_accel = float(value_numbers[2])
                abs_accel = round(((x_accel**2) + (y_accel**2) + (z_accel**2))**(0.5), 2)

                # add absolute acceleration to value_numbers list
                value_numbers.append(str(abs_accel))

                # write the valueNumber elements and elapsed time to a CSV file
                with open('accelerations.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([elapsed_time] + value_numbers)

            # check if the flag is set and if there are no valid acceleration values
            if valid_acceleration and not any(value_numbers[1:]):
                # remove the last line from the CSV file
                os.system("sed -i '$d' accelerations.csv")

                # reset the flag
                valid_acceleration = False

            # set current values as previous values for next iteration
            prev_value_numbers = value_numbers

    time.sleep(0.01)

# close the webdriver
driver.quit()
