order_amount=int(input("Enter the order amount "))
print(f"order amount {type(order_amount)}") 

delivery_fees=0


if order_amount<300:
    delivery_fees=order_amount
    print(f"delivery fees will be {delivery_fees}")