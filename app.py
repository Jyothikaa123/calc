from flask import *
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def claculator():
    result=None
    if request.method=='POST':
       num1=request.form.get('num1',type=float)
       num2=request.form.get('num2',type=float)
       operation=request.form.get('operation')

       if operation=='add':
        result=num1+num2
       elif operation=='subract':
        result=num1-num2
       elif operation=='multiply':
        result=num1*num2
       elif operation=='divide':
         if num2!=0:
            result=num1/num2
         else:
            result="error"
    return render_template('home.html',result=result)
if'__name__'=='__main__':
    app.run(debug=True)