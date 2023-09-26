deviceID = 999

paymentTier = 2
if (deviceID >3000):
  if(paymentTier==1):
    print("Statement A")
  print("Statement B")
elif (deviceID > 2000):
  if(paymentTier==2):
    print("Statement C")
  else:
    print("Statement D")
elif (deviceID > 1000):
    if(paymentTier==3):
      print("Statement E")
    elif(paymentTier==2):  
      print("Statement F")
    else:
      print("Statement G")
else:
  print("Statement H")
print("Statement I")