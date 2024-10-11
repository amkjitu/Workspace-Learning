###akhon akta jinish shikhbo seta holo: graph aka
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

##ei code ta output window er size(height width) and dpi set kore
# w = 5
# h = 4
# d = 120
# plt.figure(figsize=(w, h), dpi=d)

#points = a(x1,y1),b(x2,y2),c(x3,y3),d(x4,y4),e(x5,y5),f(x6,y6) 
#  =  xy[0]   xy[1]   xy[2]     xy[3]    xy[4]   xy[5]
#xy = [(7,6),(8,25),(9,30),(10,10),(11,5),(12,1)]

#x = [] # Time
#y = [] # People

#for i in xy:
#    x.append(i[0])
#    y.append(i[1])

#First Day; Friday
#x = [7,8,9,10,11,12] # Time
#y = [6,25,30,10,5,1] # People

#printf("%d tay manus thake %d",num1,num2)
#print("{} tay manus thake {}".format(x[0],y[0]))

#Second Day; Saterday
#x1 = [7,8,9,10,11,12] # Time
#y1 = [2,12,15,3,2,0] # People

#x and y er intercept diye scatter plot 
#plt.scatter(x,y)

#x1 and y1 er intercept diye scatter plot
#plt.scatter(x1,y1)

#graph ta show korar jonno 
#plt.show()

#x and y er intercept diye je line setar plot 
#plt.plot(x, y, c='green', label = "Friday")
#x1 and y1 er intercept diye je line setar plot
#plt.plot(x1, y1, label = "Saterday")
#x axis er labal
#plt.xlabel('Time')
#x axis er labal
#plt.ylabel('People')
#Graph er title 
#plt.title('Time VS People at the Kacha Bazar')
#Label er text guli plot e anar jonno
##X axis ar y axis er range set kora
##plt.xlim(0,3)
##plt.ylim(0,4)

#plt.legend()
#Graph ta local storage e save kora. NOTE: save obossoi plot show er age
#plt.savefig('PeopleVsTime.png')
#finally plot ta show kora

# xy = [(0,0),(4,0),(4,4),(0,4),(0,0)]

# x = []
# y = []

# for i in xy:
#     x.append(i[0])
#     y.append(i[1])

# #plt.scatter(x,y)
# #plt.plot(x,y)

# plt.show()

# ## 10 x 10 matrix 
# mat = np.arange(0,100).reshape(10,10)
# print(mat)
# #color graph of the matrix 
# plt.imshow(mat,cmap='RdYlGn')
# plt.show()

# ##10 x 10 random matrix
# mat1 = np.random.randint(0,1000,(10,10))
# #color graph of the matrix
# plt.imshow(mat1,cmap='RdYlGn')
# plt.colorbar()
# plt.show()

# ##ploting a scatter plot from a csv file directly ussing pandas
# df = pd.read_csv('./Drawable/DailyDelhiClimateTrain.csv')
# df.plot(x='meantemp', y='humidity', kind='scatter')
# plt.show()

'''
plt.style.use('ggplot')
bins = np.linspace(0, max, max)

plt.xlabel("Amount of Money")
plt.ylabel("Amount of Times")
plt.hist(listwinningprize, bins, alpha=0.5, label='Wins')
plt.hist(listlossinggprize, bins, alpha=0.5, label='Loses')
plt.legend(loc='upper right')
plt.show()
'''

'''
pen = tt.Turtle()
drawing_area = tt.Screen()

tt.pencolor("red")
tt.forward(10)
tt.left(45)

tt.pencolor("green")
tt.forward(10)
tt.right(45)

'''

##data visualization er easy tools eta, jeta notebook e kaj kore
#import pandas as pd
#import pygwalker as pyg
#df = pd.read_csv('C:/Users/HP 840 G1/Documents/VS Code Projects/Workspace Learning/#DataScience/BasicPython/Drawable/DailyDelhiClimateTest.csv')
#gwalker = pyg.walk(df)