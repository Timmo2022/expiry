from datetime import datetime, date, timedelta




expirydate = input("When is the expiry date? (in MM/DD/YY) ")
expiry_date = datetime.strptime (expirydate, "%m/%d/%Y") #To format date and time in Python we use strftime function.
""""
%d is for date  
#%m is for month  
#%Y is for Year in full exa 20222 while %y is for the year represented in half exa: 22
"""
 
expiry = expiry_date + timedelta(days=1)
""" I have added one day to the real expiry date entered by the user,simply because
the datetime function assumes any time after 00:00 is already past the expiry date.
We want our subscription to cancel out at 23:59 of the real expiry date.
"""


#getting today's date
CurrentDate=datetime.today()
#print(CurrentDate) 





 

if CurrentDate <= expiry:
    print ('Your subscription is active')
elif CurrentDate >= expiry:
    #Code to deactivate account
    print ("Your subscription expired")
else:
    print ("Enter a valid date in the given format")
quit()
