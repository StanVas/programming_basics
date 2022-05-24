import webbrowser as wbb

def web_automation():
    chrome_pat = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    urls = ('apple.com', 'github')

    for url in urls:
        print('Opening:' + url)
        wbb.get(chrome_pat).open(url)

web_automation()
