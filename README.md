This is a basic build of a chatbot backend and frontent in next.js (no python) using llama-index and astra vector data store.

Currently it allows you to interact with data from devpost containing all the people's profiles who RSVPd to the RAG-A-THON 

Live Demo:
=======
https://matchmaker-xi.vercel.app 
Ask questions like:
- I'm a javascript developer looking to join a person who already has an idea described. Who should I meet? Tell me about their skills and idea.
- I'm looking for python developers interested in health and ML.


To Run:
======
- Navigate to the project directory
- npm install
- copy .env.example to .env and fill out your keys
- To (re)generate the vector storage out of the files in /data: npm run generate
- To add more data, add files to /data
- npm run dev
- visit localhost:3000
