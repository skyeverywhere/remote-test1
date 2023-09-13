import torch
import torch.nn
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
a = torch.from_numpy(a)

print(a)
a = a.reshape(3, 2)
print(a)

a = torch.permute(a, dims=(1, 0))
print(a)
