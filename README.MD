# AI-Powered MCQ Quiz Generator
#### Video Demo:  <URL HERE>
#### Description:
This project leverages the OpenAI API to create dynamic multiple-choice question (MCQ) quizzes with accurate answers. The project is built using the Django frameworkwhile the SQLite3 database for storage and retrieval of quiz data.

#### Usage & Working:
The various tools and libraries used are:
- Django python web frameword
- sqlite3 database
- OpenAi API
- Bootstrap 

- The web pages follow the Django framewor design approach with the layout defined in "layout.html." By using the ``extends`` command subsequent pages are imported this layout to maintain consistency and manage them efficiently. The primary elements of the design included in the layout consist of a navigation bar and simple text forms. The coding logic is encapsulated within the services.py file, while views.py and url.py are used for integration of front-end and back-end features. 

- The SQLite3 database serves as the repository for all quiz-related data within the system. This information is structured and organized in a table with columns: a unique id, the initial question of each quiz, and the entirety of the quiz data. The unique id and the first question column are employed to facilitate the presentation of database content on the history web page, ensuring a coherent and meaningful display of quiz records.

- The text processing is executed utilizing OpenAI's GPT-3.5-turbo-instruct engine. Subsequently, the API response undergoes parsing wherein the relevant text is extracted for display purposes. To secure access to the API, the requisite secret key is confidentially stored in a '.env' file, and its retrieval is done using dotenv Python library. For local deployment, it is recommended to create a '.env' file within the '/quiz/' directory and store the API key with the format 'API_KEY= ???'.

- The design elements are made using Bootstrap with fundamental CSS. Currently, there is no implementation of JavaScript code. 

- I intend to revamp this project by using machine learning and alternative techniques, with the ultimate goal of discontinuing the reliance on OpenAI API.

#### Elements:
- Pages:
    - Home
    - History
    - Success Page
- Database: 
    - questions.db
    - db.sqlite3 (default)
