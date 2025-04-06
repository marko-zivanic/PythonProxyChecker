# Python proxy checker
- [Installation](#installation)
- [Usage](#usage)


## Installation

```
git clone https://github.com/marko-zivanic/PythonProxyChecker
```

## Usage

1. Copy your list of proxies in the **proxylist.txt** in the format:
	protocol://ip:port
	
	Examples:
		http://170.106.104.64:13001
		socks4://46.188.2.42:5678

2. Run **proxychecker.py** by using:
	```
	python3 proxychecker.py
	```
3. It will check all the proxies in the list with a **timeout of 5 seconds** and display all working proxies
	You will get an output file **working_proxies.txt**
