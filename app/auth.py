from flask import jsonify,Blueprint,request
from app.bcrypt import bcrypt
from app.prisma import with_prisma
from app.jwt import generate_token, require_auth

auth_bp=Blueprint("auth_bp",__name__)

@auth_bp.route("/login",methods=["POST"])
@with_prisma
async def login(prisma):

    data = request.get_json()
    if not data:
        return jsonify({"custom":True, "_meaasge":"Json body required"}), 400

    email= data.get("email")
    password=data.get("password")

    if not email:
        return jsonify({"custom":True, "_message": "Email required"})

    if not password:
        return jsonify({"custom":True, "_message": "Password required"})

    player=await prisma.player.find_unique(where={
        "email":email},
        include={
            "player_password":True
        }
    )
    if not player:
        return jsonify({"custom":True,"_message":f"Player with email {email} does not exist"}), 401

    player_password=player.player_password

    if not player_password:
        return jsonify({"custom":True,"_message":"Password not set"}), 500

    
    is_valid=bcrypt.check_password_hash(
        player_password.password,
        password
    )

    if not is_valid:
        return jsonify({"custom":True,"_message":"Invalid email or password"}), 401

    token=generate_token(id=player.id)

    return jsonify({"player":player.model_dump(),"token":token})


@auth_bp.route("/test",methods=["GET"])
@with_prisma
@require_auth
async def test_jwt(_jwt,prisma):
    print("User DATA is",_jwt)
    return "testing jwt"





@auth_bp.route("/sign-up",methods=["POST"])
@with_prisma
async def sign_up(prisma):
    #prisma = Prisma()

    #await prisma.connect()

    data = request.get_json()
    print("Request body", data)
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name:
        return jsonify({"custom":True, "_message": "Name required"}), 400

    if not email:
        return jsonify({"custom":True, "_message": "Email required"}), 400 

    if not password:
        return jsonify({"custom":True, "_message": "Password required"}), 400  

    if len(password) <3:
        return jsonify({"custom":True, "_message": "Password must have atleast 4 characters"})


    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    print("User email is", email)
    print("User password is", password)
    print("User name is", name)
    print("Password hash", hashed_password)

    player_exists = await prisma.player.find_unique(
        where={
            "email":email
        }
    )
    if player_exists:
        return jsonify({"custom":True,"_message":"Email already in use"})

    transcation=None
    async with prisma.tx() as tx:
        new_player=await tx.player.create(
            data={
                "name":name,
                "email":email
            }
        )

        new_player_pass = await tx.player_password.create(data={
            "player_id":new_player.id,
            "password":hashed_password
        })

        transaction=new_player

    return jsonify(transaction.model_dump())
