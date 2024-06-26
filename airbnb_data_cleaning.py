import pandas as pd

# Load the dataset
df = pd.read_csv('/content/sample_airbnb.listingsAndReviews (1).csv')

# Select columns of interest
data1 = df[['_id', 'name', 'summary', 'space', 'description', 'neighborhood_overview',
           'notes', 'transit', 'access', 'interaction', 'house_rules', 'property_type',
           'room_type', 'bed_type', 'minimum_nights', 'maximum_nights', 'cancellation_policy',
           'last_scraped', 'calendar_last_scraped', 'accommodates', 'bedrooms', 'beds',
           'number_of_reviews', 'bathrooms', 'price', 'weekly_price', 'monthly_price',
           'cleaning_fee', 'extra_people', 'guests_included', 'review_scores.review_scores_rating',
           'address.location.coordinates[0]', 'address.location.coordinates[1]']]

# Display the shape of data1
print("Shape of data1:", data1.shape)

# Check for missing values in data1
print("Missing values in data1:")
print(data1.isnull().sum())

# Drop unnecessary columns from data1
columns_to_drop = ['_id', 'summary', 'space', 'description', 'neighborhood_overview',
                   'transit', 'access', 'interaction', 'house_rules', 'weekly_price',
                   'monthly_price', 'cleaning_fee']
data2 = data1.drop(columns_to_drop, axis='columns')

# Save cleaned data to a new CSV file
data2.to_csv('Airbnb_data.csv', index=True)


