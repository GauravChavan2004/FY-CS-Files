class NetworkError(Exception):
    def __init__(self,args):
        self.args=args
try:
    raise NetworkError("My Error")
except NetworkError as e:
    print(e.args)
