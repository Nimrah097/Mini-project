''' Author: Nimrah Fatheen
    SOB-28,29,30
    
A company produces 9 different products. There  are 3 PR employees  to advertise the products, each employee is assigned to 3 products.
The employees get a commission along with their fixed salary every year for the amount of products sold anually. Employees selling more than
1500 products a year gets a raise of 10% of their salary. Those who sold  above 2500 get a raise of 20% and above 4000 get a 35% raise.

The programme contains a list of employee names,their salaries and another list of tuples that contain the product names. The user is required to input the name of the 
products and its sales volume to calculate the total net worth (salary+commission) of the employee. It also finds out the name of the product that was sold the least and the
most for each employee and the average number of products sold by each employee. 


'''
PR_Names=['Dua','Jack','June']
Product_Names=[('Phone Holder','Mouse Pad','Cable Protector'),('USB','Earphones','Adaptor'),('Power Bank','Socket Cover','Stylus Pen')]
Fixed_salary=[40000,40000,40000]

Net_worth=[0,0,0]       #Net_worth is a list that will be updated the final salary of each employee

ext=[[],[],[]]          #ext is a list of lists that contains the commission + salary the employee gets for each product 
     
SV=[[],[],[]]           #SV is a list of lists that contain the sale volume for each product

#This function takes the product names and their sale volume from the user to calculate the final networth. It then updates the list Networth.

def salary_calc(x,y,z): # x is the  index value, y is the list ext and z is the list SV
    for i in range(len(Product_Names[x])):    
        P_name=input('enter the product name:') #The Salary wont be calculated if an invalid product name is given
        Sale_volume=int(input('enter the number of items sold:'))
        if Sale_volume<1500:
            y[x].append(Fixed_salary[x])
            z[x].append(Sale_volume)
        elif Sale_volume>=1500 and Sale_volume<2500 :
            y[x].append(Fixed_salary[x]+0.1*Fixed_salary[x]) 
            z[x].append(Sale_volume)                         
        elif Sale_volume>=2500 and Sale_volume<4000:
            y[x].append(Fixed_salary[x]+0.2*Fixed_salary[x])
            z[x].append(Sale_volume)
        elif Sale_volume>=4000:
            y[x].append(Fixed_salary[x]+0.35*Fixed_salary[x])
            z[x].append(Sale_volume)
             
    Net_worth[x]=sum(y[x])


salary_calc(0,ext,SV)
print('')           
salary_calc(1,ext,SV)
print('')
salary_calc(2,ext,SV)

print('')  
        
print('The salary of ',PR_Names[0],'is:',Net_worth[0],'The salary of ',PR_Names[1],'is:',Net_worth[1],'The salary of ',PR_Names[2],'is:',Net_worth[2],'\n')

print('')


#This list calculates the least sold and most sold products for each employee by using min() and max() functions

def min_max(a,b): # a is the index value , b is SV
    Min_val=min(b[a])
    Max_val=max(b[a])
    if Min_val==b[a][0]:
        print('The least sold item for ',PR_Names[a],' is:',Product_Names[a][0])
    elif Min_val==b[a][1]:
        print('The least sold item for ',PR_Names[a],' is:',Product_Names[a][1])
    else:
        print('The least sold item for ',PR_Names[a],' is:',Product_Names[a][2])

    
    if Max_val==b[a][0]:
        print('The most sold item for ',PR_Names[a],' is:',Product_Names[a][0])
    elif Max_val==b[a][1]:
        print('The most sold item for ',PR_Names[a],' is:',Product_Names[a][1])
    else:
        print('The most sold item for ',PR_Names[a],' is:',Product_Names[a][2])
    
min_max(0,SV)
min_max(1,SV)
min_max(2,SV)


print('')    

#This function calculates the average number of products sold by each employee

def average(p,q): # p is the index value , q is SV
    Average_of_sale=sum(q[p])/len(q[p])
    print('The average number of products sold by',PR_Names[p],'is',round((Average_of_sale),2)) # The average is rounded to 2 decimal places and printed

average(0,SV)
average(1,SV)
average(2,SV)
