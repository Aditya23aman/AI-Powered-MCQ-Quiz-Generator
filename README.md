# AI-Powered MCQ Quiz Generator: Revolutionizing Dynamic Quizzes with OpenAI and Django
#### Video Demo:  https://youtu.be/OhUR6V4leyY
#### Description:
The AI-Powered MCQ Quiz Generator is harnesses the capabilities of the OpenAI API to create dynamic multiple-choice question (MCQ) quizzes with answers. Developed using the Django web framework and utilizing SQLite3 for efficient storage and retrieval of quiz data.


#### Tools used:
- Django Framework:
The backbone of this project is the Django web framework, which follows a Model-View-Controller (MVC) design pattern. The web pages are structured using Django's design approach, with the layout defined in ```layout.html`. Through the ```extends` command, subsequent pages import this layout, ensuring consistency and efficient management of the project.

- SQLite3 Database:
To store and organize quiz data, the project employs the SQLite3 database. The database schema includes a unique id, the initial question of each quiz, and the entire quiz data. The unique identifier and the first question column are pivotal for presenting database content on the history web page, ensuring meaningful display of quiz records.

- OpenAI API:
The text processing capabilities are executed using OpenAI's ```GPT-3.5-turbo-instruct engine```. The API response is parsed to extract relevant text for display purposes. To ensure secure access to the API, the required secret key is stored confidentially in a .env file, with retrieval facilitated using the dotenv Python library. Local deployment is simplified by creating a ```.env``` file within the /quiz/ directory and storing the API key in the format ```API_KEY= ???```.

- Bootstrap for Design
The design elements of the web pages are crafted using Bootstrap, complemented by fundamental CSS. The user interface is simple, making it easy for users to navigate through the quizzes and history using the nav bar. Currently, there is no implementation of JavaScript code, keeping the project lightweight and responsive.


#### Project Elements
- Pages
    - Home: The landing page providing users with access to the quiz generator.
    - History: A page displaying a comprehensive history of past quizzes, leveraging the SQLite3 database.
    - Success Page: Acknowledging the successful completion of a quiz, enhancing the overall user experience.
- Databases
    - questions.db: The primary database housing quiz data.
    - db.sqlite3 (default): The default SQLite3 database facilitating data storage and retrieval.

- Apps
    - Quiz:
        The only app utilized in this project is named "quiz." The URL patterns are explicitly defined in the ```url.py``` file, different web views and render functions articulated in ``` views.py```. The important project functionalities is in within ```services.py```. Within .services, functions are implemented for database initialization, API connectivity, prompt submission to the API, processing of API responses, and extraction of useful quiz data. Furthermore, services.py is responsible of generating SQL commands for the retrieval of data from the SQLite database, handling data handling operations.
