import matplotlib.pyplot as plot
# set up your lists
numlist = [18.3, 12.3, 6.3, 3.3]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['red', 'green', 'pink', 'yellow' ]
explodelist = [0.0, 0.0, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.2f%%', colors=colorlist,
    	explode = explodelist, startangle = 90)
plot.axis('equal')
plot.savefig('CS162piechart.png')
