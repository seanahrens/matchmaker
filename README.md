This is a basic build of a chatbot backend and frontent in next.js (no python) using llama-index and astra vector data store.

Currently you can ask it questions about data in the dataset, /data, which is a story about an elephant.

To Run:
======
- Navigate to the project directory
- npm install
- copy .env.example to .env.local and fill out your keys
- To (re)generate the vector storage out of the files in /data: npm run generate
- To add more data, add files to /data
- npm run dev
- visit localhost:3000
