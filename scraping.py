from urllib.request import Request, urlopen


def get_page(url):

    req = Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")

    return urlopen(req).read()
