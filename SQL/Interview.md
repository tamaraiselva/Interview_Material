# interview Question

## 1. Stripe asked this tricky SQL interview question, about identifying any payments made at the same merchant with the same credit card for the same amount within 10 minutes of each other and reporting the count of such repeated payments

**Input/Output Data:**

**`transactions` Example Input:**

| transaction Id | merchant Id | credit card | amount | transaction timestamp   |
|----------------|-------------|----------------|--------|-------------------------|
| 1              | 101         | 1              | 100    | 09/25/2022 12:00:00     |
| 2              | 101         | 1              | 100    | 09/25/2022 12:08:00     |
| 3              | 101         | 1              | 100    | 09/25/2022 12:28:00     |
| 4              | 102         | 2              | 300    | 09/25/2022 12:00:00     |
| 6              | 102         | 2              | 400    | 09/25/2022 14:00:00     |

**Example Output:**

| transaction_id |
|----------------|
| 1              |

**Solution:**

```sql
WITH payments AS (
  SELECT 
    merchant_id, 
    EXTRACT(EPOCH FROM transaction_timestamp - 
      LAG(transaction_timestamp) OVER(
        PARTITION BY merchant_id, credit_card_id, amount 
        ORDER BY transaction_timestamp)
    )/60 AS minute_difference 
  FROM transactions) 

SELECT COUNT(merchant_id) AS payment_count
FROM payments 
WHERE minute_difference <= 10;
```

## 2. Google’s Marketing Team needed to add a simple statistic to their upcoming Superbowl Ad: the median number of searches made per year. You were given a summary table that tells you the number of searches made last year, write a query to report the median searches made per user

`search_frequency` Table:

| Column Name | Type |
|----------------|----------------|
| searches              | integer              |
| num_users              | integer              |

Input/Output Data:

Example Input:

| searches      | num_users      |
|---------------|----------------|
| 1             | 2              |
| 2             | 2              |
| 3             | 3              |
| 4             | 1              |

Example Output:

| median |
|----------------|
| 2.5              |

**`Solution:`**

```sql
WITH searches_expanded AS (
  SELECT searches
  FROM search_frequency
  GROUP BY 
    searches, 
    GENERATE_SERIES(1, num_users))

SELECT 
  ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (
    ORDER BY searches)::DECIMAL, 1) AS  median
FROM searches_expanded;
```

## 3. Say you have access to all the transactions for a given merchant account. Write a query to print the cumulative balance of the merchant account at the end of each day, with the total balance reset back to zero at the end of the month. Output the transaction date and cumulative balance

`transactions` Table:

|Column Name|    Type|
|----------------|----------------|
|transaction_id  | integer |
|type | string ('deposit', 'withdrawal') |
| amount  | decimal  |
| transaction_date |  timestamp  |

**Input/Output Data:**

`transactions` Example Input:

| Transaction ID | Type       | Amount  | Transaction Date       |
|----------------|------------|---------|------------------------|
| 19153          | Deposit    | 65.90   | 07/10/2022 10:00:00    |
| 53151          | Deposit    | 178.55  | 07/08/2022 10:00:00    |
| 29776          | Withdrawal | 25.90   | 07/08/2022 10:00:00    |
| 16461          | Withdrawal | 45.99   | 07/08/2022 10:00:00    |
| 77134          | Deposit    | 32.60   | 07/10/2022 10:00:00    |

Example Output:

| Transaction Date       | Balance  |
|------------------------|----------|
| 07/08/2022 12:00:00    | 106.66   |
| 07/10/2022 12:00:00    | 205.16   |

**`Solution:`**

```sql
WITH daily_balances AS (
  SELECT
    DATE_TRUNC('day', transaction_date) AS transaction_day,
    DATE_TRUNC('month', transaction_date) AS transaction_month,
    SUM(CASE WHEN type = 'deposit' THEN amount
      WHEN type = 'withdrawal' THEN -amount END) AS balance
  FROM transactions
  GROUP BY 
    DATE_TRUNC('day', transaction_date),
    DATE_TRUNC('month', transaction_date))

SELECT
  transaction_day,
  SUM(balance) OVER (
    PARTITION BY transaction_month
    ORDER BY transaction_day) AS balance
FROM daily_balances
ORDER BY transaction_day;
```

## 4. Fleets of servers power Amazon Web Services (AWS). Senior management has requested data-driven solutions to optimize server usage

