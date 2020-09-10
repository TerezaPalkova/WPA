import os
import requests
from bs4 import BeautifulSoup


def download(url: str, dest_folder: str):
    """
        This funcion downloads pictures from website and save them as .jpeg files
        :param url: str,  URL adrdress from which you want pictures
        :param dest_folder: str,   path to folder, where you want to save your pictures
        """
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    res = requests.get(url)
    html_doc = res.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    urls = soup.find_all("img")
    for one in urls:
        one_url = one.get('src')
        if one_url.startswith("http"):
            pass
        else:
            one_url = (f"{url}{one_url}")
        # toto nieje uplne korektne   kedze nie kazdy obrazok musi byt jpeg..
        # chyba tu osetrenie a overenie, ci ten url je ozaj obrazok
        # pri www.sme.sk to pada na:
        #  urllib3.exceptions.LocationParseError: Failed to parse: https://www.sme.skdata:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
        img_name = one_url.split("/")[-1] + ".jpeg"
        file_path = os.path.join(dest_folder, img_name)
        r = requests.get(one_url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(file_path, 'wb'):
               print('Image sucessfully Downloaded: ', img_name)
        else:
            print('Image Couldn\'t be retreived')


download(input("Please write your ULR address: "), input("Please write path: "))


#nedavala som if __name__ == "__main__":  aby ti rovno isiel input
