# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: PRATIK GORE

*INTERN ID*: CTIS3274

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

This project demonstrates API integration and data visualization using Python, as required for Task 1 of the internship. The main objective of this program is to fetch weather forecast data from a public API and present the information visually using Python visualization libraries. By converting raw weather data into graphical form, the program makes it easier to understand and analyze weather trends.

The program retrieves weather data such as temperature and humidity from a public weather forecast API. The data is obtained in JSON format, which is a commonly used data structure for web based APIs. Python’s requests library is used to send an HTTP GET request to the API endpoint and receive the response. The response is then converted into JSON format so that the data can be accessed and processed using Python dictionaries and lists.

Before processing the data, the program performs a validation check to ensure that the API response contains the expected information. It verifies the presence of the required data fields and safely exits the program if the response is invalid. This step improves the reliability of the program and prevents runtime errors caused by unexpected API responses.

Once the data is validated, the program extracts key weather parameters including date and time, temperature, and humidity. These values are stored in separate lists to organize the data efficiently for visualization. This structured approach allows the program to transform raw API data into a format suitable for analysis and plotting.

For data visualization, the program uses Matplotlib and Seaborn. Matplotlib provides the core plotting functionality, while Seaborn enhances the visual appearance of the graphs, making them easier to interpret. A visualization dashboard is created using subplots, displaying multiple line graphs in a single window. One graph represents the temperature forecast over time, and the other represents the humidity forecast for the same period. Appropriate titles, axis labels, and rotated x axis labels are added to improve clarity and readability.

The temperature graph helps identify changes and trends in temperature, while the humidity graph provides insights into atmospheric moisture levels. Displaying both visualizations together allows for easy comparison of different weather parameters. Overall, this project demonstrates effective use of a public API, proper data handling, and clear data visualization techniques, fulfilling all the requirements of the internship task.
