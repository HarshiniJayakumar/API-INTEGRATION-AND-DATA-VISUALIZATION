# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: HARSHINI J

*INTERN ID*: CT04DG2834

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

 *DESCRIPTION*

The title of the project was “API Integration and Data Visualization.” I chose to work with the NewsAPI, which is a platform that provides up-to-date news articles from different countries and on a variety of topics. Using Python program where the user could input a country and a keyword, and then the script would fetch all the related news articles based on that input. After collecting the data, I used several Python libraries to clean, process, and finally visualize the information in a way that’s easy to understand. During this process i learned about many libraries namely pandas, requests, textblob, datetime, in collections especially counter, matplotlib and seaborn.
At the beginning of the project, I didn’t have much experience working with APIs. I learned to use the requests library in Python to make calls to the NewsAPI and get the response in JSON format. iI learned about JSON structure.The JSON structure was a bit confusing to understand at first, 
For organizing the data, I used pandas, a very helpful library when working with tables. I used pandas to convert the JSON data into a DataFrame. With it, I could filter the articles, clean up any missing values, and prepare the data for visualization. I also used collections.Counter to find out which news sources appeared most frequently in the results. That gave me insight into which sources were publishing more about the chosen topic.
A very interesting part is tracking the keyword over the last 10 days. For that, I used the datetime library to generate the dates, and then made a loop that sent API requests for each day. This allowed me to see if a keyword was becoming more or less popular over time. I found this dynamic tracking really interesting because it showed real-world news trends based on the keyword given by the user.
One of the most exciting features I added was sentiment analysis using the TextBlob library. It is the NLP tool to analyze the sentiment of the text. This tool allowed me to analyze the emotion behind each news headline. It told me whether a headline was positive, negative, or neutral. This added another layer of information to the project, since I could now look at not just the number of articles, but also the general tone of the news.
For the visualization part, I used matplotlib and seaborn.Because these are the visualization libraries. I created several types of graphs, including bar charts to show article counts per source and sentiment type, a line chart to show how often the keyword was mentioned over time, and a pie chart to show the sentiment breakdown. These visualizations made the data easier to understand, even for someone not familiar with coding.
This project helped me learn a lot. I didn’t just practice Python; I learned how to work with real data from the internet, clean it, and show it in a way that people can understand easily. There were a few errors in the beginning, but fixing them helped me get better at problem-solving. Overall, In this task i learned about lot of libraries and how to connect with api, and I now feel more confident with APIs, data analysis, and visualizing results.

#OUTPUT
<img width="1844" height="561" alt="Image" src="https://github.com/user-attachments/assets/a98142cd-e41d-4ec2-8159-73fa8a0bf3ff" />
![Image](https://github.com/user-attachments/assets/3bbb5ade-d8f8-47b4-9ddf-ac4823f7ee13)

#Bar plot for news from source

![Image](https://github.com/user-attachments/assets/cd7e424f-cf36-4171-9680-a1f217bdbe6d)

#Bar plot for sentiment analysis of news headlines

![Image](https://github.com/user-attachments/assets/16d5c7b9-6889-4ac9-8224-5f79687eb86c) 

#Line plot for keyword trend over last 10 days

![Image](https://github.com/user-attachments/assets/e0b2d7c3-e34d-478d-8c2f-63e1daa75ec0) 

#Pie chart for overall sentiment analysis

![Image](https://github.com/user-attachments/assets/6ac6fb27-68de-417f-817a-bbe4e079994f)