Write a query that calculates the total time that the fleet of servers was running. The output should be in units of full days.

**Assumptions:**

- Each server might start and stop several times.

- The total time in which the server fleet is running can be calculated as the sum of each server's uptime.

**`server_utilization` Table:**

| Column Name    | Type       |
|----------------|------------|
| server_id      | Integer    |
| status_time    | Timestamp  |
| session_status | String     |

**Input/Output Data:**

**`server_utilization` Example Input:**

| Server ID | Status Time          | Session Status |
|-----------|----------------------|----------------|
| 1         | 08/02/2022 10:00:00 | Start          |
| 1         | 08/04/2022 10:00:00 | Stop           |
| 2         | 08/17/2022 10:00:00 | Start          |
| 2         | 08/24/2022 10:00:00 | Stop           |

**Example Output:**

| Total Uptime (Days) |
|---------------------|
| 21                  |

**`Solution:`**

```sql
WITH running_time 
AS (
  SELECT
    server_id,
    session_status,
    status_time AS start_time,
    LEAD(status_time) OVER (
      PARTITION BY server_id
      ORDER BY status_time) AS stop_time
  FROM server_utilization
)

SELECT
  DATE_PART('days', JUSTIFY_HOURS(SUM(stop_time - start_time))) AS total_uptime_days
FROM running_time
WHERE session_status = 'start'
  AND stop_time IS NOT NULL;
```

## 5. As a Data Analyst on the People Operations team at Accenture, you are tasked with understanding how many consultants are staffed to each client, and how many consultants are exclusively staffed to a single client

Write a query that displays the outputs of client name and the number of uniquely and exclusively staffed consultants ordered by client name.

**`employees` Table:**

| Column Name   | Type    |
|---------------|---------|
| employee_id   | Integer |
| engagement_id | Integer |

**Input/Output Data:**

**`employees` Example Input:**

| Employee ID | Engagement ID |
|-------------|---------------|
| 1001        | 1             |
| 1001        | 2             |
| 1002        | 1             |
| 1003        | 3             |
| 1004        | 4             |

**`consulting_engagements` Table:**

| Column Name    | Type    |
|----------------|---------|
| engagement_id  | Integer |
| project_name   | String  |
| client_name    | String  |

**`consulting_engagements` Example Input:**

| Engagement ID | Project Name                 | Client Name           |
|---------------|------------------------------|-----------------------|
| 1             | SAP Logistics Modernization  | Department of Defense |
| 2             | Oracle Cloud Migration       | Department of Education |
| 3             | Trust & Safety Operations    | Google                |
| 4             | SAP IoT Cloud Integration    | Google                |

Example Output:

| Client Name            | Total Staffed | Exclusive Staffed |
|------------------------|---------------|-------------------|
| Department of Defense  | 2             | 1                 |
| Department of Education| 1             | 0                 |
| Google                 | 2             | 2                 |

**`Solution:`**

```sql
WITH exclusive_employees AS (
SELECT employee_id
FROM employees
JOIN consulting_engagements AS ce 
  ON employees.engagement_id = ce.engagement_id
GROUP BY employee_id
HAVING count(ce.client_name) = 1
)

SELECT 
  ce.client_name, 
  COUNT(employees.employee_id) AS total_staffed,
  COUNT(ee.employee_id) AS exclusive_staffed
FROM employees
INNER JOIN consulting_engagements AS ce 
  ON employees.engagement_id = ce.engagement_id
LEFT JOIN exclusive_employees AS ee 
  ON employees.employee_id = ee.employee_id
GROUP by ce.client_name
ORDER BY ce.client_name;
```

## 6. Facebook wants to recommend new friends to people who show interest in attending 2 or more of the same private events

Sort your results in order of user_a_id and user_b_id (refer to the Example Output below).

**`friendship_status` Table:**

| Column Name | Type                                   |
|-------------|----------------------------------------|
| user_a_id   | Integer                                |
| user_b_id   | Integer                                |
| status      | Enum ('friends', 'not_friends')        |

Each row of this table indicates the status of the friendship between user_a_id and user_b_id.

**Input/Output Data:**

**`friendship_status` Example Input:**

| User A ID | User B ID | Status      |
|-----------|-----------|-------------|
| 111       | 333       | not_friends |
| 222       | 333       | not_friends |
| 333       | 222       | not_friends |
| 222       | 111       | friends     |
| 111       | 222       | friends     |
| 333       | 111       | not_friends |

