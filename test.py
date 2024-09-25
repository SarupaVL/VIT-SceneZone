from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to initialize the Selenium WebDriver with your existing Chrome profile
def initialize_driver():
    options = webdriver.ChromeOptions()
    # Change this path to your actual profile path
    # options.add_argument(r"C:\Users\imrit\AppData\Local\Google\Chrome\User Data")
    # options.add_argument(r"profile-directory=Profile2")
    options.debugger_address = "localhost:9222"
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")
    return driver

# Function to retrieve messages from a specified group chat
def get_chat_messages(driver, chat_name):
    try:
        # Find the chat by its name and click it
        chat = driver.find_element(By.XPATH, f'//span[@title="{chat_name}"]')
        chat.click()
        time.sleep(2)  # Wait for the chat to load

        # Get all messages from the chat
        messages = driver.find_elements(By.CSS_SELECTOR, 'div.message-in, div.message-out')
        
        chat_data = []
        
        for message in messages:
            # Extract the timestamp
            try:
                timestamp = message.find_element(By.CSS_SELECTOR, 'div.copyable-text').get_attribute('data-pre-plain-text')
            except:
                timestamp = 'No timestamp'
            
            # Extract the actual message text
            try:
                text = message.find_element(By.CSS_SELECTOR, 'span.selectable-text').text
            except:
                text = 'No message text'

            # Add the extracted details to the chat data
            chat_data.append(f"{timestamp} {text}")
        
        return chat_data

    except Exception as e:
        print(f"Error: {e}")
        return []

# Main script
if __name__ == "__main__":
    driver = initialize_driver()
    group_name = input("Enter the group name: ")

    print(f"\nExtracting messages from the group: {group_name}")
    chat_data = get_chat_messages(driver, group_name)

    if chat_data:
        print("\nChat messages with names and timestamps:")
        for entry in chat_data:
            print(entry)
    else:
        print(f"Failed to retrieve messages from the group: {group_name}")

    # Close the browser
    driver.quit()