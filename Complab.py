import matplotlib.pyplot as plt

years = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
sales = [100000, 120000, 80000, 96000, 115200, 138240, 165888]

plt.figure(figsize=(10, 6)) 

plt.title('Juniper Flower Shop Sales Over the Years')
plt.xlabel('Year')
plt.ylabel('Sales Amount ($)')

plt.xticks(years)
plt.yticks(range(0, 200000, 20000))

plt.grid(True)
plt.plot(years,sales)
plt.show()
