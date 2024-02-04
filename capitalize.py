import json

# Sample JSON data
json_data = '''
[
  {
    "name": "Ajhe Babs",
    "title": "Mobile developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python"
    ],
    "interests": [
      "Beginner Friendly"
    ]
  },
  {
    "name": "Laurie Luo",
    "projects": "2 projects",
    "followers": "3 followers",
    "achievements": "5 achievements",
    "team_status": "Has a team"
  },
  {
    "name": "Magesh Kumar Rajamani",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "ai",
      "python",
      "api",
      "leader",
      "ml",
      "algorithms.io"
    ],
    "interests": [
      "Databases",
      "Design",
      "Education",
      "Enterprise",
      "Fintech",
      "Health",
      "Machine Learning/AI",
      "Mobile",
      "Open Ended",
      "Productivity",
      "Social Good",
      "Web"
    ]
  },
  {
    "name": "vijaya4babu Babu",
    "title": "Full-stack developer",
    "projects": "3 projects",
    "followers": "1 follower",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "python",
      "llm"
    ],
    "interests": [
      "Beginner Friendly"
    ]
  },
  {
    "name": "Devender Babu",
    "projects": "3 projects",
    "followers": "4 followers",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "bigworlddata-ndwi",
      "android",
      "hardware",
      "ios",
      "mac",
      "web",
      "windows",
      "windows-phone"
    ]
  },
  {
    "name": "Dauren Aubakirov",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "c",
      "python",
      "c++"
    ],
    "interests": [
      "Communication",
      "Databases",
      "IoT",
      "Productivity",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "Phuc Nguyen",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "2 followers",
    "achievements": "1 achievement",
    "skills": [
      "machine-learning",
      "statistics"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Tushar Bansal",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement"
  },
  {
    "name": "Abhishek M Shivalingaiah",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "2 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "python",
      "generativeai"
    ],
    "interests": [
      "DevOps",
      "Machine Learning/AI",
      "Social Good"
    ]
  },
  {
    "name": "Warren Lu",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement"
  },
  {
    "name": "Jithin James",
    "title": "Data scientist",
    "projects": "1 project",
    "followers": "1 follower",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "pytorch",
      "python",
      "docker"
    ],
    "interests": [
      "DevOps",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Max Zhang",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "java",
      "javascript",
      "c++",
      "swift"
    ]
  },
  {
    "name": "Josh Clawson",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "product"
    ],
    "interests": [
      "Education",
      "Enterprise",
      "Machine Learning/AI",
      "Social Good",
      "Voice skills"
    ],
    "bio": "Hey I'm Josh! I like to build stuff. Currently looking for MLE's with RAG experience to join my team."
  },
  {
    "name": "ROBERTO IBARRA LOPEZ",
    "title": "Lawyer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "skills": [
      "space"
    ],
    "interests": [
      "DevOps"
    ]
  },
  {
    "name": "Private user",
    "projects": "10 projects",
    "followers": "24 followers",
    "achievements": "9 achievements",
    "team_status": "Has a team",
    "skills": [
      "java",
      "c#",
      "web-api",
      "rest-api",
      "soa",
      "node.js",
      "html5",
      "android",
      "web",
      "react",
      "cloud",
      "angular1-8",
      "reactnative",
      "devops",
      "unity",
      "amazon-web-services",
      "azure"
    ],
    "interests": [
      "Communication",
      "Cybersecurity",
      "DevOps",
      "IoT",
      "Lifehacks",
      "Productivity",
      "Social Good",
      "Voice skills"
    ]
  },
  {
    "name": "Yufei Ma",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Sharat Paramanand Bhat",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "natural-language-processing"
    ],
    "interests": [
      "Beginner Friendly",
      "Machine Learning/AI",
      "Open Ended"
    ]
  },
  {
    "name": "Fab Fusaro",
    "title": "Security Analyst",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "networks",
      "api",
      "wireless-applications-services"
    ],
    "interests": [
      "Cybersecurity",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Kothandaraman Sikamani",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "bigdata",
      "nosql",
      "llm",
      "genai",
      "cloud",
      "microservices",
      "datala",
      "datalake",
      "data",
      "pipelines",
      "rag",
      "llamaindex",
      "langchain",
      "java",
      "python",
      "r",
      "scala",
      "sql",
      "gcp",
      "amazon-web-services",
      "azure",
      "openshift",
      "kubernetes"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Blockchain",
      "Cybersecurity",
      "Databases",
      "Design",
      "DevOps",
      "E-commerce/Retail",
      "Education",
      "Enterprise",
      "Fintech",
      "Health",
      "IoT",
      "Lifehacks",
      "Machine Learning/AI",
      "Mobile",
      "Robotic Process Automation",
      "Web"
    ],
    "bio": "Working on Data science MLOPs. Looking for teammates who can work on llm"
  },
  {
    "name": "Naresh Gupta",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "java/python"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Sean Sheng",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "coding"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Lingping-Gu Gu",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "java",
      "javascript",
      "react.js",
      "node.js",
      "mongodb",
      "mysql"
    ],
    "interests": [
      "Web"
    ]
  },
  {
    "name": "Alberto Lopez",
    "title": "I want to build a music generation app that gives producers the ability to create music from voice, instruments, studio. The whole music production process at your fingertips.",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates"
  },
  {
    "name": "Justin Woo",
    "title": "Full-stack developer",
    "projects": "4 projects",
    "followers": "8 followers",
    "achievements": "8 achievements",
    "team_status": "Working solo",
    "skills": [
      "javascript"
    ],
    "interests": [
      "AR/VR",
      "Gaming"
    ]
  },
  {
    "name": "Sree Vaddi",
    "title": "Strategic Solutions Architect",
    "projects": "2 projects",
    "followers": "1 follower",
    "achievements": "9 achievements",
    "team_status": "Working solo",
    "skills": [
      "java",
      "ai",
      "python",
      "r"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Communication",
      "Cybersecurity",
      "DevOps",
      "Fintech",
      "Gaming",
      "IoT",
      "Lifehacks",
      "Machine Learning/AI",
      "Productivity",
      "Social Good",
      "Voice skills",
      "Beginner Friendly",
      "Databases",
      "Design",
      "E-commerce/Retail",
      "Education",
      "Enterprise",
      "Health",
      "Low/No Code",
      "Mobile",
      "Music/Art",
      "Open Ended",
      "Quantum",
      "Robotic Process Automation",
      "Web"
    ]
  },
  {
    "name": "Kevin Tran",
    "title": "Machine Learning and AI",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Working solo",
    "skills": [
      "kotlin",
      "swift",
      "java",
      "c++"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "DevOps",
      "E-commerce/Retail",
      "Education",
      "Enterprise",
      "Health",
      "IoT",
      "Lifehacks",
      "Machine Learning/AI",
      "Mobile",
      "Productivity",
      "Quantum",
      "Social Good"
    ]
  },
  {
    "name": "Akshobya S H",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "c",
      "r",
      "sql",
      "c++",
      "html/css",
      "statistics",
      "tableau",
      "data-visualization",
      "excel",
      "linear-algebra",
      "frequentist-&-bayesian-statistics",
      "advanced-ml",
      "data-wrangling",
      "relational-databases-&-nosql",
      "analytics",
      "computing",
      "amazon-web-services",
      "google-cloud",
      "git",
      "mysql",
      "sqlite",
      "particle"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Databases",
      "DevOps",
      "Gaming",
      "IoT",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Tarun Sharma",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "marketing",
      "customer"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Cybersecurity",
      "Design",
      "DevOps",
      "Gaming",
      "Machine Learning/AI",
      "Social Good"
    ]
  },
  {
    "name": "Kody C. Kendall",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "ruby-on-rails",
      "react",
      "react-native"
    ],
    "interests": [
      "Machine Learning/AI",
      "Open Ended",
      "Web"
    ],
    "bio": "My name is Kody, founder and CEO of Field Rocket, a very simple CRM for small home service contractors. I am wanting to build a RAG LLM Chatbot tool to help automate my onboarding process for new users of Field Rocket, to help decrease support costs and increase customer success"
  },
  {
    "name": "Gavin Morgan",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "typescript",
      "linux",
      "html",
      "css",
      "react",
      "postgresql",
      "llama.cpp",
      "ruby-on-rails",
      "ruby"
    ],
    "interests": [
      "Design",
      "DevOps",
      "Machine Learning/AI",
      "Mobile",
      "Web"
    ],
    "bio": "10 year fullstack dev formerly at Pivotal Labs (RIP--acquired by VMware). I've recently started experimenting with llama.cpp at home. Looking to build AI-enabled apps & plugins/extensions."
  },
  {
    "name": "Jaime Mu\u00f1oz",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "c#",
      "react",
      "mysql"
    ],
    "interests": [
      "Web"
    ]
  },
  {
    "name": "Emily Jiang",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "api",
      "database"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Luis Enrique Aguilar R.",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "c#",
      ".net",
      "react-native",
      "azure"
    ],
    "interests": [
      "Cybersecurity",
      "DevOps",
      "Lifehacks"
    ]
  },
  {
    "name": "Ratbek Erkinbekov",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "lenguages",
      "robotics"
    ],
    "interests": [
      "Fintech",
      "Robotic Process Automation"
    ],
    "bio": "Passionate about making the world a better place to live! Jcjcjcjcjcjj"
  },
  {
    "name": "lisa liu",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "apis",
      "coding",
      "machine-learning",
      "python",
      "java"
    ],
    "interests": [
      "Beginner Friendly",
      "Databases",
      "E-commerce/Retail",
      "Enterprise",
      "Health",
      "IoT",
      "Machine Learning/AI",
      "Music/Art",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "Jianxiang Gao",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "rag"
    ],
    "interests": [
      "Beginner Friendly",
      "Databases",
      "Education",
      "Web"
    ]
  },
  {
    "name": "Yash Parag Butala",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "c++",
      "torch",
      "os",
      "networks",
      "linux",
      "javascript",
      "java",
      "shell"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Blockchain",
      "Communication",
      "Cybersecurity",
      "Databases",
      "Design",
      "DevOps",
      "E-commerce/Retail",
      "Education",
      "Enterprise",
      "Fintech",
      "Gaming",
      "Health",
      "IoT",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Mobile",
      "Music/Art",
      "Open Ended",
      "Productivity",
      "Quantum",
      "Robotic Process Automation",
      "Social Good",
      "Voice skills",
      "Web"
    ],
    "bio": "Grad student at CMU, undergrad at IIT Kharagpur. NLP researcher and systems guy."
  },
  {
    "name": "Rachita Chandra",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "python"
    ],
    "interests": [
      "Beginner Friendly",
      "Health",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Fateh Singh",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "java",
      "python"
    ],
    "interests": [
      "Beginner Friendly",
      "Databases",
      "Machine Learning/AI",
      "Open Ended"
    ]
  },
  {
    "name": "Homero Roman Roman",
    "projects": "2 projects",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "android",
      "javascript",
      "java",
      "html5",
      "jquery",
      "python",
      "particle",
      "tensorflow",
      "ios",
      "reactnative"
    ]
  },
  {
    "name": "Frederick Roman",
    "title": "AI",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "react",
      "vuejs",
      "python",
      "tensorflow",
      "pytorch",
      "node.js",
      "django",
      "flask",
      "typescript",
      "matlab",
      "heroku",
      "docker",
      "mui",
      "nextjs",
      "scikit-learn",
      "r",
      "express.js",
      "pwa",
      "three.js",
      "unity",
      "c#",
      "mysql",
      "mongodb",
      "mongoose",
      "natural-language-processing",
      "llama"
    ],
    "interests": [
      "AR/VR",
      "E-commerce/Retail",
      "Fintech",
      "Machine Learning/AI",
      "Music/Art",
      "Open Ended",
      "Social Good",
      "Web"
    ]
  },
  {
    "name": "Mark Kuczmarski",
    "title": "Full-stack developer",
    "projects": "2 projects",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "android",
      "ruby-on-rails",
      "javascript",
      "typescript"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Cybersecurity",
      "Fintech",
      "Gaming",
      "Machine Learning/AI",
      "Mobile",
      "Web"
    ]
  },
  {
    "name": "Hang D.",
    "title": "Back-end developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "java",
      "javascript",
      "python",
      "c",
      "c++",
      "machine-learning"
    ],
    "interests": [
      "AR/VR",
      "Machine Learning/AI",
      "Productivity",
      "Social Good",
      "Databases",
      "Music/Art"
    ]
  },
  {
    "name": "Private user",
    "title": "Business",
    "projects": "4 projects",
    "followers": "36 followers",
    "achievements": "9 achievements",
    "team_status": "Working solo",
    "skills": [
      "java",
      "kotlin",
      "python",
      "swift"
    ],
    "interests": [
      "Social Good"
    ]
  },
  {
    "name": "Harini Datla",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "machine-learning"
    ],
    "interests": [
      "Beginner Friendly",
      "Low/No Code",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Subrahmanyam Arunachalam",
    "title": "Data scientist",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "pytorch"
    ],
    "interests": [
      "Machine Learning/AI",
      "Social Good"
    ]
  },
  {
    "name": "Xin Yi",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "java",
      "pythion",
      "datbase"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Communication",
      "Cybersecurity",
      "Databases",
      "Design",
      "DevOps",
      "E-commerce/Retail",
      "Education",
      "Enterprise",
      "Fintech",
      "Gaming",
      "Health",
      "IoT",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Mobile",
      "Music/Art",
      "Open Ended",
      "Productivity",
      "Quantum",
      "Robotic Process Automation",
      "Social Good",
      "Voice skills"
    ]
  },
  {
    "name": "Sean Lee",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "react",
      "typescript",
      "python",
      "swift",
      "go",
      "rust",
      "haskell"
    ],
    "interests": [
      "Cybersecurity",
      "Databases",
      "Design",
      "DevOps",
      "Education",
      "Health",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Mobile",
      "Music/Art",
      "Open Ended",
      "Productivity",
      "Web"
    ],
    "bio": "ex-google software engineer, interested in personal complexity management RAG over twitter bookmarks, chrome tabs"
  },
  {
    "name": "Michael Ye",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "5 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "c++"
    ],
    "interests": [
      "Fintech"
    ]
  },
  {
    "name": "Satish Solanki",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "postgresql"
    ],
    "interests": [
      "AR/VR",
      "Databases",
      "DevOps",
      "Machine Learning/AI"
    ],
    "bio": "Hi, I have worked as a Data Scientist in a data privacy and database security company since 2021. I am looking for a team to join and work with them to solve the problem and gain hands-on experience."
  },
  {
    "name": "Ramandeep Ahuja",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team"
  },
  {
    "name": "Leo Toff",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "javascript",
      "typescript",
      "gpt",
      "ui",
      "mobile"
    ],
    "interests": [
      "AR/VR",
      "Databases",
      "DevOps",
      "Enterprise",
      "Fintech",
      "Health",
      "IoT",
      "Machine Learning/AI",
      "Mobile",
      "Productivity",
      "Robotic Process Automation",
      "Voice skills"
    ]
  },
  {
    "name": "Swapnil Das",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "java",
      "pyth",
      "javascript",
      "html"
    ],
    "interests": [
      "Beginner Friendly",
      "Cybersecurity",
      "Gaming",
      "Lifehacks",
      "Machine Learning/AI",
      "Mobile"
    ]
  },
  {
    "name": "Hanye Wei",
    "title": "python, sql",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates"
  },
  {
    "name": "Aman Singh",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "openai",
      "api",
      "elevenlabs"
    ],
    "interests": [
      "Beginner Friendly",
      "Machine Learning/AI",
      "Robotic Process Automation",
      "Education",
      "Enterprise",
      "Fintech",
      "Music/Art"
    ],
    "bio": "I'm a product manager/program manager with a CS degree learning to work with AI."
  },
  {
    "name": "Markus Zhang",
    "title": "Full-stack developer",
    "projects": "2 projects",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "react",
      "pytorch",
      "typescript",
      "express.js",
      "amazon-web-services",
      "nosql",
      "figma"
    ],
    "interests": [
      "Databases",
      "Machine Learning/AI",
      "Web",
      "Low/No Code",
      "Music/Art",
      "Open Ended"
    ]
  },
  {
    "name": "Fiona Lu",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "c++",
      "java"
    ],
    "interests": [
      "Beginner Friendly",
      "Enterprise",
      "Fintech",
      "Health",
      "Machine Learning/AI",
      "Open Ended"
    ]
  },
  {
    "name": "Nathan Waters",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "llm"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Dave Martin",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo"
  },
  {
    "name": "Daniel Pang",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "alan saji",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "natural-language-processing",
      "llm",
      "sql",
      "machine-learning"
    ],
    "interests": [
      "Databases",
      "Machine Learning/AI"
    ],
    "bio": "Hi, an amateur NLP enthusiast here. Looking forward to fruitful collaborations here."
  },
  {
    "name": "Alex Slater",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "design",
      "developer",
      "founder"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Blockchain",
      "Communication",
      "Cybersecurity",
      "Databases",
      "Design",
      "DevOps",
      "E-commerce/Retail",
      "Education",
      "Enterprise",
      "Fintech",
      "Machine Learning/AI",
      "Mobile",
      "Productivity",
      "Quantum",
      "Robotic Process Automation",
      "Social Good",
      "Voice skills",
      "Web"
    ]
  },
  {
    "name": "Abem Lucas",
    "title": "Back-end developer",
    "projects": "3 projects",
    "followers": "4 followers",
    "achievements": "8 achievements",
    "team_status": "Has a team",
    "skills": [
      "java",
      "python",
      "c",
      "c++",
      "apis",
      "javascript",
      "sql"
    ],
    "interests": [
      "Beginner Friendly",
      "Machine Learning/AI",
      "Web",
      "Databases",
      "Mobile",
      "Open Ended",
      "Quantum"
    ]
  },
  {
    "name": "Lucas Amlicke",
    "title": "Full-stack developer",
    "projects": "4 projects",
    "followers": "4 followers",
    "achievements": "8 achievements",
    "team_status": "Has a team",
    "skills": [
      "programming",
      "web",
      "mobile",
      "web3",
      "sec",
      "c++",
      "python",
      "java",
      "javascript",
      "html",
      "css",
      "sql",
      "php",
      "linux",
      "flutter",
      "github",
      "node.js",
      "express.js",
      "flask",
      "react",
      "mongodb",
      "django",
      "verilog",
      "ux",
      "ios",
      "android",
      "blockchain",
      "crypto",
      "arm"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Blockchain",
      "Communication",
      "Cybersecurity",
      "Design",
      "DevOps",
      "E-commerce/Retail",
      "Fintech",
      "Gaming",
      "Lifehacks",
      "Machine Learning/AI",
      "Mobile",
      "Open Ended",
      "Productivity",
      "Social Good",
      "Web",
      "Databases"
    ]
  },
  {
    "name": "Brian Reardon",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "lamp",
      "ruby-on-rails",
      "sql",
      "php",
      "javascript",
      "ios",
      "sqlalchemy",
      "flask",
      "django",
      "react",
      "llm",
      "ai",
      "natural-language-processing"
    ],
    "interests": [
      "AR/VR",
      "Communication",
      "Cybersecurity",
      "DevOps",
      "Education",
      "Enterprise",
      "Fintech",
      "Gaming",
      "Machine Learning/AI",
      "Music/Art",
      "Open Ended",
      "Productivity",
      "Quantum",
      "Robotic Process Automation",
      "Social Good",
      "Web"
    ],
    "bio": "Hey I'm Brian, former CTO and founder, former Cisco Senior Engineer, engineering grad. I'm open to pair up with people or work solo."
  },
  {
    "name": "Meri Nova",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "sql"
    ],
    "interests": [
      "Beginner Friendly",
      "Databases",
      "DevOps",
      "IoT",
      "Machine Learning/AI",
      "Web"
    ]
  },
  {
    "name": "Maheedhar Gunturu",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "artificial",
      "intelligence",
      "data",
      "ml"
    ],
    "interests": [
      "Databases",
      "IoT",
      "Machine Learning/AI",
      "Open Ended",
      "Productivity",
      "Quantum",
      "Web"
    ]
  },
  {
    "name": "Uri Zernik",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "c",
      "sql",
      "natural-language-processing",
      "machine-learning"
    ],
    "interests": [
      "Databases",
      "Design",
      "Enterprise",
      "Machine Learning/AI"
    ],
    "bio": "I am familiar (disappointed) with LangChain. PaloAltoNLP is building an App for accurate extraction of business details from English legal contracts. Looking for fun teammates who possibly have some experience with Llama"
  },
  {
    "name": "Yecheng Ma",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "amazon-web-services",
      "model",
      "sql",
      "javascript",
      "natural-language-processing",
      "ai",
      "pytorch"
    ],
    "interests": [
      "Health",
      "Beginner Friendly"
    ],
    "bio": "Hey everyone, Mark here! I'm deeply passionate about LLM innovation in healthcare, with a background in data science and ML in the industry. I'm new to RAG and eager to learn and prototype something impactful, especially around US medical billing and post-care behavioral science. If you're up for a small, impactful project this weekend, let's talk!"
  },
  {
    "name": "Gilbert Young Jr",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "ai",
      "llms",
      "api",
      "python",
      "tensorflow"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Nikhil Kumar",
    "title": "Data scientist",
    "projects": "1 project",
    "followers": "1 follower",
    "achievements": "5 achievements",
    "team_status": "Has a team",
    "skills": [
      "python",
      "data",
      "java",
      "machine-learning",
      "data-science-toolkit"
    ],
    "interests": [
      "Blockchain",
      "Design",
      "Fintech",
      "Gaming",
      "Health",
      "IoT",
      "Lifehacks",
      "Machine Learning/AI",
      "Productivity",
      "Social Good"
    ]
  },
  {
    "name": "Prionti Nasir",
    "title": "Full-stack developer",
    "projects": "3 projects",
    "followers": "11 followers",
    "achievements": "6 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "java",
      "javascript",
      "ruby",
      "c",
      "react",
      "typescript",
      "firebase",
      "postgresql"
    ],
    "interests": [
      "Social Good",
      "Machine Learning/AI",
      "Music/Art",
      "Databases",
      "E-commerce/Retail",
      "Productivity"
    ],
    "bio": "I'm a software engineer at Microsoft working on the backend side of things at 365 Copilot, interested in developing my end-to-end AI and LLM skills. Proficient in Python, Java, C, React, Javascript, Typescript. I am fairly tool-agnostic at this point, open to working with whatever it would make sense to use for the specificities of the project. Would love to team up but I'm remote so I guess this would only work so long as at least one member is in person. Request a team-up and I'm happy to talk more!"
  },
  {
    "name": "Tanmay Laud",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "java",
      "spring",
      "python",
      "react"
    ],
    "interests": [
      "Fintech",
      "Machine Learning/AI",
      "Social Good",
      "Music/Art",
      "Open Ended",
      "Productivity",
      "Web"
    ]
  },
  {
    "name": "Patrick OBrien",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "rag",
      "natural-language-processing",
      "knowledge-graphs",
      "llm",
      "langchain",
      "pydantic",
      "llamaindex"
    ],
    "interests": [
      "Beginner Friendly",
      "Blockchain",
      "Health",
      "Low/No Code",
      "Machine Learning/AI"
    ],
    "bio": "My expertise lies in enhancing language models using RAG and knowledge graphs, with a focus on healthcare applications. Proficient in Python, prompt engineering, LangChain, Llama Index, Pydantic, knowledge graphs, and structured data. Looking to join a team interested in building a knowledge enhanced llm with multimodal chat (video and text) using rag, agents, and knowledge graphs. To complement my skills, I'm in search of teammates skilled in DevOps, full-stack."
  },
  {
    "name": "Jay Shah",
    "title": "Data scientist",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "amazon-web-services",
      "cloud",
      "statistics",
      "model"
    ],
    "interests": [
      "Fintech",
      "IoT",
      "Machine Learning/AI",
      "Open Ended",
      "Productivity",
      "Robotic Process Automation",
      "Web"
    ]
  },
  {
    "name": "Duyan Ta",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "computer-vision",
      "researcher",
      "computational-geometry",
      "computer-graphics",
      "embedded-sytem-software"
    ],
    "interests": [
      "AR/VR",
      "Education",
      "Gaming",
      "Machine Learning/AI",
      "Open Ended",
      "Robotic Process Automation",
      "Social Good"
    ]
  },
  {
    "name": "Derek Anuen",
    "title": "Designer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "adobe-creative-sdk"
    ],
    "interests": [
      "Beginner Friendly"
    ]
  },
  {
    "name": "Chonghao Huang",
    "title": "Venture Capital Investor (previously software eng)",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "android",
      "recommendation-systems"
    ],
    "interests": [
      "Databases",
      "DevOps",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Sharon Tan",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "react",
      "typescript",
      "postgresql",
      "llms"
    ],
    "interests": [
      "Databases",
      "Education",
      "Health",
      "Machine Learning/AI",
      "Productivity",
      "Social Good",
      "Web"
    ],
    "bio": "Together with another developer, we are keen to build either a security product leveraging company documents and best practices to suggest code improvements, or a mental health resources assistant for an ongoing mental health hotline program."
  },
  {
    "name": "Jesse Schmidt",
    "title": "Designer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "language"
    ],
    "interests": [
      "Quantum"
    ]
  },
  {
    "name": "Manish Ravula",
    "title": "Data scientist",
    "projects": "2 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "machine-learning",
      "python",
      "c",
      "c++",
      "data-science",
      "deep-learning",
      "natural-language-processing",
      "opencv",
      "tensorflow",
      "pytorch",
      "image-processing",
      "databases",
      "sql",
      "keras",
      "ray",
      "dask",
      "gpt",
      "llm",
      "llama",
      "gpu",
      "devops",
      "distributed-computing",
      "particle",
      "scikit-learn",
      "docker",
      "kubernetes",
      "spacy",
      "nltk",
      "speech-ml"
    ],
    "interests": [
      "AR/VR",
      "Databases",
      "DevOps",
      "Enterprise",
      "Fintech",
      "Gaming",
      "IoT",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Music/Art",
      "Robotic Process Automation",
      "Social Good",
      "Voice skills",
      "Open Ended"
    ],
    "bio": "Hello everyone! I'm a ML Engineer @ Apple seasoned in building ML projects end-to-end (data to analysis to training to infra to metrics!). I'm looking to explore multimodal RAG LLM app ideas to scratch my own itch. It's always more fun to work outside of my own mind so hit me up if you want to make some awesome stuff together!"
  },
  {
    "name": "Mohit Nikhade",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "machine-learning",
      "data-science",
      "natural-language-processing",
      "deep-learning",
      "opencv",
      "tensorflow",
      "pytorch",
      "image-processing",
      "html",
      "css",
      "javascript",
      "java",
      "python",
      "flask",
      "mssql",
      "full-stack-development"
    ],
    "interests": [
      "Databases",
      "Education",
      "Fintech",
      "Health",
      "Machine Learning/AI",
      "Web"
    ]
  },
  {
    "name": "Slyracoon23 Potters",
    "projects": "5 projects",
    "followers": "5 followers",
    "achievements": "9 achievements",
    "team_status": "Working solo",
    "skills": [
      "python"
    ],
    "interests": [
      "Cybersecurity"
    ]
  },
  {
    "name": "Neo Wang",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "2 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "go",
      "web"
    ],
    "interests": [
      "AR/VR",
      "Communication",
      "Cybersecurity",
      "Design",
      "E-commerce/Retail",
      "Education",
      "Enterprise",
      "Fintech",
      "Health",
      "IoT",
      "Machine Learning/AI",
      "Music/Art",
      "Robotic Process Automation",
      "Web"
    ],
    "bio": "My ideas(subject to change): Personal assistant, Digital GF(like the movie her)/BF/BFF, Digital journal(records anything you want it to record). Or find your soulmate/match/business partner(similar thinking pattern, similar topics) in the vector cloud without leaking your actual information. Me: Full stack since 5th grade in elementary school. Swiss army knife kind of a person(software, hardware, CNC milling, laser welding, kombucha brewing...). Like Mistral-7b running on my local. Like hefeweizen(can get high without alcohol too)."
  },
  {
    "name": "Stephane Remigereau",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "2 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "pytorch",
      "java",
      "c++",
      "flask",
      "tensorflow",
      "keras"
    ],
    "interests": [
      "Fintech",
      "Machine Learning/AI"
    ],
    "bio": "With a Master's in Management Science and Engineering from Stanford and a tenure as a Machine Learning Engineer at XPeng, I've cultivated a deep expertise in neural network optimization and generative AI, particularly in computer vision. My interest for advancing Large Language Models (LLMs) and AI-driven media creation drives my pursuit of innovative collaborations. I am keen to connect with specialists in LLMs and generative AI, with experience in ML System Design, training and inference."
  },
  {
    "name": "Zake Stahl",
    "title": "Tech Support; Ops",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "troubleshooting"
    ],
    "interests": [
      "Beginner Friendly",
      "Cybersecurity",
      "Design",
      "DevOps",
      "Machine Learning/AI",
      "Open Ended"
    ]
  },
  {
    "name": "Jerry K",
    "title": "Machine Learning Engineer/ML Infra Engineer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "natural-language-processing",
      "machine-learning",
      "llm",
      "openai",
      "ray"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Marina Levay",
    "title": "Data scientist",
    "projects": "2 projects",
    "followers": "1 follower",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "python",
      "ui/ux-design"
    ],
    "interests": [
      "AR/VR",
      "Databases",
      "Design",
      "Education",
      "Gaming",
      "Machine Learning/AI",
      "Mobile",
      "Music/Art",
      "Quantum",
      "Social Good"
    ]
  },
  {
    "name": "Kinjal Nandy",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "product",
      "design"
    ],
    "interests": [
      "Blockchain",
      "Design",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Sean Ahrens",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "javascript",
      "react",
      "node.js",
      "python",
      "ruby-on-rails",
      "mongodb",
      "postgresql",
      "openai",
      "gpt4",
      "llm",
      "prompt-engineering",
      "ux",
      "ui"
    ],
    "interests": [
      "Health",
      "IoT",
      "Low/No Code",
      "Machine Learning/AI",
      "Social Good",
      "Web"
    ],
    "bio": "I'm full-stack, with solid project experience building react and python web apps that query the OpenAI API for JSON responses. I lean towards product design, UX, and front-end, but can work across the stack. My ideal teammates are other developers who are full-stack, back-end or front-end. My details: seanahrens.org"
  },
  {
    "name": "Sunir Manandhar",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "javascript",
      "chatgpt",
      "cursor",
      "ai-powered-building",
      "python",
      "react",
      "html5",
      "css3"
    ],
    "interests": [
      "Beginner Friendly",
      "Enterprise",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Mobile",
      "Open Ended",
      "Robotic Process Automation",
      "Voice skills",
      "Web"
    ],
    "bio": "18 year old , self taught hacker"
  },
  {
    "name": "Phillip Pang",
    "projects": "2 projects",
    "followers": "4 followers",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "scrum",
      "sdle",
      "agile",
      "jira",
      "slack",
      "mindmap",
      "python",
      "java",
      "swift",
      "php",
      "sql-server",
      "mysql",
      "ios",
      "tensorflow",
      "machine-learning",
      "keras",
      "talend",
      "unica",
      "adobe",
      "eloqua",
      "twilio",
      "amazon-alexa"
    ]
  },
  {
    "name": "Sushma Y",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "databases",
      "amazon-web-services",
      "unix",
      "sql"
    ],
    "interests": [
      "Beginner Friendly",
      "Databases",
      "Design",
      "DevOps",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Markus Mak",
    "title": "Product manager",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "3 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "javascript"
    ],
    "interests": [
      "E-commerce/Retail",
      "Machine Learning/AI",
      "Productivity"
    ],
    "bio": "My name is Markus and I am a product manager in the SaaS space with experience in LLM dev and full-stack."
  },
  {
    "name": "Tejas Udayakumar",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "generative-ai",
      "customer-discovery"
    ],
    "interests": [
      "Low/No Code",
      "Machine Learning/AI",
      "Social Good"
    ]
  },
  {
    "name": "Brendon Geils",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "n"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "jess-render Lin",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "javascript",
      "python",
      "react",
      "node.js",
      "full-stack",
      "postgresql",
      "mongodb"
    ],
    "interests": [
      "Databases",
      "E-commerce/Retail",
      "Enterprise",
      "Fintech",
      "Machine Learning/AI",
      "Music/Art",
      "Web"
    ]
  },
  {
    "name": "L L",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "machine-learning",
      "deep-learning",
      "data-engineering"
    ],
    "interests": [
      "Databases",
      "E-commerce/Retail",
      "Machine Learning/AI",
      "Social Good"
    ]
  },
  {
    "name": "Varun Pant",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "postgresql",
      "typescript",
      "react",
      "python",
      "java",
      "api",
      "gpt",
      "machine-learning"
    ],
    "interests": [
      "Databases",
      "DevOps",
      "Enterprise",
      "Fintech",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Kushal Therokar",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "2 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "machine-learning",
      "tensorflow",
      "deep-learning"
    ],
    "interests": [
      "Beginner Friendly",
      "Low/No Code",
      "Machine Learning/AI",
      "Communication",
      "Education",
      "Gaming",
      "Open Ended",
      "Social Good"
    ]
  },
  {
    "name": "Vineeth Sai",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "r",
      "sql",
      "machine-learning",
      "deeplearning",
      "natural-language-processing",
      "gan",
      "sqlite",
      "mysql",
      "amazon-web-services",
      "gcp",
      "heroku",
      "html/css",
      "javascript",
      "scipy",
      "spacy",
      "scikitlearn",
      "nltk",
      "tensorflow",
      "keras"
    ],
    "interests": [
      "Communication",
      "Databases",
      "DevOps",
      "Gaming",
      "IoT",
      "Machine Learning/AI",
      "Mobile",
      "Productivity",
      "Social Good",
      "Voice skills",
      "Web"
    ]
  },
  {
    "name": "Yueqian Zhang",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "c++",
      "xr"
    ],
    "interests": [
      "AR/VR",
      "Gaming",
      "Music/Art"
    ],
    "bio": "I am an engineer and an artist; ask me about computer graphics and geometry."
  },
  {
    "name": "Lei Zhao",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "javascript",
      "python"
    ],
    "interests": [
      "Communication",
      "Lifehacks",
      "Productivity",
      "Social Good"
    ]
  },
  {
    "name": "Vedant Agrawal",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo"
  },
  {
    "name": "Raymond Weitekamp",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo"
  },
  {
    "name": "Eric Liu",
    "title": "Front-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "javascript"
    ],
    "interests": [
      "Music/Art"
    ]
  },
  {
    "name": "Sushil Pandey",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "2 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "salesforce"
    ],
    "interests": [
      "Communication",
      "IoT",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Shivam Ravindra Hasurkar",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "react",
      "dart",
      "c++",
      "ai",
      "chatbot",
      "flutter"
    ],
    "interests": [
      "Databases",
      "DevOps",
      "E-commerce/Retail",
      "Enterprise",
      "Fintech",
      "Machine Learning/AI",
      "Mobile",
      "Productivity",
      "Social Good",
      "Web"
    ]
  },
  {
    "name": "Audrey Cai",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "data.gov.sg"
    ],
    "interests": [
      "Mobile",
      "Music/Art"
    ]
  },
  {
    "name": "Philip Ninan",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "pytorch",
      "mlops",
      "machine",
      "kubernetes",
      "natural-language-processing",
      "cv"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "Philip Ninan, Ex- Meta AI Product Manager. Building a copilot for multimodal RAG."
  },
  {
    "name": "Rithik Reddy Katpally",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "android",
      "git",
      "gcp",
      "amazon-web-services",
      "tensorflow",
      "pytorch",
      "linux",
      "bigquery",
      "mongodb",
      "react",
      "node.js",
      "flask",
      "django",
      "streamlit",
      "mysql",
      "postgresql",
      "oops",
      "hadoop",
      "apachespark",
      "oraclesql",
      "numpy",
      "pandas",
      "scikit-learn",
      "keras",
      "spring-boot",
      "opencv",
      "docker",
      "kubernetes",
      "spacy",
      "nltk",
      "matplotlib",
      "seaborn",
      "powerbi",
      "tableau",
      "langchain",
      "natural-language-processing"
    ],
    "interests": [
      "AR/VR",
      "Design",
      "Machine Learning/AI",
      "Mobile",
      "Open Ended",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "Krishna Gogineni",
    "title": "ML Engineer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "ml",
      "llm",
      "genai",
      "natural-language-processing",
      "speech-ml"
    ],
    "interests": [
      "Machine Learning/AI",
      "Voice skills"
    ],
    "bio": "Hi, I am a founding/principal ML engineer at a unicorn startup. I specialize in conversational AI (speech-to-text, NLP, genAI, ml platform etc). Thinking of building a multimodal RAG application for this competition."
  },
  {
    "name": "Brian Xu",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "amazon-web-services",
      "sagemaker",
      "databricks",
      "cybersecurity",
      "cloud",
      "data-security"
    ],
    "interests": [
      "Cybersecurity",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Scarlet Xu",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "c++"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Lisabeth hsu",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "html5"
    ]
  },
  {
    "name": "Justin Zhang",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "typescript",
      "python",
      "solidity"
    ],
    "interests": [
      "Blockchain",
      "Cybersecurity",
      "Gaming",
      "Machine Learning/AI",
      "Productivity",
      "Social Good",
      "hacker"
    ]
  },
  {
    "name": "Madhav Asok",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "5 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "react",
      "amazon-web-services",
      "mysql",
      "openai",
      "java",
      "typescript"
    ],
    "interests": [
      "DevOps",
      "Education",
      "Health",
      "Machine Learning/AI",
      "Music/Art",
      "Productivity",
      "Social Good"
    ],
    "bio": "Full-stack, looking to make AI products related to the health or education industry"
  },
  {
    "name": "Ankita GJ",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "java",
      "python",
      "api"
    ],
    "interests": [
      "Beginner Friendly",
      "E-commerce/Retail",
      "Health",
      "Lifehacks",
      "Machine Learning/AI"
    ],
    "bio": "I am a Software Engineer at Google who is passionate about Health-tech and the endless opportunitiesAI can provide to enable for this field. I have a few ideas but I am myself new to AI space. I am looking for anyone who is interested to collaborate and build something exciting and meaningful."
  },
  {
    "name": "Renee Huang",
    "title": "Data scientist",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "3 achievements",
    "team_status": "Has a team",
    "skills": [
      "python",
      "particle",
      "languagemodel"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Roberto Ibarra",
    "title": "Business",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "legal",
      "analizis"
    ],
    "interests": [
      "Blockchain",
      "Education",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Yin Langxuan",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "ai",
      "infra"
    ],
    "interests": [
      "Gaming"
    ],
    "bio": "I'm a backend engineer proficient in building infra and finetuning/RAGing LLMs. Looking for a team to build cool products."
  },
  {
    "name": "Mohan Dattatreya",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "llm",
      "langchain"
    ],
    "interests": [
      "DevOps",
      "Machine Learning/AI"
    ],
    "bio": "Someone who can code / hack. I can provide ideas."
  },
  {
    "name": "Max V\u00e1zquez",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "2 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      ".net",
      "react",
      "mysql",
      "azure"
    ],
    "interests": [
      "Enterprise",
      "Gaming",
      "Music/Art",
      "Web",
      "DevOps",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Pooja P",
    "title": "I'm working as a PM in the ML/AI space building simple projects, looking for hack mates.",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates"
  },
  {
    "name": "Santos Alejandro De la fuente Trevino",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "3 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "ruby-on-rails",
      "postgresql",
      "sql",
      "react",
      "javascript"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Ricardo Rodriguez",
    "title": "Designer",
    "projects": "0 projects",
    "followers": "2 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "ux",
      "ui",
      "figma",
      "html",
      "adobe-illustrator",
      "promting",
      "business"
    ],
    "interests": [
      "Beginner Friendly",
      "Education",
      "Machine Learning/AI",
      "Productivity"
    ]
  },
  {
    "name": "sid ramachandran",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "api",
      "llm",
      "llama",
      "falcon",
      "rag",
      "huggingface"
    ],
    "interests": [
      "Blockchain",
      "Fintech",
      "Machine Learning/AI",
      "Quantum"
    ],
    "bio": "I have experience building RAG applications and using NLP for language processing and generation. Looking for team mates to work with who can attend in person as I help from Scotland."
  },
  {
    "name": "Naveen Madiraju",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python"
    ],
    "interests": [
      "Design"
    ]
  },
  {
    "name": "Sai Reddy",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "c++",
      "sql",
      "langchain",
      "javascript",
      "azure",
      "ai"
    ],
    "interests": [
      "Beginner Friendly",
      "Databases",
      "Education",
      "Fintech",
      "Machine Learning/AI",
      "Open Ended"
    ]
  },
  {
    "name": "Shinnosuke Uesaka",
    "projects": "3 projects",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Has a team"
  },
  {
    "name": "Dulat A",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "javascript",
      "c++"
    ],
    "interests": [
      "Robotic Process Automation",
      "Web",
      "Machine Learning/AI"
    ],
    "bio": "Hi I am D looking team mates"
  },
  {
    "name": "zhaoqi li",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "react",
      "python",
      "nextjs",
      "llm"
    ],
    "interests": [
      "Databases",
      "Design",
      "Education",
      "Health",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Mobile",
      "Open Ended",
      "Social Good",
      "Web"
    ]
  },
  {
    "name": "Manjit Chakravarthy",
    "title": "Back-end developer",
    "projects": "1 project",
    "followers": "1 follower",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "python",
      "java",
      "llm-finetuning",
      "diffusionmodels"
    ],
    "interests": [
      "AR/VR",
      "Machine Learning/AI",
      "Mobile",
      "Music/Art",
      "Open Ended",
      "Robotic Process Automation",
      "Social Good",
      "Web"
    ]
  },
  {
    "name": "Anisha Rao",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "java",
      "python",
      "machine-learning",
      "ai",
      "sql"
    ],
    "interests": [
      "Databases",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Mark Evans",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "llm",
      "ai"
    ],
    "interests": [
      "Enterprise",
      "Machine Learning/AI",
      "Music/Art"
    ]
  },
  {
    "name": "Henry Kendall",
    "title": "Full-stack developer",
    "projects": "5 projects",
    "followers": "9 followers",
    "achievements": "5 achievements",
    "team_status": "Working solo",
    "skills": [
      "android",
      "hardware",
      "ios",
      "mac",
      "web",
      "windows",
      "windows-phone",
      "blockchain",
      "cloud",
      "linux",
      "big-data",
      "hadoop",
      "particle",
      "machine-learning",
      "artificial-intelligence"
    ],
    "interests": [
      "Blockchain"
    ]
  },
  {
    "name": "Franco G Valeriano",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team"
  },
  {
    "name": "Jesse Hu",
    "title": "Full-stack developer",
    "projects": "9 projects",
    "followers": "8 followers",
    "achievements": "6 achievements",
    "team_status": "Working solo",
    "skills": [
      "hardware",
      "web",
      "machine-learning"
    ],
    "interests": [
      "Blockchain",
      "Health",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Mobile",
      "Music/Art",
      "Productivity",
      "Social Good"
    ]
  },
  {
    "name": "Andrew Korf",
    "title": "Designer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "ux",
      "prototyping",
      "uxstrategy",
      "userresearch",
      "validation",
      "businessrequirements",
      "userrequirements"
    ],
    "interests": [
      "Design",
      "Enterprise",
      "Machine Learning/AI"
    ],
    "bio": "As an experienced enterprise UX leader, I would love to partner with a sharp team to develop and deliver an impactful experience that might solve one small slice of a broader enterprise problem, particularly in the area of horizon scanning and real time sensing of the cloud and problems, issues, topics leader need to be made aware of. Open to other interesting challenges as well."
  },
  {
    "name": "Danny W.",
    "title": "Product manager",
    "projects": "2 projects",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "solidity",
      "genai/llm",
      "python",
      "pytorch"
    ],
    "interests": [
      "Blockchain",
      "Enterprise",
      "Web",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Niraj Kumar Singh",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Has a team",
    "skills": [
      "python",
      "c++",
      "c",
      "java",
      "machine-learning"
    ],
    "interests": [
      "Machine Learning/AI",
      "Productivity"
    ]
  },
  {
    "name": "Nathan M.",
    "title": "Full-stack developer",
    "projects": "4 projects",
    "followers": "3 followers",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "java",
      "python",
      "html5",
      "css3",
      "ml",
      "natural-language-processing",
      "cv",
      "rl",
      "django",
      "react",
      "react-native"
    ],
    "interests": [
      "Blockchain",
      "Cybersecurity",
      "Fintech",
      "Gaming",
      "Machine Learning/AI",
      "Social Good"
    ],
    "bio": "Hey! I'm a recent grad from CMU with a degree in Artificial Intelligence. I've worked on Recommendation Systems at Netflix, Ads at Meta, and at some startups as well. I have experience in fullstack development, ML, and NLP, but haven't specifically implemented anything with RAG, so I'm looking forward to learning more about it!"
  },
  {
    "name": "vansh remote",
    "title": "Full-stack developer",
    "projects": "2 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "node.js",
      "express.js",
      "react",
      "json",
      "graphql",
      "javascript",
      "mongodb",
      "postgresql",
      "websockets"
    ],
    "interests": [
      "Beginner Friendly",
      "DevOps",
      "E-commerce/Retail",
      "Education",
      "Enterprise",
      "Fintech",
      "Health",
      "IoT",
      "Low/No Code",
      "Machine Learning/AI",
      "Mobile",
      "Productivity",
      "Social Good",
      "Web"
    ]
  },
  {
    "name": "Austin Fischer",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "rag",
      "machine-learning",
      "amazon-web-services",
      "computer-vision",
      "natural-language-processing",
      "data-science"
    ],
    "interests": [
      "Education",
      "Machine Learning/AI",
      "Music/Art",
      "Open Ended",
      "Social Good"
    ],
    "bio": "I work as an ML consultant on a professional services team, and we recently completed a user-access controlled RAG solution. I'm very inspired by Voyager by Fan et. al, and I'd like to work on RAG for user preferences / policy retrieval, allowing agents to dynamically retrieve natural language instructions for dealing with complex text-based problems. I'm open to mapping this onto other plans, and can work in most Python-based tech stacks."
  },
  {
    "name": "Hari Kunamneni",
    "title": "Deep Learning",
    "projects": "6 projects",
    "followers": "7 followers",
    "achievements": "4 achievements",
    "team_status": "Working solo",
    "skills": [
      "android",
      "ios",
      "web"
    ],
    "interests": [
      "Fintech",
      "Health",
      "Machine Learning/AI",
      "Mobile"
    ]
  },
  {
    "name": "Eugenia/Yujia Cao",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "streamlit",
      "sqlite",
      "mongodb",
      "natural-language-processing",
      "design"
    ],
    "interests": [
      "Beginner Friendly",
      "Databases",
      "Design",
      "Fintech",
      "Machine Learning/AI",
      "Music/Art",
      "Communication"
    ]
  },
  {
    "name": "Michael Tseng",
    "title": "Full-stack developer",
    "projects": "2 projects",
    "followers": "1 follower",
    "achievements": "5 achievements",
    "team_status": "Has a team",
    "skills": [
      "machine-learning",
      "python",
      "flask",
      "react",
      "nextjs"
    ],
    "interests": [
      "AR/VR",
      "DevOps",
      "Machine Learning/AI",
      "Voice skills",
      "Web"
    ]
  },
  {
    "name": "CY L",
    "title": "Full-stack developer",
    "projects": "2 projects",
    "followers": "0 followers",
    "achievements": "6 achievements",
    "team_status": "Has a team",
    "skills": [
      "mern"
    ],
    "interests": [
      "Web"
    ]
  },
  {
    "name": "Asher Lim",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team"
  },
  {
    "name": "TJun-Jie Tai",
    "title": "Full-stack developer",
    "projects": "4 projects",
    "followers": "1 follower",
    "achievements": "8 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "flutter",
      "react"
    ],
    "interests": [
      "Lifehacks",
      "Web"
    ]
  },
  {
    "name": "Himanshu Patel",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "java",
      "python",
      "node.js"
    ],
    "interests": [
      "Fintech",
      "IoT",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Rileyriler Noon",
    "title": "Product manager",
    "projects": "2 projects",
    "followers": "0 followers",
    "achievements": "8 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "javascript"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Fintech",
      "Gaming",
      "Productivity",
      "Open Ended",
      "Beginner Friendly",
      "Education"
    ],
    "bio": "Hello, I'm a recent college grad who obtained an economics degree and learned to code on the side. I've participated in a few hackathons and would consider myself a little above a beginner's skill level. I'm looking for teammates who want to learn new skills and build something truly useful for real users."
  },
  {
    "name": "Justin Szaday",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Has a team",
    "skills": [
      "javascript",
      "antlr",
      "c",
      "c++",
      "node.js",
      "hpc",
      "gpu"
    ],
    "interests": [
      "Databases",
      "Machine Learning/AI",
      "Open Ended",
      "Quantum"
    ]
  },
  {
    "name": "Sophie Liu",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Has a team"
  },
  {
    "name": "Venkatesh Gunda",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "machine-learning",
      "natural-language-processing"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Mehdi Allahyari",
    "title": "AI Researcher",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "machine-learning",
      "natural-language-processing",
      "llm",
      "generative-ai",
      "knowledge-graph"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Angelina  Yang",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "chinese",
      "data",
      "ml",
      "natural-language-processing",
      "python",
      "r"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Shridhar Shah",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "langchain",
      "golang",
      "javascript",
      "ai",
      "ml",
      "web",
      "docker",
      "kubernetes",
      "amazon-web-services",
      "llamaindex",
      "llm",
      "react"
    ],
    "interests": [
      "DevOps",
      "IoT",
      "Machine Learning/AI",
      "Open Ended"
    ]
  },
  {
    "name": "Kevin Smith",
    "title": "Data scientist",
    "projects": "1 project",
    "followers": "4 followers",
    "achievements": "5 achievements",
    "team_status": "Working solo",
    "skills": [
      "tensorflow",
      "huggingface",
      "sklearn",
      "numpy",
      "xgboost",
      "pandas",
      "pytorch",
      "regex",
      "matplotlib",
      "plotly",
      "scipy"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Med khalil Bousnina",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "ai",
      "devops",
      "machine",
      "deep"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Utshav Paudel",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "sql",
      "pytoch"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Takuya Nagai",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "javascript",
      "java",
      "documentum",
      "sso",
      "mfa",
      "okta",
      "jumpcloud"
    ]
  },
  {
    "name": "fmigsystems Kim",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "swift"
    ],
    "interests": [
      "AR/VR",
      "Communication",
      "Fintech",
      "Gaming",
      "Lifehacks",
      "Machine Learning/AI",
      "Social Good",
      "Voice skills"
    ]
  },
  {
    "name": "Rujun Gao",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "rag",
      "llm",
      "natural-language-processing",
      "gai",
      "api",
      "llamaindex",
      "langchain"
    ],
    "interests": [
      "Blockchain",
      "Communication",
      "Cybersecurity",
      "Databases",
      "Education",
      "Enterprise",
      "Health",
      "Machine Learning/AI",
      "Robotic Process Automation",
      "Social Good",
      "Web"
    ]
  },
  {
    "name": "brandonhyc He",
    "title": "Front-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "typescript"
    ],
    "interests": [
      "Beginner Friendly",
      "Education",
      "Productivity",
      "Web"
    ]
  },
  {
    "name": "Mike Tung",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "2 followers",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "fine-tuning",
      "information-retrieval",
      "math"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "Hi! I'm a Berkeley/Stanford grad, worked in the AI lab. Now doing a startup around knowledge graphs, and using LLMs to structure data."
  },
  {
    "name": "Bharathrham Kodungudi",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python"
    ],
    "interests": [
      "Beginner Friendly",
      "Education",
      "Fintech",
      "Gaming",
      "Health",
      "Machine Learning/AI",
      "Open Ended",
      "Robotic Process Automation",
      "Social Good"
    ]
  },
  {
    "name": "imran adem",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python"
    ],
    "interests": [
      "Health",
      "Machine Learning/AI",
      "Mobile"
    ]
  },
  {
    "name": "Yichen Mo",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "machine-learning",
      "natural-language-processing",
      "python"
    ],
    "interests": [
      "DevOps",
      "Health",
      "Machine Learning/AI"
    ],
    "bio": "As a Machine Learning Engineer with 3.5 years of experience, I am keen to collaborate with new team members. My ability to quickly adapt and work within a team environment allows me to contribute my skills effectively. I possess a passion for leveraging LLM to bring innovative ideas to fruition. If you are interested, I would be delighted to connect and explore potential opportunities to collaborate."
  },
  {
    "name": "Aumkar Renavikar",
    "projects": "1 project",
    "followers": "1 follower",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "python"
    ],
    "interests": [
      "IoT",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Tarun Malik",
    "title": "Data scientist",
    "projects": "4 projects",
    "followers": "0 followers",
    "achievements": "6 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "javascript",
      "ios",
      "jquery",
      "css",
      "html5",
      "python",
      "ml",
      "product"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "Help support teams for hardware companies"
  },
  {
    "name": "Zehra Rizvi",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "flask",
      "sql",
      "jupyter",
      "reliability",
      "node.js",
      "particle",
      "pandas"
    ],
    "interests": [
      "DevOps",
      "Machine Learning/AI",
      "Databases",
      "Robotic Process Automation",
      "Social Good",
      "Web"
    ]
  },
  {
    "name": "Sanyam Oberoi",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "postgresql",
      "mongodb",
      "weaviate",
      "pytorch",
      "fastapi"
    ],
    "interests": [
      "Beginner Friendly",
      "Machine Learning/AI"
    ],
    "bio": "Hey! I am a Machine Learning Engineer and have been working in NLP for the past few years. Have been playing around with LLMs for RAG and other use-cases. Would be cool to pair-up with folks to share knowledge and ideas and connect with them"
  },
  {
    "name": "Shafie Mukhre",
    "title": "Full-stack developer",
    "projects": "10 projects",
    "followers": "20 followers",
    "achievements": "7 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "javascript",
      "html",
      "css",
      "firebase",
      "hugo",
      "netlify",
      "flask",
      "react",
      "bootstrap",
      "crud",
      "php",
      "mysql",
      "postgresql",
      "robotics",
      "c/c++",
      "tensorflow.js",
      "ml-kit",
      "ios",
      "render",
      "amazon-web-services",
      "google-cloud"
    ],
    "interests": [
      "IoT",
      "Machine Learning/AI"
    ],
    "bio": "Fullstack dev, planning to use NextJS for this hackathon and build something related to data analytics/management."
  },
  {
    "name": "Anup Mantri",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "machine-learning",
      "big-data"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "I have been working as a software engineer for >15 yrs, mainly backend and ML. Looking to build and ship something cool."
  },
  {
    "name": "Oliver Giesecke",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "react"
    ],
    "interests": [
      "Enterprise",
      "Fintech"
    ]
  },
  {
    "name": "Avani Gadani",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "ml",
      "ai",
      "storage",
      "systems"
    ],
    "interests": [
      "Beginner Friendly",
      "Cybersecurity",
      "Education",
      "Low/No Code",
      "Machine Learning/AI",
      "Music/Art",
      "Open Ended",
      "Quantum",
      "Social Good"
    ]
  },
  {
    "name": "Fernando Ljung",
    "title": "Machine learning and back end engineer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "machine-learning"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Tanay Sood",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "sql",
      "machine-learning"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Paul Baclace",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "java",
      "hadoop",
      "linux",
      "amazon-web-services",
      "devops",
      "writing"
    ],
    "interests": [
      "DevOps",
      "Machine Learning/AI",
      "Music/Art"
    ],
    "bio": "Idea: for RAG is to structurally analyze fiction. It would be a tool for fiction writers to analyze stories, dialogue, plot, and story arc. Me: I co-founded UnravelData.com, worked on deep learning projects at Internet Archive, do AI product management. Looking for: a python coder interested in text extraction and search engine results re-ranking, plus a UI developer."
  },
  {
    "name": "Rahul Bhoyar",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "python-package-index",
      "data",
      "machine-learning",
      "natural-language-processing",
      "generative-ai"
    ],
    "interests": [
      "Beginner Friendly"
    ]
  },
  {
    "name": "Morris Hsu",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "c++",
      "javascript"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Luka \u010cubrilo",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "c",
      "c++",
      "python",
      "java",
      "gpt",
      "llm",
      "sql",
      "tensorflow",
      "langchain",
      "rag",
      "html5",
      "css3",
      "pandas",
      "qt",
      "pyqt",
      "javascript"
    ],
    "interests": [
      "Beginner Friendly",
      "DevOps",
      "Education",
      "Gaming",
      "IoT",
      "Machine Learning/AI",
      "Quantum",
      "Social Good"
    ],
    "bio": "Chameleon - can work on anything. Currently developing my own LLM-powered product. Programming for 8 years in C++, Python and a few others. Worked on a Data Science solution in Slovenia's leading research institute. I am a final-year CS student, and recently started going into the world of LLMs."
  },
  {
    "name": "Carmen Cruzado",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "docker",
      "langchain",
      "llm",
      "bash",
      "vim"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Sean Durkin",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "c",
      "typescript",
      "pytorch"
    ],
    "interests": [
      "AR/VR",
      "Cybersecurity",
      "IoT",
      "Low/No Code",
      "Machine Learning/AI",
      "Social Good"
    ],
    "bio": "Hi, I'm Sean. Interested in agent-based development for cybersecurity and consumer applications. Founder, Mastiff AI. Full stack developer, prefer Python, C for serverside, Typescript for UI/UX. Product management experience."
  },
  {
    "name": "KY HEON",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "1 follower",
    "achievements": "3 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "react",
      "node.js",
      "express.js",
      "flask"
    ],
    "interests": [
      "Design",
      "Machine Learning/AI",
      "Robotic Process Automation"
    ],
    "bio": "I'm Ky, an entry level developer interested in AI and Robotics. I am familiar with React and ExpressJS frameworks, and have some experience with building products using the OpenAI API. I am primarily interested in meeting cool people and learning more about the technology ecosystem being developed around LLM/MMM's."
  },
  {
    "name": "Cesar William",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team"
  },
  {
    "name": "Muhammad Hassan",
    "title": "AI Engineer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "langchain",
      "pytorch",
      "llm",
      "rag",
      "huggingface",
      "python",
      "generativeai"
    ],
    "interests": [
      "E-commerce/Retail",
      "Education",
      "Fintech",
      "Machine Learning/AI"
    ],
    "bio": "My name is Muhammad Hassan, and I hold a Bachelor's degree in Computer Science. I bring six months of valuable experience as a Machine Learning Trainer in an educational institute. Currently, I am dedicated to serving as an AI Engineer. I am actively seeking a collaborative opportunity to contribute my skills and expertise as a teammate in a hackathon."
  },
  {
    "name": "Robert H Lee",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python"
    ],
    "interests": [
      "Cybersecurity",
      "Health",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Productivity",
      "Quantum",
      "Social Good"
    ]
  },
  {
    "name": "Georgio Stoev",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "ai",
      "governance"
    ],
    "interests": [
      "Databases",
      "Enterprise",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Kyel Steensma",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "dataanalytics",
      "chemicalengineering"
    ],
    "interests": [
      "Beginner Friendly",
      "Education",
      "Machine Learning/AI",
      "Quantum"
    ],
    "bio": "Me and a friend (co-founder) are looking to build AI which interprets reads, interacts with and draws engineering diagrams (chemical, civil, electrical engineering etc.), in order to massively cut down time spent in large engineering projects."
  },
  {
    "name": "shotamakino Makino",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "go",
      "typescript"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Gaming",
      "IoT",
      "Quantum",
      "Robotic Process Automation",
      "Cybersecurity",
      "Design",
      "Fintech",
      "Machine Learning/AI",
      "Mobile",
      "Music/Art"
    ]
  },
  {
    "name": "ZixinxD Liu",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Has a team",
    "skills": [
      "python",
      "c++",
      "website",
      "data-strucutres-and-algorithms",
      "guitar"
    ]
  },
  {
    "name": "Lawrence Lao",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "product"
    ],
    "interests": [
      "Robotic Process Automation"
    ]
  },
  {
    "name": "John Cocjin",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python"
    ],
    "interests": [
      "Design",
      "Education",
      "Enterprise",
      "Machine Learning/AI",
      "Music/Art",
      "Robotic Process Automation",
      "Social Good"
    ]
  },
  {
    "name": "LAKSHMAN V REDDY",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "github",
      "azure"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Brennan Stewart",
    "title": "Full-stack developer",
    "projects": "3 projects",
    "followers": "0 followers",
    "achievements": "8 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "javascript",
      "react",
      "next",
      "css3",
      "html5",
      "vue",
      "amazon-web-services",
      "openai",
      "tailwind",
      "python",
      "langchain",
      "llamaindex"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Blockchain",
      "Communication",
      "Cybersecurity",
      "Databases",
      "Design",
      "E-commerce/Retail",
      "Enterprise",
      "Fintech",
      "Health",
      "IoT",
      "Lifehacks",
      "Machine Learning/AI",
      "Mobile",
      "Music/Art",
      "Productivity",
      "Quantum",
      "Web",
      "DevOps",
      "Education",
      "Gaming",
      "Open Ended",
      "Robotic Process Automation",
      "Social Good",
      "Voice skills"
    ],
    "bio": "Hello, my name is Brennan. I have been working with LlamaIndex and other RAG platforms to create robust chatbots and agentic tools. I would love to join a team using advanced RAG techniques provided by LlamaIndex to create something awesome. Skilled in RAG pipeline development and applying RAG to several verticals."
  },
  {
    "name": "Boquan Yin",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "react",
      "javascript",
      "python",
      "django",
      "vue",
      "node.js",
      "pytorch",
      "llamaindex",
      "langchain",
      "llm",
      "agent",
      "fastapi",
      "huggingface",
      "machine-learning",
      "deep-learning"
    ],
    "interests": [
      "Design",
      "DevOps",
      "Education",
      "Machine Learning/AI",
      "Mobile",
      "Web",
      "AR/VR",
      "Communication",
      "Databases",
      "Gaming",
      "Low/No Code",
      "Open Ended",
      "Robotic Process Automation"
    ],
    "bio": "Looking for teammates familiar with LlamaIndex/Langchain and a variety of RAG retrieval & ingestion strategies. I can code both frontend (React + Next.js) and backend (FastAPI, Django, etc) as well as prompt engineering with langchain & llamaindex to build RAG pipeline and agentic solutions."
  },
  {
    "name": "yina qiao",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "ux",
      "ui"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Communication",
      "Design"
    ]
  },
  {
    "name": "Raju Penmatcha",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "ml",
      "llm",
      "ai"
    ],
    "interests": [
      "Machine Learning/AI",
      "Low/No Code"
    ],
    "bio": "Looking for teammates that can code really well, or can build a functional UI. I code in Python (am a decent coder) and am a data scientist, have been working in ML since 2014 and in the AI/LLM space since one year. ex-AWS AI architect and product manager"
  },
  {
    "name": "Dongming Li",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "react",
      "python"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Evan Grenda",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "openai"
    ],
    "interests": [
      "Enterprise"
    ]
  },
  {
    "name": "Nik Shevchenko",
    "title": "Full-stack developer",
    "projects": "2 projects",
    "followers": "1 follower",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "product",
      "management",
      "marketing",
      "nocode"
    ],
    "interests": [
      "Lifehacks",
      "Machine Learning/AI",
      "Productivity",
      "AR/VR",
      "Beginner Friendly",
      "Databases",
      "Low/No Code"
    ],
    "bio": "Thiel fellow, raised $3m, built $52m company and sold it to toptal.com Let's build"
  },
  {
    "name": "Stanley Cai",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Jing Li",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "llm",
      "python",
      "machine-learning"
    ],
    "interests": [
      "Beginner Friendly",
      "Lifehacks",
      "Open Ended",
      "Productivity",
      "Social Good"
    ]
  },
  {
    "name": "Vibhu Sapra",
    "title": "ML / AI",
    "projects": "2 projects",
    "followers": "0 followers",
    "achievements": "5 achievements",
    "team_status": "Working solo",
    "skills": [
      "python",
      "machine-learning",
      "ai"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Laurie05 Luo",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team"
  },
  {
    "name": "Qianhui (Gabrielle) Sun",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "instructionaldesign",
      "django"
    ],
    "interests": [
      "Beginner Friendly",
      "Education",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Sreenivasan A.C.",
    "title": "Back-end developer",
    "projects": "1 project",
    "followers": "2 followers",
    "achievements": "4 achievements",
    "team_status": "Working solo",
    "skills": [
      "machine-learning",
      "natural-language-processing",
      "artificial-intelligence",
      "python",
      "javascript",
      "coding",
      "node.js",
      "api"
    ],
    "interests": [
      "Education",
      "Machine Learning/AI",
      "Productivity",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "Ch Abdullah Abdullah",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "tensorflow",
      "pytorch",
      "opencv"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Databases",
      "Education",
      "IoT",
      "Machine Learning/AI",
      "Robotic Process Automation",
      "Web"
    ]
  },
  {
    "name": "Gabe Liu",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "javascript",
      "flutter",
      "react",
      "gcp",
      "amazon-web-services",
      "java"
    ],
    "interests": [
      "Databases",
      "Low/No Code",
      "Machine Learning/AI",
      "Mobile",
      "Open Ended",
      "Productivity",
      "Social Good"
    ],
    "bio": "Experienced backend / data engineer, new to the world of LLM. Looking for teammates to hack together! Particularly interested in use cases related to gov tech and transportation."
  },
  {
    "name": "Leon Pan",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "database"
    ],
    "interests": [
      "Databases",
      "E-commerce/Retail",
      "Health"
    ]
  },
  {
    "name": "Siva Udayamurthy",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "english"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Beginner Friendly",
      "Communication",
      "Cybersecurity",
      "Databases",
      "Design",
      "DevOps",
      "E-commerce/Retail",
      "Education",
      "Enterprise",
      "Fintech",
      "Gaming",
      "Health",
      "IoT",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Mobile",
      "Music/Art",
      "Open Ended",
      "Productivity",
      "Quantum",
      "Robotic Process Automation",
      "Social Good",
      "Voice skills",
      "Web"
    ]
  },
  {
    "name": "Jesse Chan",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "2 achievements",
    "team_status": "Has a team",
    "skills": [
      "python",
      "pytorch",
      "c",
      "c++",
      "nltk",
      "spacy",
      "natural-language-processing",
      "linux",
      "html",
      "css",
      "javascript",
      "standard-ml",
      "sml",
      "pml",
      "regex",
      "regexlib",
      "sql",
      "azure",
      "amazon-web-services",
      "numpy",
      "pandas",
      "swift",
      "swiftui",
      "html5",
      "scikit-learn",
      "latex",
      "git",
      "vscode",
      "leancloud",
      "realm",
      "xcode",
      "opencv",
      "data-structures",
      "parallel-algorithms",
      "arduino"
    ],
    "interests": [
      "Communication",
      "Cybersecurity",
      "Fintech",
      "Lifehacks",
      "Machine Learning/AI",
      "Productivity",
      "Voice skills"
    ]
  },
  {
    "name": "Emily-Feng Feng",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "go",
      "kubernetes",
      "ruby-on-rails",
      "swift"
    ],
    "interests": [
      "Beginner Friendly",
      "DevOps",
      "Machine Learning/AI",
      "Robotic Process Automation"
    ],
    "bio": "I have 3+ yrs experience developing web and mobile apps. I have 1+ year experience working on ML infra."
  },
  {
    "name": "Akshay Raj Dhamija",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates"
  },
  {
    "name": "Umut YILDIRIM",
    "title": "Full-stack developer",
    "projects": "2 projects",
    "followers": "5 followers",
    "achievements": "5 achievements",
    "team_status": "Working solo",
    "skills": [
      "python",
      "c#",
      "tensorflow",
      "php",
      "phpmyadmin",
      "mysql"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "DevOps",
      "Gaming",
      "IoT",
      "Machine Learning/AI",
      "Communication",
      "Productivity",
      "Social Good"
    ]
  },
  {
    "name": "Ashutosh Barkule",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Ritik Sharma",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates"
  },
  {
    "name": "Sonya Chiang",
    "title": "Designer",
    "projects": "1 project",
    "followers": "2 followers",
    "achievements": "3 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "figma",
      "flutterflow",
      "adobexd",
      "userexperience"
    ],
    "interests": [
      "Design",
      "Health",
      "Low/No Code",
      "Mobile",
      "Music/Art",
      "Productivity"
    ]
  },
  {
    "name": "Freya Zhu",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "react",
      "typescript",
      "javascript",
      "tailwind",
      "ruby-on-rails",
      "sql",
      "llm"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Machine Learning/AI",
      "Music/Art",
      "Productivity",
      "Voice skills"
    ]
  },
  {
    "name": "Ishan Gupta",
    "title": "ML Engineering",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "computervision",
      "reinforcementlearning"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Fintech",
      "Gaming",
      "Machine Learning/AI",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "Daniel Chipres",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "business",
      "sales",
      "managment"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Blockchain",
      "Communication",
      "Cybersecurity",
      "Education",
      "Low/No Code",
      "Voice skills",
      "Web"
    ],
    "bio": "I'm Daniel, founder of Aiactivated. I'm looking to partner up with a develop who can bring my ideas to life. I believe with your technical skills and my business acumen, we can take over the sales industry by automating the sales process for business owners."
  },
  {
    "name": "Aniket Shirke",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "c++",
      "python",
      "sql",
      "cv",
      "ml",
      "diffusion-models",
      "llm"
    ],
    "interests": [
      "Enterprise",
      "Machine Learning/AI",
      "Music/Art",
      "Social Good",
      "Voice skills"
    ]
  },
  {
    "name": "Lily Su",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "jupyter",
      "amazon-web-services",
      "flask",
      "pytorch",
      "sql",
      "tensorflow",
      "docker"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "David O'Mara",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "organization"
    ],
    "interests": [
      "Fintech",
      "Lifehacks",
      "Mobile"
    ]
  },
  {
    "name": "Jack Retterer",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "llm",
      "frontend",
      "backend",
      "machine-learning"
    ],
    "interests": [
      "Blockchain",
      "Fintech",
      "Gaming",
      "Machine Learning/AI",
      "Productivity"
    ]
  },
  {
    "name": "Rushang Shah",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "javascript",
      "python",
      "node.js"
    ],
    "interests": [
      "Databases",
      "DevOps",
      "Education",
      "Machine Learning/AI",
      "Open Ended",
      "Productivity",
      "Web",
      "Design",
      "Enterprise",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "Deepak Bokhar",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      ".net",
      "design"
    ],
    "interests": [
      "Blockchain",
      "Fintech",
      "Machine Learning/AI",
      "Productivity",
      "Web"
    ]
  },
  {
    "name": "Girri Palaniyapan",
    "title": "Full-stack developer",
    "projects": "5 projects",
    "followers": "2 followers",
    "achievements": "9 achievements",
    "team_status": "Has a team",
    "skills": [
      "python",
      "javascript",
      "node.js",
      "react",
      "natural-language-processing"
    ],
    "interests": [
      "Lifehacks",
      "Machine Learning/AI",
      "Productivity",
      "Fintech"
    ]
  },
  {
    "name": "jia le xian",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "pytho",
      "javascript",
      "html",
      "machine-learning",
      "swift"
    ],
    "interests": [
      "Machine Learning/AI",
      "Social Good"
    ]
  },
  {
    "name": "Zifty Tran",
    "title": "Designer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "hardware",
      "ios",
      "web"
    ],
    "interests": [
      "Beginner Friendly",
      "Blockchain",
      "Cybersecurity",
      "Enterprise",
      "Fintech",
      "IoT",
      "Lifehacks",
      "Machine Learning/AI",
      "Productivity",
      "Quantum",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "Margarita Groisman",
    "title": "Full-stack developer",
    "projects": "3 projects",
    "followers": "1 follower",
    "achievements": "6 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "java",
      "swift"
    ],
    "interests": [
      "DevOps",
      "Education",
      "Machine Learning/AI"
    ],
    "bio": "Hi I am looking for teammates , have built an application that uses RAG before. Would love to have a final product and can do full stack, prefer React front end and Python backend, happy to do Node or JavaScript backend as well."
  },
  {
    "name": "Private user",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python"
    ],
    "interests": [
      "Open Ended",
      "Web",
      "Cybersecurity",
      "Design",
      "DevOps",
      "Education",
      "Fintech",
      "Machine Learning/AI",
      "Productivity"
    ]
  },
  {
    "name": "Sam Dang",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python"
    ],
    "interests": [
      "Machine Learning/AI",
      "Music/Art"
    ]
  },
  {
    "name": "Colin Alexander",
    "title": "ML Engineer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "particle",
      "pandas",
      "machine-learning",
      "finance",
      "crypto"
    ],
    "interests": [
      "Blockchain",
      "Fintech",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Shivram Krishnamurthy",
    "title": "Back-end developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "3 achievements",
    "team_status": "Working solo",
    "skills": [
      "java"
    ],
    "interests": [
      "Machine Learning/AI",
      "Web",
      "Beginner Friendly",
      "Fintech"
    ]
  },
  {
    "name": "Shaohua Zhou",
    "projects": "2 projects",
    "followers": "1 follower",
    "achievements": "4 achievements",
    "team_status": "Has a team"
  },
  {
    "name": "Qin Lonnie",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo"
  },
  {
    "name": "Parth Jain",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "llms",
      "langchain",
      "llamaindex",
      "fast",
      "api",
      "rag"
    ],
    "interests": [
      "Beginner Friendly"
    ],
    "bio": "Hello, My name is Parth Jain. I am Currently Working for A RAG-based startup, and I generally work with prompt engineering, RAG pipeline building, and advanced vector database Retrieval techniques, I can Build RAG pipelines with Langchain and Llama index and serve them as API."
  },
  {
    "name": "Shankha Mullick",
    "title": "Data Engineer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "python",
      "pandas",
      "scikit-learn",
      "machine-learning",
      "pyspark",
      "amazon-web-services",
      "azure",
      "bigdata",
      "data",
      "modelling",
      "warehousing",
      "bi",
      "ingestion",
      "genai",
      "largelanguagemodel",
      "langchain"
    ],
    "interests": [
      "AR/VR",
      "Gaming",
      "Health",
      "IoT",
      "Lifehacks",
      "Machine Learning/AI",
      "Music/Art",
      "Productivity",
      "Databases",
      "DevOps",
      "Enterprise"
    ]
  },
  {
    "name": "kris k",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python"
    ],
    "interests": [
      "DevOps",
      "Enterprise"
    ]
  },
  {
    "name": "Nikhil Shrestha",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "data-science-toolkit",
      "ai",
      "natural-language-processing"
    ],
    "interests": [
      "Beginner Friendly",
      "Machine Learning/AI",
      "Quantum"
    ],
    "bio": "I am a data scientist, frequently playing kaggle competitions. Coding and learning new things in group really fascinates me. Interest on llamaindex grew when I started working on open source project PrivateGPT and cracked substantially difficult logic."
  },
  {
    "name": "Kannuraj Nathamuni",
    "title": "Machine learning engineer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "databases",
      "frameworks",
      "languages",
      "api"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "E-commerce/Retail",
      "Fintech",
      "Gaming",
      "Health",
      "Machine Learning/AI",
      "Social Good",
      "Voice skills"
    ]
  },
  {
    "name": "Radha Krishna Srimanthula",
    "title": "Machine Learning / Deep Learning",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "machine-learning",
      "deep-learning",
      "llms",
      "compilers"
    ],
    "interests": [
      "DevOps",
      "IoT",
      "Machine Learning/AI",
      "Productivity"
    ]
  },
  {
    "name": "Meir Peretz",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "react",
      "nextjs",
      "node.js",
      "mongodb",
      "python",
      "postgress"
    ],
    "interests": [
      "Blockchain",
      "Databases",
      "IoT",
      "Lifehacks",
      "Mobile",
      "Productivity",
      "Web"
    ]
  },
  {
    "name": "Aiswarya Sunil Sankar",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "llm"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "Looking for a cofounder for entelligence.ai"
  },
  {
    "name": "Sandeep S",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "java",
      "langchain",
      "llamaindex",
      "angular.js",
      "sql",
      "pandas",
      "pytorch"
    ],
    "interests": [
      "Beginner Friendly",
      "Machine Learning/AI"
    ],
    "bio": "I am a full time working full stack engineer at Apple with over 15 years of experience, pursuing MS in data science at UT. Currently exploring LLMS, and able to to query internal documents using Langchain and LlamaIndex. With this opportunity looking forward to learn more about Llamaindex and meet great minds. I have an idea to create a solution for efficiently capturing meeting minutes (MOM) and action items. The goal is to streamline the process and enhance the effectiveness of tracking key discussions and tasks during meetings. Open to any other idea's and collaborate. Thanks"
  },
  {
    "name": "Aabid Ismail",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "rag",
      "backend",
      "nextjs"
    ],
    "interests": [
      "Beginner Friendly",
      "Education",
      "Machine Learning/AI",
      "Music/Art",
      "Open Ended",
      "Social Good"
    ]
  },
  {
    "name": "Steve pousty",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "java",
      "python",
      "postgresql",
      "geospatial",
      "cloud-native",
      "containers",
      "kubernetes",
      "remote-sensing",
      "ai"
    ],
    "interests": [
      "Databases",
      "Education",
      "Fintech",
      "Gaming",
      "IoT",
      "Machine Learning/AI",
      "Web"
    ]
  },
  {
    "name": "Tan Yu",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Kevin Dela Rosa",
    "title": "Full-stack developer",
    "projects": "2 projects",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Working solo",
    "skills": [
      "web",
      "machine-learning",
      "python",
      "node.js",
      "javascript"
    ],
    "interests": [
      "Blockchain",
      "AR/VR",
      "Cybersecurity",
      "Machine Learning/AI",
      "Music/Art"
    ]
  },
  {
    "name": "Adel Zaalouk",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "go",
      "amazon-web-services",
      "azure",
      "gcp",
      "kubernetes",
      "networking",
      "mobile",
      "python",
      "natural-language-processing"
    ],
    "interests": [
      "Machine Learning/AI",
      "Social Good",
      "E-commerce/Retail",
      "Education",
      "Health",
      "Music/Art",
      "Open Ended",
      "Web"
    ],
    "bio": "Engineering turned product manager turned productioneer."
  },
  {
    "name": "Armen Hacopian",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Working solo",
    "skills": [
      "java",
      "c#"
    ],
    "interests": [
      "AR/VR",
      "Machine Learning/AI",
      "Voice skills"
    ]
  },
  {
    "name": "Siddhartha Sharma",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "cloud",
      "deep",
      "learning",
      "ai",
      "amazon-web-services",
      "azure",
      "python",
      "npm",
      "linux",
      "ubuntu",
      "dotnet",
      "conda",
      "cmake",
      "c",
      "c++",
      "iot"
    ],
    "interests": [
      "Cybersecurity",
      "Databases",
      "DevOps",
      "E-commerce/Retail",
      "Education",
      "IoT",
      "Lifehacks",
      "Machine Learning/AI",
      "Music/Art",
      "Open Ended",
      "Robotic Process Automation",
      "Voice skills"
    ]
  },
  {
    "name": "Anice Charaf",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "llm",
      "flask",
      "finetuning",
      "machine-learning",
      "react",
      "angular.js",
      "android-studio"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Communication",
      "Cybersecurity",
      "Databases",
      "Design",
      "DevOps",
      "Enterprise",
      "Fintech",
      "Gaming",
      "IoT",
      "Lifehacks",
      "Machine Learning/AI",
      "Robotic Process Automation",
      "Voice skills",
      "Web"
    ]
  },
  {
    "name": "Jaisantosh A",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "rust",
      "python",
      "java",
      "golang",
      "amazon-web-services",
      "gcp",
      "react",
      "sql"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "David Zhuang",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "llm",
      "langchain",
      "pinecone"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "My name is David Zhuang, I am a software engineer, I am interested in chatbox application."
  },
  {
    "name": "Chang Yu",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "java"
    ],
    "interests": [
      "Web"
    ]
  },
  {
    "name": "Matthew Mo",
    "title": "Data science/ML Ops",
    "projects": "1 project",
    "followers": "1 follower",
    "achievements": "5 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "go",
      "pytorch",
      "tensorflow",
      "amazon-web-services",
      "aleo",
      "rust"
    ],
    "interests": [
      "DevOps",
      "Health",
      "Machine Learning/AI",
      "Open Ended",
      "Quantum",
      "Robotic Process Automation",
      "Beginner Friendly",
      "E-commerce/Retail"
    ]
  },
  {
    "name": "Nigel Scott Higgs",
    "title": "general programming",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "c",
      "c#",
      "arduino"
    ],
    "interests": [
      "Machine Learning/AI",
      "Mobile",
      "Open Ended",
      "Quantum",
      "Robotic Process Automation"
    ],
    "bio": "Hi, I'm Nigel, a senior majoring in Computer Science with a focus on AI at Oregon State University. I'm looking for teammates who have a concept they're passionate about and need help bringing it to life."
  },
  {
    "name": "Christopher Chan",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "c++",
      "python",
      "matlab"
    ]
  },
  {
    "name": "deepakrox Menghani",
    "title": "Back-end developer",
    "projects": "1 project",
    "followers": "1 follower",
    "achievements": "5 achievements",
    "team_status": "Has a team",
    "skills": [
      "machine-learning",
      "backend",
      "cloud"
    ],
    "interests": [
      "Fintech",
      "Machine Learning/AI",
      "Open Ended",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "Paritosh Kulkarni",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "pandas",
      "pytoch",
      "natural-language-processing",
      "r"
    ],
    "interests": [
      "E-commerce/Retail",
      "Machine Learning/AI",
      "Social Good",
      "Voice skills"
    ],
    "bio": "Paritosh Kulkarni, developing a personalized executive assistant for professionals, and creative individuals which writes journals and to do lists from chats, transcripts etc crested during each day. I'll use Claude or custom LLAMA-2 with RAG."
  },
  {
    "name": "Sagar Jethi",
    "projects": "11 projects",
    "followers": "10 followers",
    "achievements": "6 achievements",
    "team_status": "Working solo",
    "skills": [
      "javascript",
      "php",
      "laravel",
      "smart-contract",
      "blockchain",
      "bitcoin",
      "node.js",
      "react"
    ],
    "interests": [
      "Blockchain",
      "Communication",
      "Fintech",
      "Machine Learning/AI",
      "Productivity",
      "Voice skills"
    ]
  },
  {
    "name": "Yosun Chang",
    "title": "Mobile developer",
    "projects": "116 projects",
    "followers": "1191 followers",
    "achievements": "11 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "augmentedreality",
      "ios",
      "android",
      "unity",
      "php",
      "mysql",
      "c#",
      ".net",
      "photoshop",
      "3dsmax",
      "hardware",
      "mac",
      "web",
      "windows",
      "windows-phone",
      "java",
      "opencv",
      "c++",
      "realsense",
      "vr",
      "ar",
      "hmd",
      "shakespeare",
      "physics",
      "quantum-computing",
      "string-theory",
      "loop-theory",
      "oculus",
      "vive",
      "vuforia",
      "arkit",
      "arcloud",
      "leap-motion",
      "intel-real-sense",
      "kinect",
      "microsoft-hololens",
      "realityscript",
      "faced.io",
      "photogrammetry",
      "three.js",
      "jquery",
      "bootstrap4",
      "magic-leap",
      "windows-mixed-reality",
      "google-cardboard",
      "gearvr",
      "dlib",
      "tensorflow",
      "python",
      "webgl",
      "gpt3",
      "ai",
      "apple-vision-pro",
      "ai3d"
    ],
    "interests": [
      "Blockchain",
      "AR/VR",
      "IoT",
      "Machine Learning/AI",
      "Productivity",
      "Voice skills",
      "Design",
      "Music/Art",
      "Open Ended",
      "Quantum"
    ]
  },
  {
    "name": "tracy yu",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "product"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "E-commerce/Retail",
      "Gaming",
      "Low/No Code",
      "Machine Learning/AI",
      "Music/Art",
      "Productivity",
      "Social Good"
    ]
  },
  {
    "name": "Xian Ke",
    "title": "Full-stack developer",
    "projects": "12 projects",
    "followers": "21 followers",
    "achievements": "10 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "android",
      "ios",
      "web"
    ],
    "interests": [
      "Databases",
      "DevOps",
      "Education",
      "Health",
      "Lifehacks",
      "Machine Learning/AI",
      "Productivity",
      "Social Good",
      "Web"
    ]
  },
  {
    "name": "Wayne Chan",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "javascript",
      "typescript",
      "amazon-web-services"
    ],
    "interests": [
      "Fintech",
      "Machine Learning/AI",
      "Social Good"
    ]
  },
  {
    "name": "Private user",
    "title": "Product manager",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "product-life-cycle-support",
      "customerinsights",
      "machine"
    ],
    "interests": [
      "E-commerce/Retail",
      "Health",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Productivity"
    ]
  },
  {
    "name": "Medi M",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "javascript",
      "c++"
    ],
    "interests": [
      "Beginner Friendly",
      "Databases",
      "DevOps",
      "E-commerce/Retail",
      "Enterprise",
      "Fintech",
      "IoT",
      "Low/No Code",
      "Machine Learning/AI",
      "Open Ended",
      "Web"
    ]
  },
  {
    "name": "Manu Suryavansh",
    "projects": "2 projects",
    "followers": "9 followers",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "android",
      "javascript",
      "java",
      "python",
      "twilio",
      "intel-edison",
      "sensors",
      "hardware",
      "tensorflow",
      "pytorch"
    ],
    "interests": [
      "IoT",
      "Machine Learning/AI"
    ],
    "bio": "ML Engineer, experience building RAGs with llama-index."
  },
  {
    "name": "HANZHE LONG",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "c++",
      "react",
      "javascript",
      "ts",
      "docker",
      "amazon-web-services",
      "kubernetes",
      "pinecone"
    ],
    "interests": [
      "Web"
    ],
    "bio": "Creator of NewsGPT, a ChatGPT like Q&A application enabling you to ask questions about recent news. (Tech stack: Django, Redis, Celery, Kafka, Docker, AWS, Pinecone, LangChain, Streamlit) Here's the link: http://newsgpt-lb-1480397016.us-east-2.elb.amazonaws.com:8501/"
  },
  {
    "name": "Howard Gil",
    "projects": "8 projects",
    "followers": "1 follower",
    "achievements": "8 achievements",
    "team_status": "Has a team"
  },
  {
    "name": "Sung Kim",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "python"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Balaji Viswanathan",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "figma",
      "ros"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "CS PhD (thesis in Human Robot Interaction). Ex-Microsoft. Founder@MitraRobot."
  },
  {
    "name": "Benjamin Bimanywaruhanga",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "python",
      "opencv"
    ],
    "interests": [
      "Blockchain",
      "Machine Learning/AI",
      "Social Good",
      "Voice skills"
    ]
  },
  {
    "name": "Solomon Wang",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "1 follower",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "javascript",
      "java",
      "jquery",
      "css",
      "node.js",
      "python"
    ],
    "interests": [
      "AR/VR",
      "Communication",
      "Cybersecurity",
      "Databases",
      "Design",
      "DevOps",
      "Education",
      "Enterprise",
      "Fintech",
      "Health",
      "IoT",
      "Machine Learning/AI",
      "Productivity",
      "Quantum",
      "Robotic Process Automation",
      "Social Good"
    ],
    "bio": "AI/ML Ex-FB/Bing and Serial SAAS Entrepreneur"
  },
  {
    "name": "Andrew Pang",
    "title": "Mobile developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "ios",
      "android"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "I'm a Product Manager that has also been a mobile engineer for 5+ years, I can code and design"
  },
  {
    "name": "Raymond Lee",
    "projects": "1 project",
    "followers": "4 followers",
    "achievements": "5 achievements",
    "team_status": "Working solo",
    "skills": [
      "python",
      "sql",
      "google-cloud",
      "amazon-web-services",
      "scikit-learn",
      "keras",
      "tensorflow",
      "pytorch",
      "machine-learning"
    ],
    "interests": [
      "Fintech",
      "Machine Learning/AI",
      "Productivity",
      "Social Good"
    ]
  },
  {
    "name": "Gary Guo",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "java",
      "sql",
      "node.js",
      "mysql",
      "r",
      "python"
    ],
    "interests": [
      "Databases",
      "E-commerce/Retail",
      "Machine Learning/AI",
      "Mobile",
      "Web"
    ]
  },
  {
    "name": "Jonathan Sweeney",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "Skilled in Python, full stack ML, worked in finance and legal tech, interested in personalized AI."
  },
  {
    "name": "Robert H Lee",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "pytoch",
      "pandas",
      "tables",
      "r"
    ],
    "interests": [
      "Education",
      "Health",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Social Good"
    ]
  },
  {
    "name": "Dom Steil",
    "title": "Full-stack developer",
    "projects": "11 projects",
    "followers": "14 followers",
    "achievements": "9 achievements",
    "team_status": "Working solo",
    "skills": [
      "javascript",
      "blockchain",
      "visualforce",
      "apex",
      "ethereum",
      "bitcoin",
      "lightning",
      "unity",
      "c#",
      "angular.js",
      "node-red",
      "web3",
      "botkit",
      "bot-builder",
      "serverless",
      "hyperledger-fabric",
      "composer-client",
      "claudia.js",
      "amazon-web-services",
      "luis",
      "prolog",
      "kotlin",
      "corda",
      "ngrok",
      "gcp",
      "go",
      "cosmos-sdk",
      "tailwind",
      "nextjs"
    ],
    "interests": [
      "Blockchain"
    ]
  },
  {
    "name": "Alexander Pena",
    "title": "Front-end developer",
    "projects": "2 projects",
    "followers": "2 followers",
    "achievements": "6 achievements",
    "team_status": "Has a team",
    "skills": [
      "javascript"
    ],
    "interests": [
      "Beginner Friendly",
      "Blockchain",
      "Cybersecurity"
    ]
  },
  {
    "name": "SitingT Tang",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "javascript",
      "typescript",
      "java",
      "python"
    ],
    "interests": [
      "Blockchain",
      "Databases",
      "Design",
      "Fintech",
      "Machine Learning/AI",
      "Web"
    ]
  },
  {
    "name": "Georgi Dagnall",
    "title": "Full-stack developer",
    "projects": "2 projects",
    "followers": "0 followers",
    "achievements": "5 achievements",
    "team_status": "Working solo",
    "skills": [
      "android",
      "ios",
      "java",
      "kotlin",
      "javascript",
      "ajax",
      "sql",
      "sqlite",
      "amazon-web-services"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Communication",
      "Cybersecurity",
      "Design",
      "DevOps",
      "E-commerce/Retail",
      "Education",
      "Enterprise",
      "Machine Learning/AI",
      "Mobile",
      "Open Ended",
      "Productivity",
      "Quantum",
      "Web"
    ]
  },
  {
    "name": "Vineet Shah",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "1 follower",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "ai",
      "machine-learning"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Sean Javiya",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "git",
      "c++",
      "java",
      "kotlin",
      "python",
      "html",
      "css",
      "docker",
      "gradle",
      "x86-64",
      "qualtrics",
      "pascal",
      "bash",
      "linux",
      "ios",
      "android",
      "mac-os-x",
      "windows",
      "ms-office(including-excel)"
    ],
    "interests": [
      "Machine Learning/AI",
      "Open Ended"
    ]
  },
  {
    "name": "Roey Ben Chaim",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "backend",
      "frontend",
      "react",
      "ml",
      "ai"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Cybersecurity",
      "DevOps",
      "Fintech",
      "IoT",
      "Quantum",
      "Social Good"
    ]
  },
  {
    "name": "Kevin Leffew",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "replit",
      "ai",
      "rag",
      "object"
    ],
    "interests": [
      "Blockchain"
    ]
  },
  {
    "name": "NadiaAnwar121 Nadia Anwar",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "machine-learning",
      "natural-language-processing",
      "deep-learning",
      "computer-vision"
    ],
    "interests": [
      "Beginner Friendly",
      "Communication",
      "Databases",
      "Education",
      "Machine Learning/AI",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "Jacob Somer",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "5 achievements",
    "team_status": "Working solo",
    "skills": [
      "python"
    ],
    "interests": [
      "E-commerce/Retail",
      "Fintech",
      "Machine Learning/AI",
      "Web"
    ]
  },
  {
    "name": "Sushant Dahal",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "security",
      "python",
      "react",
      "javascript",
      "amazon-web-services",
      "gcp",
      "openai",
      "fastapi",
      "flask",
      "node.js",
      "typescript",
      "serverless",
      "sql"
    ],
    "interests": [
      "Cybersecurity",
      "Databases",
      "Enterprise",
      "Fintech",
      "IoT",
      "Machine Learning/AI",
      "Web"
    ],
    "bio": "Experienced in building automation at scale . I have been working on RAG applications and data driven automation leveraging LLM. Looking for partner to help integrate AI/ML further into solving security and modern day software development challenges"
  },
  {
    "name": "Amanda Piyapanee",
    "title": "Data scientist",
    "projects": "3 projects",
    "followers": "5 followers",
    "achievements": "7 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "java",
      "c",
      "swift",
      "sql"
    ],
    "interests": [
      "Health",
      "Machine Learning/AI",
      "Quantum",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "Sam caraliu",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "node.js",
      "php",
      "html5",
      "javascript"
    ],
    "interests": [
      "E-commerce/Retail",
      "Low/No Code",
      "Machine Learning/AI",
      "Robotic Process Automation",
      "Web"
    ]
  },
  {
    "name": "Zahidul Islam",
    "projects": "4 projects",
    "followers": "5 followers",
    "achievements": "8 achievements",
    "team_status": "Has a team",
    "skills": [
      "javascript",
      "node.js",
      "chatbot",
      "natural-language-processing"
    ]
  },
  {
    "name": "Vinit Mankar",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Has a team",
    "skills": [
      "product-design",
      "ux",
      "ui",
      "frontend",
      "unity"
    ],
    "interests": [
      "AR/VR",
      "Communication",
      "IoT",
      "Lifehacks",
      "Productivity",
      "Social Good",
      "Voice skills"
    ]
  },
  {
    "name": "WenyuP Pan",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "java",
      "typescript",
      "javascript",
      "python",
      "c",
      "c++",
      "sql",
      "react.js",
      "redux",
      "graphql",
      "angular.js",
      "html",
      "css",
      "tailwind",
      "jest.js",
      "spring",
      "springmvc",
      "junit",
      "node.js",
      "express.js",
      "microservices",
      "docker",
      "redis",
      "mongodb",
      "mysql",
      "oauth2",
      "amazon-web-services",
      "ec2",
      "cloudwatch",
      "rds",
      "cloudformation",
      "gcp",
      "kubernetes",
      "nats",
      "scaffold",
      "git",
      "github",
      "ssh",
      "linux",
      "postman",
      "sha-256",
      "https",
      "cors",
      "grafana",
      "google",
      "agile-scrum",
      "ctk",
      "stk",
      "ai",
      "machine-learning"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Blockchain",
      "Communication",
      "Cybersecurity",
      "Databases",
      "Design",
      "DevOps",
      "E-commerce/Retail",
      "Education",
      "Enterprise",
      "Fintech",
      "Gaming",
      "Health",
      "IoT",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Mobile",
      "Music/Art",
      "Open Ended",
      "Productivity",
      "Quantum",
      "Robotic Process Automation",
      "Social Good",
      "Voice skills",
      "Web"
    ],
    "bio": "Hi, my name is Wenyu Pan and I am a 2nd-year Master's student majoring in CS at Northeastern University. I am graduating in the upcoming spring of 2024. I love coding, especially pair-coding with friends and peers"
  },
  {
    "name": "Jinxin Hu",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "java",
      "javascript",
      "css",
      "html5"
    ],
    "interests": [
      "Databases",
      "Fintech",
      "Machine Learning/AI",
      "Web"
    ]
  },
  {
    "name": "Romain Lopez",
    "title": "I am a researcher in AI and computational biology.",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates"
  },
  {
    "name": "AKASH MITTAL",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Has a team",
    "skills": [
      "machine-learning",
      "gnn",
      "recommender"
    ],
    "interests": [
      "E-commerce/Retail",
      "Education",
      "Health",
      "IoT",
      "Machine Learning/AI",
      "Mobile",
      "Social Good"
    ]
  },
  {
    "name": "Mantek Singh",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "c++",
      "llm",
      "ai",
      "ml"
    ],
    "interests": [
      "Beginner Friendly",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Gagan Ganapathy",
    "projects": "1 project",
    "followers": "4 followers",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "react",
      "javascript",
      "python",
      "c++",
      "machine-learning",
      "firebase",
      "graphql"
    ]
  },
  {
    "name": "Konrad Gnat",
    "title": "Full-stack developer",
    "projects": "16 projects",
    "followers": "11 followers",
    "achievements": "9 achievements",
    "team_status": "Working solo",
    "skills": [
      "javascript",
      "react",
      "node.js",
      "java",
      "swift",
      "php"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Machine Learning/AI",
      "Music/Art"
    ]
  },
  {
    "name": "siddhant kochrekar",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "natural-language-processing",
      "c",
      "c++",
      "sql",
      "sqlite",
      "sqlalchemy",
      "r",
      "matlab",
      "opencv",
      "mysql",
      "postgresql",
      "amazon-dynamodb",
      "redis",
      "mongodb",
      "pandas",
      "pytorch",
      "scipy",
      "scikit-learn",
      "raspberry-pi",
      "arduino",
      "llm",
      "langchain",
      "llamaindex"
    ],
    "interests": [
      "Machine Learning/AI",
      "AR/VR",
      "E-commerce/Retail",
      "Fintech",
      "Gaming",
      "Health",
      "IoT",
      "Open Ended"
    ],
    "bio": "I have an industrial experience ~5 years as a Data Scientist in Lending, Buy-Now-Pay-Later, Cloud Gaming, and the Cognitive Science space. I have been working on RAG applications for a couple of months now. Looking forward to teaming up with great minds at the hackathon."
  },
  {
    "name": "Meenakshi K",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "llm"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Divija N",
    "projects": "2 projects",
    "followers": "0 followers",
    "achievements": "6 achievements",
    "team_status": "Looking for teammates"
  },
  {
    "name": "Devansh Shah",
    "title": "Machine Learning Engineer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "pytorch",
      "tensorflow",
      "python",
      "ml",
      "mlops"
    ],
    "interests": [
      "Databases",
      "Machine Learning/AI"
    ],
    "bio": "I am an Applied Scientist at Amazon. I bring forth strong machine learning, LLM foundation knowledge, and ml infra skills."
  },
  {
    "name": "Nilay Pochhi",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "pytorch",
      "rag",
      "pinecone"
    ],
    "interests": [
      "Low/No Code",
      "Machine Learning/AI",
      "Productivity",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "Vamsi Bedapudi",
    "title": "AI",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "llm"
    ],
    "interests": [
      "Beginner Friendly",
      "Communication",
      "Cybersecurity",
      "Databases",
      "E-commerce/Retail",
      "Enterprise",
      "Fintech",
      "Machine Learning/AI",
      "Music/Art",
      "Open Ended"
    ]
  },
  {
    "name": "Mona Mahmoudi",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "ml",
      "python"
    ],
    "interests": [
      "Health",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Dmytro Filatov",
    "projects": "2 projects",
    "followers": "3 followers",
    "achievements": "4 achievements",
    "team_status": "Working solo",
    "skills": [
      "android",
      "javascript",
      "ios",
      "css",
      "ruby-on-rails",
      "html5",
      "quickblox",
      "java",
      "jquery",
      "python",
      "twilio"
    ]
  },
  {
    "name": "Jerry J",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python"
    ],
    "interests": [
      "Machine Learning/AI",
      "Databases",
      "E-commerce/Retail",
      "Social Good"
    ],
    "bio": "hey, this is Jiri, I am a AI lover, worked in Ai for multiple years."
  },
  {
    "name": "Chen Yu",
    "title": "Designer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "design"
    ],
    "interests": [
      "Music/Art",
      "Design tool"
    ]
  },
  {
    "name": "Ali Ahmed",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "java",
      "python",
      "kafka"
    ],
    "interests": [
      "Databases"
    ]
  },
  {
    "name": "Balaji xb02",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "python",
      "c",
      "terraform"
    ],
    "interests": [
      "DevOps",
      "Productivity"
    ]
  },
  {
    "name": "Vishal Pugazhendhi",
    "title": "Full-stack developer",
    "projects": "3 projects",
    "followers": "4 followers",
    "achievements": "8 achievements",
    "team_status": "Working solo",
    "skills": [
      "react",
      "flutter",
      "java",
      "python",
      "javascript"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Mobile",
      "Web",
      "Beginner Friendly"
    ]
  },
  {
    "name": "Hunter Whitney",
    "title": "Designer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "ux",
      "writing",
      "journalism"
    ],
    "interests": [
      "AR/VR",
      "Communication",
      "Design",
      "Education",
      "Health",
      "Low/No Code",
      "Machine Learning/AI",
      "Open Ended"
    ],
    "bio": "I am interested in working on a team that has an interest in human-centered design."
  },
  {
    "name": "Mengdi Huang",
    "title": "Full-stack developer",
    "projects": "4 projects",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Working solo",
    "skills": [
      "ai"
    ],
    "interests": [
      "Databases",
      "DevOps",
      "Enterprise",
      "Fintech",
      "Health",
      "IoT",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Music/Art",
      "Open Ended",
      "Productivity"
    ]
  },
  {
    "name": "Jin Liu",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "node.js",
      "java"
    ],
    "interests": [
      "Databases",
      "DevOps",
      "Enterprise",
      "Health",
      "IoT",
      "Machine Learning/AI",
      "Web"
    ]
  },
  {
    "name": "Parvez Akhtar",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "node.js",
      "openai",
      "langchain",
      "flowise"
    ],
    "interests": [
      "AR/VR"
    ],
    "bio": "I am looking to work on RAGs that take up medical prescriptions and change it to more structures way so that I notify my grandpa for his medicines."
  },
  {
    "name": "Abhishek Thakur",
    "title": "Data scientist",
    "projects": "1 project",
    "followers": "1 follower",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "c++"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "huijun wu",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python"
    ],
    "interests": [
      "Beginner Friendly",
      "Communication",
      "Databases",
      "Machine Learning/AI",
      "Beginner Eng"
    ]
  },
  {
    "name": "Xuexi Ai",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "2 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "coding",
      "ml"
    ],
    "interests": [
      "Machine Learning/AI",
      "I ai Xuexi."
    ]
  },
  {
    "name": "Yang Pei",
    "title": "Back-end developer",
    "projects": "3 projects",
    "followers": "8 followers",
    "achievements": "5 achievements",
    "team_status": "Has a team",
    "skills": [
      "python",
      "machine-learning",
      "llm",
      "recommendation-system"
    ],
    "interests": [
      "Beginner Friendly",
      "E-commerce/Retail",
      "Fintech",
      "Gaming",
      "Health",
      "Machine Learning/AI",
      "Productivity"
    ]
  },
  {
    "name": "Wendy Ran Wei",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "3 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "machine-learning",
      "llm",
      "data",
      "data-mining",
      "python",
      "natural-language-processing",
      "ai"
    ],
    "interests": [
      "E-commerce/Retail",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Riya Jagetia",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "ux",
      "prds",
      "front-end",
      "design",
      "strategy",
      "storytelling",
      "market"
    ],
    "interests": [
      "Enterprise",
      "Fintech",
      "Lifehacks",
      "Machine Learning/AI",
      "Robotic Process Automation"
    ],
    "bio": "Hi, I'm Riya - an MIT CS grad working in AI/ ML! Looking forward to playing around with some new tools at this hackathon! My idea is to build a chatbot that can serve as a Trevor Project counselor. The Trevor Project is a organization based in the US that aims to eradicate suicide among LGBTQ+ youth, and I'm currently training to be a counselor (i.e. a volunteer who responds to incoming texts/ messages/ calls from youth in crisis). Training takes 10 weeks and 5-10 hours of studying per week, and once I'm a counselor, I'm supposed to follow some very strict guidelines on how to talk to and guide youth who are in crisis. While doing the training, I've often thought about how nice it would be if I had an LLM to help me -- suggest responses, resources, etc. -- so that I could be more effective, because right now, I have a bunch of tabs open with resources. Will be hacking on this alone if needed, but would love some help from anyone interested in working together!"
  },
  {
    "name": "Eric Saund",
    "title": "Cognitive Architecture",
    "projects": "1 project",
    "followers": "1 follower",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "android",
      "javascript",
      "java",
      "html5",
      "python"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "Are you looking for better chunking of pdf documents? I developed some logical structure parsing for certain types of pdfs. I am seeking more use cases to test it on, and extend capabilities. See https://devpost.com/software/pdflogical."
  },
  {
    "name": "Journalwere Chen",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "3 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "sql",
      "bash",
      "linux",
      "html5",
      "css",
      "javascript",
      "django",
      "flask",
      "postgresql",
      "kali"
    ],
    "interests": [
      "Blockchain",
      "Cybersecurity",
      "Databases",
      "IoT",
      "Machine Learning/AI",
      "Quantum",
      "Robotic Process Automation",
      "Web"
    ],
    "bio": "I'm very passionate about building coding project, and with some coding experience. I'm looking for anyone who wants to find a teammate"
  },
  {
    "name": "debabrata pattnayak",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Working solo"
  },
  {
    "name": "Sumanth Sathyanarayana",
    "title": "Back-end developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "3 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "go"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Blockchain",
      "Communication",
      "Cybersecurity",
      "Databases",
      "Design",
      "DevOps",
      "E-commerce/Retail",
      "Education",
      "Enterprise",
      "Fintech",
      "Gaming",
      "Health",
      "IoT",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Music/Art",
      "Open Ended",
      "Productivity",
      "Quantum",
      "Robotic Process Automation",
      "Social Good",
      "Voice skills",
      "Web"
    ]
  },
  {
    "name": "tanmeshnm Mishra",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "react",
      "react-native",
      "java",
      "backend",
      "frontend"
    ],
    "interests": [
      "Beginner Friendly",
      "Design",
      "E-commerce/Retail",
      "Mobile",
      "Productivity",
      "Social Good",
      "Web"
    ]
  },
  {
    "name": "qihuang xie",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "r",
      "business",
      "strategy",
      "product"
    ],
    "interests": [
      "Health",
      "Machine Learning/AI"
    ],
    "bio": "Hi guys! Qihuang here! I am a healthcare student from Singapore interested in digital health and innovation in healthcare. I have experience building and evaluating some RAG based model for healthcare use case during my free time!"
  },
  {
    "name": "Ming-yeung Lee",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "1 follower",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "pandas",
      "scikit-learn",
      "jenkins",
      "golang",
      "typescript",
      "java"
    ],
    "interests": [
      "DevOps",
      "Lifehacks",
      "Machine Learning/AI",
      "Open Ended",
      "Productivity",
      "Social Good"
    ],
    "bio": "Let's build a local-first personal knowledge management system with LlamaIndex.\u3011 Keen on personal knowledge management. Blog posts reached #1 on Hacker News 2x. I wrote the \"why LlamaIndex\" section on docs.llamaindex.ai. Frequently seen on LlamaIndex Discord. Focused on democratizing RAG technology for offline chatbot & agents."
  },
  {
    "name": "Anar Taori",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "usecases",
      "machine-learning",
      "enterprise",
      "saas",
      "b2c",
      "product",
      "strategy",
      "business-models",
      "consumer",
      "b2b",
      "python-programming",
      "problem-solving",
      "ideation",
      "design",
      "mobile"
    ],
    "interests": [
      "Cybersecurity",
      "Design",
      "E-commerce/Retail",
      "Enterprise",
      "Fintech",
      "Health",
      "Machine Learning/AI",
      "Mobile",
      "Productivity",
      "Robotic Process Automation",
      "Voice skills",
      "Web",
      "DevOps",
      "Social Good"
    ],
    "bio": "I am a product management leader with experience building successful 0 to 1 products at startups and F500 companies. I am trained in AI/ML/LLMs and have some ideas on what we could build, I am also open to other ideas and combined brainstorming. I am looking for a teammate with complementary skills - someone who is technical, has software development expertise specifically in Python and machine learning. This will nicely complement my business and product skills. More details about me are at www.linkedin.com/in/anartaori"
  },
  {
    "name": "Welintong Cabascango",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python"
    ],
    "interests": [
      "Cybersecurity",
      "Education",
      "Quantum"
    ]
  },
  {
    "name": "SVET Rating",
    "title": "Investor",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "solidity",
      "python"
    ],
    "interests": [
      "Blockchain",
      "Fintech",
      "Gaming"
    ]
  },
  {
    "name": "Evan Dang",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "java",
      "design",
      "website"
    ],
    "interests": [
      "Design",
      "Machine Learning/AI",
      "Open Ended",
      "Productivity",
      "Web"
    ]
  },
  {
    "name": "Anh Tran",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "automation",
      "business",
      "strategy"
    ],
    "interests": [
      "AR/VR",
      "Communication",
      "Databases",
      "Fintech",
      "Health",
      "Quantum",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "Salvador Salcedo",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "6 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "javascript",
      "react",
      "node.js",
      "java",
      "c++"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Blockchain",
      "Design",
      "Open Ended",
      "Web"
    ],
    "bio": "SoCal to UC Berkeley, Applied Math transfer. Looking to work on implementing office document workflows into LLM actionable tasks for review and execution. Particularly interested in construction documentation workflow."
  },
  {
    "name": "Arka Bagchi",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "scikit-learn",
      "rag",
      "a/b",
      "llmops",
      "cot",
      "hugginface",
      "sql",
      "pandas",
      "scipy",
      "matplotlib",
      "seaborn",
      "langchain",
      "pydantic",
      "llamaindex",
      "weaviate",
      "pgvector",
      "gradio"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Farshad Movahed",
    "title": "Strategic Alliances Manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "rag",
      "llm",
      "inference",
      "fine-tuning"
    ],
    "interests": [
      "Communication",
      "Lifehacks",
      "Machine Learning/AI",
      "Productivity"
    ],
    "bio": "I'm a Strategic Alliances Manager at NVIDIA specializing in RAG systems and LLMs. I'd like to build a team with people with whom I can build a multi-modal RAG application."
  },
  {
    "name": "Darryl Grier",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "javascript",
      "sql",
      "search",
      "react"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Blockchain",
      "Communication",
      "Databases",
      "Education",
      "Enterprise",
      "Fintech",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Mobile",
      "Open Ended",
      "Social Good",
      "Web"
    ]
  },
  {
    "name": "Gaurav Kamdar",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Mrunmayee Dhapre",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "sql",
      "azure",
      "llm",
      "rag",
      "bigdata"
    ],
    "interests": [
      "Databases",
      "DevOps",
      "Enterprise",
      "Fintech",
      "IoT",
      "Machine Learning/AI",
      "Web"
    ],
    "bio": "Hi, I am a novice at Gen AI. Worked on a RAG project with LangChain."
  },
  {
    "name": "Charles Tung",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "javascript",
      "ios",
      "html5",
      "python"
    ]
  },
  {
    "name": "Homen Shum",
    "title": "Full-stack developer",
    "projects": "3 projects",
    "followers": "1 follower",
    "achievements": "7 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "c++",
      "python",
      "rag",
      "llamaindex",
      "ray",
      "async",
      "data",
      "pandas",
      "numpy"
    ],
    "interests": [
      "Fintech",
      "Health",
      "Social Good",
      "Databases",
      "Machine Learning/AI",
      "Productivity",
      "Voice skills",
      "Communication",
      "Design",
      "E-commerce/Retail",
      "Web"
    ],
    "bio": "A Journey of Growth: From San Francisco to Beijing and Beyond My journey began in the vibrant city of San Francisco, but at the tender age of three, my life took a turn eastward to Beijing, where I lived with my grandparents. These early years were foundational, as my grandfather instilled in me the importance of diving deep into my passions and understanding the consequences of my choices. By four, I unearthed a natural talent for strategy, a skill that led me to clinch a regional championship in Go. My artistic side also flourished, culminating in becoming the lead YangQin performer at my school by eleven. My return to San Francisco presented new challenges, including a battle with obesity, which I overcame by shedding 70 lbs through disciplined training. In high school and college, my leadership drove teams to win in investment competitions, CAPSIM, and hackathons. Now, in my banking career, I blend these experiences with my passion for technology. I innovate in machine learning and artificial intelligence, developing automation tools that not only streamline workflows but also enhance productivity. What sets my approach apart in banking is my focus on the human element. I delve deep into understanding founders and investors, grasping not only their technological approach, but also their vision and mission. This insight is critical in fostering and establishing fruitful relationships, ensuring a harmonious alignment of goals and expectations. Sharing Excellence: A Curated Tech Perspective As a final note, I am discerning in what I share and repost. The materials you see on my profile are not just random selections; they represent the cr\u00e8me de la cr\u00e8me of the tech world, carefully chosen for their excellence and relevance to my work. These are the solutions that I believe in and use, reflecting the high standards I uphold in both my professional and personal endeavors. My Latest Web Applications: Medical Code Search and Report Generation: https://www.youtube.com/watch?v=qO6HbByOOCI Patient Screening Chat and Report Generation: https://cosmaneura-patient-screening-demo.streamlit.app/ Auto Shop E-Commerce RAG Chat App: https://clickcar-sales-assistant.streamlit.app/ Banker's Prospecting Assistant App: https://banking-assistant-vhs2.streamlit.app/"
  },
  {
    "name": "Mckenzie Prince",
    "title": "Front-end developer",
    "projects": "4 projects",
    "followers": "1 follower",
    "achievements": "5 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "angular.js",
      "flutter",
      "vertexai",
      "python",
      "r",
      "tensorflow",
      "llamaindex",
      "machine-learning",
      "firebase"
    ],
    "interests": [
      "Education",
      "Mobile",
      "Web"
    ],
    "bio": "I'm a Master's student in Computer Science at the University of Texas at Tyler. Would love to team up with anyone who is willing to work for pretty much the entire duration of the Hackathon. Software Development, Machine Learning, Data Analytics are my areas of expertise, and I have also used Gen AI technologies for my projects and hackathons. Won 2 out of the 3 hackathons I have been part of - won overall in the HackUNC (North Carolina), best use of AI in education and Google Cloud's Best use of Generative AI at AI ATL (Georgia Tech - Atlanta). Hoping to win again"
  },
  {
    "name": "Kevin Verre",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "javascript",
      "databases"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Blockchain",
      "Cybersecurity",
      "Databases",
      "DevOps",
      "Education",
      "Enterprise",
      "Fintech",
      "Health",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Mobile",
      "Music/Art",
      "Open Ended",
      "Social Good",
      "Voice skills",
      "Web"
    ],
    "bio": "I'm a software engineer, with experience in full-stack web development. I am interested in things like: computer programming, making the world a better place, education, psychology, finance, business, sports, gaming, and music."
  },
  {
    "name": "Dino Ilievski",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "linkedin"
    ],
    "interests": [
      "AR/VR",
      "E-commerce/Retail",
      "Machine Learning/AI",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "K. Tuba T\u00fcrkcan",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "pytorch",
      "chatbot",
      "sqlalchemy",
      "sql",
      "api",
      "java",
      "html5",
      "css",
      "pandas",
      "scikit-learn",
      "machine-learning",
      "ai",
      "natural-language-processing"
    ],
    "interests": [
      "Beginner Friendly",
      "Machine Learning/AI"
    ],
    "bio": "Hello! I'm Tuba. I live in Einsiedeln. Since 2019, I have been learning and improving myself about Python, Data Science, Coding, Machine Learning , Deep Learning, Generative AI, CNN. Finally, since last June, I have been dealing with Llama Index."
  },
  {
    "name": "Barun Amalkumar Halder",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "python",
      "java",
      "c"
    ]
  },
  {
    "name": "ttitans4ever banerjee",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "ai"
    ],
    "interests": [
      "Machine Learning/AI",
      "Idea TBD"
    ]
  },
  {
    "name": "Phuoc Bui",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "pytorch",
      "llamaindex"
    ],
    "interests": [
      "Communication",
      "Cybersecurity",
      "Education",
      "IoT",
      "Low/No Code",
      "Machine Learning/AI",
      "Productivity"
    ]
  },
  {
    "name": "Krishna Manchikalapudi",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "api",
      "microsee",
      "devops",
      "mlops"
    ],
    "interests": [
      "Beginner Friendly",
      "Databases",
      "Design",
      "DevOps",
      "Education",
      "Enterprise",
      "Fintech",
      "Health",
      "Lifehacks",
      "Low/No Code",
      "Machine Learning/AI",
      "Open Ended",
      "Productivity",
      "Web"
    ]
  },
  {
    "name": "Aditya Bahl",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "machine-learning",
      "natural-language-processing",
      "ai-safety"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "Hi my name is Aditya Bahl, looking forward to this event! :) Here is my Linkedin for reference: https://www.linkedin.com/in/aditya-bahl-b03947ab/"
  },
  {
    "name": "Shrey Jain",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "machine-learning"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Shalini Ananda",
    "title": "Data scientist",
    "projects": "4 projects",
    "followers": "1 follower",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python"
    ],
    "interests": [
      "AR/VR",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Indar Kumar",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "machine-learning",
      "python"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Charlie Davidmann",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "llm",
      "rag",
      "javascript",
      "jsx"
    ],
    "interests": [
      "Databases",
      "Fintech",
      "IoT",
      "Machine Learning/AI",
      "Open Ended",
      "Productivity",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "J\u00e9r\u00e9mie Kalonji",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "ml",
      "finance",
      "api",
      "llm"
    ],
    "interests": [
      "Education",
      "Health",
      "Machine Learning/AI",
      "Open Ended",
      "Productivity",
      "Social Good"
    ],
    "bio": "I am passionate about the possibilities that RAGs offer. My main reason is: I absolutely hate spending time looking for information. RAGs tackle this. Less search, more execution."
  },
  {
    "name": "Joseph Socarras",
    "title": "Product owner",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "data"
    ],
    "interests": [
      "Blockchain",
      "Cybersecurity",
      "Databases",
      "Design",
      "DevOps",
      "E-commerce/Retail",
      "Enterprise",
      "Fintech",
      "Gaming",
      "Health",
      "IoT",
      "Low/No Code",
      "Machine Learning/AI",
      "Mobile",
      "Music/Art",
      "Open Ended",
      "Productivity",
      "Quantum",
      "Robotic Process Automation",
      "Social Good",
      "Voice skills",
      "Web"
    ]
  },
  {
    "name": "Carlos Mastrangelo",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "blockchain",
      "machine-learning",
      "finance"
    ],
    "interests": [
      "Beginner Friendly",
      "Blockchain",
      "Databases",
      "Design",
      "Education",
      "Gaming",
      "Health",
      "Machine Learning/AI",
      "Robotic Process Automation"
    ],
    "bio": "I am a software developer with 10+ years of experience. Working on data-science and machine learning applications"
  },
  {
    "name": "Anna Matlin",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "sql",
      "a/b"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "Hi there, I'm Anna. I've been a data scientist for more than 6 years. I recently started doing some RAG / fine-tuning in my day to day. I'll prepare some ideas in advance of the hackathon!"
  },
  {
    "name": "Atif Ghogha",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "tensorflow",
      "pytorch",
      "machine",
      "learning"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "praveenhm maya",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "rust"
    ],
    "interests": [
      "DevOps",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Joshua Gotto",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "legal",
      "mandarin"
    ],
    "interests": [
      "Beginner Friendly",
      "Communication",
      "E-commerce/Retail",
      "Fintech",
      "Low/No Code",
      "Social Good",
      "Web"
    ]
  },
  {
    "name": "Abhinav Balasubramanian",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python"
    ],
    "interests": [
      "Design",
      "DevOps",
      "Machine Learning/AI",
      "Web"
    ],
    "bio": "I am a full stack engineer looking for a team. Interested to work and learn more about llama index"
  },
  {
    "name": "jjacob Ji",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python"
    ],
    "interests": [
      "Beginner Friendly",
      "Databases",
      "E-commerce/Retail",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Viacheslav Zhenylenko",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "amazon-web-services",
      "machine-learning",
      "ai",
      "llm",
      "langchain",
      "llamaindex"
    ],
    "interests": [
      "Machine Learning/AI",
      "Open Ended",
      "Productivity",
      "Quantum",
      "Robotic Process Automation"
    ],
    "bio": "Full-stack Python developer with experience in AI, particularly in LLMs. Competencies include developing backend and data engineering processes from scratch (0 to 1) and establishing and running ML pipelines. Seeking teammates for brainstorming ideas and collaboratively developing solution. Linkedin: https://www.linkedin.com/in/viacheslav-zhenylenko/"
  },
  {
    "name": "Sai vamsi Pujari",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates"
  },
  {
    "name": "Steven Lee",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "pytorch"
    ],
    "interests": [
      "Beginner Friendly",
      "DevOps",
      "Education",
      "Fintech",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "shao-shuai Shao",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "javascript",
      "typescript",
      "sql"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "Hi, my name is Shuai. I am working on RAG with patent text, the idea is building a RAG app that can help both engineers and patent practitioners. Engineers normally do patent search to find technical solutions in their domain, as well as just seaching ideas for inspiration. Patent practitioners normally search patent to locate prior art, which help them evaluate the novelty of invention of their cases. Therefore, being able to build a RAG app for patent search with pricision and quickness would benefit both engineers and patent practitioners."
  },
  {
    "name": "Adarsh Nagesh",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "flask"
    ],
    "interests": [
      "Beginner Friendly",
      "Databases",
      "Open Ended"
    ],
    "bio": "I am Adarsh - I work at Uber. I won an internal hack at Uber and am interested to take place in other hacks."
  },
  {
    "name": "Kody Low",
    "title": "Full-stack developer",
    "projects": "3 projects",
    "followers": "0 followers",
    "achievements": "8 achievements",
    "team_status": "Working solo",
    "skills": [
      "javascript",
      "react",
      "node.js"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Fintech",
      "Gaming",
      "Open Ended",
      "Web"
    ]
  },
  {
    "name": "Max Luis Felipe Levill Fl\u00e1ndez",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "llm",
      "langchain",
      "openai"
    ],
    "interests": [
      "Beginner Friendly",
      "Machine Learning/AI"
    ],
    "bio": "Soy ingeniero matem\u00e1tico y desarrollador. Busco m\u00e1s compa\u00f1eros desarrolladores"
  },
  {
    "name": "Sandeep Suresh",
    "title": "Back-end developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "postgresql",
      "react",
      "api"
    ],
    "interests": [
      "AR/VR",
      "Machine Learning/AI"
    ],
    "bio": "My name is Sandeep! I've been a backend engineer and have created APIs and dev tools that have scales to millions is users!"
  },
  {
    "name": "Alex Paiz",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "machine-learning",
      "natural-language-processing",
      "reinforcement-learning"
    ],
    "interests": [
      "E-commerce/Retail",
      "Gaming",
      "Lifehacks",
      "Machine Learning/AI",
      "Music/Art",
      "Voice skills"
    ]
  },
  {
    "name": "Christos Magganas",
    "title": "Machine Learning Engineer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "sql",
      "pytorch",
      "flask",
      "fastapi",
      "tensorflow"
    ],
    "interests": [
      "Education",
      "Machine Learning/AI",
      "Music/Art",
      "Productivity"
    ],
    "bio": "Looking to create a mentor/coach style agent that can help me with my day-to-day developer time management and ideation. Also interested in joining other teams (Education, Automation, Music, Technology) I am a pretty easy-going MLE generalist."
  },
  {
    "name": "Sahil Jain",
    "projects": "3 projects",
    "followers": "3 followers",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "android",
      "javascript",
      "php",
      "java",
      "ios",
      "css",
      "html5",
      "python"
    ]
  },
  {
    "name": "Yash Jain",
    "title": "Back-end developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "5 achievements",
    "team_status": "Working solo",
    "skills": [
      "react"
    ],
    "interests": [
      "Beginner Friendly",
      "Blockchain"
    ]
  },
  {
    "name": "Sathiskumar Jothi",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "r",
      "machine-learning",
      "sql",
      "gcp"
    ],
    "interests": [
      "Cybersecurity",
      "Databases",
      "DevOps",
      "E-commerce/Retail",
      "Health",
      "IoT",
      "Machine Learning/AI",
      "Quantum"
    ]
  },
  {
    "name": "Loc Nguyen",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python"
    ],
    "interests": [
      "Fintech",
      "Health",
      "IoT",
      "Machine Learning/AI",
      "Mobile",
      "Open Ended",
      "Web"
    ]
  },
  {
    "name": "Mouad Ennasiry",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "transformers",
      "gradio",
      "llms",
      "python",
      "rag",
      "r"
    ],
    "interests": [
      "Health",
      "Machine Learning/AI"
    ],
    "bio": "Hello im a student persuing a master degree in data science im curi learning all about generative ai, im looking for passionnant team looking forward to learn and groq"
  },
  {
    "name": "Phuc Nguyen",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "machine-learning"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "selvakumar kandasamy",
    "title": "Solutions architect",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "ml",
      "cloud",
      "timeseries",
      "integration",
      "data"
    ],
    "interests": [
      "Design",
      "Enterprise",
      "Fintech",
      "Lifehacks",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Ming Lyu",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "natural-language-processing",
      "machine-learning",
      "python",
      "java"
    ],
    "interests": [
      "Beginner Friendly",
      "Gaming",
      "IoT",
      "Machine Learning/AI",
      "Open Ended"
    ],
    "bio": "Hi, I work as a data scientist focusing on natural language applications. Interested in LLM and also RAG applications. Looking for teammates to work on RAG-related projects. Any idea is welcome!"
  },
  {
    "name": "Bassim Eledath",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "react",
      "postgresql",
      "r",
      "java"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Shashank Bharadwaj",
    "title": "Full-stack developer",
    "projects": "4 projects",
    "followers": "6 followers",
    "achievements": "6 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "javascript",
      "jquery",
      "css",
      "html5",
      "ionic",
      "parse",
      "swift",
      "ios",
      "android",
      "java"
    ],
    "interests": [
      "Design",
      "Education",
      "Machine Learning/AI",
      "Mobile",
      "Social Good",
      "Web"
    ],
    "bio": "Generalist developer. LLM tinkerer"
  },
  {
    "name": "nassarhayat Hayat",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "javascript",
      "python"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Kai Hayden",
    "title": "Data scientist",
    "projects": "6 projects",
    "followers": "5 followers",
    "achievements": "6 achievements",
    "team_status": "Has a team",
    "skills": [
      "machine-learning",
      "deep-learning",
      "big-data",
      "predictive-analytics"
    ],
    "interests": [
      "Blockchain",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Sarah deSouza",
    "title": "Business",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "n/a"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "David Min",
    "title": "Business",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "langchain",
      "llamaindex",
      "open",
      "opensource",
      "llm"
    ],
    "interests": [
      "Lifehacks"
    ]
  },
  {
    "name": "saravana periyasamy",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "2 achievements",
    "team_status": "Working solo",
    "skills": [
      "ios"
    ]
  },
  {
    "name": "Divyansh Jain",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "llm",
      "rag",
      "python",
      "ai"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Mehul Khetrapal",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "machine-learning"
    ],
    "interests": [
      "Beginner Friendly",
      "Education",
      "Enterprise",
      "Fintech",
      "Health",
      "IoT",
      "Machine Learning/AI",
      "Quantum",
      "Robotic Process Automation",
      "Social Good"
    ]
  },
  {
    "name": "Richy Chen",
    "title": "Product manager",
    "projects": "1 project",
    "followers": "2 followers",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "ruby-on-rails",
      "python",
      "sql"
    ],
    "interests": [
      "Fintech",
      "IoT",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Mohnish Shah",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "2 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "machine-learning"
    ],
    "interests": [
      "Fintech",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Laikh Tewari",
    "projects": "4 projects",
    "followers": "1 follower",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "java",
      "ios",
      "python",
      "javascript",
      "machine-learning"
    ]
  },
  {
    "name": "Deep Rodge",
    "title": "Data scientist",
    "projects": "5 projects",
    "followers": "1 follower",
    "achievements": "9 achievements",
    "team_status": "Working solo",
    "skills": [
      "flutter",
      "python",
      "pytorch",
      "pandas",
      "numpy"
    ],
    "interests": [
      "Machine Learning/AI",
      "Design",
      "Mobile",
      "Music/Art"
    ]
  },
  {
    "name": "Jay Rodge",
    "projects": "3 projects",
    "followers": "2 followers",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "python",
      "deep-learning",
      "machine-learning",
      "natural-language-processing",
      "data-science"
    ]
  },
  {
    "name": "Harshul Agarwal",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "1 follower",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "machine-learning",
      "natural-language-processing",
      "llms",
      "java"
    ],
    "interests": [
      "Machine Learning/AI"
    ],
    "bio": "Hey, I am Harshul working as data scientist at AB Inbev. Having a basic knowledge of RAGs and LLMs. Looking for a teammate to collaborate for the hackathon and learn and build solutions."
  },
  {
    "name": "Abel Regalado",
    "projects": "4 projects",
    "followers": "6 followers",
    "achievements": "6 achievements",
    "team_status": "Working solo",
    "skills": [
      "javascript",
      "react",
      "mongodb",
      "express.js"
    ]
  },
  {
    "name": "Rahul Parundekar",
    "title": "Data scientist",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "3 achievements",
    "team_status": "Working solo",
    "skills": [
      "ai"
    ],
    "interests": [
      "Machine Learning/AI",
      "Open Ended"
    ]
  },
  {
    "name": "Akkati Vishwa Reddy",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "3 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "mern"
    ],
    "interests": [
      "AR/VR",
      "Beginner Friendly",
      "Databases",
      "Education",
      "Machine Learning/AI",
      "Mobile",
      "Open Ended",
      "Quantum",
      "Social Good",
      "Web"
    ],
    "bio": "I'm Vish, a second year at UCD who has recently discovered the world of AI and its applications. With experience in building RAG assisted real time voice bots, I'm interested in building solutions related to that."
  },
  {
    "name": "Sam Goodwin",
    "title": "Back-end developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "typescript",
      "python",
      "athena",
      "amazon-web-services",
      "cdk",
      "pulumi"
    ],
    "interests": [
      "Databases",
      "DevOps",
      "Enterprise",
      "Health",
      "IoT",
      "Low/No Code",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Elizabeth Crouther",
    "title": "Back-end developer",
    "projects": "5 projects",
    "followers": "6 followers",
    "achievements": "6 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "java",
      "visual-studio",
      "python",
      "sql",
      "django"
    ],
    "interests": [
      "Health",
      "Machine Learning/AI",
      "Social Good"
    ]
  },
  {
    "name": "Vanessa Sauter",
    "title": "Adversarial Security",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team",
    "skills": [
      "python",
      "streamlit",
      "openai",
      "cli",
      "burp"
    ],
    "interests": [
      "Machine Learning/AI"
    ]
  },
  {
    "name": "dillanhoyos Hoyos",
    "title": "Full-stack developer",
    "projects": "5 projects",
    "followers": "6 followers",
    "achievements": "8 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "sound",
      "unity",
      "music",
      "javascript"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "Fintech",
      "Gaming",
      "IoT",
      "Lifehacks",
      "Machine Learning/AI",
      "Voice skills"
    ],
    "bio": "Hey I am Dillan Software Engineer looking for a team, I am experienced in server side architecture and the OpenAIAPI I want to learn more about llama index and how to create useful augmented bots that can automate the workplace"
  },
  {
    "name": "Ajay Sharma",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Has a team"
  },
  {
    "name": "Quynh Le",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "machine-learning"
    ],
    "interests": [
      "Beginner Friendly",
      "Machine Learning/AI",
      "Social Good"
    ]
  },
  {
    "name": "Yachee Gupta",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "machine-learning",
      "python",
      "llm",
      "rag",
      "ai"
    ],
    "interests": [
      "Blockchain",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Shubham Jitendra Shinde",
    "title": "Back-end developer",
    "projects": "3 projects",
    "followers": "2 followers",
    "achievements": "5 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "cloud",
      "amazon-web-services"
    ],
    "interests": [
      "AR/VR",
      "Blockchain",
      "DevOps",
      "Fintech",
      "Lifehacks",
      "Machine Learning/AI"
    ],
    "bio": "Hi I'm Shubham a recent MS CSE graduate. I was an SDE intern at Amazon and I work on a research project in UC Berkeley. I have hands on experience creating RAG's. I'm proficient in Python focused on Backend. Looking forward to the amazing teammates."
  },
  {
    "name": "Sagar Jadhav",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Has a team",
    "skills": [
      "java",
      "golang"
    ],
    "interests": [
      "Blockchain",
      "IoT",
      "Machine Learning/AI",
      "Productivity",
      "Social Good"
    ]
  },
  {
    "name": "Samad Ahmed",
    "title": "Full-stack developer",
    "projects": "2 projects",
    "followers": "2 followers",
    "achievements": "7 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "node.js",
      "typescript",
      "react"
    ],
    "interests": [
      "IoT",
      "Machine Learning/AI",
      "AR/VR",
      "Education",
      "Enterprise"
    ]
  },
  {
    "name": "Rohan Rao",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "python",
      "langchain"
    ],
    "interests": [
      "Enterprise",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Warp Smith",
    "projects": "29 projects",
    "followers": "123 followers",
    "achievements": "9 achievements",
    "team_status": "Working solo",
    "skills": [
      "android",
      "javascript",
      "java",
      "css",
      "html5",
      "python",
      "unity",
      "c#",
      "unreal-engine",
      "django"
    ],
    "interests": [
      "Blockchain",
      "AR/VR",
      "DevOps",
      "Gaming",
      "IoT",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Pagadi Shyam",
    "title": "Data scientist",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Working solo",
    "skills": [
      "ai"
    ],
    "interests": [
      "DevOps",
      "Machine Learning/AI"
    ]
  },
  {
    "name": "Griffin Clark",
    "title": "Product manager",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "typescript",
      "nosql"
    ],
    "interests": [
      "Communication",
      "Cybersecurity",
      "DevOps",
      "Education",
      "Enterprise",
      "Fintech",
      "Lifehacks",
      "Machine Learning/AI",
      "Mobile",
      "Open Ended",
      "Productivity",
      "Social Good",
      "Web"
    ],
    "bio": "I'm the TPM on an AI product that builds tailored daily journaling exercises for people"
  },
  {
    "name": "Joseph Pollack",
    "title": "CIO",
    "projects": "2 projects",
    "followers": "1 follower",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "statistics",
      "data",
      "python",
      "autogen",
      "falcon",
      "llama",
      "mistral",
      "yi",
      "gradio",
      "torch",
      "semantic-kernel",
      "langchain"
    ],
    "interests": [
      "Beginner Friendly",
      "Machine Learning/AI",
      "Education",
      "Productivity",
      "DevOps",
      "Fintech",
      "Health",
      "Open Ended",
      "Robotic Process Automation"
    ]
  },
  {
    "name": "Charlene Wang",
    "projects": "4 projects",
    "followers": "2 followers",
    "achievements": "4 achievements",
    "team_status": "Has a team",
    "skills": [
      "python",
      "javascript"
    ]
  },
  {
    "name": "Hiroaki Ozasa",
    "title": "Data scientist",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "4 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "python",
      "ai",
      "machine-learning"
    ],
    "interests": [
      "Beginner Friendly",
      "Machine Learning/AI",
      "Music/Art"
    ],
    "bio": "I'm PM and ML engineer."
  },
  {
    "name": "Carter Rabasa",
    "title": "Full-stack developer",
    "projects": "1 project",
    "followers": "6 followers",
    "achievements": "2 achievements",
    "skills": [
      "javascript",
      "twilio",
      "node.js",
      "nosql",
      "astra-db",
      "react"
    ],
    "interests": [
      "Machine Learning/AI",
      "Web"
    ]
  },
  {
    "name": "Rob Zazueta",
    "title": "Full-stack developer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "skills": [
      "api",
      "javascript",
      "python",
      "linux"
    ],
    "interests": [
      "Web"
    ]
  },
  {
    "name": "Matt Weeks",
    "title": "Designer",
    "projects": "0 projects",
    "followers": "0 followers",
    "achievements": "1 achievement",
    "skills": [
      "apis",
      "c++",
      "java",
      "lamp",
      "html",
      "mysql",
      "python"
    ],
    "interests": [
      "Blockchain",
      "Design",
      "E-commerce/Retail",
      "Enterprise",
      "Fintech",
      "Health",
      "Lifehacks",
      "Low/No Code",
      "Mobile",
      "Music/Art",
      "Productivity",
      "Quantum",
      "Web"
    ]
  },
  {
    "name": "Mark Evans",
    "title": "Business",
    "projects": "1 project",
    "followers": "0 followers",
    "achievements": "2 achievements",
    "team_status": "Looking for teammates",
    "skills": [
      "strategist",
      "product",
      "advisor"
    ],
    "interests": [
      "Machine Learning/AI",
      "Communication",
      "Enterprise",
      "Music/Art"
    ],
    "bio": "Hi all, I'm hosting the RAG-A-THON; testing out team formation functionality. If you questions, let me know."
  }
]
'''

# Function to capitalize names properly
def capitalize_name(name):
    return ' '.join(word.capitalize() for word in name.split())

# Function to process the JSON data
def process_json(data):
    # Load the JSON data
    entries = json.loads(data)

    # Iterate through each entry and fix the name capitalization
    for entry in entries:
        name = entry.get("name", "")
        # Check if the name is all lowercase or all uppercase
        if name.islower() or name.isupper():
            entry["name"] = capitalize_name(name)

    # Return the processed JSON data
    return json.dumps(entries, indent=2)

# Process the JSON data and print the result
processed_json = process_json(json_data)
print(processed_json)