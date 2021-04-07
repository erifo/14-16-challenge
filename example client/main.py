import requests 

def upload(filename):
    """Currently unable to send an image correctly"""
    url = "http://127.0.0.1:8000/post/" + filename
    with open(filename, 'rb') as image:
        files = {'media': image}
        requests.post(url, files=files)


def main():
    """Example of usage"""
    upload("./duck2.png")


if __name__ == "__main__":
    main()