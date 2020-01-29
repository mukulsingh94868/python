d = {'pen':0.24,'notebook':1,'calculator':50}
print(d)
d['pen'] = 5
print(d)
print(d['notebook'])
print(d['pen'])
print(d['calculator'])
del d['calculator']
del d['pen']

print(d)
list(d.keys())