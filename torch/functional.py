'''
Script provides functional interface for SharkFin activation function.
'''

# import pytorch
import torch
import torch.nn.functional as F

def sharkfin(input):
    '''
    Applies the sharkfin function element-wise:
    sharkfin(x) = tanh(e^{x}) * relu(-1, x) = tanh(e^{x}) * max(-1,x)
    '''
    return F.tanh(torch.exp(input)) * torch.clamp(input, min=-1)
