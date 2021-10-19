#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program formats your address to a mailing address


def address_formatter(
    full_name,
    street_number,
    street_name,
    city_name,
    province_name,
    postal_code,
    apartment_number=None,
):
    # This function formats your address to a mailing address
    if apartment_number != None:
        mailing_address = "{0}\n{1}-{2} {3}\n{4} {5}  {6}".format(
            full_name,
            apartment_number,
            street_number,
            street_name,
            city_name,
            province_name,
            postal_code,
        ).upper()
    else:
        mailing_address = "{0}\n{1} {2}\n{3} {4}  {5}".format(
            full_name, street_number, street_name, city_name, province_name, postal_code
        ).upper()

    return mailing_address


def main():
    # This function is the main function
    input_apartment_number = None

    print("This program formats your address to a mailing address")

    # input
    try:
        input_name = input("Enter your full name: ")

        input_apartment = input("Do you live in an apartment? (y/n): ")
        if input_apartment.upper() == "Y" or input_apartment.upper() == "YES":
            input_apartment_number = input("Enter your apartment number: ")
            # checks if input_apartment_number is an integer
            input_apartment_number = int(input_apartment_number)

        input_street_number = input("Enter your street number: ")
        # checks input_street_number is an integer
        input_street_number = int(input_street_number)

        input_street_name = input(
            "Enter your street name And type (Main St, ExpressPkwy...): "
        )
        input_city = input("Enter your city: ")
        input_province = input(
            "Enter your province (as an abbreviation, ex: ON, BC..): "
        )
        input_postal_code = input("Enter your postal code (A1B 2C3): ")

        # process & output
        print("")
        if input_apartment_number != None:
            print(
                address_formatter(
                    input_name,
                    input_street_number,
                    input_street_name,
                    input_city,
                    input_province,
                    input_postal_code,
                    input_apartment_number,
                )
            )
        else:
            print(
                address_formatter(
                    input_name,
                    input_street_number,
                    input_street_name,
                    input_city,
                    input_province,
                    input_postal_code,
                )
            )
    except (Exception):
        print("\nInvalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
