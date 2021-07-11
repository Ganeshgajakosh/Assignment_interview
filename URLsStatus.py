import requests
#from twisted.internet import task, reactor
#timeout=120.0
import time
import threading




def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
    urls = []
    for line in lines:
        urls.append(line.strip(' \t\n'))
    while '' in urls:
        urls.remove('')
    #print(urls)
    return urls


def urlsStatusChecker(urls):
    for url in urls:
        try:
            url_response = requests.get(url, verify=False)
            if url_response.status_code == 200:
                print('{} - OK'.format(url))
        except requests.exceptions.ConnectionError:
            print('{} - NOT OK'.format(url))     


if __name__ == '__main__':
    filename = 'URLs.txt'
    urls = readFile(filename)
    starttime=time.time()
    while True:
        threads=[threading.Thread(target=urlsStatusChecker, args=(urls,))]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        time.sleep(120)
        print("\n After 120 seconds runnin script again \n")
    #l=task.LoopingCall(urlsStatusChecker(urls))
    #l.start(timeout)
    #reactor.run()
