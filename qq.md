Username: lemon1964
Password: 
Login Succeeded
(.venv) (base) lemon@MacBook-Air-Lemon MySite % docker push lemon1964/mysite:latest

The push refers to repository [docker.io/lemon1964/mysite]
481b9167b771: Preparing 
3489f2399569: Preparing 
58cff3df4143: Preparing 
c81e5190b3a6: Preparing 
42001edc536b: Preparing 
ea178852b3c6: Waiting 
a0115e3405be: Waiting 
c81e5190b3a6: Pushed 
bfc1deb8136e: Mounted from library/python 
1f123186824c: Mounted from library/python 
3d6eb1152931: Mounted from library/python 
100796cdf3b1: Mounted from library/python 
54acb5a6fa0b: Mounted from library/python 
8d51c618126f: Mounted from library/python 
9ff6e4d46744: Mounted from library/python 
a89d1d47b5a1: Mounted from library/python 
655ed1b7a428: Mounted from library/python 
latest: digest: sha256:37a92766770a8c7d2c68ccaa0f4a1a9892edbdd9c825b587f8a5c281bbebec96 size: 3891

на https://hub.docker.com/repositories/lemon1964
образ появился

(.venv) (base) lemon@MacBook-Air-Lemon MySite % docker pull lemon1964/mysite:latest

latest: Pulling from lemon1964/mysite
Digest: sha256:37a92766770a8c7d2c68ccaa0f4a1a9892edbdd9c825b587f8a5c281bbebec96
Status: Image is up to date for lemon1964/mysite:latest
docker.io/lemon1964/mysite:latest

What's Next?
  View a summary of image vulnerabilities and recommendations → docker scout quickview lemon1964/mysite:latest

(.venv) (base) lemon@MacBook-Air-Lemon MySite % docker run -d -p 8000:8000 lemon1964/mysite:latest
7d63a75e75bbfb84662effb67797f8d2714fdde4c06cf2f74266192796854e6e

Где можно посмотреть?
Контейнеры все остановлены
на
http://localhost:8000/
https://mysite.com/
Не удается получить доступ к сайту