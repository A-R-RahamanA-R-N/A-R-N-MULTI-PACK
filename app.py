


from flask import Flask,request

app=Flask(__name__)

@app.route('/',methods=["GET"])

def homepage():
      
      return "I am ARN"

if __name__="__main__":
    
    app.run(threaded=True)