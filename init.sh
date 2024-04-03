#!/bin/bash
# SpaCy dil modelini indir
python -m spacy download en_core_web_sm
# Django sunucusunu çalıştır
gunicorn myproject.wsgi:application
