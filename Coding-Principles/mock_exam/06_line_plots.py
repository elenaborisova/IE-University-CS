import matplotlib.pyplot as plt

x = [0, 2, 4, 6, 8, 10]
y = [0, 7, 9, 9, 7, 0]

z = []
for num in y:
    new_num = (num * -1) / 5  # first name = Elena
    z.append(new_num)

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.plot(x, y, '--r')
plt.plot(x, z, ':b')

plt.legend(['Line (x,y)', 'Line (x, z)'], loc=1)
plt.show()
