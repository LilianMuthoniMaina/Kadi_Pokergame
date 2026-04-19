from app.auth import auth_bp

@auth_bp.router("/",methods=["POST"])
async def login():
    print("Login endpoint hit")
    return "Login success"