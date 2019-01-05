import os
import urllib.error
import urllib.request
import time

with open('./img_url') as f:
    for v in f:
        data = urllib.request.urlopen(v).read()
        path = os.path.join('faces', os.path.basename(v).strip('\n'))
        with open(path, mode='wb') as f:
            f.write(data)

        time.sleep(1)