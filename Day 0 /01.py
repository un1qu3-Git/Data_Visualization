#A simple program to plot points in graph (user entered data)
import matplotlib.pyplot as plt
list = []
while True:
        a = input("Do you want to continue? (yes/no): ")
        if a == 'no':
            break
        else:
            v = int(input('Enter a number '))
            list.append(v)

plt.plot(list)
plt.title(list)
plt.show()
        
        
        
