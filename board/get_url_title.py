import requests


def get_title(url):
    """Gets the url page title

    Args:
        url (string): url

    Returns:
        string: url title
    """
    hearders = {
        "headers": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0"
    }
    n = requests.get(url, headers=hearders)
    al = n.text
    title = al[al.find("<title>") + 7 : al.find("</title>")]
    # if title is empty return url instead
    if title.isspace() or len(title) == 0:
        return url
    else:
        return title
