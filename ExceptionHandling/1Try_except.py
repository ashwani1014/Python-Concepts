flavour={"Choclate":80,"Mongo":40,"Candy":50,"Pineapple":90}

try:
    print(flavour["AAM"])

except KeyError:
    print("AAm does not exist")
    

print("hello exception is done")    