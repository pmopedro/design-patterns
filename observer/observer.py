from abc import ABCMeta, abstractmethod


class NewsPublisher:
    def __init__(self):
        self.__subscribers=[]
        self.__latestNews = None
    
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)
    
    def detach(self):
        return self.__subscribers.pop()
    
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()
    
    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return "Got News:", self.__latestNews

class Subscriber(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass

class SmsSubscriber:
    def __init__(self,publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__,self.publisher.getNews())

class EmailSubscriber:
    def __init__(self,publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__,self.publisher.getNews())

class MagazineSubscriber:
    def __init__(self,publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    
    def update(self):
        print(type(self).__name__,self.publisher.getNews())

epoca = NewsPublisher()

for Subscriber in [SmsSubscriber,EmailSubscriber,MagazineSubscriber]:
    Subscriber(epoca)
print("\n Subscribers: ", epoca.subscribers())

epoca.addNews("Obama is the first black president")
epoca.notifySubscribers()

print("\n Detached: ", type(epoca.detach()).__name__)
print("\n Subscribers: ", epoca.subscribers())

epoca.addNews("Brasil é Brasil, desde que brasil é brasil!")
epoca.notifySubscribers()