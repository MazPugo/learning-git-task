# Zadanie 1

#key ----shop name
#value--- list of items

shopping_list = { 'piekarnia':['chleb','paczek','bulki'] , 'warzywniak':['marchewka','seler','rukola']}
# creating a dictionary with 2 lists: stores and products
count_product= 0 # initializing a counter to 0
for key, value in shopping_list.items(): #  creating a loop to go through the list of products per store
   value = [s.capitalize() for s in value] # creating a loop to change the fist small letter of the products to the capital letter, using the function capitalize
   print("Idę do " + str(key).capitalize() + " i kupuję tam " + str(value))# display the content of dictionary, using the function capitalize to change the first small letter in the name of the store to the capital letter
   count_product= count_product + len(value)# count  the total number of products
print("W sumie kupuje " + str (count_product) + " produktow")# display the sentence "w sumie kupuje 6 produktow"