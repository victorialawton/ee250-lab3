# Lab 3

## Team Members
- Victoria Lawton
- Sriya Kuruppath

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?

RESTful APIs are scalable because they are stateless and cache efficiently (according to the AWS article). Statelessness meand that each time a client requests something to the server, all of the information needed to complete that request is present. Thus, no information has to be stored on the server, so many clients can communicate with the server at one time. Additionally, RESTful APIs use HTTP chacing, which limits server load so many clients can use the server at a time. Both of these contribute to scaleability because they allow more clients to interact with a server.

Question 2: According to the definition of "resources" provided in the AWS article above, What are the resources the mail server is providing to clients?

Resources can be "images, videos, text, numbers, or any type of data" (according to the AWS article). Resources that the mail server could provide to clients are: emails (text), attachments (images and videos), and contact information (text, structured data).

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?

One common RESTful API method that was listed in the AWS article but is used in our mail server is PUT. PUT is used to update existing resources on the server (or create a new resource if it doesn't exist). To implement this in our mail server, we could use a route to update mail entries that exist.

Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!

API keys are used for many RESTful APIs because they provide project identification and authorization. Once the API key identifies the project that's calling the API, it will check to see if that project is granted access to that API. This could be useful if a developer wanted to block anonymous traffic, limit calls made to the API, identify usage patterns of the API, or fliter logs by API key.

Source: https://cloud.google.com/endpoints/docs/openapi/when-why-api-key#:~:text=API%20keys%20provide%20project%20authorization,-To%20decide%20which&text=By%20identifying%20the%20calling%20project,or%20enabled%20in%20the%20API.


