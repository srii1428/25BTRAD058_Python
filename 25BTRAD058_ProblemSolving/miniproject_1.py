#Bill Generator
# To create a simple Python program that calculates the total bill based on the item price, quantity, and GST
print("----- BILL GENERATOR -----")
item = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
subtotal = price * quantity
gst = subtotal * 0.05
total = subtotal + gst
print("\n----- BILL -----")
print("Item :", item)
print("Price :", price)
print("Quantity :", quantity)
print("Subtotal :", subtotal)
print("GST 5% :", gst)
print("Total :", total)
print("----------------")
print("Thank you!")
