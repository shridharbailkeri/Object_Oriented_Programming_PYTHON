class Property:

    def __init__(self, square_feet="", beds="", baths="", **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.beds = beds
        self.baths = baths

    def display(self):
        print("Property Details")
        print("===============")
        print("area(square feet): {}".format(self.square_feet))
        print("number of beds: {}".format(self.beds))
        print("number of baths: {}".format(self.baths))

    def prompt_init():
        return dict(square_feet=input("Enter square feet"),
                    beds=input("Enter number of beds"),
                    baths=input("Enter number of baths"))
    prompt_init = staticmethod(prompt_init)

def get_valid_input(input_string,valid_option):

    input_string = input_string + " ({}) ".format(
        ",".join(valid_option))
    response = input(input_string)

    while response.lower() not in valid_option:
        response = input(input_string)

    return response


class Apartment(Property):

    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')

    def __init__(self, laundry="", balcony="", **kwargs):
        super().__init__(**kwargs)
        self.laundry = laundry
        self.balcony = balcony

    def display(self):
        super().display()
        print("==================")
        print("Apartment details")
        print("laundry: {}".format(self.laundry))
        print("balcony: {}".format(self.balcony))

    def prompt_init():

        parent_init = Property.prompt_init()

        laundry = get_valid_input(
                "What options are available for laundry",
                Apartment.valid_laundries)

        balcony = get_valid_input(
                "Does the building have balconies",
                Apartment.valid_balconies)

        parent_init.update({"laundra": laundry,
                            "balcony": balcony})

        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):

    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, garage="", fenced="", **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced

    def display(self):
        super().display()
        print("===============")
        print("House details")
        print("garage: {}".format(self.garage))
        print("fence: {}".format(self.fenced))

    def prompt_init():
        parent_init = Property.prompt_init()

        garage = get_valid_input("What options are available"
                                  "for garage: ", House.valid_garage)

        fenced = get_valid_input("What about fencing for the House",
                                 House.valid_fenced)

        parent_init.update({"garage": garage,
                            "fenced": fenced})

        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:

    def __init__(self, price="", taxes="", **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("Purchase details")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        return dict(price=input("What is the sellijng price?"),
                    taxes=input("What are the estimated taxes?"))

    prompt_init = staticmethod(prompt_init)


class Rental:

    def __init__(self, furnished="", utilities="", rent="", **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().display()
        print("Rental details")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():

        return dict(rent=input("What is the monthly rent?"),
                    utilities=input("What are the monthly utilities?"),
                    furnished=get_valid_input("Is property furnished?", ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):

    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):

    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Apartment, Purchase):

    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    def add_external_property(self, external_prop):
        self.property_list.append(external_prop)

    def add_property(self):

        property_type = get_valid_input("What type of property would u prefer", ("house", "apartment")).lower()
        payment_type = get_valid_input("What type of payment would you like to prefer", ("rental", "purchase")).lower()

        propertyClass = self.type_map[(property_type, payment_type)]

        init_args = propertyClass.prompt_init()

        self.property_list.append(propertyClass(**init_args)) # append a clas


if __name__ == '__main__':
    house1 = House(garage="attached", fenced="yes", beds="5",
                   baths="5", square_feet="500")
    apartment1 = Apartment(laundry="coin", balcony="yes", beds="7",
                           baths="7", square_feet="300")
    payment1 = Purchase(price="500", taxes="3%")
    payment2 = Rental(furnished="yes", utilities="garden", rent="500")
    real_estate_agent = Agent()
    real_estate_agent.add_external_property(house1)
    real_estate_agent.add_external_property(apartment1)
    real_estate_agent.display_properties()
    real_estate_agent.add_property()
    real_estate_agent.display_properties()







