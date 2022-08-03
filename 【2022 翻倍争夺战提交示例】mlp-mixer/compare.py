from model import *

import json
from glob import glob
import numpy as np
import torch
import torchvision
import timm


def read_image(path):
    img = torchvision.io.read_image(path)
    img = img.float() / 255
    img = torchvision.transforms.functional.resize(img, 224)
    img = torchvision.transforms.functional.center_crop(img, 224)
    img = torchvision.transforms.functional.normalize(img, [0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
    return img.numpy()


def softmax(logits):
    logits = logits - logits.max(-1, keepdims=True)
    exp = np.exp(logits)
    return exp / exp.sum(-1, keepdims=True)


model = MLPMixer(num_blocks=12, embed_dim=768)
torch_model = timm.models.mlp_mixer.mixer_b16_224(pretrained=True)
model.load_from_torch(torch_model.state_dict())

data = np.stack([read_image(path) for path in glob('data/*.jpg')])
print(f'input shape {data.shape} max {data.max()} min {data.min()}')
text_labels = json.load(open('imagenet-labels.json'))

logits = model(mge.tensor(data)).numpy()
torch_model.train(False)
with torch.no_grad():
    torch_logits = torch_model(torch.tensor(data)).numpy()

np.testing.assert_allclose(torch_logits, logits, rtol=1e-3)

print()
print('torch')
print('megengine')
print()
for p1, p2 in zip(softmax(torch_logits), softmax(logits)):
    print(text_labels[p1.argmax()], p1.max())
    print(text_labels[p2.argmax()], p2.max())
    print()
