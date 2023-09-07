from ping3 import ping
import requests
import time

def is_proxy_stable(ip, port, times=5):
    proxies = {
        "http": f"http://{ip}:{port}",
        "https": f"https://{ip}:{port}",
    }
    success_count = 0

    for _ in range(times):
        try:
            response = requests.get("http://www.google.com", proxies=proxies, timeout=5)  # A shorter timeout like 5 seconds
            if response.status_code == 200:
                success_count += 1
        except requests.RequestException:
            pass

    # Consider the proxy stable if more than 80% of the requests succeed
    return success_count / times > 0.8


def check_proxy(ip, port):
    proxies = {
        "http": f"http://{ip}:{port}",
        "https": f"http://{ip}:{port}",
    }
    start_time = time.time()

    try:
        response = requests.get("http://www.google.com", proxies=proxies, timeout=10)
        response_time = round(time.time() - start_time, 2)
        
        # The following line is where the change is made
        stability = is_proxy_stable(ip, port)

        if response.status_code == 200:
            return True, response_time, stability
        else:
            return False, response_time, False
    except requests.RequestException as e:
        return False, None, False

if __name__ == "__main__":
    with open("http_proxies.txt", "r") as file:
        proxy_list = [tuple(line.strip().split(":")) for line in file.readlines()]
    
    with open("alive_http_proxies.txt", "a") as file:
        for ip, port in proxy_list:
            is_alive, response_time, stability = check_proxy(ip, port)
            if is_alive:
                file.write(f"{ip}:{port} - {response_time:.2f} seconds - Stable: {stability}\n")
                print(f"Proxy {ip}:{port} is alive and {stability}!")
            else:
                print(f"Proxy {ip}:{port} is down or not working.")

