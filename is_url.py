def is_url(text):
    from urllib.parse import urlparse

    parsed_url = urlparse(text)
    return bool(parsed_url.scheme) and bool(parsed_url.netloc)
