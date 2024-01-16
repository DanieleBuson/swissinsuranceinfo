# SwissInsurance-Info

SwissInsurance-Info is a web application built using Django for the backend and jQuery for the frontend. This application allows users to ask questions related to insurance, and the answers are generated using ChatGPT, which has been trained on context scraped from data collected through web scraping. The questions and answers are stored in AWS and processed to provide users with informative responses.

## Setting Up a Django Project

To set up a Django project similar to SwissInsurance-Info, follow these steps:

1. **Create a Virtual Environment:**
python -m venv myenv


2. **Activate the Virtual Environment:**
- On Windows:
  ```
  myenv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source myenv/bin/activate
  ```

3. **Install Django:**
pip install django


4. **Create a New Django Project:**
django-admin startproject myproject


5. **Create Apps Within the Project:**
python manage.py startapp myapp


6. **Define Models, Views, and Templates:**
- Define your data models in the `models.py` file of your app.
- Create views to handle user requests in the `views.py` file.
- Design HTML templates for the frontend in the `templates` directory.

7. **Configure URLs:**
Define URL patterns in the `urls.py` files of your app and project to route requests to the appropriate views.

8. **Configure the Database:**
Set up your database settings in the `settings.py` file.

9. **Migrate the Database:**
python manage.py makemigrations
python manage.py migrate


10. **Create Superuser (Admin):**
 ```
 python manage.py createsuperuser
 ```

11. **Run the Development Server:**
 ```
 python manage.py runserver
 ```

12. **Access the Admin Panel:**
 Open your browser and go to `http://localhost:8000/admin/`. Log in with the superuser credentials created earlier.

Now, you have a basic Django project set up. You can start building your web application and integrating the necessary features like user authentication, data storage, and more.

## SwissInsurance-Info

SwissInsurance-Info is a practical example of a web application built using Django and jQuery. It provides users with a platform to ask insurance-related questions, and the answers are generated using ChatGPT. 
The project utilizes web scraping to collect data and context, which is used to train ChatGPT and provide relevant responses to user queries.

### Features

- Ask Questions about Insurance
- ChatGPT Integration for Answering Questions
- AWS Integration for Data Storage
- Data Scraping for Context Building
- Data Processing for Improved Responses

### Usage


1. **Ask Questions:** Users can ask questions related to insurance topics. These questions are processed and answered using ChatGPT.

2. **Answers:** ChatGPT generates informative answers based on the context gathered from data scraping and training.

3. **Data Storage:** The questions and answers are stored in AWS, ensuring data integrity and accessibility.

4. **Data Processing:** The collected data is processed to improve the quality of responses and maintain relevance.

SwissInsurance-Info is a valuable tool for those seeking information about insurance and provides a seamless user experience by leveraging Django and ChatGPT.

