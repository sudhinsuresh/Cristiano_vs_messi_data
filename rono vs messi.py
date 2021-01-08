#!/usr/bin/env python
# coding: utf-8

# In[83]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[84]:


df=pd.read_csv(r'E:\my\rono_vs_messi.csv')


# In[85]:


df.info()


# In[86]:


df.head(30)


# In[87]:


df.columns


# In[88]:


df['comp']=df['comp'].ffill()
df['roung']=df['round'].ffill()
df['date']=df['date'].ffill()
df['venue']=df['venue'].ffill()
df['opp']=df['opp'].ffill()
df.info()


# In[89]:


df['min']=df['min'].apply(lambda x:x.replace("'",''))
df['min']=df['min'].apply(lambda x:x.replace("+",''))
df['min'].unique()


# In[90]:


df.info()


# In[91]:


df['min']=pd.to_numeric(df['min'])
df['time_class']=df['min'].apply(lambda x:'first_half' if x<=45 else ('secound_half' if 45<x<=90 else 'extra_time'))
df.head(20)


# In[92]:


df['assist']=df['assisted'].fillna(0)
df['solo']=df['assist'].apply(lambda x:'solo' if x==0 else 'assisted')
df.head(20)


# In[93]:


df['player'].value_counts()


# In[94]:


df_ronaldo=df.loc[df['player']=='ronaldo']
df_messi=df.loc[df['player']=='messi']
ronaldo_solo=df_ronaldo[df_ronaldo['solo']=='solo']
ronaldo_assisted=df_ronaldo[df_ronaldo['solo']=='assisted']
slices=[len(ronaldo_solo),len(ronaldo_assisted)]
labels=['solo','assisted']
#
messi_solo=df_messi[df_messi['solo']=='solo']
messi_assisted=df_messi[df_messi['solo']=='assisted']
slices1=[len(messi_solo),len(messi_assisted)]
labels1=['solo','assisted']
#
fig, axes =plt.subplots(1 , 2, figsize=(15, 5), sharey=False)
fig.suptitle('Cristiano Vs Messi/solo & Assisted')
axes[0].pie(slices,labels=labels,startangle=90,shadow=1,explode=(0,0.4),autopct='%.2f%%',colors=['#808080','#F2EBED']);
axes[0].set_title('Cristiano Ronaldo')
axes[1].pie(slices1,labels=labels1,startangle=90,shadow=1,explode=(0,0.4),autopct='%1.2f%%',colors=['#7868DF']);
axes[1].set_title('Lionel Messi');


# In[95]:


r_goal=pd.DataFrame(df_ronaldo['date'].value_counts().sort_values(ascending=False))
r_goal['nick']=r_goal['date'].apply(lambda x:'hatrick' if x==3 else ('haul' if x==4 else ('glut' if x==5 else ('brace' if x ==2 else 'single goal'))))
r_goal.head()


# # home and away goals

# In[96]:


plt.figure(figsize=(14,7))
sns.countplot(data=df,x='player',hue='venue',palette="Paired").set_title('Cristano Vs Messi (Home & Away)');


# # goal type

# In[97]:


plt.figure(figsize=(24,7))
sns.countplot(data=df,x='type',hue='player',palette="hls").set_title('Cristano Vs Messi (Goal Type)');


# In[98]:


plt.figure(figsize=(25,7))
sns.countplot(data=df,x='pos',hue='player',palette="cubehelix").set_title('Cristano Vs Messi (Goalposition)');


# # best friends to Cristiano & Messi

# In[99]:


r_assist =df_ronaldo['assisted'].value_counts()
r_assist = r_assist[:10]
sns.set_style("darkgrid")
plt.figure(figsize=(20,6));
r_assist_vis = sns.barplot(r_assist.index, r_assist.values, alpha=0.8,palette='winter');
plt.title('Most Player assisted to cristiano',fontsize=15);
plt.ylabel('assists', fontsize=12);
plt.xlabel('player name', fontsize=12);
r_assist_vis.set_xticklabels(rotation=30,labels=r_assist.index,fontsize=15);
plt.show();


