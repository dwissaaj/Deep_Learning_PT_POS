import re

def url(data):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    data = url_pattern.sub(r'', data)
    return data

def email(data):
    data = re.sub('\S*@\S*\s?', '', data)
    return data

