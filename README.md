<h1>About</h1>

<p>This is my submission for Project P4: Build an Item Catalog Application, part of Udacity's Full Stack Web Developer Nanodegree.</p>

<h1>project Overview</h1>
<p>You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.</p>


## table of contents

- [Quick start](#quick-start)
- [Documentation](#documentation)
- [Setup](#setup)
- [Usage](#usage)

## quick-start
The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system.
	 - The homepage displays all current categories along with the latest added items.
	 - Selecting a specific category shows you all the items available for that category.
	 - Selecting a specific item shows you specific information of that item.
	 - After logging in, a user has the ability to add, update, or delete item info.
	 - The application provides a JSON endpoint, at the very least.
	 
   ![category-image](https://raw.githubusercontent.com/ashishchopra605/Item-Catalog/master/images/category.png)
   
## Documentation

This is a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication. Also, properly implementing authentication mechanisms and appropriately mapping HTTP methods to CRUD operations are core features of a properly secured web application.   

## Setup

 - Install all required Package first :

    - install python
    - apt-get -qqy update
    - apt-get -qqy upgrade
    - apt-get -qqy install postgresql python-psycopg2
    - apt-get -qqy install python-sqlalchemy
    - apt-get -qqy install python-pip
    - pip install --upgrade pip
    - pip install werkzeug==0.8.3
    - pip install flask==0.9
    - pip install Flask-Login==0.1.3
    - pip install oauth2client
    - pip install requests
    - pip install httplib2
    


 # virtualbox 
 
  -VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.]  (https://www.virtualbox.org/wiki/Downloads)  Install the *platform package* for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it. 

  -**Ubuntu 14.04 Note:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a [reported bug](http://ubuntuforums.org/showthread.php?t=2227131), installing VirtualBox from the site may uninstall other software you need. 
# usage

- Run the virtual machine!
    - Open a terminal and execute:
    - sudo apt-get install virtualbox  
- Clone this Repository and change directory to this project
- Now type in terminal  
    - **python database_setup.py** to initialize the database.
    - **python project.py** to run the Flask web server.
