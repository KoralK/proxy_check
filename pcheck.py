import requests

def check_proxy(ip, port):
    proxies = {
        "http": f"socks5://{ip}:{port}",
        "https": f"socks5://{ip}:{port}",
    }
    try:
        response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=5)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        pass
    return False

if __name__ == "__main__":
    proxy_list = [
    ("37.187.91.192", 17605),
    ("192.241.149.84", 37455),
    ("54.38.176.200", 58346),
    ("162.144.74.156", 3620),
    ("199.102.107.145", 4145),
    ("115.127.89.202", 1088),
    ("129.154.51.255", 8388),
    ("162.241.6.97", 34725),
    ("89.202.238.81", 61104),
    ("173.249.20.169", 9060),
    ("91.217.178.94", 24153),
    ("115.127.97.25", 1088),
    ("212.83.138.132", 65177),
    ("134.122.21.142", 3377),
    ("70.166.167.55", 57745),
    ("37.187.73.7", 49697),
    ("147.182.209.238", 21944),
    ("192.252.208.67", 14287),
    ("161.35.117.30", 19109),
    ("31.217.221.74", 8192)
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
