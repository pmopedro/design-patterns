
class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("init method called")
        else:
            print("instance already created")
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s=Singleton()
print("Object created ", Singleton.getInstance())
s1=Singleton()
print(s,s1)