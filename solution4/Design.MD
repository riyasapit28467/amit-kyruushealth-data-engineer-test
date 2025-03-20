# Technical Documentation for SSA Engineers

## Overview
The purpose of this document is to guide the SSA engineering team in providing a daily feed of popular baby names to our company. This system will be crucial in ensuring that our company can monitor trends in baby names in near real time.

## Data Format
1. **Data Type**: The data will consist of a list of popular baby names, along with their count of occurrences, and the year in which they were popular.
2. **File Format**: The recommended format for data delivery is JSON or .txt, as these formats are lightweight and widely used for data interchange.

## Delivery Schedule
The SSA should provide this feed daily, preferably at the same time every day so Data should be available and allow for ingestion and processing.

```
+--------------------------+
|                          |
|    SSA Data Feed         |
|   (JSON/CSV Format)      |
|                          |
+------------+-------------+
             |
             v
+--------------------------+
|    Data Ingestion Layer  |
|                          |
| - REST API or Webhook    |
| - Message Queue (Kafka)  |
|                          |
+------------+-------------+
             |
             v
+--------------------------+
|    Data Transformation   |
|                          |
| - ETL Process (Airflow)  |
|    - Extract             |
|    - Transform           |
|    - Load                |
|                          |
+------------+-------------+
             |
             v
+--------------------------+
|    Data Storage Layer    |
|                          |
| - Database               |
| - Data Lake (for         |
|   historical data)       |
|                          |
+------------+-------------+
             |
             v
+--------------------------+
|    Data Analysis         |
|                          |
| - Analytics Engine       |
|   (Spark)                |
| - Aggregation Queries    |
|                          |
+------------+-------------+
             |
             v
+--------------------------+
|    Visualization Layer   |
|                          |
| - Dashboards             |
|                          |
+--------------------------+
```

## Non-functional Requirements

- **Scalability**: Design the system to scale with an increase in data volume and user queries.
- **Fault Tolerance**: Implement mechanisms that ensure the system can handle downtimes in SSA's feeds and automatically retry deliveries.
- **Security**: Protect data in transit via encryption (TLS) and ensure secure storage.
- **Compliance**: Stay compliant with relevant data governance standards and privacy regulations, providing necessary access controls.