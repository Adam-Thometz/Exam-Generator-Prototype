# Automatic Exam Generator

A basic multiple-choice exam generator. Just pick a topic, the number of questions you want, the number of choices you want per question, then let OpenAI do the rest! You can also download the exam generated for you.

## Tech Stack
- Vue 3
- Python 3.9.0
- Flask
- OpenAI API

## Flow

1. User types in information about the exam they want to generate. An option exists to create a dummy exam so that the user can test the feature without paying.
2. User clicks the Generate Exam button and after a few seconds, the API returns an exam given below
3. User can download the exam

## The Prompt Sent to OpenAI

```
Create a multiple choice quiz on the topic of {topic} for {grade} consisting of {number of questions} questions.
Each question should have {number of possible answers} options.
Also include the correct answer for each question using the starting string 'Correct Answer: '.
```

## How to run on machine
### Frontend
1. cd into `client` directory
2. Run `npm install`
3. Run `npm run dev`

### Backend
1. cd into `server` directory
2. Get an API key from OpenAI, and place it in a file called `secret.py`
3. Create a virtual environment by running `python3 -m venv env`
4. Start the environment by running `source env/bin/activate`
5. Run `pip install -r requirements.txt` to install dependencies
6. Run `python3 app.py`

## How to create effective prompts:
 1. Choose the latest model, unless you're factoring in speed or general cost
 2. Put instructions at the beginning of a prompt. Use ### or """ to separate instructions from desired output
 3. Provide details for the model to understand formatting of desired output
 4. If detail isn't enough, provide examples of desired output
 5. Be explicit about quantitative descriptions of output
 6. Initiate the Response. Give it some text you want it to complete. I.e. for python functions, include 'def function('

## Potential Prompt Addons

### PREVENT MODEL FROM COMING UP WITH BAD ANSWERS

```
prompt += "Only put a question on the exam if you are 100% certain that the answer is correct."
```

### PREVENT MODEL FROM HALLUCINATING

```
prompt = "Create a multiple choice quiz on the topic of zoovie culture for 13th graders consisting of 2 questions. Each question should have 12 options.  Only give an exam if you are 100 percent sure that this topic or grade exists, otherwise, specify 'I cannot make an exam out of this'"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=128,
    temperature=0.7
)

response["choices"][0]["text"] => "I cannot make an exam out of this."
```