from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'HEAD'])
def calculate():
    result = None
    username = None
    error = None
    
    if request.method == 'POST':
        try:
            username = request.form['username']
            microscope_size = float(request.form['microscope_size'])
            magnification = float(request.form['magnification'])
            
            if magnification == 0:
                error = "Magnification cannot be zero"
            else:
                result = f"{microscope_size / magnification:.2f}"
                
        except ValueError:
            error = "Please enter valid numbers"
    
    return render_template('index.html', 
                         result=result, 
                         username=username,
                         error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
