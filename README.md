This is a basic build of a chatbot backend and frontent in next.js (no python) using llama-index and astra vector data store.

Currently you can ask it questions about data in the dataset, /data, which has both some data about people, and a story about an elephant.

Live Demo:
=======
https://matchmaker-cgqwg28y8-seanahrens.vercel.app
Ask questions like:
- Who is looking for a sports buddy?
- Who is a founder?
- What is Olivia's phone number?

WHAT THIS REPO CURRENTLY DOES NOT DO:
- Answer questions about who is most like who because it is vectorizing the people json into arbitrary chunks rather than distinct chunks per person.
- Sean A's goal is to fix that Sunday morning.


To Run:
======
- Navigate to the project directory
- npm install
- copy .env.example to .env and fill out your keys
- To (re)generate the vector storage out of the files in /data: npm run generate
- To add more data, add files to /data
- npm run dev
- visit localhost:3000
