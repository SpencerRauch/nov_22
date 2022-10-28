from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/form') #VIEW
def display_form():
    return render_template("form.html")

@app.route('/food_form_process', methods=['POST','GET']) #ACTION NEVER RENDER ON AN ACTION ROUTE
def process_form():
    print(request.method)
    if request.method == "POST":
        pass
        
    else:
        pass
        
    print(request.form)
    session['food_name'] = request.form['name']
    session['spicy'] = request.form['is_spicy']
    if 'check' in request.form:
        session['check'] = request.form['check']
    # return "test"
    # return render_template("show.html", food_name=request.form['name'] , spicy=request.form['is_spicy']) #THIS IS BAD PRACTICE
    return redirect('/show')


@app.route('/show')
def show():
    if "check" not in session:
        return redirect('/form')
    return render_template("show.html")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.