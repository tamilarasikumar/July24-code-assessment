import re
import smtplib
while(True):
    name=input("Please Enter Customer Name :")
    email=input("Please Enter the Customer Email Id :")
    regex12 = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
    valid12=re.match(regex12,email)
    if valid12:
        class Tea:
            def price_tea(self):
                self.tea_p=7
                return self.tea_p
        class Coffee:
            def price_coffee(self):
                self.coffe_p=10 
                return self.coffe_p
        class Masala_Dosa:
            def price_dosa(self):
                self.dosa_p=50
                return self.dosa_p

        class Bill_Order(Coffee,Tea,Masala_Dosa):
            pass

        billing=Bill_Order()
        cost=0

        while(True):

            print("\nSelect an option from menu ")
            print("\n")
            print("1. Tea (Rs.7)")
            print("2. Coffee (Rs.10)")
            print("3. Masala Dosa (Rs.50)")
            print("4. View Bill and Email ")
            choice=int(input("Enter your Order choice: "))
            if choice==1:
                print("\nTea selected")
                teap=billing.price_tea()
                cost+=teap
            if choice==2:
                print("\nCoffee selected")
                cofp=billing.price_coffee()
                cost+=cofp
            if choice==3:
                print("\nMasala Dosa Selected")
                dosap=billing.price_dosa()
                cost+=dosap
            if choice==4:
                print("Your Bill ")
                print("RS",cost)
                cost=str(cost)
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("hariompateldada@gmail.com","Sparsh@01")
                connection.sendmail("hariompateldada@gmail.com",email,cost)

                print("Email for your bill successfully sent")
                connection.quit()
                break
        break          
    else:
        print("Please Enter a valid Email ID")
        continue


    