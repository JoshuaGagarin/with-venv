from flask import Flask, render_template, request, jsonify

chat_list = []

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',todos=chat_list)

# @app.route('/run-python-function', methods=['POST'])
# def run_python_function():
#     data = request.json
#     input_value = data.get('input_value', '')
#     result = my_python_function(input_value)
#     return jsonify(result=result)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        chat_list.append(task)
    print(chat_list)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
