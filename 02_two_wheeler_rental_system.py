import datetime
import time

class BikeRental:

    def __init__(self, stock=0):
        self.stock = stock

    def rental_system(self, customer_rent_request):
        rented_time, rental_basis, number_of_bikes = customer_rent_request

        try:
            number_of_bikes = int(number_of_bikes)
        except ValueError:
            print('That is not positive integer')
            return -1

        if rental_basis == "hourly" or rental_basis == "weekly" or rental_basis == "daily":
            print("")
        else:
            print("This is not a valid option")
            return -1

        if number_of_bikes > self.stock:
            print("We have {} number of bikes to rent, so we cannot process your request".format(self.stock))
            return -1
        else:

            self.stock -= number_of_bikes
            print('Thankyou, your order details are: ')
            print("rental basis: ", rental_basis)
            print("number of bikes: ", number_of_bikes)
            print("renting time: ", rented_time)


    def display_stock(self):
        print("Available number of bikes for rent: {}".format(self.stock))

    def return_billing(self, return_details):

        bill = 0.0
        rented_time, returned_time, rental_basis, number_of_bikes = return_details
        try:
            number_of_bikes = int(number_of_bikes)
        except ValueError:
            print('That is not positive integer')
            return -1

        total_time_billing = returned_time - rented_time

        if rented_time and returned_time and number_of_bikes and rental_basis:
            if rental_basis == 'hourly':
                bill = (total_time_billing.seconds/3600) * 50 * number_of_bikes
            elif rental_basis == 'daily':
                bill = (total_time_billing.days) * 30 * number_of_bikes
            elif rental_basis == 'weekly':
                bill = (total_time_billing.days/7) * 20 * number_of_bikes

            if (3 <= number_of_bikes <= 5):
                print("You are eligible for Family promotion discount")
                bill *= 0.7

            print("You opted to return your bikes")
            print("you have rented {} number of bikes, with basis plan: {}, and your total rental time is {}".format(number_of_bikes,rental_basis,total_time_billing))
            print("That would be $: {}".format("%.2f" % float(bill)))
            print("Thank you for using our services")
        else:
            print("Are you sure, you rented a bike with us?")


class Customer:

    def __init__(self):

        self.bikes = input("Please enter number of bikes you would like to rent: ")
        self.basis = input("Please enter basis plan(hourly/daily/weekly) other inputs are not processed: ")
        self.rented_time = 0
        self.returned_time = 0





    def place_order(self):
            self.rented_time = datetime.datetime.now()
            return (self.rented_time, self.basis, self.bikes)

    def return_bikes(self):
        self.returned_time = datetime.datetime.now()
        return (self.rented_time, self.returned_time, self.basis, self.bikes)







if __name__ == '__main__':
    rental1 = BikeRental(50)
    dude = Customer()
    rental1.rental_system(dude.place_order())
    time.sleep(30)
    rental1.return_billing(dude.return_bikes())


