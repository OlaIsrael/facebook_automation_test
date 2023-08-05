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

    # Find and fill in the username
    email_input = driver.find_element("id", "email")
    email_input.send_keys(username)
    print("email or phone number inputted")
    time.sleep(3)

    # Find and fill in the password
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
        #path to various elements to be used
        click_to_post = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span'
        post_box_path = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/p'
        post_button = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div'
        live_video = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/span[2]/span'


        #find and click home button
        driver.find_element(By.CSS_SELECTOR, '[aria-label=Home]').click()
        print("home button clicked")
        time.sleep(8)

        driver.find_element(By.XPATH, click_to_post).click()
        print("container clicked")
        time.sleep(3)

        # find and click on post box
        post_box = driver.find_element(By.XPATH, post_box_path)
        print('post box found')
        driver.execute_script("arguments[0].value = arguments[1];", post_content, post_box)

        try:
            keyboard = driver.find_element(By.XPATH, post_box_path)
            keyboard.send_keys(post_content)
            time.sleep(2)

        except Exception as e:
            print("Error occurred while making a post:", str(e))

        print(post_content + " typed ")

        driver.find_element(By.XPATH, post_button).click()
        print("post button clicked")
        time.sleep(5)




        #visiting google.com
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


        #Log in to your Facebook account manualyto see the content you just posted


    except Exception as e:
        print("Error occurred while making a post:", str(e))

    # Wait for the post to be uploaded
    time.sleep(5)

    # Close the browser
    driver.quit()
    print("browser closed")


if __name__ == "__main__":
    # get user login credentials through the terminal

    username = input("Enter your email address or phone number :")

    password = input("Enter your password : ")

    post_content = input("Press the Enter key to continue or enter another text your what you want to post : ")
    if post_content == "":
        post_content = "I Kill Bugs!"
    else:
        post_content == post_content

    print("Your details has been stored and will be used to log you in")
    print(" Browser is launching.................................. ")

    login_and_make_post(
        username, password, post_content)
