from flask import Flask, request
from flask_cors import CORS
from utils import create_test_prompt, generate_exam

app = Flask(__name__)
CORS(app)

dummy_exam = '\n\nQ1. What is the syntax for declaring a variable in Python?\nA. #variable\nB. var variable\nC. !variable\nD. var = variable\nCorrect Answer: D. var = variable\n\nQ2. What type of language is Python?\nA. Interpreted\nB. Compiled\nC. Assembly\nD. Machine\nCorrect Answer: A. Interpreted\n\nQ3. What type of loop is used when a set of instructions need to be repeated until a condition is met?\nA. For loop\nB. While loop\nC. Do-while loop\nD. If-else loop\nCorrect Answer: B. While loop\n\nQ4. What is the result of the following expression?\n2 + 5 * 3\nA. 23\nB. 17\nC. 11\nD. 25\nCorrect Answer: B. 17'

@app.route("/")
def index():
    return "Hello world!"

@app.route("/create", methods=["POST"])
def create_exam():
    data = request.get_json()["data"]
    is_dummy_exam = data["isDummyExam"]
    if is_dummy_exam:
        return dummy_exam
    
    topic = data["topic"]
    grade = data["grade"]
    num_questions = data["numQuestions"]
    num_choices = data["numChoices"]

    prompt = create_test_prompt(topic, grade, num_questions, num_choices)
    
    exam = generate_exam(prompt)
    return exam

if __name__ == '__main__':
    app.run(host="localhost", port=3001, debug=True)
