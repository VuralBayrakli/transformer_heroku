#!/bin/bash
# SpaCy dil modelini indir
python -m spacy download en_core_web_sm
# Django sunucusunu çalıştır
python myproject/manage.py runserver 0.0.0.0:8000
