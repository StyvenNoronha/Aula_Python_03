import csv
from faker import Faker

def generate_fake_data(num_entries=10):
    fake = Faker()
    fake_data = []

    for _ in range(num_entries):
        name = fake.name()
        age = fake.random_int(min=18, max=100)
        city = fake.city()

        fake_data.append({'name': name, 'age': age, 'city': city})

    return fake_data

def save_to_csv(data, file_name):
    with open(file_name, mode='w', newline='') as csv_file:
        fieldnames = ['Name', 'Age', 'City']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for entry in data:
            writer.writerow({'Name': entry['name'], 'Age': entry['age'], 'City': entry['city']})

if __name__ == "__main__":
    num_entries_to_generate = 10
    fake_data_list = generate_fake_data(num_entries_to_generate)

    csv_file_name = "arquivo.csv"
    save_to_csv(fake_data_list, csv_file_name)

    print(f"Generated fake data has been saved to {csv_file_name}.")
