class ParkingGarage():

    def __init__(self, capacity, spaces, dictionary):
        self.capacity = capacity
        self.spaces = spaces
        self.dictionary = dictionary

    def showParkingGarage(self):
        print('There are spaces avalible!')
    for item in self.spaces:
        print(spaces)

    def showCapacity(self):
        print(f'there are {self.capacity}tickets avalible')

    def showDictionary(self):
        print(f'You are {self.dictionary}in line')

    def decreseCapacity(self, changed_capacity = 12):
        if self.capacity == isinstance(self.capacity, str):
            print("You can't add only take away")
        else:
            self.capacity += changed.capacity

my_garage = ParkingGarage(12,12,[])

def run():
    while True:
        response = input('What would you like to do? take ticket/show spaces/quit? ')

        if response.lower == 'take ticket':
            my_garage.showParkingGarage()
            print('Please take ticket and enjoy')
            break
        elif response.lower == 'show spaces':
            my_garage.showParkingGarage()
            print('There are [] parking spaces')
            break
        elif response.lower == 'quit':
        my_garage.parkingGarage()
        print('Please pay and have a great day!')
