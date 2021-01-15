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

# # POP1 lossmodel BET plots
# Read in three csv files:
# 1. matrix_pp.csv: predicted probaility matrix created in R - gives hypothetical pp or each subject per condition. Used to creaqte a pp plot that is not inluenced by the fact that some participants only contributed to some cells 
# 2. ind_diffs_POP2.csv: contains group assignment for each participant, as matrix_pp creates values as if participant was in both groups.
# 3. full_data_pp.csv: Trial by trial data + diagnostics. Created with R. All excluded trials are removed so use this instead of actual raw data

# +
# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

import sys
sys.path.append('../../../../../')


from POP_functions import *
# -

group1=('Cash')
group2=('Credit')
correctp=load_predicted_data(group1,group2,'POP1')
data_crop=load_behav()
robust_correctp=load_predicted_data(group1,group2,'POP1',1)


# ## Machine balance plots

# +
# use uncentred name for linear variables as this is what we plot
plot_for_pop('POP1',correctp,data_crop,
             'Final.balance','Next.bet.binary', 
             [0,20,30,40,50,np.inf],
             ['','<20','30','40','>50'],
             'Machine balance ($)','p(high bet)')

plot_for_pop('POP1',robust_correctp,data_crop,
             'Final.balance','Next.bet.binary', 
             [0,20,30,40,50,np.inf],
             ['','<20','30','40','>50'],
             'Machine balance ($)','p(high bet)',1)
# -

# ## Loss streak plot

plot_for_pop('POP1',correctp,data_crop,
             'logLoss.streak','Next.bet.binary', 
             [0,1,2,3,np.inf],
             ['0','1','2','>3'],
             'log(Loss Streak)','p(High bet)')
plot_for_pop('POP1',robust_correctp,data_crop,
             'logLoss.streak','Next.bet.binary', 
             [0,1,2,3,np.inf],
             ['0','1','2','>3'],
             'log(Loss Streak)','p(High bet)',1)

# ### Histograms

plot_hist_for_pop('POP1',data_crop,'Loss.streak.outcome...zero')
plot_hist_for_pop('POP1',data_crop,'logLoss.streak')
plot_hist_for_pop('POP1',data_crop,'Trial.no')
plot_hist_for_pop('POP1',data_crop,'sqrtTrial.no')
plot_hist_for_pop('POP1',data_crop,'Final.balance')

plot_hist_for_pop('POP1',data_crop,'ISIms')
plot_hist_for_pop('POP1',data_crop,'logISI')



data_crop.loc[:,'ISIms']

data_crop.loc[:,'logISI']


