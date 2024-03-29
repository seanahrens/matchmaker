/* eslint-disable turbo/no-undeclared-env-vars */
import * as dotenv from "dotenv";
import {
  AstraDBVectorStore, 
  SimpleDirectoryReader,
  VectorStoreIndex,
  storageContextFromDefaults,
} from "llamaindex";
import { STORAGE_DIR, checkRequiredEnvVars } from "./shared.mjs";

dotenv.config();

async function loadAndIndex() {
  // Create a new client and connect to the server

  // load objects from storage and convert them into LlamaIndex Document objects
  const documents = await new SimpleDirectoryReader().loadData({
    directoryPath: STORAGE_DIR,
  });

  // Initialize AstraDB Vector Store and connect
  const vectorCollectionName = "matchmaker";
  const astraVS = new AstraDBVectorStore();
  await astraVS.create(vectorCollectionName, {
    vector: { dimension: 1536, metric: "cosine" }
  });
  await astraVS.connect(vectorCollectionName);
  const vectorStore = astraVS;

  // now create an index from all the Documents and store them in Atlas
  const storageContext = await storageContextFromDefaults({ vectorStore });
  await VectorStoreIndex.fromDocuments(documents, { storageContext });
  console.log(
    `Successfully created embeddings in the AstraDB collection ${vectorCollectionName}.`,
  );
}

(async () => {
  checkRequiredEnvVars();
  await loadAndIndex();
  console.log("Finished generating storage.");
})();
