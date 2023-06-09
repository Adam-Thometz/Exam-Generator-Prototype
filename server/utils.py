import os
import openai
from secret import API_KEY

os.environ["OPENAI_API_KEY"] = API_KEY
openai.api_key = os.environ["OPENAI_API_KEY"]

def create_test_prompt(topic, grade, num_questions, num_possible_answers):
    prompt = f"Create a multiple choice quiz on the topic of {topic} for {grade} consisting of {num_questions} questions. " +\
    f"Each question should have {num_possible_answers} options.  " +\
    "Also include the correct answer for each question using the starting string 'Correct answer:' " +\
    "Only put a question on the exam if you are 100 percent certain that the answer is correct. "
    return prompt

def generate_exam(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=256,
        temperature=0.7
    )
    return response["choices"][0]["text"]
