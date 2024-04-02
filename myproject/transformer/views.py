from django.shortcuts import render
from io import open
import unicodedata
import string
import re
import random
import os
import torch
from torch import nn
import torch.nn.functional as F
from torch.nn.utils.rnn import pad_sequence
import pickle
import spacy
from .forms import TranslationForm
from .utils import en_vocab, tr_vocab, PAD_IDX, BOS_IDX, EOS_IDX, model
from .predict import predict_transformer

def translate_text(request):
    translated_text = ""
    if request.method == "POST":
        form = TranslationForm(request.POST)
        if form.is_valid():
            text_to_translate = form.cleaned_data['text_to_translate']
            # Burada çeviri modelinizi çağırın. Şimdilik yer tutucu bir metin döndürelim.
            translated_text = predict_transformer(text_to_translate, model)  # Örnek yer tutucu çeviri
    else:
        form = TranslationForm()
    
    context = {
        'form': form,
        'translated_text': translated_text,
        
    }

    return render(request, 'translate.html', context)

def index(request):
    return render(request, "home.html", {"name": "Vural"})