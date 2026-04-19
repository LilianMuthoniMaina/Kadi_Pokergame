from app.auth import auth_bp

@auth_bp.router("/",methods=["POST"])
async def signup():
    print(" Signup endpoint hit")
    return "Signup success"