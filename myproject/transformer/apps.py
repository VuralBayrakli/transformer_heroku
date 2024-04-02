from django.apps import AppConfig
import pickle
from .utils import init
from .model import TransformerModel
import torch
import spacy


class TransformerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "transformer"

    def ready(self):
        from . import utils

        # İngilizce dil modelini yükleme
        utils.en_nlp = spacy.load("en_core_web_sm")
        
        utils.device = "cpu"

        with open('pickles/en_vocab.pkl', 'rb') as f:
            utils.en_vocab = pickle.load(f)

        with open('pickles/tr_vocab.pkl', 'rb') as f:
            utils.tr_vocab = pickle.load(f)

        utils.PAD_IDX = utils.en_vocab['<pad>']
        utils.BOS_IDX = utils.en_vocab['<bos>']
        utils.EOS_IDX = utils.en_vocab['<eos>']

        transformer = TransformerModel(input_dim=len(utils.en_vocab), 
                        output_dim=len(utils.tr_vocab), 
                        d_model=256, 
                        num_attention_heads=8,
                        num_encoder_layers=6, 
                        num_decoder_layers=6, 
                        dim_feedforward=2048,
                        max_seq_length=32,
                        pos_dropout=0.15,
                        transformer_dropout=0.3)

        transformer = transformer.to(utils.device)

        transformer.load_state_dict(torch.load("model/model.pt", map_location=utils.device))

        utils.model = transformer
