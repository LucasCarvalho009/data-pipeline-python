import csv

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

def transform_data(data):
    result = []
    for row in data:
        try:
            valor = float(row["valor"])
            if valor > 10:
                result.append(row)
        except ValueError:
            pass
    return result

def write_csv(data, output_path):
    if not data:
        print("There's no data written yet.")
        return

    headers = data[0].keys()
    with open(output_path, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    input_file = "data.csv"
    output_file = "filtered_data.csv"

    data = read_csv(input_file)
    filtered = transform_data(data)
    write_csv(filtered, output_file)

    print("ETL Finished!")

