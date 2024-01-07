import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Ajitha123@*",database="amazon")
mycursor=mydb.cursor()

def validate_user(name,password):
    mycursor.execute("Select * from User_details where name like %s",(name,))
    data=mycursor.fetchone()
    for i in data:
        us_name=data[0]
        us_pwd=data[1]
        if(us_name==name and us_pwd==password):
            return 1

def order(name):
    print("1.Electronics \n2.Beauty products \n3.Groceries")
    inp2=input("Enter your choice : ")
    if(inp2=="1"):
        print("List of electronic items : \nGaming Laptops : 75,0000 \nMobile phones : 50,000 \nHeadsets : 15,0000")
        e={"Gaming Laptops" : "75,0000", "Mobile phones" : "50,000","Headsets" : "15,0000"}
        buy=input("Enter what you wanna buy : ")
        item=e[buy]
        mycursor.execute("Select price from e_items where ename like %s",(buy,))
        data=mycursor.fetchall()
        price=int(data[0][0])
        print("Enter the count of order :")
        count=int(input())
        #global totalcost
        totalcost=price*count
        mycursor.execute("insert into orderdetails(name,item,totalcost) values (%s,%s,%s)",(name,item,totalcost,))
        mydb.commit()
        mycursor.execute("select * from orderdetails where name like %s",(name,))
        data=mycursor.fetchone()
        us_name=data[0]
        us_item=data[1]
        us_cos=data[2]
        print("Name :%s"%us_name)
        print("Item Ordered :%s"%us_item)
        print("Total Cost :%s"%us_cos)
        return 1

def display_orders():
    mycursor.execute("select * from orderdetails")
    data=mycursor.fetchone()
    for i in data:
        print("Name :%s"%data[0])
        print("Ordered item :%s"%data[1])
        print("Totalcost :%s"%data[2])
        break
    


if __name__=="__main__":
    print("Welcome to the world of amazon!")
    print("1.Signup \n2.Login")
    inp=input("Enter your choice : ")
    if(inp=="1"):
        name=input("Enter your name :")
        password=input("Create a password :")
        mail=input("Enter your mail :")
        phone=input("Enter your Phone number :")
        address=input("Enter your address :")
        mycursor.execute("insert into User_details(name,password,mail,phone,address)values(%s,%s,%s,%s,%s)",(name,password,mail,phone,address,))
        mydb.commit()
        print("You have successfully signed up!")
    elif(inp=="2"):
        name=input("Enter your name :")
        password=input("Enter your password :")
        if validate_user(name,password):
            print("1. Order items \n2. Display my previous orders")
            inp1=input("Enter your choice : ")
            if(inp1=="1"):
                if(order(name)):
                    print("Item ordered successfully!")
            elif(inp1=="2"):
                display_orders()
                         
    else:
        print("You have entered the wrong choice. \nKindly enter the correct choice!") 
        
                         
        
        
    
