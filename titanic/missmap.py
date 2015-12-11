import pandas as pd

import numpy as np
import matplotlib.pyplot as plt


def missmap(df, ax=None):
    if ax is None:
        fig, ax = plt.subplots()
    dfn = pd.isnull(df)
    ny = len(df)
    nx = len(df.columns)
    dfn = pd.isnull(df)
    x = np.arange(len(df.columns))
    xgrid = np.tile(x, (len(df), 1)).T
    c = {True: 'y', False: 'k'}
    ax.set_xlim(0, nx)
    for x, col in zip(xgrid, dfn.columns):

        yvals = dfn[col]
        ax.bar(x, yvals, bottom=np.arange(1, ny+1), width=1,
               color=dfn[col].map(c), edgecolor=dfn[col].map(c))
    ax.set_xticks(.5 + np.arange(nx))
    ax.set_xticklabels(dfn.columns)
    for t in ax.get_xticklabels():
        t.set_rotation(90)
    return ax
