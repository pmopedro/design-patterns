

class EventManager(object):
    def __init__(self):
        print("Event Manager:: Let me talk to the folks\n")
    def arrange(self):
        self.hotel = Hotel()
        self.hotel.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.cooker = Cooker()
        self.cooker.setKitchen()
        
        self.musician = Musician()
        self.musician.setMusicPlaylist()

class Hotel(object):
    def __init__(self):
        print("Arranging the hotel for Marrige? --")
    def __isAvailable(self):
        print("Is the hotel free for the event on given day?")
        return True
    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the Booking")

class Florist(object):
    def __init__(self):
        print("Flower Decorations for the event?")
    def setFlowerRequirements(self):
        print("Roses and Lillies would be used for Decorations\n")

class Cooker(object):
    def __init__(self):
        print("Food Arrangements for the Event")
    def setKitchen(self):
        print("Chinese & Continental Cusine to be served\n")
    
class Musician(object):
    def __init__(self):
        print("Musical Arrangements for the Marrige")

    def setMusicPlaylist(self):
        print("Jazz and Classical will be played")

class You(object):
    def __init__(self):
        print("You - Marrige Arrangements? ")
    def askEventMannager(self):
        print("You - Lets contact the event mannager\n")
        em = EventManager()
        em.arrange()
    def __del__(self):
        print("You - Thanks to the Event Mannager all preparations done! :)")

you = You()
you.askEventMannager()