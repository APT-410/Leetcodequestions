"""
Leetcode 175 

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
personId is the primary key (column with unique values) for this table.
This table contains information about the ID of some persons and their first and last names.
 

Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key (column with unique values) for this table.
Each row of this table contains information about the city and state of one person with ID = PersonId.
 

Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
Output: 
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
Explanation: 
There is no address in the address table for the personId = 1 so we return null in their city and state.
addressId = 1 contains information about the address of personId = 2.
"""

import pandas as pd

class Solution:
    def combine_two_tables(self, person: pd.DataFrame, address: pd.DataFrame):# -> pd.DataFrame:
        merged = person.merge(
            address[['personId','city','state']],
            on='personId',
            how='left',
            sort=False
        )[['firstName','lastName','city','state']]

        merged = merged.replace('', )
        print(merged)
        #return merged
    

if __name__ == "__main__":
    sol = Solution()

    #make two data tables with the info in doc string
    person_data = {
        'personId': [1, 2],
        'lastName': ['Wang', 'Alice'],
        'firstName': ['Allen', 'Bob']
    }
    address_data = {
        'addressId': [2, 3],
        'personId': [2,3],
        'city': ['New York City', 'Leetcode'],
        'state': ['New York', 'California']
    }

    person_data_df = pd.DataFrame(person_data)
    address_data_df = pd.DataFrame(address_data)
    sol.combine_two_tables(person_data_df,address_data_df)
