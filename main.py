from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def login_and_make_post(username, password, post_content):
    driver = webdriver.Chrome()
    print("browser opened")
    driver.maximize_window()
    print("Window maximized")

    # Open Facebook login page
    driver.get('https://www.facebook.com/')
    print("facebook Opened")

    # Find and fill in the login credentials
    email_input = driver.find_element("id", "email")
    email_input.send_keys(username)
    print("email or phone number inputted")

    time.sleep(3)

    password_input = driver.find_element("id", "pass")
    password_input.send_keys(password)
    print("password inputted")

    # Submit the login form
    password_input.send_keys(Keys.ENTER)
    print("enter button clicked")

    # Wait for the login process to complete
    time.sleep(7)

    # Make a post
    try:
        homeButton = '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div/div[1]/div[1]/ul/li[1]/span/div/a/span/svg/path'
        click_to_post = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span'
        input_field = 'div.x1lkfr7t > span:nth-child(1)'
        pa = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/p'
        word = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p[1]'
        post_button = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div'

        # click's on the home button incase random prompts of add friend or accept friend request is shown
        # driver.find_element(By.XPATH, homeButton).click()
        # driver.find_element(By.TAG_NAME, 'Home').click()
        driver.find_element(By.CSS_SELECTOR, '[aria-label=Home]').click()
        print("home button clicked")

        time.sleep(5)

        click_on_container = driver.find_element(By.XPATH, click_to_post).click()
        print("container clicked")
        time.sleep(3)

        # post_box = driver.find_element(By.XPATH, input_field)
        post_box = driver.find_element(By.XPATH, pa)
        print('post box found')
        post_box.is_enabled()

        driver.execute_script("arguments[0].value = arguments[1];", post_content, post_box)
        print(post_content + " typed ")

        # post_box.send_keys(post_content)
        # print("text inputted")

        driver.find_element(By.XPATH, post_button).click()
        print("post button clicked")

        driver.get('https://www.google.com/')
        print("google.com visited")
        time.sleep(1)
        google_search_box = driver.find_element(By.CSS_SELECTOR, "[aria-label=Search]")
        print("search box found")
        google_search_box.send_keys('best QA Engineering practices')
        time.sleep(2)
        google_search_box.send_keys(Keys.ENTER)
        print("search report shown")
        time.sleep(3)






    except Exception as e:
        print("Error occurred while making a post:", str(e))

    # Wait for the post to be uploaded
    time.sleep(5)

    # Close the browser
    driver.quit()
    print("browser closed")


if __name__ == "__main__":
    # Replace 'your_facebook_username' and 'your_facebook_password' with your actual Facebook credentials
    username = '08100439822'
    password = 'Playschool'
    post_content = "I Kill Bugs!"

    login_and_make_post(
        username, password, post_content)
