import psycopg2 , requests, random

conn = psycopg2.connect(
      host="localhost",
        database="restaurant",
        user="postgres",
        password="postgres" 
)
cursor = conn.cursor()

url = "https://restcountries.com/v3.1/all?fields=name,capital,flag,subregion,population"
response = requests.get(url)
countries_data = response.json()
random_countries = random.sample(countries_data, 10)

for country in random_countries:
    name = country.get('name', {}).get('common', 'N/A')
    capital = country.get('capital', ['N/A'])[0] if country.get('capital') else 'N/A'
    flag = country.get('flag', 'N/A')
    subregion = country.get('subregion', 'N/A')
    population = country.get('population', 0)
    
    cursor.execute(
        "INSERT INTO countries (name, capital, flag, subregion, population) VALUES (%s, %s, %s, %s, %s)",
        (name, capital, flag, subregion, population)
    )

conn.commit()
cursor.close()
conn.close()
print("10 random countries inserted successfully!")