**`event_rsvp` Table:**

| Column Name      | Type                                      |
|------------------|-------------------------------------------|
| user_id          | Integer                                   |
| event_id         | Integer                                   |
| event_type       | Enum ('public', 'private')                |
| attendance_status| Enum ('going', 'maybe', 'not_going')      |
| event_date       | Date                                      |

**`event_rsvp` Example Input:**

| User ID | Event ID | Event Type | Attendance Status | Event Date |
|---------|----------|------------|-------------------|------------|
| 111     | 567      | Public     | Going             | 07/12/2022 |
| 222     | 789      | Private    | Going             | 07/15/2022 |
| 333     | 789      | Private    | Maybe             | 07/15/2022 |
| 111     | 234      | Private    | Not Going         | 07/18/2022 |
| 222     | 234      | Private    | Going             | 07/18/2022 |
| 333     | 234      | Private    | Going             | 07/18/2022 |

**Example Output:**

| User A ID | User B ID |
|-----------|-----------|
| 222       | 333       |
| 333       | 222       |

Users 222 and 333 who are not friends have shown interest in attending 2 or more of the same private events.

**`Solution:`**

```sql
WITH private_events AS (
SELECT user_id, event_id
FROM event_rsvp
WHERE attendance_status IN ('going', 'maybe')
  AND event_type = 'private'
)

SELECT 
  friends.user_a_id, 
  friends.user_b_id
FROM private_events AS events_1
INNER JOIN private_events AS events_2
  ON events_1.user_id != events_2.user_id
  AND events_1.event_id = events_2.event_id
INNER JOIN friendship_status AS friends
  ON events_1.user_id = friends.user_a_id
  AND events_2.user_id = friends.user_b_id
WHERE friends.status = 'not_friends'
GROUP BY friends.user_a_id, friends.user_b_id
HAVING COUNT(*) >= 2;
```

## 7. The MERGE statement performs INSERT, UPDATE, or DELETE operations on a target table based on the results of a join with a source table

**Example:**

```sql
MERGE INTO target_table AS target
USING source_table AS source
ON target.id = source.id
WHEN MATCHED THEN
    UPDATE SET target.column1 = source.column1
WHEN NOT MATCHED THEN
    INSERT (id, column1) VALUES (source.id, source.column1);
```

## 8. You’re a consultant for a major pizza chain that will be running a promotion where all 3-topping pizzas will be sold for a fixed price, and are trying to understand the costs involved

Given a list of pizza toppings, consider all the possible 3-topping pizzas, and print out the total cost of those 3 toppings. Sort the results with the highest total cost on the top followed by pizza toppings in ascending order.

Break ties by listing the ingredients in alphabetical order, starting from the first ingredient, followed by the second and third.

**`pizza_toppings` Table:**

| Column Name    | Type            |
|----------------|-----------------|
| topping_name   | Varchar(255)    |
| ingredient_cost| Decimal(10,2)   |

**Input/Output Data:**

**`pizza_toppings` Example Input:**

| Topping Name  | Ingredient Cost |
|----------------|-----------------|
| Pepperoni      | 0.50            |
| Sausage        | 0.70            |
| Chicken        | 0.55            |
| Extra Cheese   | 0.40            |

**Example Output:**

| Pizza                               | Total Cost |
|-------------------------------------|------------|
| Chicken, Pepperoni, Sausage         | 1.75       |
| Chicken, Extra Cheese, Sausage      | 1.65       |
| Extra Cheese, Pepperoni, Sausage    | 1.60       |
| Chicken, Extra Cheese, Pepperoni    | 1.45       |

**`Solution:`**

```sql
SELECT 
  CONCAT(p1.topping_name, ',', p2.topping_name, ',', p3.topping_name) AS pizza,
  p1.ingredient_cost + p2.ingredient_cost + p3.ingredient_cost AS total_cost
FROM pizza_toppings AS p1
INNER JOIN pizza_toppings AS p2
  ON p1.topping_name < p2.topping_name 
INNER JOIN pizza_toppings AS p3
  ON p2.topping_name < p3.topping_name 
ORDER BY total_cost DESC, pizza;
```

## 9. The Apple retention team needs your help to investigate buying patterns. Write a query to determine the percentage of buyers who bought AirPods directly after they bought iPhones. Round your answer to a percentage (i.e. 20 for 20%, 50 for 50) with no decimals

