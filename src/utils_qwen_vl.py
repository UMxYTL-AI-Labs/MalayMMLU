import torch
import torch.nn.functional as F
import numpy as np


def softmax(x):
    z = x - max(x)
    numerator = np.exp(z)
    denominator = np.sum(numerator)
    softmax = numerator/denominator
    return softmax


@torch.no_grad()
def get_logprobs_causal(model, processor, prompt, device):
    torch.manual_seed(42)
    inputs = processor(text=[prompt], return_tensors="pt")
    if model.config.model_type == 'falcon':
        inputs.pop("token_type_ids")
        
    input_ids, output_ids = inputs["input_ids"].to(device), inputs["input_ids"][:, 1:].to(device)
    for k, v in inputs.items():
        inputs[k] = v.to(device)
    outputs = model(**inputs, labels=input_ids)

    logits = outputs.logits.to(torch.double).to(device)
    output_ids = output_ids.to(logits.get_device()) 
    logprobs = torch.gather(F.log_softmax(logits, dim=2), 2, output_ids.unsqueeze(2))
    
    return logprobs.mean()

def predict_classification_causal(model, processor, input_text, labels, device):
    torch.manual_seed(42)
    probs = [get_logprobs_causal(model, processor, input_text+label, device) for label in labels]
    return probs

def predict_classification_causal_by_letter(model, processor, input_text, labels, device):
    torch.manual_seed(42)
    choices = ['A', 'B', 'C', 'D', 'E'][:len(labels)]
    #choice_ids = [processor(text=[choice])[-1] for choice in choices]
    
    choice_ids = []
    for choice in choices:
        choice_id = processor(text=[choice])['input_ids'][0][0]
        choice_ids.append(choice_id)

    with torch.no_grad():
        inputs = processor(text=[input_text], return_tensors="pt")
        input_ids = inputs["input_ids"].to(device)
        if model.config.model_type == 'falcon':
            inputs.pop("token_type_ids")
        for k, v in inputs.items():
            inputs[k] = v.to(device) 
        outputs = model(**inputs, labels=input_ids)
        last_token_logits = outputs.logits[:, -1, :]
        choice_logits = last_token_logits[:, choice_ids].detach().cpu().numpy()
        conf = softmax(choice_logits[0])
        pred = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}[np.argmax(choice_logits[0])]
    return conf, pred

