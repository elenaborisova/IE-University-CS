# -*- coding: utf-8 -*-

# %%
import utilities

print(utilities.i)
print(utilities.name)
print(utilities.add(5, 6))


# %%
import sys

for entry in sys.path:
    print(entry)


# %%
import time

while True:
    time.sleep(0.3)
    print('hello')
