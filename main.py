import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#---------------------------------------------------------------------------------------------------------
# LOGIN
PSSWD = '__Your_Password__'
EMAIL = '__Your_Email__'


# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=4028885563&f_LF=f_AL&geoId=102257491&keywords=python+developer&location=London%2C+England%2C+United+Kingdom')
time.sleep(2)

def standard_first_process():
    # Search job        1ST TIME
    time.sleep(2)
    # FOR 2FA AUTH.
    apply_button = driver.find_element(By.CSS_SELECTOR, value='.jobs-apply-button--top-card button')
    apply_button.click()

    # Fill Phone Number
    p_no = driver.find_element(By.CSS_SELECTOR, value='#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4028885563-1150535892202505571-phoneNumber-nationalNumber')
    p_no.send_keys('9996520214')

    # Next Button
    # nxt = driver.find_element(By.CSS_SELECTOR, value='button#ember403')
    nxt = driver.find_element(By.CSS_SELECTOR, value='.ember-view button')
    nxt.click()

    # save Button
    save = driver.find_element(By.CSS_SELECTOR, value='.artdeco-modal__confirm-dialog-btn')
    save.click()
    time.sleep(2)
    # ------------------------
    apply_button = driver.find_element(By.CSS_SELECTOR, value='.jobs-apply-button--top-card button')
    apply_button.click()

    # Fill Phone Number
    p_no = driver.find_element(By.CSS_SELECTOR, value='#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4028885563-1150535892202505571-phoneNumber-nationalNumber')
    p_no.send_keys('9996520214')

    # Next Button
    # nxt = driver.find_element(By.CSS_SELECTOR, value='button#ember403')
    nxt = driver.find_element(By.CSS_SELECTOR, value='.ember-view button')
    nxt.click()

    # save Button
    save = driver.find_element(By.CSS_SELECTOR, value='.artdeco-modal__confirm-dialog-btn')
    save.click()

    # Review Button
    review = driver.find_element(By.CSS_SELECTOR, value='.artdeco-button')
    review.click()

    submit_bttn = driver.find_element(By.CSS_SELECTOR, value='.artdeco-button')
    submit_bttn.click()

def discard_application():
        close = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
        close.click()

        # Discard Application
        discard = driver.find_element(By.CLASS_NAME, value='artdeco-modal__dismiss')
        discard.click()

        time.sleep(2)       

login = False
while not login:
    try:
        sign_in = driver.find_element(By.CSS_SELECTOR, value='#base-contextual-sign-in-modal > div > section > div > div > div > div.sign-in-modal > button')
        # sign_in = driver.find_element(By.CSS_SELECTOR, value='nav div a.nav__button-tertiarybtn-mdbtn-tertiary')
        sign_in.click()

        time.sleep(1)
        email = driver.find_element(By.NAME, value='session_key')
        # email.click()
        email.send_keys(EMAIL)

        psswd = driver.find_element(By.NAME, value='session_password')
        # psswd.click()
        psswd.send_keys(PSSWD)

        sign_in_button = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
        sign_in_button.click()

        login = True
    except NoSuchElementException:
        driver.close()
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.linkedin.com/jobs/search/?currentJobId=4028885563&f_LF=f_AL&geoId=102257491&keywords=python+developer&location=London%2C+England%2C+United+Kingdom')
        time.sleep(2)

# CAPTCHA 
input("Press any key after CAPTCHA")


#-----------------------------------------------------------------------------------
# Get all job listings
time.sleep(5)
job_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in job_listings:
    listing.click()
    time.sleep(2)
    
    try:
        # Attempt to apply for the job
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys('9996524568')

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            discard_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException as e:
        print(f"An error occurred: {e}")
        try:
            # Try closing and discarding application if an error occurs
            close = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
            close.click()

            discard = driver.find_element(By.CLASS_NAME, value='artdeco-modal__dismiss')
            discard.click()
            time.sleep(2)

        except NoSuchElementException as discard_error:
            print(f"An error occurred while closing or discarding: {discard_error}")

        continue

time.sleep(5)
driver.quit()
