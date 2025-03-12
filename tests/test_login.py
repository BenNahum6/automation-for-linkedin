from pages.login_page import LoginPage

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login()

    assert "feed" in driver.current_url, "Login failed!"
