import numpy as np

# File paths
aqi_file = "ClassRoomLearning\LabExam\AQI_Data.csv"  
output_file = "updated_pollutants.txt"

def count_rows_by_city(file_path):
    data = np.genfromtxt(file_path, delimiter=',', dtype=str, skip_header=1)
    
    cities = data[:, 0]
    
    unique_cities, counts = np.unique(cities, return_counts=True)
    return dict(zip(unique_cities, counts))

def add_pollutant_sum(file_path, output_path):
    data = np.genfromtxt(file_path, delimiter=',', dtype=str, skip_header=1)
    
    pollutant_data = data[:, 3:].astype(float)
    pollutant_sums = pollutant_data.sum(axis=1)
    
    updated_data = np.column_stack((data, pollutant_sums))
    
    header = "City,Date,AQI,PM2.5,PM10,NO2,CO,O3,SO2,Total"
    np.savetxt(output_path, updated_data, delimiter=',', header=header, comments='', fmt='%s')

city_counts = count_rows_by_city(aqi_file)
print("City Counts:", city_counts)

add_pollutant_sum(aqi_file, output_file)
print(f"Updated pollutants data saved to {output_file}")