**`transactions` Table:**

| Column Name          | Type           |
|----------------------|----------------|
| transaction_id       | Integer        |
| customer_id          | Integer        |
| product_name         | Varchar        |
| transaction_timestamp| Datetime       |

**Input/Output Data:**

**`transactions` Example Input:**

| Transaction ID | Customer ID | Product Name | Transaction Timestamp     |
|----------------|-------------|--------------|---------------------------|
| 1              | 101         | iPhone       | 08/08/2022 00:00:00       |
| 2              | 101         | AirPods      | 08/08/2022 00:00:00       |
| 5              | 301         | iPhone       | 09/05/2022 00:00:00       |
| 6              | 301         | iPad         | 09/06/2022 00:00:00       |
| 7              | 301         | AirPods      | 09/07/2022 00:00:00       |

**Example Output:**

| Follow Up Percentage |
|----------------------|
| 50                   |

**`Solution:`**

```sql
WITH lag_products AS (
  SELECT
  customer_id,
  product_name,
  LAG(product_name)
    OVER(PARTITION BY customer_id
    ORDER BY transaction_timestamp) AS prev_prod
  FROM transactions
  GROUP BY
  customer_id,
  product_name,
  transaction_timestamp
),
interested_users AS (
  SELECT customer_id AS airpod_iphone_buyers
  FROM lag_products
  WHERE LOWER(product_name) = 'airpods'
    AND LOWER(prev_prod) = 'iphone'
  GROUP BY customer_id
)

SELECT
ROUND(
  COUNT(DISTINCT iu.airpod_iphone_buyers)::DECIMAL
  / COUNT(DISTINCT transactions.customer_id)::DECIMAL
  * 100, 0)
FROM transactions
LEFT JOIN interested_users AS iu
  ON iu.airpod_iphone_buyers = transactions.customer_id;
```

## 10. The LAG and LEAD functions allow accessing data from previous or subsequent rows in a result set

**`Example:`**

```sql
SELECT employee_id, salary,
       LAG(salary) OVER (ORDER BY hire_date) AS prev_salary,
       LEAD(salary) OVER (ORDER BY hire_date) AS next_salary
FROM employees;
```

## 11. As a Data Analyst on Snowflake's Marketing Analytics team, your objective is to analyze customer relationship management (CRM) data and identify contacts that satisfy two conditions

1. Contacts who had a marketing touch for three or more consecutive weeks.

2. Contacts who had at least one marketing touch of the type `trial_request`.

Marketing touches, also known as touch points, represent the interactions or points of contact between a brand and its customers.

Your goal is to generate a list of email addresses for these contacts.

**`marketing_touches` Table:**

| Column Name | Type                                          |
|-------------|-----------------------------------------------|
| event_id    | Integer                                       |
| contact_id  | Integer                                       |
| event_type  | String ('webinar', 'conference_registration', 'trial_request') |
| event_date  | Date                                          |

**Input/Output Data:**

**`marketing_touches` Example Input:**

| Event ID | Contact ID | Event Type            | Event Date  |
|----------|------------|-----------------------|-------------|
| 1        | 1          | Webinar               | 4/17/2022   |
| 2        | 1          | Trial Request         | 4/23/2022   |
| 3        | 1          | Whitepaper Download   | 4/30/2022   |
| 4        | 2          | Hands-on Lab          | 4/19/2022   |
| 5        | 2          | Trial Request         | 4/23/2022   |
| 6        | 2          | Conference Registration | 4/24/2022 |
| 7        | 3          | Whitepaper Download   | 4/30/2022   |
| 8        | 4          | Trial Request         | 4/30/2022   |
| 9        | 4          | Webinar               | 5/14/2022   |

**`crm_contacts` Table:**

| Column Name | Type   |
|-------------|--------|
| contact_id  | Integer|
| email       | String |

**`crm_contacts` Example Input:**

| Contact ID | Email                           |
|------------|---------------------------------|
| 1          | andy.markus@att.net             |
| 2          | rajan.bhatt@capitalone.com      |
| 3          | lissa_rogers@jetblue.com       |
| 4          | kevinliu@square.com            |

**`Example Output:`**

| Email                           |
|---------------------------------|
| andy.markus@att.net             |

**`Solution:`**

