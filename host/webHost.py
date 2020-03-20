from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def Index():
   return app.send_static_file('index.html');

@app.route('/GetTaskTypes')
def GetTaskTypes():
   return "访问成功"

@app.route('/GetTaskList/<int:id>')
def GetTaskList(id):
   return "获取所有任务"+str(id)

@app.route('/GetTakDetails/<int:id>')
def GetTakDetails(id):
   return "获取任务详情"+str(id)

if __name__ == '__main__':
   app.run(debug=True)