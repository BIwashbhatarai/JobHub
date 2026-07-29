# 🚀 JobHub – Django Job Portal

JobHub is a full-stack job portal built with **Django** that connects **job seekers** with **recruiters**. Recruiters can post and manage jobs, while job seekers can search, apply, and track their applications through a clean and responsive interface.

This project was built to practice real-world Django development concepts such as authentication, role-based access control, CRUD operations, file uploads, search & filtering, dashboards, and relational database design.

---

## ✨ Features

### 🔐 Authentication & User Management

* Custom User Model
* User Registration & Login
* Logout
* Role-Based Authentication
* Recruiter and Job Seeker Accounts
* Django Messages Framework
* Protected Routes

---

### 👤 User Profiles

* Automatic Profile Creation using Django Signals
* View Profile
* Edit Profile
* Profile Picture Upload
* Skills
* Phone Number
* Address
* Bio

---

### 💼 Recruiter Features

* Recruiter Dashboard
* Create Job
* Edit Job
* Delete Job
* View Posted Jobs
* Manage Active Jobs
* View Applicants
* Update Application Status

---

### 👨‍💻 Job Seeker Features

* Job Seeker Dashboard
* Browse Jobs
* View Job Details
* Apply for Jobs
* Resume Upload
* Cover Letter Submission
* Prevent Duplicate Applications
* Track Application Status
* View Applied Jobs

---

### 🔎 Job Search

* Search by Job Title
* Search by Company
* Search by Location
* Filter by Job Type
* Filter by Experience Level
* Sort by:

  * Newest
  * Oldest
  * Salary (Low → High)
  * Salary (High → Low)

---

### 📊 Dashboards

#### Recruiter Dashboard

* Total Jobs Posted
* Active Jobs
* Total Applicants
* Recent Jobs
* Quick Actions

#### Job Seeker Dashboard

* Applied Jobs
* Available Jobs
* Recent Applications
* Latest Jobs
* Quick Actions

---

### 📁 File Uploads

* Profile Picture Upload
* Resume Upload
* Recruiter Resume Download

---

### 🛡️ Security & Validation

* Role-Based Permissions
* Login Required Views
* Duplicate Application Prevention
* Form Validation
* Deadline Validation
* Active Job Validation

---

## 🛠️ Tech Stack

### Backend

* Python
* Django

### Database

* SQLite

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Other

* Django ORM
* Django Signals
* ModelForms
* File Uploads
* Authentication System
* Messages Framework

---

## 📂 Project Structure

```text
JobHub/
│
├── accounts/
├── application/
├── jobs/
├── media/
├── static/
├── templates/
├── JobHub/
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/BIwashbhatarai/JobHub.git
```

### Navigate into the project

```bash
cd JobHub
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply migrations

```bash
python manage.py migrate
```

### Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### Run the development server

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

Add screenshots here after deployment.

* Home Page
* Recruiter Dashboard
* Job Seeker Dashboard
* Job Listing
* Job Details
* Applicant Management

---

## 📈 Future Improvements

* PostgreSQL Support
* Django REST Framework API
* React Frontend
* Email Notifications
* Saved Jobs
* Company Profiles
* AI Job Recommendations
* Resume Parsing
* Docker Deployment
* CI/CD Pipeline

---

## 📚 What I Learned

During this project, I gained hands-on experience with:

* Django Project Structure
* Custom User Models
* Authentication & Authorization
* Django Signals
* Model Relationships
* CRUD Operations
* ModelForms
* File Upload Handling
* Search & Filtering
* Query Optimization
* Role-Based Dashboards
* Git & GitHub Workflow
* Building a Real-World Django Application

---

## 👨‍💻 Author

**Biwash Bhattarai**

* GitHub: https://github.com/BIwashbhatarai
* LinkedIn: https://www.linkedin.com/in/biwash-bhattarai/

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It motivates me to continue building and sharing more projects.
