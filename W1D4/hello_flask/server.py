from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"



@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return '<h1>Hello World!</h1>'  # Return the string 'Hello World!' as a response

@app.route('/say/<word_path_var>/<int:times>')
def say_word(word_path_var, times):
    # phrase = ""
    # for i in range(times):
    #     phrase += word + " "
    # return phrase
    return render_template("say_times.html",word=word_path_var,times=times,color="blue")

@app.route("/list")
def list():
    student_info = [
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]
    return render_template("list.html",list=student_info)

@app.route('/template')
def template():
    return render_template("index.html", num = 7)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5001,host="0.0.0.0")    # Run the app in debug mode.


#pip install pipenv <--- run this once ever so we can create virtual environments
#pipenv install flask <--- run this once PER PROJECT to set up a ve
#pipenv shell <--- activate our virtual env
#exit <--- leave ve

# *you may need to add python -m or python3 -m depending on your system
