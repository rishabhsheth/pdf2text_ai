import torch
print(torch.cuda.is_available())           # should return True
print(torch.version.cuda)                  # should show 12.9
print(torch.backends.cudnn.version())     # shows cuDNN version
print(torch.cuda.get_device_name(0))      # should print RTX 4060
print(torch.cuda.memory_allocated(0))    # should be 0 if no tensors on GPU
print(torch.cuda.memory_reserved(0))     # should be 0 if no tensors on GPU
# show number of tensor cores
print(torch.cuda.get_device_properties(0).multi_processor_count)  # should be >= 16         