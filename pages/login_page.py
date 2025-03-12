from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import LINKEDIN_EMAIL, LINKEDIN_PASSWORD, LINKEDIN_LOGIN_URL

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self):
        self.driver.get(LINKEDIN_LOGIN_URL)

        # ממתין עד שהשדה של האימייל יופיע
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "username")))
        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

        # הזנת פרטים ולחיצה על התחברות
        email_input.send_keys(LINKEDIN_EMAIL)
        password_input.send_keys(LINKEDIN_PASSWORD)
        login_button.click()
