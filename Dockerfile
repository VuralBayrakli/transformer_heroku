# Python resmi image'ını temel al
FROM python:3.8-slim

# Çalışma dizinini ayarla
WORKDIR /transformer_heroku

# Uygulamanın gereksinimlerini yükle
# requirements.txt dosyanızın olduğundan emin olun
COPY init.sh /transformer_heroku
COPY requirements.txt /.requirements.txt
RUN pip install -r /.requirements.txt

# Uygulama dosyalarını kopyala
COPY . /transformer_heroku

# Uygulamanı başlatmak için kullanılacak komut
CMD ["/transformer_heroku/init.sh"]
