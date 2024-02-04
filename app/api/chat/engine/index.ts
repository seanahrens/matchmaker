import {
  ContextChatEngine,
  LLM,
  AstraDBVectorStore, 
  //MongoDBAtlasVectorSearch,
  serviceContextFromDefaults,
  VectorStoreIndex,
} from "llamaindex";
//import { MongoClient } from "mongodb";
import { checkRequiredEnvVars, CHUNK_OVERLAP, CHUNK_SIZE } from "./shared.mjs";

async function getDataSource(llm: LLM) {
  checkRequiredEnvVars();
  //const client = new MongoClient(process.env.MONGO_URI!);

  //const client = new MongoClient(process.env.MONGO_URI!);
  const serviceContext = serviceContextFromDefaults({
    llm,
    chunkSize: CHUNK_SIZE,
    chunkOverlap: CHUNK_OVERLAP,
  });


  // const store = new MongoDBAtlasVectorSearch({
  //   mongodbClient: client,
  //   dbName: process.env.MONGODB_DATABASE,
  //   collectionName: process.env.MONGODB_VECTORS,
  //   indexName: process.env.MONGODB_VECTOR_INDEX,
  // });

  // Initialize AstraDB Vector Store and connect
  const vectorCollectionName = "matchmaker";
  const astraVS = new AstraDBVectorStore();
  await astraVS.create(vectorCollectionName, {
    vector: { dimension: 1536, metric: "cosine" }
  });
  await astraVS.connect(vectorCollectionName);
  const vectorStore = astraVS;
  
  return await VectorStoreIndex.fromVectorStore(vectorStore, serviceContext);
  // return await VectorStoreIndex.fromVectorStore(store, serviceContext);
}

export async function createChatEngine(llm: LLM) {
  const index = await getDataSource(llm);
  const retriever = index.asRetriever({ similarityTopK: 100 });
  return new ContextChatEngine({
    chatModel: llm,
    retriever,
  });
}
