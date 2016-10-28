from splinter import Browser

with Browser('firefox',profile='D:/ff_profile',profile_preferences={'executable_path':'D:/geckodriver.exe'})as browser:
    browser.visit('https://192.168.2.203')
