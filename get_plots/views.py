from django.shortcuts import render

import numpy as np
import matplotlib.pyplot as plt
import io
import urllib, base64
from json import load
from scipy.spatial.distance import cosine, euclidean, correlation, cityblock

# Create your views here.



def home(request):
    # if you are running a webserver
    # and using it to save Matplotlib
    # make sure to set the backend to a non-interactive one
    # so that your server does not try to create (and then destroy)
    # GUI windows that will never be seen
    plt.switch_backend('Agg')

    # plot setup
    # plt.plot(range(100))
    fig = plt.figure()
    ax1 = fig.add_subplot()
    x=range(1984, 1995)
    y1=[10, 11, 9, 7, 6, 8, 3, 5, 4, 2, 1]
    y2=[1, 2, 4, 5, 3, 8, 6, 7, 9, 11, 10]
    # plt.scatter(x, y1, label="word1")
    ax1.scatter(x, y1, label="word1")
    ax1.scatter(x, y2, label="word2")
    
    # word1 trend line
    z = np.polyfit(x, y1, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), 'b--')

    # word2 trend line
    z2 = np.polyfit(x, y2, 1)
    p2 = np.poly1d(z2)
    plt.plot(x, p2(x), 'r--')

    
    # plot labels
    plt.title("diachronic word vector distance with respect to word1 and word2", fontdict={'fontsize':13})
    plt.xlabel('year')
    plt.ylabel('cosine distance')
    plt.legend()

    #convert graph into string buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return render(request,'get_plots/home.html',{'data':uri})
