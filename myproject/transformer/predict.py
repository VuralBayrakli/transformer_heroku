from .utils import en_vocab, tr_vocab, PAD_IDX, BOS_IDX, EOS_IDX, model, en_nlp, device
import torch

MAX_SENTENCE_LENGTH = 32



def tokenize_en(text):
    return [tok.text for tok in en_nlp.tokenizer(text)]

def predict_transformer(text, model, 
                        src_vocab=en_vocab, 
                        src_tokenizer=tokenize_en, 
                        tgt_vocab=tr_vocab, 
                        device=device):
    
    input_ids = [src_vocab[token.lower()] for token in src_tokenizer(text)]
    input_ids = [BOS_IDX] + input_ids + [EOS_IDX]
    
    model.eval()
    with torch.no_grad():
        input_tensor = torch.tensor(input_ids).to(device).unsqueeze(1) 
        
        causal_out = torch.ones(MAX_SENTENCE_LENGTH, 1).long().to(device) * BOS_IDX
        for t in range(1, MAX_SENTENCE_LENGTH):
            decoder_output = model(input_tensor, causal_out[:t, :])[-1, :, :]
            next_token = decoder_output.data.topk(1)[1].squeeze()
            causal_out[t, :] = next_token
            if next_token.item() == EOS_IDX:
                break
                
        pred_words = [tgt_vocab.lookup_token(tok.item()) for tok in causal_out.squeeze(1)[1:(t)]]
        return " ".join(pred_words)
