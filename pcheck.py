import requests

def check_proxy(ip, port):
    proxies = {
        "http": f"socks5://{ip}:{port}",
        "https": f"socks5://{ip}:{port}",
    }
    try:
        response = requests.get("http://www.google.com", proxies=proxies, timeout=10)  # increased timeout
        if response.status_code == 200:
            return True
    except requests.RequestException as e:
        print(f"Error for proxy {ip}:{port} - {e}")
    return False

if __name__ == "__main__":
    proxy_list = [
    ("43.154.21.246", 10000),
    ("159.223.76.234", 30305),
    ("98.181.137.80", 4145),
    ("72.195.114.184", 4145),
    ("192.111.139.163", 19404),
    ("68.1.210.163", 4145),
    ("51.161.130.195", 41157),
    ("122.10.101.145", 3333),
    ("199.102.106.94", 4145),
    ("5.42.87.164", 56789),
    ("139.59.14.115", 63971),
    ("98.175.31.195", 4145),
    ("199.102.107.145", 4145),
    ("36.92.111.49", 52471),
    ("103.146.197.43", 4996),
    ("173.249.2.58", 5964),
    ("142.54.237.34", 4145),
    ("70.166.167.55", 57745),
    ("115.127.91.122", 1088),
    ("192.111.129.145", 16894),
    ("72.206.181.103", 4145),
    ("85.175.226.248", 1080),
    ("199.102.105.242", 4145),
    ("204.48.21.220", 54845),
    ("98.188.47.150", 4145),
    ("174.77.111.198", 49547),
    ("91.218.102.187", 1080),
    ("174.138.44.248", 24639),
    ("192.254.79.108", 53614),
    ("192.111.135.17", 18302)
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
