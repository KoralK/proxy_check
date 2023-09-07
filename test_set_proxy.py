import os
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


def set_system_proxy(ip, port):
    # Setting up HTTP and HTTPS proxies
    os.system(f"networksetup -setwebproxy Wi-Fi {ip} {port}")
    os.system(f"networksetup -setsecurewebproxy Wi-Fi {ip} {port}")


def unset_system_proxy():
    # Disabling HTTP and HTTPS proxies
    os.system("networksetup -setwebproxystate Wi-Fi off")
    os.system("networksetup -setsecurewebproxystate Wi-Fi off")


def check_internet_access():
    try:
        output = subprocess.check_output(
            ["ping", "-c", "1", "8.8.8.8"], stderr=subprocess.STDOUT, timeout=5
        )
        return True
    except subprocess.CalledProcessError:
        return False
    except subprocess.TimeoutExpired:
        return False


def check_with_selenium(ip, port):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Prevent GUI launch
    service = Service('/opt/homebrew/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get("https://www.google.com/")
        title = driver.title
        driver.quit()
        return "Google" in title
    except TimeoutException:
        driver.quit()
        return False


with open("http_proxies.txt", "r") as file:
    proxies = file.readlines()

valid_proxies = []

for proxy in proxies:
    ip, port = proxy.strip().split(":")
    set_system_proxy(ip, port)

    if check_internet_access():
        if check_with_selenium(ip, port):
            valid_proxies.append(proxy.strip())
            print(f"Proxy {ip}:{port} provides internet access!")
        else:
            print(f"Proxy {ip}:{port} failed the Selenium test.")
    else:
        print(f"Proxy {ip}:{port} doesn't provide internet access.")

    unset_system_proxy()

with open("working_proxies.txt", "w") as out_file:
    for proxy in valid_proxies:
        out_file.write(proxy + "\n")
