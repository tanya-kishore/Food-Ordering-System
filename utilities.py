import db

def login(uname,password):
    data = db.check_user(uname)
    if data is None:
        print('Create Account first')
        return -1
    else:
        stored_password = data[0][1] if len(data[0]) > 2 else None

        if stored_password is not None and stored_password == password:
            return 1
        else:
            return 0
        
def forget(uname,password):
    # data = db.check_user(uname)
    # if data is None:
    #     return 0

    new_password = input("Enter new password: ")
    db.update_password(uname, new_password)
    if (new_password==password):
        print("Already existed password")
        return 0
    else:
        print("Password successfully updated")
        return 1