```sql
WITH consecutive_events_cte AS (
  SELECT
    event_id,
    contact_id, 
    event_type, 
    DATE_TRUNC('week', event_date) AS current_week,
    LAG(DATE_TRUNC('week', event_date)) OVER (
      PARTITION BY contact_id 
      ORDER BY DATE_TRUNC('week', event_date)) AS lag_week,
    LEAD(DATE_TRUNC('week', event_date)) OVER (
      PARTITION BY contact_id 
      ORDER BY DATE_TRUNC('week', event_date)) AS lead_week
FROM marketing_touches)

SELECT DISTINCT contacts.email
FROM consecutive_events_cte AS events
INNER JOIN crm_contacts AS contacts
  ON events.contact_id = contacts.contact_id
WHERE events.lag_week = events.current_week - INTERVAL '1 week'
  OR events.lead_week = events.current_week + INTERVAL '1 week'
  AND events.contact_id IN (
    SELECT contact_id 
    FROM marketing_touches 
    WHERE event_type = 'trial_request'
  );
```

## 12. The Growth Team at DoorDash wants to ensure that new users, who make orders within their first 14 days on the platform, have a positive experience. However, they have noticed several issues with deliveries that result in a bad experience

**`These issues include:`**

- Orders being completed incorrectly, with missing items or wrong orders.

- Orders not being received due to incorrect addresses or drop-off spots.

- Orders being delivered late, with the actual delivery time being 30 minutes later than the order placement time. Note that the `estimated_delivery_timestamp` is automatically set to 30 minutes after the `order_timestamp`.

Write a query that calculates the bad experience rate for new users who signed up in June 2022 during their first 14 days on the platform. The output should include the percentage of bad experiences, rounded to 2 decimal places.

**`orders` Table:**

| Column Name      | Type                                        |
|------------------|---------------------------------------------|
| order_id         | Integer                                     |
| customer_id      | Integer                                     |
| trip_id          | Integer                                     |
| status           | String ('completed successfully', 'completed incorrectly', 'never received') |
| order_timestamp  | Timestamp                                   |

**Input/Output Data:**

**`orders` Example Input:**

| Order ID | Customer ID | Trip ID | Status               | Order Timestamp       |
|----------|-------------|---------|----------------------|-----------------------|
| 727424   | 8472        | 100463  | Completed Successfully | 06/05/2022 09:12:00  |
| 242513   | 2341        | 100482  | Completed Incorrectly  | 06/05/2022 14:40:00  |
| 141367   | 1314        | 100362  | Completed Incorrectly  | 06/07/2022 15:03:00  |
| 582193   | 5421        | 100657  | Never Received        | 07/07/2022 15:22:00  |
| 253613   | 1314        | 100213  | Completed Successfully | 06/12/2022 13:43:00  |

**`trips` Table:**

| Column Name                | Type      |
|----------------------------|-----------|
| dasher_id                  | Integer   |
| trip_id                    | Integer   |
| estimated_delivery_timestamp | Timestamp |
| actual_delivery_timestamp  | Timestamp |

**`trips` Example Input:**

| Dasher ID | Trip ID | Estimated Delivery Timestamp | Actual Delivery Timestamp |
|-----------|---------|------------------------------|---------------------------|
| 101       | 100463  | 06/05/2022 09:42:00          | 06/05/2022 09:38:00       |
| 102       | 100482  | 06/05/2022 15:10:00          | 06/05/2022 15:46:00       |
| 101       | 100362  | 06/07/2022 15:33:00          | 06/07/2022 16:45:00       |
| 102       | 100657  | 07/07/2022 15:52:00          | -                         |
| 103       | 100213  | 06/12/2022 14:13:00          | 06/12/2022 14:10:00       |

**`customers` Table:**

| Column Name     | Type      |
|-----------------|-----------|
| customer_id     | Integer   |
| signup_timestamp| Timestamp |

**`customers` Example Input:**

| Customer ID | Signup Timestamp       |
|-------------|------------------------|
| 8472        | 05/30/2022 00:00:00    |
| 2341        | 06/01/2022 00:00:00    |
| 1314        | 06/03/2022 00:00:00    |
| 1435        | 06/05/2022 00:00:00    |
| 5421        | 06/07/2022 00:00:00    |

**Example Output:**

| Bad Experience Percentage |
|---------------------------|
| 75.00                     |

**Solution:**

