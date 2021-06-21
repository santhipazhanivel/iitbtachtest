#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\Admin\\Desktop\\santhi\\test1.csv")
print(df)



# In[ ]:


import pandas as pd
import numpy as np


# In[13]:


my_series=pd.Series([1,2,3,4])

my_series


# In[14]:


df=pd.DataFrame(index=my_series)


# In[15]:


df


# In[16]:


df['name']=['santhi','giriyash','vijay','shunmugam']


# In[17]:


df


# In[18]:


import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\Admin\\Desktop\\santhi\\test1.csv")
print(df)


# In[27]:


df["gender"].replace({"female":"1","male":"2","other":"3"},inplace=True)
print(df)


# In[10]:


import pandas as pd
import numpy as np
lst=['L','w','M']
pd.Series(lst)


# In[14]:


lst2=['a','b','c']
pd.Series(lst2)


# In[15]:


pd.Series(data=lst,index=lst2)


# In[16]:


crc=['dhoni','kohil','andreson','sachin']
s1=pd.Series(crc,index=[1,2,3,4])


# In[17]:


s1


# In[18]:


avg=['xxx','yyy','zzz']
s2=pd.Series(avg,index=[1,2,3])
s2


# In[20]:


ser1=pd.Series([1,2,3,4],index=['usa','Germany','italy','japan'])
ser1


# In[21]:


ser2=pd.Series([1,2,3,4],index=['usa','Germany','italy','japan'])
ser2


# In[23]:


a= ser1 + ser2
a


# In[49]:



from random import seed
from random import random
from numpy.random import randn


# In[55]:


d={'col':[1,2,3,4,7],'col2':[4,5,6,7,7],'col3':[7,8,4,8,9]}
df=pd.DataFrame(data=d)
print(df)


# In[58]:


import random
print(random,range(1,10))


# In[62]:





# In[63]:


df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD')


# In[ ]:


from numpy.random import randn
    


# In[67]:


df=pd.DataFrame(randn(5,5),index='A B C D E'.split(),columns='P Q R S T'.split())
df


# In[71]:


df['P']


# In[73]:


df[['P','Q']]


# In[74]:


df.R


# In[76]:


type(df['R'])


# In[77]:


df['U']=df['P']-df['Q']
df['U']


# In[78]:


df.drop('U',axis=1)


# In[79]:


df


# In[83]:


df.drop('U',axis=1)


# In[84]:


df.drop('E',axis=0)


# In[85]:


df.loc['B']


# In[86]:


df.iloc[2]


# In[88]:


df.loc[['A'],['P']]


# In[89]:


df.loc[['A','B'],['P','Q']]


# In[90]:


df>0


# In[91]:


df[df<0]


# In[93]:


df[df['P']<0]


# In[95]:


df


# In[96]:


df.reset_index()


# In[7]:


import pandas as pd
import numpy as np
from numpy.random import randn
    


# In[15]:


df=pd.DataFrame(randn(5,5),index='A B C D E'.split(),columns='P Q R S T'.split())
df


# In[18]:


lst ='aa bb cc dd ee'.split()
df['index']=lst
df


# In[19]:


df.set_index('index')


# In[21]:


outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.from_tuples(hier_index)
        


# In[22]:


hier_index


# In[23]:


df=pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df


# In[25]:


df.loc['G2']


# In[26]:


df.loc['G1']


# In[29]:


df.loc['G1'].loc[1]


# In[30]:


df.index.names=['Group','Num']
df


# In[1]:


import pandas as pd
import numpy as np


# In[18]:


df=pd.read_csv('C:\\Users\\Admin\\Desktop\\abc.csv')
df.head()


# In[19]:


df.dtypes


# In[20]:


df_obj=df.select_dtypes(include=['object']).copy()
df_obj.head()


# In[24]:


df[df.isnull().any(axis=1)]


# In[25]:


df_obj=df.select_dtypes(include=['object']).copy()
df_obj.head()


# In[26]:


df_obj[df_obj.isnull().any(axis=1)]


# In[29]:


df_obj['num_doors'].valuecounts()


# In[30]:


df


# In[33]:


df['num_doors'].value_counts()


# In[37]:


obg_df = df_obj.fillna({"num_doors":'four'})


# In[39]:


obg_df.head()


# In[42]:


obg_df['num_doors'].value_counts()


# In[48]:


obg_df[obg_df.isnull().any(axis=1)]


# In[50]:


obg_df


# In[51]:


obg_df['num_cylinders'].value_counts()


# In[59]:


clean_up_find_replace = {"num_doors": {"four":4, "two":2},
                             "num_cylinders":{"four":4,"six":6,"five":5,"eight":8,"two":2,"twelve":12,"three":3}}


# In[60]:


obj_df = obg_df.replace(clean_up_find_replace)
obj_df


# In[61]:


obj_df['body_style'].value_counts()


# In[65]:


obj_df['body_style'] = obj_df['body_style'].astype('category')
obj_df.dtypes


# In[66]:


obj_df.head()


# In[67]:


obj_df['body_style_category']=obj_df['body_style'].cat.codes
obj_df.head()


# In[71]:


obj_df['drive_wheels'].value_counts()


# In[72]:


pd.get_dummies(obj_df,columns=['drive_wheels'],prefix=['drive']).head()


# In[ ]:




