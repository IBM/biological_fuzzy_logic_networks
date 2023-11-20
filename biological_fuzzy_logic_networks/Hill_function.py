"""A Pytorch module defining a Hill function"""

__copyright__ = """
LICENSED INTERNAL CODE. PROPERTY OF IBM.
IBM Research Licensed Internal Code
(C) Copyright IBM Corp. 2021
ALL RIGHTS RESERVED
"""

import torch

torch.set_default_tensor_type(torch.DoubleTensor)


class HillTransferFunction(torch.nn.Module):
    """Apply a Hill transformation on 1D input"""

    def __init__(self):
        """
        Initialise the parameters if the transfer functino
        """
        torch.nn.Module.__init__(self)

        self.n = torch.nn.Parameter(torch.normal(mean=1.3, std=0.4, size=(1,)))
        self.K = torch.nn.Parameter(torch.normal(mean=-0.7, std=0.4, size=(1,)))

    def forward(self, x):
        """
        Tranforms a value through the transfer function
        Args:
            x = value to be transformed
        """
        # I want to constrain K and n to be positive
        # Hence I'll feed them into an exponential
        output = (x ** (1 + torch.exp(self.n))) / (
            torch.exp(self.K) ** (1 + torch.exp(self.n)) + x ** (1 + torch.exp(self.n))
        )

        self.output_value = output
        return output
