## Blog-site
# Author
    Joan Kirui
## Email
    joankirui99@gmail.com
## Project description
    This is a flask application that allows writers to post blogs, edit and delite blogs. It also allows users who have signed up to comment on the blogs that has been posted by a writer. It also allows a person to subscribed to recieve email everytime a new blog is posted by a writer.

## Live link
    blogsitejk.herokuapp.com/
## User story
    * A user can view the most recent posts.
    * View and comment the blog posts on the site.
    * A user should an email alert when a new post is made by joining a subscription.
    * Register to be allowed to log in to the application
    * A user sees random quotes on the site
    * A writer can create a blog from the application and update or delete blogs I have created.

## Development
    * Fork the repo
    * Clone the repo in your machine but ensure you have all the necessary modules.(You can find them in the set up instructions above) git clone https://github.com/joankirui/Blog_site.git
    * Create a new branch git branch contributions
    * Edit your changes in your branch
    * Run the application python3.6 manage.py runserver
    * Push your changes so we can have a view!
## BDD
|Behaviour|Input|Output|
|---------|-----|------|
|Load page|On page load|Get all blogs,select between sign up and login|
|select signup|email,username,password|redirect to login|
|select login|username and password|redirect to page with blogs that have been posted by writers and be able to subscribe to the blog|
|select comment button|comment|form that you input your comment|
|click on submit||redirect to all comments template with your comment and other comments|

## Technologies used
    * Python3.6
    * Flask
    * Heroku
 ## Known bugs
    updating blog gives an internal server error

## License
    * MIT License
    * Copyright (c) 2021 Joan Kirui
