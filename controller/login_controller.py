from dbconnect import register_collection
from model.login_model import Login
from bcryptEx import hash_password,verify_password
from bson import ObjectId

async def User_login(login : Login):
    try:
        query= {"username": login.Username}
        result= await register_collection.find_one(query)
        print(result)
        if result:
            print(result.get("password"),login.Password)
            data = verify_password(login.Password, result.get("password"))
            print(data)

            if verify_password(login.Password, result.get("password")):
                return{"mess": "loged in successfully"}
            else:
                return{"not found"}
    except Exception as e:
        return{"error":str(e)}
