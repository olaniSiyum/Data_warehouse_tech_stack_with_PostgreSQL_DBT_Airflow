# Data_warehouse_tech_stack_with_PostgreSQL_DBT_Airflow

The data warehouse techstack is built based on pNEUMA which is an open large-scale dataset of naturalistic trajectories of half a million vehicles that have been collected by a one-of-a-kind experiment by a swarm of drones in the congested downtown area of Athens, Greece. 

# objectives 
To establish a scalable data infrastructure, leveraging AI-driven analysis of swarm UAV footage and static cameras, to collect and manage vehicle trajectory data. This infrastructure aims to support the city's traffic department in optimizing traffic flow and facilitating undisclosed projects by utilizing comprehensive, real-time data insights gathered from a city locations.

# Data

There are 6 types of vehicles. These are Car, Taxi, Bus, Medium Vehicle, Heavy Vehicle, Motorcycle.
For each .csv file the following apply:
– each row represents the data of a single vehicle
– the first 10 columns in the 1st row include the columns’ names
– the first 4 columns include information about the trajectory like the unique trackID, the type of vehicle, the distance traveled in meters and the average speed of the vehicle in km/h
– the last 6 columns are then repeated every 6 columns based on the time frequency. For example, column_5 contains the latitude of the vehicle at time column_10, and column­­­_11 contains the latitude of the vehicle at time column_16.
– Speed is in km/h, Longitudinal and Lateral Acceleration in m/sec2 and time in seconds.
# Installation and Steps