#activity 1 : find the average
house_price1 = 240
house_price2 = 567
house_price3 = 345
house_price4 = 678
sum= house_price1+house_price2+house_price3+house_price4
print(sum)
avg=sum/4
print("the average price of theese houses are",avg)

#activity 2: count the notes
randy=int(input("enter the amount:"))
notes100=randy//100
notes50=(randy%100)//50
notes10=(randy%50)//10

print(notes100)
print(notes50)
print(notes10)

#activity3:find the percentage
math=int(input("enter mark obtained in math"))
geography=int(input("enter mark obtained in geography"))
spanish=int(input("enter mark obtained in spanish"))
computing=int(input("enter mark obtained in computing"))
sum_of_subjects=math+geography+spanish+computing
score=(sum_of_subjects/400)*100
print("score of tests",score)