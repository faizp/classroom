# classroom
e-learning platform

<!-- TABLE OF CONTENTS 
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>-->



<!-- ABOUT THE PROJECT -->
## About The Project

Classroom is a e-learning platform built with Django.

Key Features:
* Group Video calling using `Webrtc`
* OTP login using `twilio`
* Test module for instructors
* Report module for Students
* Q and A
* Announcements module

### Built With

* Backend - `Django`
* Database - `PostgreSQL`
* Frontend - `HTML`, `CSS`, `Boostrap`, `Js`
* Api's and other libraries - `twilio`, `Ajax`, `Jquery`
* Video call and chat - `webrtc`, `django-channels`, `web-socket`

<!-- GETTING STARTED -->
## Getting Started

If you would love to run this project on your local env I will walk you through:

### Installation

1. Create virutal environment
   ```sh
   virtualenv venv
   ```
2. Activate virtualenv
   ```sh
   source venv/bin/activate
   ```
3. Clone the repo
   ```sh
   git clone https://github.com/faizp/classroom.git
   ```
4. Install requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
5. Run Project: <br>
   go to the project folder where manage.py file is present
   ```JS
   python manage.py runserver
   ```

