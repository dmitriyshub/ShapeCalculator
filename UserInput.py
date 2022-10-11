dict1 = {'age': {'youth':{'no':3,'yes':2},'middle_age':{'no':0,'yes':4},'senior':{'no':2,'yes':3}}}
dict2 = {'income':{'low':{'no':1,'yes':3},'medium':{'no':2,'yes':4},'high':{'no':2,'yes':2}}}
dict3 ={'student':{'no':{'no':4,'yes':1},'yes':{'no':3,'yes':6}}}
dict4 ={'credit_rate':{'fair':{'no':2,'yes':6},'excellent': {'no':3,'yes':3}}}
dict5 ={'buy_computer':{'no':5,'yes':9}}
#print(dict1['age']['youth'])
for k,v in dict3.items():
     for k2,v2 in v.items():
         print(k2)
         print(v2)


