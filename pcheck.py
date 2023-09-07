import requests
import time

def check_proxy(ip, port):
    proxies = {
        "http": f"http://{ip}:{port}",
        "https": f"http://{ip}:{port}",
    }
    
    start_time = time.time()
    
    try:
        response = requests.get("http://www.google.com", proxies=proxies, timeout=10)
        elapsed_time = time.time() - start_time
        if response.status_code == 200:
            print(f"Proxy {ip}:{port} took {elapsed_time:.2f} seconds to respond.")
            return True, elapsed_time
    except requests.RequestException as e:
        print(f"Error for proxy {ip}:{port} - {e}")

    return False, None  # Ensure this is always returned if no successful response

if __name__ == "__main__":
    try:
        # Read proxies from the file
        with open("http_proxies.txt", "r") as file:
            proxy_list = [tuple(line.strip().split(":")) for line in file]

        alive_proxies = []

        for ip, port in proxy_list:
            result = check_proxy(ip, port)
            if result:  # Check if result is not None
                is_alive, response_time = result
                if is_alive:
                    print(f"Proxy {ip}:{port} is alive!")
                    alive_proxies.append((ip, port, response_time))
                else:
                    print(f"Proxy {ip}:{port} is down or not working.")


        # Let's print a statement before writing to the file
        print("Writing to file...")

        # Write alive proxies to a file
        with open("alive_http_proxies.txt", "w") as file:
            for ip, port, response_time in alive_proxies:
                file.write(f"{ip}:{port} - {response_time:.2f} seconds\n")
        
        print("File writing complete!")

    except Exception as e:
        # If there's any exception, it'll be printed
        print(f"An error occurred: {e}")
