from urllib.parse import urlparse


def domain_name(url):
    if not url.startswith("http"):
        url = "https://" + url
    return urlparse(url).netloc.replace("www.", "").split('.')[0]
