# Step 1: Create a list of store item names and a list of matching stock counts.
store_items=["Pencil","Eraser","Book","Pen"]
stock_count=[10,5,0,15]
price=[2,1,3,1]
# Step 2: Pair items with stock counts into a dictionary using zip() and dictionary comprehension.
inventory={i:j for i,j in zip(store_items,stock_count)}
print(inventory)
# Step 3: Filter out only the items that are still in stock using list comprehension.
stocked=[i for i in store_items if inventory[i]!=0]
print(stocked)
# Step 4: Ask which item the shopper wants to buy.
bought=input("Enter what you want to buy:")
# Step 5: Stop the checker immediately using exit() if that item has run out.
if bought not in inventory or inventory[bought]==0:
    print("Item not available:Bye!")
    exit()
else:
    print("Item available!")
# Step 6: Apply a markup to every price using map().
price_updated=int(input("Enter the amount you want to update:"))
updated_prices=list(map(lambda p: p+price_updated,price))
print(updated_prices)
# Step 7: Print the final price paid and the updated inventory.
index=store_items.index(bought)
item_price=updated_prices[index]
print("Item bought:",bought)
print("Item price:",item_price)
print("=====================")