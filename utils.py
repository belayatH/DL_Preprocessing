"""
Author- Belayat Hossain, 27/3/2020, AMEC, U of Hyogo
Purpose: Export confusion matrix (with/without normalize) as figure

Call:  
    export_Plot_confusion_matrix(cf, class_name, CM_type = False, figsize = (10,7), fontsize=14) # without normalized
    export_Plot_confusion_matrix(cf_norm, class_name, CM_type = True, figsize = (10,7), fontsize=14) # with normalization
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np

def export_Plot_confusion_matrix(confusion_matrix, class_names, CM_type, figsize = (10,7), fontsize=14):
    """
    1. Calculate not normalized confusion matrix (CM) & normalized CM using "sklearn.metrics.confusion_matrix' 
        cf = confusion_matrix(testGen.classes, predIdxs) # without normalized
        cf_norm = confusion_matrix(testGen.classes, predIdxs, normalize= 'true') # with normalization
    2. Select type of CM and then export as a heatmap using seaborn.
    ---------------------------------------------------------------------------------
    Arguments:
    confusion_matrix: numpy.ndarray # returned by calling sklearn.metrics.confusion_matrix
    class_names: list # i.e. ["cat", "dog"]
    CM_type = True # True - for normalized CM plot; False - for not normalized CM
    figsize: tuple of 2-long, # figsize = (x,y), x for horizontal axis size; y = vertical axis size
    fontsize: int # Font size labels of axes
        
    Returns
    matplotlib.figure.Figure # CM as heat map as figure
    ----------------------------------------------------------------------------------------
    """

    if CM_type:
        confusion_matrix = confusion_matrix.astype('float') / confusion_matrix.sum(axis=1)[:, np.newaxis]
        print("Confusion matrix with normalization:")
        fmt = ".2f" # for float type data
        plotname = "normalize_cmatrix.png"
	
    else:
        print('Confusion matrix without normalization:')
        fmt = "d" # for int  type data in CM
        plotname = "not_normalize_cmatrix.png"

    df_cm = pd.DataFrame(confusion_matrix, index=class_names, columns=class_names)   
    fig = plt.figure(figsize=figsize)
    
    try:
        print("Saving cmatrix as png --->:", plotname)
        heatmap = sns.heatmap(df_cm, annot=True, fmt=fmt)
    except ValueError:
        # not raised an ValueError about datatype 
        raise ValueError("Check confusion matrix data type which must be integers for not normalization.")
    
    heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=fontsize)
    heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=fontsize)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    #plotname = "cmatrix.png"
    plt.savefig(plotname)
    return fig
