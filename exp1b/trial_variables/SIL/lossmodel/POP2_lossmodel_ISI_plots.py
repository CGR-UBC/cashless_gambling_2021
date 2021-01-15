# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## POP2 loss model ISI plots

# +
# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

import sys
sys.path.append('/Users/eoldfiel/Data/github/painofpaying')

from POP_functions import *
# -

group1=('Windfall')
group2=('Earned')
correctp=load_predicted_data(group1,group2,'POP2')
data_crop=load_behav()
robust_correctp=load_predicted_data(group1,group2,'POP2',1)

# use uncentred name for linear variables as this is what we plot
plot_for_pop('POP2',robust_correctp,data_crop,
             'Final.balance','logISI', 
             [0,20,30,40,50,np.inf],
             ['','<20','30','40','>50'],
             'Machine balance ($)','log(Spin initiation latency)',1)

plot_for_pop('POP2',correctp,data_crop,
             'logLoss.streak','logISI', 
             [0,1,2,3,np.inf],
             ['0','1','2','>3'],
             'log(Loss Streak)','log(Spin initiation latency)')


# use uncentred name for linear variables as this is what we plot
plot_for_pop('POP2',correctp,data_crop,
             'Final.balance','logISI', 
             [0,20,30,40,50,np.inf],
             ['','<20','30','40','>50'],
             'Machine balance ($)','log(Spin initiation latency)')

plot_for_pop('POP2',robust_correctp,data_crop,
             'logLoss.streak','logISI', 
             [0,1,2,3,np.inf],
             ['0','1','2','>3'],
             'log(Loss Streak)','log(Spin initiation latency)',1)

plot_hist_for_pop('POP2',data_crop,'Loss.streak.outcome...zero')
plot_hist_for_pop('POP2',data_crop,'logLoss.streak')
plot_hist_for_pop('POP2',data_crop,'Trial.no')
plot_hist_for_pop('POP2',data_crop,'sqrtTrial.no')
plot_hist_for_pop('POP2',data_crop,'Final.balance')
plot_hist_for_pop('POP2',data_crop,'logISI')
plot_hist_for_pop('POP2',data_crop,'ISIms')



