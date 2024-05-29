from flask import Flask, render_template, request, jsonify

chat_list = []
response_list = []
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',todos=chat_list, responses=response_list, zip=zip)


@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        chat_list.append(task)
        response_list.append(task)
        print(chat_list)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
