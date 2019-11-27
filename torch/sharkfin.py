'''
Applies the sharkfin function element-wise:
sharkfin(x) = tanh(e^{x}) * relu(-1, x) = tanh(e^{x}) * max(-1,x)
'''

# import pytorch
from torch import nn

# import sharkfin function definition
import torch.functional as Func

class SharkFin(nn.Module):
    '''
    Applies the sharkfin function element-wise:
    sharkfin(x) = tanh(e^{x}) * relu(-1, x) = tanh(e^{x}) * max(-1,x)

    Shape:
        - Input: (N, *) where * means, any number of additional
          dimensions
        - Output: (N, *), same shape as the input

    Examples:
        >>> m = SharkFin()
        >>> input = torch.randn(2)
        >>> output = m(input)

    '''
    def __init__(self):
        '''
        Init method.
        '''
        super().__init__()

    def forward(self, input):
        '''
        Forward pass of the function.
        '''
        return Func.sharkfin(input)
