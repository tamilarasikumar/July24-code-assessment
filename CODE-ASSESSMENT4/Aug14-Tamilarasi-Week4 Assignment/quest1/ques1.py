import smtplib,re,logging,json,pymongo,collections
from datetime import date

#########  Connection MongoDb
client=pymongo.MongoClient("mongodb://localhost:27017/")  
mydatabase=client["BloodBankDb"]
collection_name=mydatabase["BloodBank"]

print("############    BLOOD BANK MANAGEMENT SYSTEM     #############")
a=collections.deque()
logging.basicConfig(filename='bloodbank.log',level=logging.DEBUG)

class BloodBank:
    def addDonors(self,name,address,blood_group,pincode,mbl_no,last_donated_date,place,email_id):
            dict={"name":name,"address":address,"blood_group":blood_group,"pincode":pincode,"mbl_no":mbl_no,"last_donated_date":last_donated_date,"place":place,"email_id":email_id}
            a.append(dict)
obj=BloodBank()

############ Validation
def validate(vname,vaddress,vpincode,vmbl_no,vemail_id):
    name1=re.search("^[A-Z]{1}[a-z]{0,25}$",vname)
    print(name1)
    address1=re.search("^[0-9a-zA-Z\s,-]+$",vaddress)
    print(address1)
    pincode1=re.search("^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",vpincode) 
    print(pincode1)
    mobilenumber1=re.search("^91[6-9]\d{9}$",vmbl_no)
    print(mobilenumber1)
    emailid1=re.search("[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",vemail_id)
    print(emailid1)
    if name1 and address1 and pincode1 and mobilenumber1 and emailid1:
        return True
    else:        
        return False
try:
    if __name__== "__main__":
            while(1):
                print("0.View the Donors Details ")
                print("1.Add Donors Details ")
                print("2.Search Donors Based On Blood Group ")
                print("3.Search Donors Based On Blood Group And Place ")
                print("4.Update All The Donors With The Mobile Number ")
                print("5.Delete The Donor Using Mobile Number ")
                print("6.Display The Total Number Of Donors On Each Blood Group ")
                print("7.Send Mail To Donors ")
                print("8.Exit ")
                option=int(input("Enter Your Option: "))
                if option==1:
                    vname=input("Enter The Donor Name: ")
                    vaddress=input("Enter The Donor Address: ")
                    blood_group=input("Enter The Donor Blood Group: ")
                    vpincode=input("Enter The Donor Pincode: ")
                    vmbl_no=input("Enter The Donor Mobile Number: ")
                    last_donated_date=input("Enter The Donor Last Donated Date: ")
                    place=input("Enter The Donor Place: ")
                    vmail_id=input("Enter The Donor Mail ID: ")
                    if validate(vname,vaddress,vpincode,vmbl_no,vmail_id):
                        obj.addDonors(vname,vaddress,blood_group,vpincode,vmbl_no,last_donated_date,place,vmail_id)
                        collection_name.insert_many(a)
                    else:
                        logging.error("Wrong!Check Your Validation")
################   View the Donors Details
                if option==0:
                    r=collection_name.find()
                    for i in r:
                        print(i)

################   Search Donors Based On Blood Group 
                if option==2:
                    a=input("Search the Donors Based On Blood Group: ")
                    r=collection_name.find({"blood_group":a})
                    for i in r:
                        print(i)
                        logging.info("Successfully!!! Search the data")

################   Search Donors Based On Blood Group And Place            
                if option==3:
                    a=input("Search the Donors Based On Blood Group: ")
                    b=input("Search the Donors Based On Place: ")
                    r=collection_name.find({"blood_group":a,"place":b})
                    for i in r:
                        print(i)
                        logging.info("Successfully!!! Search the data")

################   Update All The Donors With The Mobile Number
                if option==4:
                    u=input("Enter The Donors Name: ")
                    update_mblno=input("Update The Donors Mobile Number: ")
                    r=collection_name.update_many({"name":u},{"$set":{"mbl_no":update_mblno}})
                    print(r)
                    logging.info("Successfully!!! update the data")

################   Delete The Donor Using Mobile Number
                if option==5:
                    d=input("Delete Donors Mobile Numbers: ")
                    r=collection_name.delete_many({"mbl_no":d})
                    print(r.deleted_count)
                    logging.info("Successfully!!! delete the data")

################   Display The Total Number Of Donors On Each Blood Group 
                if option==6:
                    r=collection_name.aggregate([{"$group":{"_id":"$blood_group","count":{"$sum":1}}}])
                    for i in r:
                        print(i)
                        logging.info("Successfully!!! count the data")

################   Send Mail To Donors
                if option==7:
                    try:
                        blood=input("Enter Urgent Blood Group: ")
                        result=collection_name.find()
                        for x in result:
                            if x["blood_group"]==blood:
                                a.append(x)
                                message='''URGENT! URGENT! PLEASE CONTACT ME SOON   
        Immediately We Want Your blood group in Saravana Hospital,So Please Contact Me Soon!!!
        CONTACT NUMBER:9876543215 '''
                                print(message)
                                connection=smtplib.SMTP("smtp.gmail.com",587)
                                connection.starttls()
                                connection.login("tamilarasiiprimed@gmail.com","Iprimed@123")
                                connection.sendmail("tamilarasiiprimed@gmail.com",x["email_id"],message)
                                connection.quit
                                print("Mail Sent Successfully:)")
                    except Exception:
                        logging.error("Please Check Your Mail")

                if option==8:
                    break
except ValueError:
    logging.error("Please Check Value int or string")

except IndexError:
    logging.error("Please Check Your Index")

except Exception:
    logging.error("Something Went Wrong")

finally:
    print("Äll Block Completed Successfully")










            

