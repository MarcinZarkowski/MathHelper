from tkinter import *

#Calculation section
def factors(y): #iterates through given number and if divisable, adds to list of factors. Then returns factors list. 
    if len(y)==0: #if no input is given, the function returns "No input. Click Reset.".
        return "No input. Click Reset."
    if "," in y:
        return "Too many inputs. Click Reset."
    x=int(y)
    x_factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            x_factors.append(i)
    return x_factors

def euclids_alg(x,y):
    if abs(x)==abs(y):
        return abs(x)
    else:
        greater=max(x,y)
        lesser=min(x,y)
    while True:
        remainder=greater%lesser
        if remainder==0:
            
            return abs(lesser)
        return euclids_alg(lesser,remainder)
    
def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)   

def n_choose_k(n,k):
    if k==0 :
        return 1
    else:
        return int(factorial(n)/(factorial(n-k)*factorial(k)))
    
  

def gcf(x): #finds greatest common factor
    if len(x)==0:
        return "No input. Click Reset."
    if len(x)==1:
        return x
    
    given=x.split(",")
    
    GCDs={}
    min_matches=n_choose_k(len(given),2) 
    for x in range(len(given)):
        for y in range(len(given)):
            if y>x:
                num=euclids_alg(int(given[x]),int(given[y]))
                if num ==1:
                    return 1
                if num not in GCDs:
                    GCDs[num]=1
                else:
                    GCDs[num]+=1

    possible=-1
    for number in GCDs:
        if GCDs[number]>=min_matches and number >possible:
            possible=number
    if possible==-1:#if no common factors where found using Euclids Algorithm, the function uses the factors of each number to find the GCF
        GoodFactors=[]
        for x in given:
            numFactors=factors(x)
            
            GoodFactors.append(numFactors)
        NewCheck={}
        for array in GoodFactors:
            for factor in array:
                if factor not in NewCheck:
                    NewCheck[factor]=1
                else:
                    NewCheck[factor]+=1

        for m in NewCheck:
            if NewCheck[m]>=len(given) and m>possible:
                possible=m


    return possible


    

def lcm(x): #finds least common multiple             
    
    if len(x)==0:
        return "No input. Click Reset."
    
    if len(x)==1:
        return x  
    
    given=x.split(",")
    given=list(set(given))#gets rid of duplicates
    for string in given:# checks for case where the lcm is one of the numbers in the string
        if max(list(map(int, given)))%int(string)!=0:
            break
        elif string==given[-1]:
            return max(list(map(int, given))) 
        
    given=list(map(int, given))
    given.sort()
    to_remove = set()

    # Iterate over the list and find elements to remove  (numbers are removed if they are factors of a greater number in the list)
    for i in range(len(given)):
        for j in range(i+1,len(given)):
            
            if given[j] % given[i] == 0:
                to_remove.add(given[i])
            elif given[i] % given[j] == 0:
                to_remove.add(given[j])

    #Create a new list without the elements to be removed
    given = [x for x in given if x not in to_remove]
    given=list(map(str,given))    

    LCMs={}
    for i in range(len(given)):#this loop uses the fact that M*N=GCD(M*N)*LCM(M*N)
        for j in range(len(given)):
            if j>i:
                product=int(given[i])*int(given[j])
                string=str(given[i])+','+str(given[j])
                hcm=gcf(string)
                lcm=product/hcm
                if lcm not in LCMs:
                    LCMs[lcm]=1
                else:
                    LCMs[lcm]+=1
    min_matches=n_choose_k(len(given),2)

    possible=float('inf')#set to infinity to find the lowest possible LCM
    for number in LCMs:
        if LCMs[number]>=min_matches and number < possible:
            possible=number
        
    if possible==float('inf'):# if LCM is not found until now, the function returns the product of all the numbers
        
        possible=1
        for x in list(map(int, given)):
            possible*=x

    return int(possible)
   

def proceed(): #proceed function is called in the button_Enter function. It is used to organize the usage of the program forcing the user to first input GCM, LCM, or Factors, then the numbers. 
    
    if entered[0:3]=="LCM": #When proceed is called, global variabl entered is set to a string which the user inputted. This string is then used to find which function the user wanted to use. 
        lcmString=entered[33::]#for each condition, if the program knows which function the user wants to use, it passes the rest of the string which includes the numbers inputted to the function and passes the answer to the entry box. 
        e.delete(0,END)
        e.insert(0, lcm(lcmString))
        False
    elif entered[0:3]=="GCF":
        gcfString=entered[33::]
        e.delete(0,END)
        e.insert(0, gcf(gcfString))
        False
    elif entered[0:7]=="FACTORS":
        num=entered[19::]
        e.delete(0,END)
        e.insert(0, factors(num))
        False
    else:#to serve as a constant, after clicking Enter the entry box needs to include a function (LCM, GCF, or Factors). If not the user is prompted to click reset and start over. 
        e.delete(0,END) 
        e.insert(0,"Invalid input. Click Reset.")
        
                        
