import openai
import sqlite3
from dotenv import load_dotenv
import os


def config():
    load_dotenv()
    openai.api_key = os.getenv('API_KEY')

def initialize_database():
    # connecting to sqlit3 database
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    #create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions
                   (id INTEGER PRIMARY KEY, summary TEXT, first TEXT UNIQUE, quiz TEXT)''')
    conn.commit()
    conn.close()

def generate_questions(text):
    initialize_database()
    config()

    #connect to database
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    # openAi prompt
    prompt = f"Create a practice test with multiple choice questions on the following text:\n{text}" \
             f"Each question should be on a different line. Each question should have 4 possible answers. "\
             f"Under the possible answers we should have the correct answer."  

    #respons
    response = openai.Completion.create(
        engine = "gpt-3.5-turbo-instruct",
        prompt = prompt,
        max_tokens = 3500,
        stop = None,
        temperature = 0.7
    )

    #exract generated questions
    all_questions = response.choices[0].text
    all_questions= all_questions.strip()


    first_question = all_questions.splitlines()[0][3:]

    # print(all_questions)
    # print(first_question)

    # loading questions into the dababase
    conn.execute('INSERT INTO questions(first, quiz) VALUES(?,?)', (first_question,all_questions,))
    conn.commit()
    conn.close()

    return all_questions

def get_all_questions():
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    # fetch data from database
    cursor.execute('SELECT id, first FROM questions ORDER BY id')
    data = cursor.fetchall()

    # data = str(data)
    conn.commit()
    conn.close() 
    return (data)

def create_quiz_txt(quiz_id):
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

    # fetch data from database
    cursor.execute('SELECT quiz FROM questions WHERE id = ?', (quiz_id,))
    data = cursor.fetchall()
    data = data[0][0]
    # data = str(data)
    # print(data)

    # Open the file in write mode ('w' flag) and write the string to it
    file_name = f"{quiz_id}_questions.txt"
    with open(file_name, 'w') as file:
        file.write(data)

    os.startfile(file_name)
    conn.commit()
    conn.close()

    return  

        
