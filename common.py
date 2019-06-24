# -*- coding: utf-8 -*-

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

sns.set(style="whitegrid")


def produce_sns_plot(result, kind):
    """Save plot of result

    Parameters:
    result: data to draw
    kind: type of data used to plot
    """

    sns.barplot([u"\"{}\"".format(i[0]) for i in result], [i[1] for i in result])
    plt.ylabel('total')
    plt.xlabel('term')
    # change the font to one that support Japanese and Korean characters
    plt.xticks(rotation=90, fontsize=18, fontname='Arial Unicode MS')
    plt.yticks(fontsize=18)
    plt.title("Top {}{} from a sample of tweets containing the hashtag \"#BringBackNationalDex\" ".format(kind, 's'), 
              fontsize=18)
    plt.subplots_adjust(bottom=0.30)
    plt.savefig("plots/{}.png".format(kind), dpi=300)
    plt.show()
