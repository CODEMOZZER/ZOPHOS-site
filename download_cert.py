import urllib.request

url = "https://cockroachlabs.cloud/clusters/2c05540a-7a52-4dd9-bc42-48dce2e323e0/cert"
dest = "/app/root.crt"

urllib.request.urlretrieve(url, dest)
