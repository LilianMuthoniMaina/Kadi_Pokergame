#from dotenv import load_dotenv
from prisma import Prisma
from flask import Flask
#import asyncio
#from app import create_app


app=Flask(__name__)

@app.route("/student", methods=["GET"])
async def list_students():
    prisma=Prisma()
    await prisma.connect()

    student=await prisma.student.find_first(include-{
        "parent": True
    })
    student_dict=student.model_dump()
    prisma.disconnect()
    return jsonify(student_dict),200

if __name__=="__main__":
    app.run(debug=True)
    #asyncio.run()