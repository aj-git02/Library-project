# Library-project
Dev-Club assignment for creating a library management website
(Created using Django)

Salient Features-
1. Registration portal for new users
2. Webpage for each user ,Mentioning thier details such as books issued, pending issues,etc.
3. Ability to issue books (with system for approval by librarian)
4. implemented a search box which when entered keywords of a book name gives the list of books starting with that name.
5. Creation of three groups admin, librarians, active users. The powers of the admin are maximum and can alocate a user to be a librarian. A librarian can change the book info ,approve issuing of books,change content. (via the admin webpage) (but thier powers are limited on making other users librarians in which admin is required)
7. list of all available books, books with pending approval, approved books
8. Each book has its own Webpage with information such as name, rating, description.

For signing in as a user use-
username: user4,
password: devclub1

for signing as librarian use-
username: librarian1,
password: devclub1

For signing as admin use-
username: akarsh,
password: dev

To navigate thorugh website:
1. clone the repository on your computer
2. run python manage.py runserver
3. take the web-adress provided and open in a browser (http://127.0.0.1:8000/admin/ to go to the admin page) 
4. for approving borrow status login as librarian to the admin page then go to Borrow and on clicking on any request you can view the On-approval check box.
5. for taking part as a user start from http://127.0.0.1:8000/books/ this will first redirect to login/signup page from where nearly everything is connected.
6. you may signup as a new user or use the credentials given above.
