from flask import  Flask

app=Flask(__name__)

@app.route('/',methods=['Get','Post'])

def index():
    return  "<hi>This is flask application created by Akhil </hi>"

if __name__=="__main__":
   app.run()
