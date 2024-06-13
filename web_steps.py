# features/steps/web_steps.py

from behave import then
from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Chrome()

@then('I should see the text "{text}"')
def step_impl(context, text):
    assert text in driver.page_source, f"Expected text '{text}' not found in page source"
