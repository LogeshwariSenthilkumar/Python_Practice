def validate(s_user,s_pass):
    s_username="EMC"
    s_password="123" 
    if(s_user==s_username and s_pass==s_password):
        return True
    else:
        return False
username=input("Enter Name:")
password=input("Enter Password:")
print(validate(username,password))
