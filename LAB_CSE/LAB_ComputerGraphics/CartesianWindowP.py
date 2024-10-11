import matplotlib.pyplot as plt
class CWindow:

    @staticmethod
    def __init__(height, widht):
        h=height
        w=widht

        x_axis_x=[-w,w]
        x_axis_y=[0,0]

        y_axis_x=[0,0]
        y_axis_y=[-h,h]

        plt.style.use('bmh')

        plt.plot(x_axis_x,x_axis_y,color='k')
        plt.plot(y_axis_x,y_axis_y,color='k')

        plt.xlabel('X')
        plt.ylabel('Y')

        plt.xticks(range(-w,w+1))
        plt.yticks(range(-h,h+1))



    