```sql
WITH june22_cte AS (
SELECT 
  orders.order_id,
  orders.trip_id,
  orders.status
FROM customers
INNER JOIN orders
  ON customers.customer_id = orders.customer_id
WHERE EXTRACT(MONTH FROM customers.signup_timestamp) = 6
  AND EXTRACT(YEAR FROM customers.signup_timestamp) = 2022
  AND orders.order_timestamp BETWEEN customers.signup_timestamp 
    AND customers.signup_timestamp + INTERVAL '14 DAYS'
)

SELECT 
  ROUND(
    100.0 *
      COUNT(june22.order_id)
      / (SELECT COUNT(order_id) FROM june22_cte)
  ,2) AS bad_experience_pct
FROM june22_cte AS june22
INNER JOIN trips
  ON june22.trip_id = trips.trip_id
WHERE june22.status IN ('completed incorrectly', 'never received');
```

## 13. Assume you're given a table with measurement values obtained from a Google sensor over multiple days with measurements taken multiple times within each day

Write a query to calculate the sum of odd-numbered and even-numbered measurements separately for a particular day and display the results in two different columns.

**`measurements` Example Input:**

| Measurement ID | Measurement Value | Measurement Time       |
|----------------|-------------------|------------------------|
| 131233         | 1109.51           | 07/10/2024 09:00:00    |
| 135211         | 1662.74           | 07/10/2024 11:00:00    |
| 523542         | 1246.24           | 07/10/2024 13:15:00    |
| 143562         | 1124.50           | 07/11/2024 15:00:00    |
| 346462         | 1234.14           | 07/11/2024 16:45:00    |

**Example Output:**

| Measurement Day        | Odd Sum | Even Sum |
|------------------------|---------|----------|
| 07/10/2024 00:00:00    | 2355.75 | 1662.74  |
| 07/11/2024 00:00:00    | 1124.50 | 1234.14  |

**Example Explanation:**

Based on the results,

- On 07/10/2024, the sum of the odd-numbered measurements is 2355.75, while the sum of the even-numbered measurements is 1662.74.

- On 07/11/2024, there are only two measurements available. The sum of the odd-numbered measurements is 1124.50, and the sum of the even-numbered measurements is 1234.14.

**`Answer:`**

```sql
WITH ranked_measurements AS (
  SELECT 
    CAST(measurement_time AS DATE) AS measurement_day, 
    measurement_value, 
    ROW_NUMBER() OVER (
      PARTITION BY CAST(measurement_time AS DATE) 
      ORDER BY measurement_time) AS measurement_num 
  FROM measurements
) 

SELECT 
  measurement_day, 
  SUM(measurement_value) FILTER (WHERE measurement_num % 2 != 0) AS odd_sum, 
  SUM(measurement_value) FILTER (WHERE measurement_num % 2 = 0) AS even_sum 
FROM ranked_measurements
GROUP BY measurement_day;
```

## 14. As a Data Analyst on the Google Maps User Generated Content team, you and your Product Manager are investigating user-generated content (UGC) – photos and reviews that independent users upload to Google Maps

Write a query to determine which type of place (place_category) attracts the most UGC tagged as "off-topic". In the case of a tie, show the output in ascending order of place_category.

**`place_info` Example Input:**

| Place ID | Place Name   | Place Category |
|----------|--------------|----------------|
| 1        | Baar Baar    | Restaurant     |
| 2        | Rubirosa     | Restaurant     |
| 3        | Mr. Purple   | Bar            |
| 4        | La Caverna   | Bar            |

**`maps_ugc_review` Example Input:**

| Content ID | Place ID | Content Tag   |
|------------|----------|---------------|
| 101        | 1        | Off-topic     |
| 110        | 2        | Misinformation|
| 153        | 2        | Off-topic     |
| 176        | 3        | Harassment    |
| 190        | 3        | Off-topic     |

**Example Output:**

| Off Topic Places |
|------------------|
| Restaurant      |

The restaurants (Baar Baar and Rubirosa) have a total of has 2 UGC posts tagged as "off-topic". The bars only have 1. Restaurant is shown here because it's the type of place with the most UGC tagged as "off-topic".

**`Answer:`**

```sql
WITH reviews
AS (
 SELECT
  place.place_category,
  COUNT(ugc.content_id) AS content_count
FROM place_info place
JOIN maps_ugc_review ugc
  ON place.place_id = ugc.place_id
WHERE content_tag = 'Off-topic'
GROUP BY place_category
)
SELECT
  place_category,
  content_count,
  RANK() OVER (ORDER BY content_count MYSTERY_KEYWORD) 
  AS top_place
FROM reviews;
```

