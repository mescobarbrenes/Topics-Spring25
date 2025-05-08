# Topics-Spring25
Repository for **Topics In Computer Science: Web Application Development With Python** for Spring 2025.

# **Homework 4: User Login**

## **Step 1: User Sign-Up**
In order for users to use MUMUNDO, they must first create an account. To sign up for an account, they must go to the sign-up page, and create a username and password for their account. They are required to fill out both fields. A message pops up stating that the user has successfully signed up when the user clicks sign up.

In order for users to use MUMUNDO, they must first create an account. To sign up for an account, they can press the login button, which will redirect them to a login page. If the user needs to make an account, they are able to sign up at the button of the login form.

![User Starts Here](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_hw4/hw4_start.png?raw=true)

![User Redirected to Login Page](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_hw4/hw4_redirected_1.png?raw=true)

![User Sign-Up Page](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_hw4/hw4_signup_1.png?raw=true)

![User Sign-Up Error](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_hw4/hw4_signup_2.png?raw=true)

![User Successful Sign-Up](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_hw4/hw4_signup_3.png?raw=true)

## **Step 2: User Log-In**
Once the user creates an account, they are redirected to the user login page, where they are prompted to enter their username and password. Like the sign-up process, if the user doesn't input both username and password, an error message will pop up telling the user they must fill out all fields. Once the user has filled out all fields, they are able to click to login to their account. If the account doesn't exist, an error message will also pop up stating that the account does not exist.

![User Login Page](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_hw4/hw4_login_1.png?raw=true)

![User Login Error](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_hw4/hw4_login_2.png?raw=true)

## **Step 3: Logged-In User and Logging Out**
Once the user has successfully logged-in, they are able to post, view, edit, and delete their posts in the music playlist. If the user chooses to log out of their account, there is a log out button on the top right-hand corner of the page. Once the user logs out, it redirects the user to the login page.

![Logged-In User 1](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_hw4/hw4_loggedin_1.png?raw=true)

![Logged-In User 2](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_hw4/hw4_loggedin_2.png?raw=true)

## **MongoDB Integration**
When a user has an account, they can be found in the user collection of Cluster0 in MongoDB. For example, user snoopy has been added in the user collection.
![MongoDB Integration](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_hw4/hw4_mongodb.png?raw=true)

<pre> \`\`\`bash uvicorn mumundo.backend.main:app --reload \`\`\` </pre>
