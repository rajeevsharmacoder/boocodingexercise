# boocodingexercise
Coding Exercise Showing django and mongodb integration using djongo

This is a simple app for below assignment (only backend part) -

Part 1:

Store the profile data in a MongoDB database instead of in memory. For ease of testing, use mongodb-memory-server (https://github.com/nodkz/mongodb-memory-server) instead of connecting to an external database.
Add a post route for creating new profiles. Note: you can re-use the same image for all profiles. You do not need to handle picture uploads.
Update the get route to handle profile ids in the url. The server should retrieve the corresponding profile from the database and render the page accordingly.


Part 2:

Implement a backend API that supports the commenting and voting functionality described in the Figma: https://www.figma.com/file/8Iqw3VwIrHceQxaKgGAOBX/HTML%2FCSS-Coding-Test?node-id=0%3A1
You do not need to implement the frontend. Assume that the frontend will call your backend API in order to create user accounts, post comments, get/sort/filter comments, and like/unlike comments.
You do not need to implement secure auth or picture uploads. The only attribute needed for user accounts is name. Assume that anyone can access and use any user account.
All data should be stored in the same database used in Part 1.


Part 3:

Add automated tests to verify the implementation of Part 1 and Part 2.


You should have python3 on your machine.
You will need to install pymongo, djongo, Django, Pillow and "/Applications/Python\ 3.x/Install\ Certificates.command". So better to use a virtual environment for the same.



As database I have not used the suggestion in the part 1 but made use of an Atlas Cluster on "https://cloud.mongodb.com/". I have removed my credentials from the settings.py file of the project.
In case you want to run the project successfully then -
1) You will have to create your own Atlas cluster at "https://cloud.mongodb.com/".
2) Get the connection string by clicking Connect > Connect your application and getting the URI from there and using it in the settings.py file.
3) Once you have connected to the database, you have to make migrations and and migrate them so that appropriate collections are made in the database.
Congratulations, now you can start hitting the API's like shown in the "api_exeuctions_screenshots_from_postman.docx" document via Postman.

Also you will have to add a sample image in the media directory and you can use the same image for testing purpose.

Hope this project helps you understand how django connects to mongodb.