## 15. For this scenario, assume that Google wants to analyze the top searched categories in their platform to optimize their search results. We have two tables, searches which has information about each search, and categories where every category ID is associated with a category name

The searches table has the following structure:

**`searches` Example Input:**

| Search ID | User ID | Search Date          | Category ID | Query              |
|-----------|---------|----------------------|-------------|--------------------|
| 1001      | 7654    | 06/01/2024 00:00:00 | 3001        | "chicken recipe"   |
| 1002      | 2346    | 06/02/2024 00:00:00 | 3001        | "vegan meal prep"  |
| 1003      | 8765    | 06/03/2024 00:00:00 | 2001        | "google stocks"    |
| 1004      | 9871    | 07/01/2024 00:00:00 | 1001        | "python tutorial"  |
| 1005      | 8760    | 07/02/2024 00:00:00 | 2001        | "tesla stocks"     |

The categories table has the following structure:

**`categories` Example Input:**

| Category ID | Category Name          |
|-------------|------------------------|
| 1001        | "Programming Tutorials"|
| 2001        | "Stock Market"         |
| 3001        | "Recipes"              |
| 4001        | "Sports News"          |

The question is: Can you write a SQL query that gives the total count of searches made in each category by month for the available data in the year 2024?

**Expected output:**

**Example Output:**

| Category Name          | Month | Total Searches |
|------------------------|-------|----------------|
| "Programming Tutorials"| 07    | 1              |
| "Stock Market"         | 06    | 1              |
| "Stock Market"         | 07    | 1              |
| "Recipes"              | 06    | 2              |

Answer:

```sql
SELECT 
  categories.category_name, 
  EXTRACT(MONTH FROM searches.search_date) AS month, 
  COUNT(*) OVER (PARTITION BY categories.category_name, EXTRACT(MONTH FROM searches.search_date)) AS total_searches
FROM
  searches
LEFT JOIN 
  categories ON categories.category_id = searches.category_id
WHERE
  EXTRACT(YEAR FROM searches.search_date) = 2024
ORDER BY
  total_searches DESC
```

## 16. As a data analyst at Google, you are tasked with examining the Google Ads data for better ad placement and customer targeting. You are asked to retrieve all records of ads from the database that fall into the following coditions

1. The 'status' of the ad is 'active'.

2. The 'impressions' is greater than 500,000.

3. The ad 'last_updated' in the year 2024.

Your task is to write a query to filter down the ads records following these conditions.

**`ads` Example Input:**

| Ad ID | Name           | Status    | Impressions | Last Updated         |
|-------|----------------|-----------|-------------|----------------------|
| 1234  | Google Phone   | Active    | 600000      | 06/25/2024 12:00:00 |
| 5678  | Google Laptop  | Inactive  | 800000      | 05/18/2024 12:00:00 |
| 9012  | Google App     | Active    | 300000      | 04/02/2024 12:00:00 |
| 3456  | Google Cloud   | Active    | 700000      | 08/12/2024 12:00:00 |
| 7890  | Google Mail    | Inactive  | 550000      | 09/03/2024 12:00:00 |

**`Answer:`**

```sql
SELECT *
FROM ads
WHERE status = 'active'
AND impressions > 500000
AND YEAR(last_updated) = 2024;
```

## 17. Stored procedures are a lot like functions in programming. They're used to encapsulate and organize business logic into one unit of code, and they can accept multiple input parameters and return multiple output values

For example, if you were a Data Analyst at Google working on a HR analytics project, you might create a stored procedure to calculate the average salary for a given department:

```sql
CREATE FUNCTION get_avg_salary(department_name TEXT)
RETURNS NUMERIC AS
$BODY$
BEGIN
  RETURN (SELECT AVG(salary) FROM google_employees WHERE department = department_name);
END;
$BODY$
LANGUAGE 'plpgsql';
```

To call this stored procedure and find the average salary for the Data Analytics department you'd write the following query:

```sql
SELECT get_avg_salary('Data Analytics');
```

## 18. As a data analyst on Google Shopping, one of your tasks is to monitor the efficiency of various Google Shopping ads. Specifically, you are interested in the click-through rate (CTR) and conversion rate (each click that results in placing an item into the shopping cart)

Given the two data tables ad_clicks and cart_addition, write a SQL query to assess the click-through rate (CTR) and conversion rate for each ad.

