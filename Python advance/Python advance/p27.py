def functionString(Explevel):
    if explevel<1:
        raise  Exception(explevel)
    return explevel
try:
    r=functionString(-5)
    print("level=",r)
except Exception as e:
    print("error is an arg level",e.args[0])
else:
    print("program wprk good")
    
