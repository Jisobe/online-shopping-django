






# Assessment 4: Django
- **Craigslist Jr**

## Important Grading Information
- Make sure you read the [Assessment-4 Grading Rubric](https://docs.google.com/spreadsheets/d/11bCD5tstmbPhq8eqQD6NswuFOhiBLEBZv56ujREpPtQ/edit?usp=sharing).
  - Django Front-End (50%)
  - Django Back-End (50%)
- You need to get a 75% or better to pass. (You must pass all assessments in order to graduate Code Platoon's program.)
- If you fail the assessment, you have can retake it once to improve your score. For this assessment... 
  - 5% penalty: If you complete and submit the retake within **one week** of receiving your grade. 
  - 10% penalty: If you complete and submit the retake afterwards.

## Rules / Process
- This test is fully open notes and open Google, but is not to be completed with the help of other students/individuals
- Do not open a pull request against this repository.

## Requirements
- This assessment must be completed using Django. 
- You must use a PostgreSQL for your database.
  - Make sure you provide some seed data using Django fixtures 

## Challenge
Everyone loves going on Craigslist to find interesting people and interesting items. The joy of Craigslist is that it doesn't upgrade itself to stay up to date with the times - it's the same old Craigslist that everyone knows and loves. The core schema has also remained relatively unchanged over the years. Today, you will build a basic Craigslist CRUD app with nested routes. We will call this site: Craigslist Junior.

Here are a list of the routes you will need to build:
- `/categories`: A welcome page that lists all of the categories (with links to the categories)
- `/categories/new`: A page with a form to create a new category
- `/categories/<int:category_id>`: A page to view the detail of a specific category and a list of all of its associated posts (with links to those posts)
- `/categories/<int:category_id>/edit`: A page with a form to update a specific category, **with current values filled in already**. Also include the ability to delete the specific category from here. 
- `/categories/<int:category_id>/posts/new`: A page with a form to create a new post, **with the current category filled in already**.
- `/categories/<int:category_id>/posts/<int:post_id>`: A page to view the detail of a specific post. Also include the ability go back to the parent category detail page (`/categories/<int:category_id/>`).
- `/categories/<int:category_id>/posts/<int:post_id>/edit`: A page with a form to update a specific post, **with current values filled in already**. Also include the ability to delete the specific post from here.

Make sure your application has proper links on pages. The user should never have to type in the browser's address bar to get to pages (aside from getting to the home page). Also provide proper re-routing, i.e. for creating, updating, or deleting data... all actions should automatically redirect to another appropriate page, if successful, or display an error message if unsuccessful.

Also, please make sure you supply some seed data for your project (using [Django Fixtures](https://docs.djangoproject.com/en/4.0/howto/initial-data/)).

You do not need to style your pages (as Craigslist really doesn't make an effort to), but you should still have a nice basic visual presentation. You can earn a small bonus if you choose to add in some nice CSS styling to your front-end.  
