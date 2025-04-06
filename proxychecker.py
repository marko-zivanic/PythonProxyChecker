import requests

proxy_urls = []

def check_proxy(proxy_url): #Checks if the proxy works by requesting www.google.com
    try:
        if proxy_url.startswith("socks5"):
            proxies = {
                'http': proxy_url,
                'https': proxy_url
            }
        else:
            proxies = {
                'http': proxy_url,
                'https': proxy_url
            }
        
        response = requests.get('https://www.google.com', proxies=proxies, timeout=5) #timeout 5 sec
        
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def main():
    proxy_urls = []
    with open('proxylist.txt', 'r') as f: #opens the proxylist.txt and puts all proxies in a list
        for line in f:
            proxy_urls.append(line.strip()) 
    working_proxies = []
    non_working_proxies = []
    
    for p in proxy_urls: #Checks each proxy
        print(f"Checking proxy: {p} ...")
        if check_proxy(p):
            working_proxies.append(p)
            print(f"\033[92m[*]Proxy {p} is working\033[0m")
        else:
            non_working_proxies.append(p)
            print(f"\033[91m[X]Proxy {p} is not working\033[0m")
            
    #Prints final result in red or green
    print("\033[91m\n[X] NON working proxies:\033[0m")
    for proxy in non_working_proxies:
        print("\033[91m" + str(proxy) + "\033[91m")

    print("\033[92m\n[*] Working proxies: \033[0m")
    for proxy in working_proxies:
        print("\033[92m" + str(proxy) + "\033[92m")
    with open('working_proxies.txt','w') as f:
        for proxy in working_proxies:
            f.write(str(proxy) + '\n')

if __name__ == "__main__":
    main()

