import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def pieChart(hashtag, pos, neg):
    labels = ['Positive', 'Negative']
    sizes = [pos, neg]
    colors = ['lime', 'red']
    explode=(0.1,0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title(hashtag, size=15)
    plt.legend(labels)
    plt.show()
    
    """
    axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
    
    text_box = TextBox(axbox, 'Enter Hashtag', initial=initial_text)
    text_box.on_submit(submit)
    """
pieChart("asd", 34, 66)