**`ad_clicks` Example Input:**

| Ad ID | User ID | Click Date  |
|-------|---------|-------------|
| 1001  | 123     | 06/08/2024  |
| 1002  | 265     | 06/10/2024  |
| 1001  | 362     | 06/18/2024  |
| 1003  | 192     | 07/26/2024  |
| 1002  | 981     | 07/05/2024  |

**`cart_addition` Example Input:**

| Ad ID | User ID | Cart Date   |
|-------|---------|-------------|
| 1001  | 123     | 06/08/2024  |
| 1003  | 192     | 07/26/2024  |
| 1002  | 265     | 06/11/2024  |

**`Answer:`**

```sql
SELECT 
  a.ad_id,
  COUNT(DISTINCT a.user_id) AS total_clicks,
  COUNT(DISTINCT c.user_id) AS total_conversions,
  COUNT(DISTINCT c.user_id)*1.0 / COUNT(DISTINCT a.user_id) * 100.0 AS conversion_rate
FROM 
  ad_clicks a
LEFT JOIN 
  cart_addition c
ON 
  a.ad_id = c.ad_id AND a.user_id = c.user_id
GROUP BY 
  a.ad_id;
```

## 19. As a data analyst on the advertiser solutions team at Google, your task is to analyze the performance of various ad campaigns running on Google AdWords for a F500 client. You were asked to find the average cost per click (CPC) for each campaign and each ad group within those campaigns for the previous month. CPC is calculated as the total cost of all clicks divided by the number of clicks

For this task, you have been given access to the ad_clicks table which stores data about each click on the ads.

**`ad_clicks` Example Input:**

| Click ID | Date       | Campaign ID | Ad Group ID | Clicks | Cost   |
|----------|------------|-------------|-------------|--------|--------|
| 4325     | 06/08/2024 | 1302        | 2001        | 50     | 100.00 |
| 4637     | 06/10/2024 | 1403        | 2002        | 65     | 130.00 |
| 4876     | 06/18/2024 | 1302        | 2001        | 70     | 140.00 |
| 4531     | 07/05/2024 | 1604        | 3001        | 80     | 200.00 |
| 4749     | 07/05/2024 | 1604        | 2002        | 75     | 180.00 |

You'd like to return an output table in the following format:

**Example Output:**

| Campaign ID | Ad Group ID | Avg CPC |
|-------------|-------------|---------|
| 1302        | 2001        | 2.4     |
| 1403        | 2002        | 2.0     |
| 1604        | 3001        | 2.50    |
| 1604        | 2002        | 2.4     |

Answer:

```sql
SELECT 
    campaign_id,
    ad_group_id, 
    SUM(cost) / SUM(clicks) AS avg_CPC
FROM 
    ad_clicks
GROUP BY 
    campaign_id, 
    ad_group_id;
```

## 20. As a data analyst at Google on the Android PlayStore team, you are tasked with providing insights into in-app purchases made via the PlayStore

Write a SQL query to get a list of customers along with their last purchase. The result should contain customer_id, first name, last name, product, and latest purchase date.

**`Customers` Table:**

| Customer ID | First Name | Last Name | App           |
|-------------|------------|-----------|---------------|
| 1           | John       | Doe       | Tinder        |
| 2           | Jane       | Smith     | CandyCrush    |
| 3           | Jack       | Brown     | Fortnite      |
| 4           | Emily      | Johnson   | Uber          |
| 5           | Jake       | Kenny     | Google Music  |

**`Purchases` Table:**

| Purchase ID | Customer ID | Price  | Date       |
|-------------|-------------|--------|------------|
| 101         | 1           | 79.99  | 2024-02-23 |
| 102         | 2           | 49.99  | 2024-03-18 |
| 103         | 3           | 89.99  | 2024-06-08 |
| 104         | 4           | 119.99 | 2024-07-05 |

**`Answer:`**

```sql
SELECT C.customer_id, 
       C.first_name, 
       C.last_name, 
       C.app, 
       MAX(P.date) AS latest_purchase_date
FROM Customers C
JOIN Purchases P
ON C.customer_id = P.customer_id
GROUP BY C.customer_id, C.first_name, C.last_name, C.app;
```

## key Interview

![REFERNCE](https://drive.google.com/file/d/1_kfG7tT4Lm9BDZQtuRiUUDbc0SZkY2dE/preview)