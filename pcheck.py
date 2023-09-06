import requests

def check_proxy(ip, port):
    proxies = {
        "http": f"http://{ip}:{port}",
        "https": f"https://{ip}:{port}",
    }
    try:
        response = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=5)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        pass
    return False

if __name__ == "__main__":
    proxy_list = [
    ("184.170.248.5", 4145),
    ("167.71.250.32", 36995),
    ("138.68.81.7", 21551),
    ("164.68.115.155", 63424),
    ("107.152.98.5", 4145),
    ("103.234.27.78", 9090),
    ("66.42.224.229", 41679),
    ("72.195.114.184", 4145),
    ("195.248.242.15", 1237),
    ("142.54.228.193", 4145),
    ("199.229.254.129", 4145),
    ("209.126.9.164", 27651),
    ("54.39.49.42", 47925),
    ("98.181.137.80", 4145),
    ("188.191.164.55", 4890),
    ("192.111.129.145", 16894),
    ("199.102.104.70", 4145),
    ("192.111.134.10", 4145),
    ("157.245.139.82", 49502),
    ("110.235.250.155", 1080)
]

    alive_proxies = []

    for ip, port in proxy_list:
        if check_proxy(ip, port):
            print(f"Proxy {ip}:{port} is alive!")
            alive_proxies.append((ip, port))
        else:
            print(f"Proxy {ip}:{port} is down or not working.")

    # Write the alive proxies to a file
    with open("alive_proxies.txt", "w") as file:
        for ip, port in alive_proxies:
            file.write(f"{ip}:{port}\n")
