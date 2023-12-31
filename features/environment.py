from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param scenario_name:
    :param context: Behave context
    """
    # service = Service(executable_path='/Users/chelsy/QA/Lesson 5/python-selenium-automation/chromedriver')
    # context.driver = webdriver.Chrome(service=service)
    # context.driver.maximize_window()

    ### OTHER BROWSERS ###
    # service = Service(executable_path='/Users/svetlanalevinsohn/careerist/15-python-selenium-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE CHROME ####
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    service = Service(executable_path='/Users/chelsy/Documents/Careerist QA Automation Homework/Python Course/Automation/Internship/JIRA_task_1/chromedriver')
    context.driver = webdriver.Chrome(
        options=options,
        service=service
    )

    ### HEADLESS MODE FIREFOX ####
    # options = FirefoxOptions()
    # options.add_argument("--headless")
    # context.driver = webdriver.Firefox(executable_path='/Users/chelsy/Documents/Careerist QA Automation Homework/Python Course/Automation/Internship/JIRA_task_1/geckodriver', options=options)

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = ''
    # bs_key = ''
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, 'Logged In User Selects Visualization Options')
    # Pass scenario.name to init() for browserstack config:
    browser_init(context, 'Logged In User Selects Visualization Options')


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
