FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


RUN set -eux; \
        apt-get update; \
        apt-get install -y --no-install-recommends \
                libgl1-mesa-glx \
                ffmpeg \
        ; \
        rm -rf /var/lib/apt/lists/*


COPY ./ /usr/src/app

CMD ["gunicorn", "--bind" , "213.226.117.171:8090","--workers=4","--timeout","600", "routes:app"]