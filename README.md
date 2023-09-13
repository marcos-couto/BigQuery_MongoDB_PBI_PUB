# Project Title: Global Life Expectancy Data Analysis and Visualization


## Introduction:
Life expectancy is a critical indicator of the overall health and well-being of populations around the world. It is also a fundamental metric that reflects the development level of countries and their healthcare systems' contribution to different regions.
This project uses data from an [International Organization](https://www.census.gov/data-tools/demo/idb/#/table?menu=tableViz) to gather, analyze, and visualize information about life expectancy for both men and women in countries worldwide. The goal is to gain insights into disparities, trends, and factors that influence life expectancy, ultimately contributing to a deeper understanding of global health. 
This will help to establish comparisons between countries, elucidate what is being done to improve life expectancy, as well as what is not being done, and the impact of both on the general quality of life.

## Project description:
 This project uses advanced data technologies and cloud services to create a comprehensive data pipeline. It begins with the extraction of life expectancy data from a source such as Google BigQuery. 
 Python scripts are then used to transform the data into JSON documents and store them in a MongoDB database. Simultaneously, data is securely backed up in an AWS S3 bucket for data preservation.

To enable data-driven decision-making, this project integrates Power BI with MongoDB. Power BI is employed to design interactive dashboards and reports that visualize life expectancy data. These visualizations provide users with the ability to explore variations in life expectancy across countries, gender differences, and potential correlations with socioeconomic factors.

## Methods and Results: ( In Progress)
The project successfully extracts and transforms life expectancy data, creating a structured and accessible database in MongoDB.
In future, as a chalengeing, data will regularly updated through automated processes, ensuring that the visualizations in Power BI reflect the latest information.

The visualizations in Power BI provide valuable insights into global life expectancy trends. Users can interact with the data, uncovering variations in life expectancy between men and women and identifying countries with higher or lower life expectancies. Additionally, the project allows for comparisons of life expectancy across different regions and the exploration of potential factors influencing life expectancy disparities.

## Conclusion and Future Directions: ( In progress )
The project successfully extracts and transforms life expectancy data, creating a structured and accessible database in MongoDB. Data is regularly updated through automated processes, ensuring that the visualizations in Power BI reflect the latest information.

The visualizations in Power BI provide valuable insights into global life expectancy trends. Users can interact with the data, uncovering variations in life expectancy between men and women and identifying countries with higher or lower life expectancies. 
Additionally, the project allows for comparisons of life expectancy across different regions and the exploration of potential factors influencing life expectancy disparities.


## Visualizations and Graphs (In Progress)
![Graph1](https://github.com/marcos-couto/BigQueryToMongoDB_PBI/blob/main/graph1.png)

![Graph2](https://github.com/marcos-couto/BigQueryToMongoDB_PBI/blob/main/graph2.png)

![Graph3](https://github.com/marcos-couto/BigQueryToMongoDB_PBI/blob/main/graph3.png)

## Tech

For this solution development, I used the following open source and free tools and resources:

-  Visual Studio Code 
-  Python 3.10 along with dedicated libraries
-  Amazon Web Services Portal
-  GCP Portal
-  BigQuery for table management and SQL queries
-  Microsoft Power Bi for the creation of interactive dashboards
-  AWS Atlas MongoDB
-  AWS S3
-  AWS Lambda Function
-  PyCharm for script development
-  Git for version control (GitHub)
-  Google Sheets
-  Terraform
-  SQL queries

## Diagrams

Solution Diagram:

![Solution Diagram](https://github.com/marcos-couto/BigQueryToMongoDB_PBI/blob/main/diagram.png)

Pipeline:

![Solution Diagram](https://github.com/marcos-couto/BigQueryToMongoDB_PBI/blob/main/pipeline.png)


## Next Steps

- Dashboard Improvements
- SQL queries 