# In[100]:


m_assist =df_messi['assisted'].value_counts()
m_assist = m_assist[:10]
sns.set_style("darkgrid")
plt.figure(figsize=(20,6));
m_assist_vis = sns.barplot(m_assist.index, m_assist.values, alpha=0.8,palette='winter');
plt.title('Most Player assisted to messi',fontsize=15);
plt.ylabel('assists', fontsize=12);
plt.xlabel('player name', fontsize=12);
m_assist_vis.set_xticklabels(rotation=30,labels=m_assist.index,fontsize=15);
plt.show();


# # favourite opponent

# In[101]:


r_opp=df_ronaldo['opp'].value_counts()
r_opp=r_opp[:15]
sns.set_style("darkgrid")
plt.figure(figsize=(20,6));
r_opp_vis=sns.barplot(r_opp.index , r_opp.values, alpha=0.8,palette="dark");
plt.title('Cristiano Ronaldo favourite opponent',fontsize=15);
plt.ylabel('Goals',fontsize=12);
plt.xlabel('opponent',fontsize=12);
r_opp_vis.set_xticklabels(rotation=30,labels=r_opp.index,fontsize=15);
plt.show();


# In[102]:


m_opp=df_messi['opp'].value_counts()
m_opp=m_opp[:15]
sns.set_style("darkgrid")
plt.figure(figsize=(20,6));
m_opp_vis=sns.barplot(m_opp.index , m_opp.values, alpha=0.8,palette="dark");
plt.title('Lional Messi favourite opponent',fontsize=15);
plt.ylabel('Goals',fontsize=12);
plt.xlabel('opponent',fontsize=12);
m_opp_vis.set_xticklabels(rotation=30,labels=m_opp.index,fontsize=15);
plt.show();


# In[109]:


min_ronaldo1=df_ronaldo.groupby(['min']).size().to_frame('count').reset_index()
min_ronaldo=min_ronaldo1.sort_values(by='count', ascending=False)[:10]
min_ronaldo=min_ronaldo.reset_index()
min_ronaldo=min_ronaldo.rename(columns={'min':('Ronald_min')})
min_ronaldo=min_ronaldo.drop(columns=['index'])
#=====
#=====
min_messi=df_messi.groupby(['min']).size().to_frame('count').reset_index()
min_messi=min_messi.sort_values(by='count', ascending=False)[:10]
min_messi=min_messi.reset_index()
min_messi=min_messi.rename(columns={'min':('messi_min')})
min_messi=min_messi.drop(columns='index')
#==== 
min_ronaldo


# In[110]:


min_messi


# In[112]:


min_cr7=df_ronaldo[df_ronaldo['min']<90]
min_values=min_cr7['min'].values
#========
min_messi=df_messi[df_messi['min']<90]
min_values_messi=min_messi['min'].values
min_values_messi
#=== 
#figure,axes = plt.subplots(1,2,figsize=(10,5))
plt.figure(figsize=(15,5))
plt.hist(min_values,histtype='bar',bins=45,density=True,label='Ronaldo');
plt.hist(min_values_messi,bins=45,histtype='bar',density=True,label='Messi');
plt.legend(loc='upper left')


# In[113]:


plt.figure(figsize=(14,7))
sns.kdeplot(min_values, shade = True)
sns.kdeplot(min_values_messi, shade = True)
plt.legend(['Cristiano','Messi'])
plt.xlabel('Home Factor')


# In[114]:


df_champ=df.loc[df['comp']=='Champions League']
df_champ['player'].value_counts()


# # Conclusion
 Ronaldo Score more goals than Messi
 Ronaldo score single goals more than Messi but Messi score more brace and hatricks
 Cristiano scored more in away matches but Messi scored more in home
 Ronaldo Scored more in UEFA
 Messi and Cristiano Scored more against the same team which is Sevilla
# In[ ]:




