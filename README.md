# Fashion App - API View

## Project Overview
This Django-based API returns video content for the home screen of a fashion app. The API delivers detailed information about videos, users, products, and more. It also incorporates pagination for large datasets and is designed to scale efficiently with a growing user base.
I have implemneted two apps, Fashion_app that return the API response in the standard way. Fashion_app2 that returns the API response with cursor-pagination, caching etc.

## Features
- **Video Content API**: Returns video details, user profiles, product details, and engagement statistics (likes, comments, shares).
- **User Profiles**: Displays user information such as username, bio, follower count, and profile picture.
- **Products**: Associates fashion products with each video, including product details, store information, and available variants.
- **Pagination**: Efficient handling of large datasets with pagination.
- **Scalability**: Designed to scale to support a large user base.

## Technology Stack
- **Backend Framework**: Django, Django REST Framework
- **Database**: PostgreSQL
- **ORM**: Django's ORM

  ## Prerequisites
Make sure you have the following installed before proceeding:
- Docker(for database creation)
- Python 3.8+
- PostgreSQL
- Git

  ## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Ayushsinha2629/Attyre.git
cd Attyre
cd fashion_app
```
### To create a database you can either use docker(for fashion_app)
```bash
docker run -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5434 postgres
```
or create your own usuing neon.tech and update the database credentials in fashion_app/settings.py

### Create a databse named fashion_db
```bash
docker exec -it "container_id" bin/bash
psql -U "your_db_username"
CREATE DATABASE fashion_db
\q
```

### Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create dummy data using python shell
```bash
python manage.py shell

from myapp.models import User, Store, Variant, Product, Music, Video

# Create a user
user = User.objects.create_user(username='fashion_lover', password='password123', display_name='Fashion Lover', verified=True)

# Create a store
store = Store.objects.create(name='WinterWear Co.', logo_url='https://example.com/stores/winterwear_logo.jpg')

# Create variants
size_variant = Variant.objects.create(name='Size', options=['S', 'M', 'L', 'XL'])
color_variant = Variant.objects.create(name='Color', options=['Red', 'Blue', 'Green'])

# Create a product
product = Product.objects.create(
    name='Cozy Sweater',
    price=59.99,
    original_price=79.99,
    discount_percentage=25,
    image_url='https://example.com/products/cozy_sweater.jpg',
    timestamp=15,
    currency='USD',
    store=store,
    in_stock=True
)
product.variants.set([size_variant, color_variant])

# Create music
music = Music.objects.create(
    name='Winter Wonderland',
    artist='Frosty Tunes',
    cover_url='https://example.com/music/winter_wonderland.jpg'
)

# Create a video
video = Video.objects.create(
    video_url='https://example.com/videos/newvideo.mp4',
    thumbnail_url='https://example.com/thumbnails/newthumbnail.jpg',
    description='Winter fashion trends 2024 #winterfashion #trendalert',
    view_count=1500,
    duration=60,
    user=user,
    likes_count=500,
    comments_count=150,
    shares_count=75,
    is_liked=False,
    is_bookmarked=False,
    music=music,
    hashtags=['winterfashion', 'trendalert']
)
video.products.set([product])

exit()
```

### Run the server 
```bash
python manage.py runserver
```
### Test the API Endpoint "http://127.0.0.1:8000/myapp/response" using POSTMAN

## Follow the same steps for fashion_app2 

### Create a new database
```bash
docker run -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5435 postgres
```
### Follow the same steps of creating a fashion_db database and run the same commands.

### Test the API Endpoint "http://127.0.0.1:8001/myapp2/response" using POSTMAN






