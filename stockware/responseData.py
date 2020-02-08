import matplotlib.pyplot as plt
import numpy as np

class graphing:

    def lineGraph():
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
        plt.ylabel('some numbers')
        plt.show()
        
    def autolabel(ax,rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    def past_week_open_low_high(stockValue, daysList, openList, highList, lowList, closeList):
            
        fig, ax = plt.subplots()
        ax.set_title(stockValue + '\'s Opening, Low, High, and Closing Stock Values')
        ax.set_ylabel('Stock Values')
        ax.legend()

        x = np.arange(len(daysList))
        rect1 = ax.bar(x-.4, openList, width=0.2, color='y', align='center', label='Open')
        rect2 = ax.bar(x-.2, lowList, width=0.2, color='b', align='center', label='Low')
        rect3 = ax.bar(x+.2, highList, width=0.2, color='g', align='center', label='High')
        rect4 = ax.bar(x+.4, closeList, width=0.2, color='r', align='center', label='Close')
        ax.set_xticklabels(daysList)
        fig.tight_layout()

        '''graphing.autolabel(ax,rect1)
        graphing.autolabel(ax,rect2)
        graphing.autolabel(ax,rect3)
        graphing.autolabel(ax,rect4)'''
        
        plt.show()
        
        
