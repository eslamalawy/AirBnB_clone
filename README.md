<h1> AirBnB_clone </h1>

The goal of the project is to deploy on your server a simple copy of the AirBnB website.

The AirBnB website operates an online marketplace for travel information and booking services. The Company offers lodging, home-stay, and tourism services via websites and mobile applications. Airbnb serves clients worldwide.

<h2>Files and Directories</h2>

* <b>models</b> directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.

* <b>tests directory</b> will contain all unit tests.

* <b>console.py</b> file is the entry point of our command interpreter.

* <b>models/base_model.py</b> file is the base class of all our models. It contains common elements:

* <b>attributes:</b> id, created_at and updated_at

* <b>methods:</b> save() and to_json()

* <b>models/engine</b> directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py**

<h2> Steps </h2>

<h3>The console</h3>

* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

<h3> Web static </h3>

* learn HTML/CSS
* create the HTML of your application
* create template of each object

<h3>MySQL storage</h3>

* replace the file storage by a Database storage
* map your models to a table in database by using an O.R.M.

<h3>Web framework - templating</h3>

* create your first web server in Python
* make your static HTML file dynamic by using objects stored in a file or database

<h3> RESTful API </h3>

* expose all your objects stored via a JSON web interface
* manipulate your objects via a RESTful API
