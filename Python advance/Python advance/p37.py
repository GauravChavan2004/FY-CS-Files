import re
phone="2004-959-559 #this is phone number"
num=re.sub(r'#.*$'," ",phone)
print("Phone Num:",(num))
num=re.sub(r'\D'," ",phone)
print("Phone Num:",(num))
