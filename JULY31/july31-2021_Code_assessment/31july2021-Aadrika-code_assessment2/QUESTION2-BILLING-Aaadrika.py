import re
import smtplib
while(True):
    name=input("Please Enter your Name :")
    email=input("Please Enter the Email Id :")
    regex1 = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
    valid1=re.match(regex1,email)
    if valid1:
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


        bill=Bill_Order()
        cost=0

        while(True):

            print("\nSelect an option from menu ")
            print("\n")
            print("1. Tea (Rs.7)")
            print("2. Coffee (Rs.10)")
            print("3. Masala Dosa (Rs.50)")
            print("4. View Bill and Email ")
            choice=int(input("\nEnter your Order choice:"))
            


            if choice==1:
                print("\nTea selected")
                teap=bill.price_tea()
                cost+=teap
                    

            if choice==2:
                print("\nCoffee selected")
                cofp=bill.price_coffee()
                cost+=cofp
            

            if choice==3:
                print("\nMasala Dosa Selected")
                dosap=bill.price_dosa()
                cost+=dosap
                
            if choice==4:
                print("Your Bill ")
                print("RS",cost)
                message=str(cost)
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("ridhimathur10@gmail.com","ridhima@10")
                connection.sendmail("ridhimathur10@gmail.com",email,message)

                print("Email for your Bill has successfully send")
                connection.quit()
                break
        break          
    else:
        print("Please Enter valid Email ID")
        continue




