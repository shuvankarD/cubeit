# features/steps/login.py
from behave import given, when, then

@given('username and pwd password')
def fill_username_and_password(context):
    context.page.goto("http://uitestingplayground.com/sampleapp")  # Open the target URL
    context.page.fill("#username", "JohnDoe")  # Fill the username field
    context.page.fill("#password", "pwd")  # Fill the password field

@when('Log In button clicked')
def click_login_button(context):
    context.page.click("#login")  # Click the login button

@then('show welcome message')
def check_welcome_message(context):
    welcome_message = context.page.text_content("#welcomeMessage")  # Check the welcome message
    assert "Welcome" in welcome_message, "Login failed!"
