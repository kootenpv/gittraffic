import lxml.html
from selenium import webdriver
import datetime
import sys
import os
import json
from .gitplot import plot_all

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]
SAVE_PATH = sys.argv[3]
PACKAGES = sys.argv[4:]

# login


def login(driver):
    driver.get('https://github.com/login')
    ele = driver.find_element_by_id('login_field')
    ele.send_keys(USERNAME)

    ele = driver.find_element_by_id('password')
    ele.send_keys(PASSWORD)

    ele.submit()


def update_results(tree, results):
    header = tree.xpath('//*[contains(text(), "Referring sites")]')
    if header:
        table = header[0].getnext()
        now = str(datetime.datetime.now())
        for row in table.xpath('.//tr'):
            cells = row.xpath('./td')
            if cells:
                site, views, unique = cells
                results.append((now, site.text_content().strip(), views.text, unique.text))
        return results


def main():
    # get history
    if len(sys.argv) == 2 and 'plot' in sys.argv:
        plot_all()
        return
    if len(sys.argv) < 4:
        print('Usage: <username> <password> <save_path> <package_name_1> <package_name_2> <etc>')
        print('Usage: plot')
        return

    if os.path.isfile(SAVE_PATH):
        with open(SAVE_PATH) as f:
            package_results = json.load(f)
    else:
        package_results = {}

    # create driver
    driver = webdriver.Firefox()

    # login
    login(driver)

    # update package info
    for package in PACKAGES:
        if package not in package_results:
            package_results[package] = []
        url = 'https://github.com/{}/{}/graphs/traffic'.format(USERNAME, package)
        driver.get(url)
        tree = lxml.html.fromstring(driver.page_source)
        update_results(tree, package_results[package])

    # close driver
    driver.close()

    # save results
    with open(SAVE_PATH, 'w') as f:
        json.dump(package_results, f)
