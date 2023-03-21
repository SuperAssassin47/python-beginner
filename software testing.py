import urllib.request


def connect(host='http://nxgconnect.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


print('Success! Connected!' if connect() else 'no connections made!!')
