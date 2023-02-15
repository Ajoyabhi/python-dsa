d = {1 :['A','B'], 2 : ['C','B'], 4: ['C','D','E']}

d_swap = {v: k for k, v in d.items()}
print(d_swap)
# {'val1': 'key1', 'val2': 'key2', 'val3': 'key3'}