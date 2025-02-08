# Ray McMillin, 2/7/25, Shipping Cost Total

def weight_conversion(weight):
    # Calculate the shipping charge.
    shippingCost = 0.0
    ######################
    if weight <= 2:
        price_per_pound = 1.50
    elif weight <= 6:
        price_per_pound = 3.00
    elif weight <= 10: 
        price_per_pound = 4.00
    else:
        price_per_pound = 4.75

    shippingCost = weight * price_per_pound
    
    ######################
    
    return shippingCost

#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))
