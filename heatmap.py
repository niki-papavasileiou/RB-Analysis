import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

pd.options.mode.chained_assignment = None

df = pd.read_csv('High_MEO_FEDO.csv')

df['epoch'] = pd.to_datetime(df['epoch']).dt.date
df = df.set_index('epoch')   

df['fedo_1'][df['fedo_1']< 0] = np.nan
#df = df[df['fedo_1'].notna()]

df['fedo_2'][df['fedo_2']< 0] = np.nan
#df = df[df['fedo_2'].notna()]

df['fedo_3'][df['fedo_3']< 0] = np.nan 
df = df[df['fedo_3'].notna()]

df = df.loc[(df['odi_unilib_l'] > 1 ) & (df['odi_unilib_l'] < 8) &(df['odi_unilib_alpha_eq']<90)  &(df['odi_unilib_alpha_eq']>0) ]

startdate = pd.to_datetime("2006-01-10 23:50:13").date()
enddate = pd.to_datetime("2010-10-13 12:07:53").date()
date= df.loc[startdate:enddate]
l = date['odi_unilib_l']


date['epoch'] = date.index
df_new = date.filter(['epoch','odi_unilib_l','fedo_3'], axis= 1 )
fedo3= df_new['fedo_3'] 

df_new.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3) ,colorbar = True)
plt.show()
