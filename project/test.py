import os
a = 'C:\\Users\\danie\\PycharmProjects\\mgr\\project\\frames'

files = [f for f in os.listdir(a) if os.path.isfile(os.path.join(a, f))]
files.sort(key=lambda x: int(x[5:-4]))
for filename in files:
    print(filename)