#UI section
root = Tk()
root.title("Math Helper")
e = Entry(root, width=50, borderwidth=5,)
e.insert(0, "Click GCF, LCM, or Factors. Then click Enter.")
function_in_use=1
e.grid(row=0, column=0, columnspan=3,padx=10, pady=10)

def button_click(action):#this function is used for all numbers and comma button only. 
    if function_in_use==1:#checks if the user inputted the GCF, LCM, or Factors button first. 
        e.delete(0, END)
        e.insert(0, "Choose your calculation type first. GCF, LCM, or Factors.")
    else:
        current=e.get()
        e.delete(0,END)
        e.insert(0,str(current)+str(action))

def button_function_click(action):#a seperate funciton is used for the LCM, GCF, and Factors button in order to manipulate the funtion_in_use variable. 
    e.delete(0,END)
    global function_in_use #this variable is used to keep track if the user inputted LCM, GCF, Factors button first. 
    function_in_use=action
    e.insert(0,str(action))

def button_Clear():#deletes entry box
    global function_in_use
    function_in_use=1 
    e.delete(0,END)

def button_Enter():#used only with Enter button to call proceed function.
    global entered
    entered= e.get()
    proceed()

   
def reset_click():#created a reset button incase the user gets confused etc or wants to use program again without making an error. 
    e.delete(0,END)
    global function_in_use
    function_in_use=1 
    e.insert(0, "Click GCF, LCM, or Factors. Then click Enter.")

#initializing buttons. Includes sizes, Text, and functions connected ot button. 
button_gcf=Button(root, text="GCF", padx=38, pady=20, command=lambda:button_function_click('GCF of (seperate # with "comma"):'))
button_lcm=Button(root, text="LCM", padx=36.6, pady=20, command=lambda:button_function_click('LCM of (seperate # with "comma"):'))
button_factors=Button(root, text="Factors", padx=30.4, pady=20, command=lambda:button_function_click("FACTORS of (one #):"))
button_clear=Button(root, text="Clear", padx=35.9, pady=20, command=button_Clear)

button_9=Button(root, text="9", padx=46, pady=20, command=lambda:button_click("9"))
button_8=Button(root, text="8", padx=46, pady=20, command=lambda:button_click("8"))
button_7=Button(root, text="7", padx=46, pady=20, command=lambda:button_click("7"))
button_6=Button(root, text="6", padx=46, pady=20, command=lambda:button_click("6"))
button_5=Button(root, text="5", padx=46, pady=20, command=lambda:button_click("5"))
button_4=Button(root, text="4", padx=46, pady=20, command=lambda:button_click("4"))
button_3=Button(root, text="3", padx=46, pady=20, command=lambda:button_click("3"))
button_2=Button(root, text="2", padx=46, pady=20, command=lambda:button_click("2"))
button_1=Button(root, text="1", padx=46, pady=20, command=lambda:button_click("1"))
button_0=Button(root, text="0", padx=46, pady=20, command=lambda:button_click("0"))
button_comma=Button(root, text='"comma"', padx=23.3, pady=20, command= lambda:button_click(","))
button_enter=Button(root, text="Enter", padx=30, pady=110, command= button_Enter)
button_reset=Button(root,text="Reset", padx=30, pady=52,command=reset_click)

#Button placment using grid system. 
button_gcf.grid(row=1, column=0)
button_lcm.grid(row=1, column=1)
button_factors.grid(row=1, column=2)

button_9.grid(row=2, column=2)
button_8.grid(row=2, column=1)
button_7.grid(row=2, column=0)

button_6.grid(row=3, column=2)
button_5.grid(row=3, column=1)
button_4.grid(row=3, column=0)

button_3.grid(row=4, column=2)
button_2.grid(row=4, column=1)
button_1.grid(row=4, column=0)

button_0.grid(row=5, column=0)
button_clear.grid(row=5, column=1)
button_comma.grid(row=5, column=2)

button_enter.grid(row=0, column=3, rowspan=4)
button_reset.grid(row=4, column=3, rowspan=3)

root.mainloop()      


         
           
 
            
