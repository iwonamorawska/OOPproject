# Start Your Code here


class ParkingGarage():

    def __init__(self, tickets=2, spaces=2):
        self.tickets = tickets
        self.spaces = spaces
        self.current_ticket = {}

    def runGarage(self):
        self.active = True
        while self.active:
            self.intro = input(
                "\nWhat would you like to do? ('Park', 'Pay', 'Leave', or 'Quit')")

            if self.intro.strip().lower() == "park":
                self.takeTicket()

            if self.intro.strip().lower() == "pay":
                self.payParking()

            if self.intro.strip().lower() == "leave":
                self.leaveGarage()

            if self.intro.strip().lower() == "quit":
                if self.current_ticket:
                    print("\nTickets unresolved, cannot quit.")
                else:
                    self.active = False

            # developer's command to check stored info
            if self.intro.strip().lower() == "info":
                print(self.current_ticket)
                print(f"{self.tickets} ticket(s)")
                print(f"{self.spaces} space(s)")

    def takeTicket(self):
        self.question = input("\nTake a ticket? 'yes' or 'no': ")
        if self.question.strip().lower() == 'yes':
            if self.tickets == 0:
                print("\nSorry we are capacity. Come back later. ")
            elif self.tickets >= 1:
                self.tickets -= 1
                self.spaces -= 1
                self.name = input("\nPlease enter your name: ")
                self.name_fix = self.name.strip().lower()
                self.current_ticket[self.name_fix] = False
                print(
                    f"\nThank you {self.name_fix}! Here's your ticket, you have 15 minutes to leave")
                self.payParking()
        if self.question.strip().lower() == 'no':
            print("\nPlease choose again: ")

    def payParking(self):
        if self.current_ticket:
            self.question2 = input(
                "\nWould you like to pay for your ticket now? 'yes' or 'no' ")
            if self.question2 == 'yes':
                self.name_pay = input("\nPlease enter name on ticket: ")
                self.name_pay_fix = self.name_pay.strip().lower()
                if self.name_pay_fix in self.current_ticket:
                    self.current_ticket[self.name_pay_fix] = True
                    print(
                        f"\nHello {self.name_pay.title()} your ticket had been paid. Thank you!")
                elif self.name_pay_fix not in self.current_ticket:
                    print(
                        "There's currently no ticket with that name, please choose again: ")
                    self.payParking()
            elif self.question2 == 'no':
                print("Please choose again: ")
            else:
                print("Invalid response please choose again: ")
                self.payParking()
        else:
            print(
                "\nNo tickets to pay currently, Please choose another option.")

    def leaveGarage(self):
        if self.current_ticket:
            self.question3 = input(
                "\nWould you like to leave the garage? 'yes' or 'no': ")
            if self.question3 == 'yes':
                self.name_leave = input("\nWhat is your name?")
                self.name_leave_fix = self.name_leave.strip().lower()
                if self.name_leave_fix not in self.current_ticket:
                    print("\nNo ticket with that name please choose again: ")
                    self.leaveGarage()
                elif self.name_leave_fix in self.current_ticket and self.current_ticket[self.name_leave_fix] == True:
                    del self.current_ticket[self.name_leave_fix]
                    self.tickets += 1
                    self.spaces += 1
                    print("\nThank you have a nice day.")
                else:
                    print("\nPlease pay ticket")
            elif self.question3 == 'no':
                print("\nPlease choose again: ")
            else:
                print("\nInvalid response choose again: ")
        else:
            print("\nNo tickets currently, please choose again: ")


garage1 = ParkingGarage()
garage1.runGarage()
