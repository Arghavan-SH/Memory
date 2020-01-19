# -*- coding: utf-8 -*-
"""Copy of Decision Making V2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FA_-xaSXLnhYDMRpTZA7m4Iu6BgAcBvC
"""

from google.colab import drive
drive.mount('/gdrive')

ls

cd ..

cd /gdrive/My\ Drive/

cd dataset/

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statistics 
from scipy import stats
df=pd.read_csv('exp1testing.csv')

delay =pd.get_dummies(df['delay'],drop_first=True)
length= pd.get_dummies(df['length'],drop_first=True)
block= pd.get_dummies(df['block'])
target= pd.get_dummies(df['type'])
wf=pd.get_dummies(df['wf'],drop_first=True)

df1 = pd.concat([df,delay,length,wf,target,block],axis=1)
df1.drop(['lure','response','trial','type','wf','length','delay','block','subj'],axis=1,inplace=True)

df1.shape

"""# LETS TAKE LOOK AT EACH ATTRIBUTE"""

df1_b0=df1.loc[df1['b0']==1]
df1_b1=df1.loc[df1['b1']==1]
df1_b2=df1.loc[df1['b2']==1]
df1_b3=df1.loc[df1['b3']==1]
df1_Immed=df1.loc[df1['Immed']==1]
df1_delay=df1.loc[df1['Immed']==0]
df1_LF=df1.loc[df1['LF']==1]
df1_HF=df1.loc[df1['LF']==0]
df1_short=df1.loc[df1['Short']==1]
df1_long=df1.loc[df1['Short']==0]
df1_target=df1.loc[df1['target']==1]
df1_lure=df1.loc[df1['target']==0]
names=['RT','correct','Immed','Short','LF','target','b0','b1','b2','b3']

f1_b0_list=df1_b0.mean().tolist()
f1_b1_list=df1_b1.mean().tolist()
f1_b2_list=df1_b2.mean().tolist()
f1_b3_list=df1_b3.mean().tolist()
f1_Immed_list=df1_Immed.mean().tolist()
f1_delay_list=df1_delay.mean().tolist()
f1_LF_list=df1_LF.mean().tolist()
f1_HF_list=df1_HF.mean().tolist()
f1_short_list=df1_short.mean().tolist()
f1_long_list=df1_long.mean().tolist()
f1_target_list=df1_target.mean().tolist()
f1_lure_list=df1_lure.mean().tolist()

d = {'target':f1_target_list,'lure':f1_lure_list,'long':f1_long_list,'short':f1_short_list,'HF':f1_HF_list,'LF':f1_LF_list,
     'Immed':f1_Immed_list,'delay':f1_delay_list,'b0': f1_b0_list, 
     'b1': f1_b1_list,'b2': f1_b2_list, 
     'b3': f1_b3_list,'names':names}
df_indiv= pd.DataFrame(data=d)
df_indiv

df_indiv.describe()

tc =df_indiv.corr()
fig, ax = plt.subplots(figsize=(10,10)) 
sns.heatmap(tc,annot=True,ax=ax)

tc =df_indiv.cov()
fig, ax = plt.subplots(figsize=(10,10)) 
sns.heatmap(tc,annot=True,ax=ax)

sns.pairplot(df_indiv)

"""# WE CAN DO THIS FOR EACH SUBJECT"""

df=pd.read_csv('exp1testing.csv')

delay =pd.get_dummies(df['delay'],drop_first=True)
length= pd.get_dummies(df['length'],drop_first=True)
block= pd.get_dummies(df['block'])
target= pd.get_dummies(df['type'])
wf=pd.get_dummies(df['wf'],drop_first=True)

df1 = pd.concat([df,delay,length,wf,target,block],axis=1)
df1.drop(['lure','response','trial','type','wf','length','delay','block'],axis=1,inplace=True)

df1=df1.loc[df['subj']==0]
df1.drop(['subj'],axis=1,inplace=True)

df1_b0=df1.loc[df1['b0']==1]
df1_b1=df1.loc[df1['b1']==1]
df1_b2=df1.loc[df1['b2']==1]
df1_b3=df1.loc[df1['b3']==1]
df1_Immed=df1.loc[df1['Immed']==1]
df1_delay=df1.loc[df1['Immed']==0]
df1_LF=df1.loc[df1['LF']==1]
df1_HF=df1.loc[df1['LF']==0]
df1_short=df1.loc[df1['Short']==1]
df1_long=df1.loc[df1['Short']==0]
df1_target=df1.loc[df1['target']==1]
df1_lure=df1.loc[df1['target']==0]
names=['RT','correct','Immed','Short','LF','target','b0','b1','b2','b3']
f1_b0_list=df1_b0.mean().tolist()
f1_b1_list=df1_b1.mean().tolist()
f1_b2_list=df1_b2.mean().tolist()
f1_b3_list=df1_b3.mean().tolist()
f1_Immed_list=df1_Immed.mean().tolist()
f1_delay_list=df1_delay.mean().tolist()
f1_LF_list=df1_LF.mean().tolist()
f1_HF_list=df1_HF.mean().tolist()
f1_short_list=df1_short.mean().tolist()
f1_long_list=df1_long.mean().tolist()
f1_target_list=df1_target.mean().tolist()
f1_lure_list=df1_lure.mean().tolist()
d = {'target':f1_target_list,'lure':f1_lure_list,'long':f1_long_list,'short':f1_short_list,'HF':f1_HF_list,'LF':f1_LF_list,
     'Immed':f1_Immed_list,'delay':f1_delay_list,'b0': f1_b0_list, 
     'b1': f1_b1_list,'b2': f1_b2_list, 
     'b3': f1_b3_list,'names':names}
df_subj0= pd.DataFrame(data=d)
df_subj0

"""#Scaling RT"""

df1=pd.read_csv('exp1testing.csv')

delay =pd.get_dummies(df1['delay'],drop_first=True)
length= pd.get_dummies(df1['length'],drop_first=True)
block= pd.get_dummies(df1['block'])
target= pd.get_dummies(df1['type'])
wf=pd.get_dummies(df1['wf'],drop_first=True)
df2 = pd.concat([df1,delay,length,wf,target,block],axis=1)
df2.drop(['type','wf','length','delay','trial','lure','response','block','subj'],axis=1,inplace=True)

df2.shape



"""Desision Tree"""



from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from IPython.display import Image
from sklearn.externals.six import StringIO
import pydot
from sklearn.metrics import classification_report,confusion_matrix
X=df2[[ 'Immed', 'Short', 'LF', 'target', 'b0','b1','b2','b3']]
y=df2['correct']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

dtc=DecisionTreeClassifier()
dtc.fit(X_train,y_train)
predict_dtc = dtc.predict(X_test)
print(confusion_matrix(y_test,predict_dtc))
print('\n')
print(classification_report(y_test,predict_dtc))

features=[ 'Immed','target','Short', 'b0','b1','b2','b3','LF']

clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,y)

dot_data=StringIO()
tree.export_graphviz(clf,out_file=dot_data,feature_names=features)

(graph,) = pydot.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())



"""# Test arghavan"""

from random import shuffle
X=df2[[ 'Immed', 'Short', 'LF', 'target', 'b0','b1','b2','b3']]
print(X)