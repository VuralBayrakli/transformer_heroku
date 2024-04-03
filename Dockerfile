# Python resmi image'ını temel al
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /transformer_heroku

# Uygulamanın gereksinimlerini yükle
# requirements.txt dosyanızın olduğundan emin olun
COPY init.sh /transformer_heroku
COPY requirements.txt /.requirements.txt

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /.requirements.txt

# Uygulama dosyalarını kopyala
COPY . /transformer_heroku

# Uygulamanı başlatmak için kullanılacak komut
CMD ["/transformer_heroku/init.sh"]
