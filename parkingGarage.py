class ParkingGarage():
    def __init__(self, tickets=2, spaces=2):
        self.tickets = tickets
        self.spaces = spaces
        self.current_ticket = {}
    def take_ticket(self):
        self.question = input("Take a ticket? 'yes' or 'no' ")
        if self.question == 'yes':
            if self.tickets == 0:
                print("Sorry we are capacity. Come back later.")
                self.runGarage()
            elif self.tickets >= 1:
                self.tickets -= 1
                self.spaces -= 1
                self.name = input("please enter your name: ")
                self.current_ticket[self.name] = False
                self.pay_for_parking()
        if self.question == 'no':
            self.runGarage()
        # if self.question != 'yes' or 'no':
        #     print('Invalid response. Please respond with "yes" or "no"')
        #     self.take_ticket()
    def pay_for_parking(self):
        if self.current_ticket:
            self.current_ticket[self.name] = False
            self.question2 = input("Would you like to pay now?")
            if self.question2 == 'yes':
                self.name_pay = input("What is your name?")
                self.current_ticket[self.name_pay] = True
                print(
                    f"Your ticket had been paid. Thanks {self.name_pay}, you have 15 minutes to leave.")
                self.runGarage()
            elif self.question2 == 'no':
                self.runGarage()
        else:
            print(
                "You don't currently have any blance due, Please choose another option.")
            self.runGarage()
    def leave_garage(self):
        if self.current_ticket:
            self.question3 = input(
                "Would you like to leave the garage? 'yes' or 'no'")
            if self.question3 == 'yes' and self.current_ticket[self.name] == True:
                self.name_leave = input("What is your name?")
                if self.name_leave not in self.current_ticket:
                    print("Name not in there please enter again")
                    self.leave_garage()
                elif self.name_leave in self.current_ticket:
                    del self.current_ticket[self.name_leave]
                    self.tickets += 1
                    self.spaces += 1
                    print("Thank you have a nice day.")
                    self.runGarage()
            elif self.question3 == 'yes' and self.current_ticket[self.name] == False:
                print("Please pay for your ticket.")
                self.pay_for_parking()
            elif self.question3 == 'no':
                self.runGarage()
        else:
            self.runGarage()
            # self.question4 = input("Would you like to stay longer?")
            # if self.question4 == 'yes':
            #     self.leave_garage()
            # elif self.question4 == 'no' and self.current_ticket["paid"] == False:
            #     print("Please pay your ticket")
            #     self.pay_for_parking()
            # elif self.question4 == 'no' and self.current_ticket["paid"] == True:
            #     print("Have a nice day.")
    def runGarage(self):
        self.active = True
        while self.active:
            self.intro = input(
                "What would you like to do? 'Park', 'Pay', or 'Leave' or 'Quit' ")
            if self.intro == "park":
                self.take_ticket()
            if self.intro == "pay":
                self.pay_for_parking()
            if self.intro == "leave":
                self.leave_garage()
            if self.intro == "dict":
                print(self.current_ticket)
            if self.intro == "quit":
                if self.current_ticket:
                    print("Tickets unresolved, cannot quit")
                    self.runGarage()
                else:
                    self.active = False
garage1 = ParkingGarage()
garage1.runGarage()