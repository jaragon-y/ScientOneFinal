import flask
from flask_cors import CORS
from flask import Flask
from Controller import ProfileController
from scraper import getPersona
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep

    #api = Linkedin('theterx118@gmail.com', '2102jaay')
    #test-test-a3049122b
    #alonsoaguinaga
    #marcomartinezlinares

app = Flask(__name__)
CORS(app)

@app.route('/app/api/persona',methods=['GET'])
def show2():
    name = flask.request.args.get('nombre')
    return getPersona(name)

@app.route('/app/api/profile',methods=['GET'])
def show():
    cuenta = flask.request.args.get('cuenta')
    contrasenia = flask.request.args.get('contrasenia')
    persona = flask.request.args.get('persona')
    return ProfileController.getProfile(cuenta,
                                        contrasenia,
                                        persona)


def login():
    FIREFOX_BINARY = FirefoxBinary('/usr/bin/firefox')

    PROFILE = webdriver.FirefoxProfile()
    PROFILE.set_preference("browser.cache.disk.enable", False)
    PROFILE.set_preference("browser.cache.memory.enable", False)
    PROFILE.set_preference("browser.cache.offline.enable", False)
    PROFILE.set_preference("network.http.use-cache", False)
    PROFILE.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0")

    FIREFOX_OPTS = Options()
    FIREFOX_OPTS.headless = True
    ff_opt = {
        'firefox_binary': FIREFOX_BINARY,
        'firefox_profile': PROFILE,
        'options': FIREFOX_OPTS,
        'executable_path': '/usr/bin/geckodriver'
    }

    driver = webdriver.Firefox(**ff_opt)
    driver.get("https://www.linkedin.com/")

    element = driver.find_element(By.CSS_SELECTOR, "input[autocomplete='username']")
    usuario = 'a34299720@gmail.com'
    element.send_keys(usuario)

    element = driver.find_element(By.CSS_SELECTOR, "input[autocomplete='current-password']")
    contrasenia = 'aaaaeeee'
    element.send_keys(contrasenia)

    element = driver.find_element(By.CSS_SELECTOR, "button[class='sign-in-form__submit-button']")
    element.click()
    sleep(1)
    driver.quit()

if __name__ == '__main__':
    login()
    app.run(port=1598)

