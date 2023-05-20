from faker import Faker
import datetime
import random
import csv

# Set up Faker
fake = Faker()

# Define start and end dates
start_date = datetime.date(2020, 1, 1) # '2020-01-01' 
end_date = datetime.date(2023, 12, 31) # '2023-12-31'

# Define number of purchases to generate
num_purchases = 1000

# Create list to hold customer data
customers = []

# Generate customer data
for i in range(num_purchases):
    customer_name = fake.name()
    customer_email = fake.email()
    customer_address = fake.address()
    customer_phone = fake.phone_number()

    # Append customer data to list
    customers.append([i+1, customer_name, customer_email, customer_address, customer_phone])

# Write customer data to CSV file
with open('customers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Customer ID', 'Name', 'Email', 'Address', 'Phone'])
    for customer in customers:
        writer.writerow(customer)

# Define product categories
categories = ['Laptops', 'Desktops', 'Smartphones', 'Tablets', 'Headphones', 'Speakers']

# Create list to hold purchase data
purchases = []

# Generate purchase data
for i in range(num_purchases):
    # Generate purchase date
    purchase_date = fake.date_between_dates(date_start=start_date, date_end=end_date)

    # Generate customer ID
    customer_id = random.randint(1, num_purchases)

    # Generate product data
    product_category = random.choice(categories)
    product_name = fake.text(max_nb_chars=50)
    product_price = random.randint(50, 2000)

    # Append purchase data to list
    purchases.append([purchase_date, customer_id, product_category, product_name, product_price])

# Write purchase data to CSV file
with open('purchases.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Customer ID', 'Product Category', 'Product Name', 'Product Price'])
    for purchase in purchases:
        writer.writerow(purchase)
