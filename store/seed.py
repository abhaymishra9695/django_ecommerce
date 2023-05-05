from faker import Faker
fake = Faker()
import sys
print(sys.path)
from decimal import Decimal
import random
from .models import *
from django.utils.text import slugify
from datetime import datetime, timedelta
def product_seed(n=22):
    try:
        for _ in range(n):
            category_objs=Category.objects.all()
            rendom_index=random.randint(0,len(category_objs)-1)
            category=category_objs[rendom_index]
            product_name=fake.name()
            product_slug=slugify(product_name)
            sort_description=fake.paragraph(nb_sentences=1, variable_nb_sentences=True)
            description=fake.paragraphs(nb=3, ext_word_list=None)
            regular_price=Decimal(random.uniform(100, 100000))
            SKU=f'DIGI{random.randint(100, 500)}'
            stock_status='instock'
            quantity=random.randint(100, 200)
            imagesname=f'digital_0{random.randint(1,22)}.jpg'
            category=category_objs[rendom_index]
            start_date = datetime.now() - timedelta(days=365)
            end_date = datetime.now()
            date_joined = fake.date_between(start_date=start_date, end_date=end_date)
           
            Product.objects.create(
                    name=product_name,
                    slug=product_slug,
                    sort_description=sort_description,
                    description=description,
                    regular_price=regular_price,
                    SKU=SKU,
                    stock_status=stock_status,
                    quantity = quantity,
                    imagesname=imagesname,
                    category=category,
                    date_joined=date_joined
            )
    except Exception as e:
        print(e)



import os
import shutil

def save_image_to_media(image_path):
    # Get the filename of the image
    filename = os.path.basename(image_path)

    # Define the paths to the static and media directories
    static_path = "/path/to/static//"
    media_path = "/path/to/media/directory/"

    # Define the paths to the source and destination files
    source_file = os.path.join(static_path, filename)
    dest_file = os.path.join(media_path, filename)

    # Copy the file from the static directory to the media directory
    shutil.copy2(source_file, dest_file)

    # Return the path to the saved image
    return os.path.join("media", filename)
