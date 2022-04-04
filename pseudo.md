## Paths in craigslist_app.urls 
- `/categories`: A welcome page that lists all of the categories (with links to the categories)
- `/categories/new`: A page with a form to create a new category
- `/categories/<int:category_id>`: A page to view the detail of a specific category and a list of all of its associated posts (with links to those posts)
- `/categories/<int:category_id>/edit`: A page with a form to update a specific category, **with current values filled in already**. Also include the ability to delete the specific category from here. 
- `/categories/<int:category_id>/posts/new`: A page with a form to create a new post, **with the current category filled in already**.
- `/categories/<int:category_id>/posts/<int:post_id>`: A page to view the detail of a specific post. Also include the ability go back to the parent category detail page (`/categories/<int:category_id/>`).
- `/categories/<int:category_id>/posts/<int:post_id>/edit`: A page with a form to update a specific post, **with current values filled in already**. Also include the ability to delete the specific post from here.

## Models
- category
  -name(req)
  -description(req)
- post(item)
  -name(req)
  -description(req)
  -price(req)
  -contact info (poster)(req)
  -picture(opt)
  -post date(req)
  -delivery or pick-up()

## Admin
-Username:admin
-pass:admin

## TODO
-fix jpeg render on post detail page
-fix category selecting in add-post
-fix edit category not showing entire desc and / at end of cat name
-ablility to select multiple categories
