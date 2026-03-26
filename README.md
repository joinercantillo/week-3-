Main Menu Loop:
The script uses a while loop to keep the program running until the user selects option 7 (EXIT). It displays a menu and captures user input to trigger specific functions.
Product Management (CRUD):

Add: addProduct prompts for a name, cost, and quantity, storing them as a dictionary within a main list.

Read/Show: showInv iterates through the list to display all current items and their stock.

Update: updateProduct searches for a specific product by name and allows the user to modify its details.

Delete: delproduct removes a specific item from the list if the name matches.

Search & Analytics:

Search: searchProduct filters the list to find products matching a specific string (case-insensitive).

Statistics: calculateStatistics summarizes the data, showing the total number of products, the total inventory cost, and identifying the most expensive item.

Technical Observations (Potential Bugs):

Key Name Inconsistency: In addProduct, you define the name as 'product', but in delproduct, searchProduct, and updateProduct, you try to access it using 'name'. This will cause a KeyError.

Variable Naming: You are using list as a variable name. Since list is a reserved keyword in Python, it is better to use something like inventory or product_list.

Redundancy: You have import statements at the top for functions that you then define manually at the bottom. You should choose one method to avoid confusion.
