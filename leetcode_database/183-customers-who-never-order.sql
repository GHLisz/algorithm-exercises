/*
183. Customers Who Never Order
Easy


SQL Schema
Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
*/


# Write your MySQL query statement below
SELECT c.Name AS Customers
FROM Customers AS c
WHERE c.Id NOT IN (SELECT o.CustomerId FROM Orders as o);

# SELECT c.Name AS Customers
# FROM Customers AS c
#        LEFT JOIN Orders as o ON c.Id = o.CustomerId
# WHERE o.CustomerId is NULL;
