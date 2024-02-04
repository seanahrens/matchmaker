export const STORAGE_DIR = "./data";
export const CHUNK_SIZE = 250;
export const CHUNK_OVERLAP = 125;

const REQUIRED_ENV_VARS = [
  // "MONGO_URI",
  // "MONGODB_DATABASE",
  // "MONGODB_VECTORS",
  // "MONGODB_VECTOR_INDEX",
  "ASTRA_DB_ENDPOINT",
  "ASTRA_DB_APPLICATION_TOKEN",
];

export function checkRequiredEnvVars() {
  const missingEnvVars = REQUIRED_ENV_VARS.filter((envVar) => {
    return !process.env[envVar];
  });

  if (missingEnvVars.length > 0) {
    console.log(
      `The following environment variables are required but missing: ${missingEnvVars.join(
        ", ",
      )}`,
    );
    throw new Error(
      `Missing environment variables: ${missingEnvVars.join(", ")}`,
    );
  }
}
