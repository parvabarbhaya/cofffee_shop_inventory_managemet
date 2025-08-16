# cofffee_shop_inventory_managemet
It contains a IMS of  a coffee shop created using the python and Django Framework , and used the Sqlite3 for database 

# 1 problem statement 
Createa inventory management system for coffee shop owners to manage there inventory.

## 2 Tech stack used in this 
The technological use case in this is Django Frame Work , Python programming language and UI features is also being used in this 

## File Structure :
The file structurer is consist of two main types of file where 1) is of project in which we are creating our product and the 2 ) is consist of apps floder shich is inside the project file, which is connecte with the certin file of the project file , hear the main file is the manage.py fiel which manage the integration of both the project and app folders integration and connection the Structure is as follows :

<h2>my_django_project/</h2><br/>
│
├── manage.py<br/>
│
├── my_project/<br/>
│   ├── __init__.py<br/>
│   ├── settings.py<br/>
│   ├── urls.py<br/>
│   ├── wsgi.py<br/>
│   └── asgi.py<br/>
│
└── my_app/<br/>
    ├── migrations/<br/>
    │   └── __init__.py<br/>
    ├── __init__.py<br/>
    ├── admin.py<br/>
    ├── apps.py<br/>
    ├── models.py<br/>
    ├── tests.py<br/>
    └── views.py<br/>
<img width="1080" height="1080" alt="Gemini_Generated_Image_6qe07c6qe07c6qe0" src="https://github.com/user-attachments/assets/55c7229c-5a90-453e-aa78-984d9e38d1ad" />

## key Django Files with code understanding and excution 
⚙️ manage.py
This file provides a command-line interface for interacting with the Django project. It is utilized for executing administrative tasks such as initiating the development server, creating new applications, and applying database migrations. Consequently, it functions as the primary utility for project management operations.



🎛️ settings.py
As the central configuration file, settings.py governs the entire project's operational parameters. It contains critical definitions for the database connection, registered applications, middleware components, and other foundational configurations. This file is integral to defining the project's runtime behavior and its integration with various services.

🔗 urls.py
The urls.py file serves as the primary URL dispatcher for the project. It contains a mapping of URL patterns to their corresponding view functions, thereby directing incoming web requests to the appropriate application logic. This mechanism effectively serves as the navigational framework for the website.

💾 migrations/
This directory contains a version-controlled history of the database schema. Django's migration system automatically generates scripts within this folder in response to modifications in the models.py file. These scripts facilitate the systematic and reliable evolution of the database structure across different environments.

🛡️ admin.py
The admin.py file is used to register application models with Django's built-in administrative interface. By registering a model, its data becomes accessible for creation, retrieval, updating, and deletion operations within the admin panel. This provides a powerful and convenient interface for data management.

🧩 apps.py
Each application within a Django project includes an apps.py file for its specific configuration. This file allows for the definition of application-specific attributes and metadata. It is primarily used to declare the application's configuration class, which is then registered in the project's settings.py file.

📜 models.py
The models.py file is where the data structure of an application is defined through Python classes. Each class, inheriting from django.db.models.Model, corresponds to a table in the database. This file, therefore, constitutes the definitive blueprint for the application's data storage and organization.

🧠 views.py
This file contains the core logic for processing incoming HTTP requests and generating appropriate HTTP responses. A
