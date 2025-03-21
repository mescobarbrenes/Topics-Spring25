# Topics-Spring25
Repository for **Topics In Computer Science: Web Application Development With Python** for Spring 2025.

# **MUMUNDO: A Music Collection Management App**

## **History of MUMUNDO**
MUMUNDO was originally an idea I came up with in my Human-Computer Interaction class. MUMUNDO is currently a personal music list where users can post music entrys consisting of a song title, an artist's name and a description, however, in the future, and my original intention for MUMUMUNDO, was for it to become a community-driven platform to share and discuss music, inspired by current music review sites like AOTY (Artist of the Year) and RYM (Rate Your Music), but also from social medias like Twitter (X) and Reddit. MUMUNDO is derived from taking the first two words of the word music and mundo (world in spanish).

## **Project Overview**
As stated previously, MUMUNDO is a personal music collection where the user can add a music entry (song title, artist name, and description) to a playlist. The user will be able to see their music collection as they add songs, and they will be able to go back and edit and/or delete their music entrys.

### **Adding Music Entry and Reading Music Collection**
To add music, the user will be prompted to add a song title, an artist name, and a description. The user could perhaps write an opinion, a review, it's really up to the user on what they want to write about their music entry. Once the user is finished putting in their input, they can click to add the music entry to the music collection, which will pop up below. The user will be able to read their music collection as they add songs.

![Adding Music Entry Screenshot 1](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_midterm/midterm_gif_1.gif)

Please note that the user is required to put a song title and an artist name for the music entry to be posted. However, the user is not required to have a description for their music entry.

![Adding Music Entry Screenshot 2](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_midterm/midterm_gif_2.gif)

### **Editing and Deleting Music Entry**
In the existing music collection, the user is able to edit their music entrys by clicking the edit button in the music entry they want to edit. Once they click the edit button, the user will have the ability to edit the music title, then the artist name, and then the description.

![Editing Music Entry Screenshot](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_midterm/midterm_gif_3.gif)

The user is also able to delete their music entrys by clicking the delete button in the music entry they want to delete. Once they click the delete button, the music entry will disappear from the music collection.

![Deleting Music Entry Screenshot](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_midterm/midterm_gif_3.gif)

## **Accessing the Data in the API**
As the project stated, the data could be stored in the in-memory data. Once you add entrys to the music collection, you will be able to see all the music entrys in the API under /music.

![/music Data Screenshot](https://github.com/mescobarbrenes/Topics-Spring25/blob/main/images_midterm/midterm_data.png?raw=true)

## **Future Prospects For MUMUNDO**
I would like to be able to expand the adding music feature to where users can add other formats of music (albums, EPs, music videos, live performances) by utilizing the Spotfiy API. I would also like to expand customization on a post, possibly adding a reviewing system (which could further lead to organizing music by rating, or perhaps customizable organization in general) and the use of genre tags. 

As the plan is to have multiple users in the final project, I would like for users to be able to have their own respective profiles, where they are able to add a username, a profile picture, a description for their page, and perhaps their favorite music. As there will also be multiple users on the site, I would especially like to work on the interaction and socialization aspect, where users can like and comment on each others music entry posts, with the possibility to reblog each others posts (it would be really cool to be able to make comments when reblogs like on X).
