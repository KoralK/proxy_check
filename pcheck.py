import requests
import time

def check_proxy(ip, port):
    proxies = {
        "http": f"http://{ip}:{port}",
        "https": f"http://{ip}:{port}",
    }
    
    start_time = time.time()  # Start the timer
    
    try:
        response = requests.get("http://www.google.com", proxies=proxies, timeout=10)
        elapsed_time = time.time() - start_time  # Calculate the elapsed time
        if response.status_code == 200:
            print(f"Proxy {ip}:{port} took {elapsed_time:.2f} seconds to respond.")
            return True, elapsed_time
    except requests.RequestException as e:
        print(f"Error for proxy {ip}:{port} - {e}")
        return False, None

if __name__ == "__main__":
    # Read the proxies from the file
    with open("http_proxies.txt", "r") as file:
        proxy_list = [tuple(line.strip().split(":")) for line in file]

    alive_proxies = []

    for ip, port in proxy_list:
        is_alive, response_time = check_proxy(ip, port)
        if is_alive:
            print(f"Proxy {ip}:{port} is alive!")
            alive_proxies.append((ip, port, response_time))
        else:
            print(f"Proxy {ip}:{port} is down or not working.")

    # Write the alive proxies with their response times to a file
    with open("alive_http_proxies.txt", "w") as file:
        for ip, port, response_time in alive_proxies:
            file.write(f"{ip}:{port} - {response_time:.2f} seconds\n")
