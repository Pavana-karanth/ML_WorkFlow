# Scones Unlimited — Automated Image Classification Workflow (AWS Machine Learning Nanodegree)

## 🌸 Overview

This repository contains the complete project files for the AWS Machine Learning Nanodegree Program, focused on building, deploying, and automating a machine learning workflow using AWS Lambda, Step Functions, and SageMaker.

The goal of this project is to design and implement an end-to-end serverless ML pipeline capable of classifying delivery driver images as bicycle or motorcycle (and extended here to include poppy, tulip, and willow tree) using the CIFAR-100 dataset and AWS cloud services.

## 🌸 Project Description

The project demonstrates the following key machine learning and AWS engineering concepts:

- Data Preparation: Extracting and filtering CIFAR-100 dataset classes
- Model Training: Using a SageMaker Image Classification model
- Endpoint Deployment: Deploying the trained model as a real-time endpoint
- Workflow Automation: Creating a Step Functions state machine to automate the process across multiple Lambda functions
- Inference and Evaluation: Capturing inference results, confidence thresholds, and visualizing performance metrics
- Serverless Integration: Orchestrating end-to-end ML tasks without any manual intervention

## 🌸 Repository Structure

```
├── README.md                                               # This file — detailed project overview
├── Cutiepies.asl.json                                      # AWS Step Functions workflow definition (ASL model)
├── Workflow execution.png                                  # Screenshot of workflow execution summary
├── Workflow - Lambda functions!.png                        # Screenshot showing successful Lambda executions
├── Workflow Error Log.png                                  # Screenshot showing log for error in low confidence image test
├── Workflow execution (with error as expected).png         # Screenshot showing failure and error in execution
├── lambda_functions.py                                     # Python script containing all 3 Lambda functions
├── starter.ipynb                                           # Complete Jupyter Notebook (data prep, training, deployment, & tests)
```


---

## 🌸 Lambda Functions Overview  

The project uses **three AWS Lambda functions**, orchestrated through the Step Functions state machine defined in `Cutiepies.asl.json`.

| Function | AWS Name | Purpose | Input / Output |
|-----------|-----------|----------|----------------|
| **Function 1 — serialiseImageRaiseYourYaya** | `arn:aws:lambda:us-east-1:709627069804:function:serialiseImageRaiseyourYaya` | Reads image from S3 and serializes it into Base64 format. | **Input:** S3 bucket & key → **Output:** serialized image data |
| **Function 2️ — serialiseImageWhattheHeck** | `arn:aws:lambda:us-east-1:709627069804:function:serialiseImageWhattheHeck` | Sends the serialized image to the SageMaker endpoint for inference. | **Input:** Base64 image → **Output:** inference array (via `.body`) |
| **Function 3️ — interferencesSlay** | `arn:aws:lambda:us-east-1:709627069804:function:interferencesSlay` | Evaluates inference confidence and determines if threshold is met. | **Input:** inference scores → **Output:** classification result + threshold status |

Each function is **stateless**, follows **JSON input/output schemas**, and uses **IAM roles** for secure access to SageMaker and S3.

---

## ⚙️ Step Function Workflow  

The **Step Function** (`Cutiepies.asl.json`) orchestrates the Lambda chain with retry logic and structured payload passing using **JSONata expressions**.

### Workflow Sequence:
1. **Function1: serialiseImageRaiseYourYaya**  
   - Reads image from S3 → outputs serialized Base64  
   - Output passed to next state via `{% $states.result.Payload %}`  

2. **Function2: serialiseImageWhattheHeck**  
   - Takes Base64 image → calls SageMaker inference endpoint  
   - Returns inference result (from `.body`) to next function  

3. **Function3: interferencesSlay**  
   - Applies confidence threshold logic and produces final classification decision  

- **All states** include robust retry logic for AWS Lambda exceptions and exponential backoff.

📸 *See `Workflow execution.png` and `Workflow - Lambda functions!.png` for successful run examples.*

---

## 🌸 Notebook: `starter.ipynb`

The notebook documents and executes the **entire ML lifecycle**:

- Loading and filtering CIFAR-100 dataset  
- Extracting label indices for `bicycle`, `motorcycle`, `poppy`, `lily`, and `willow`  
- Reshaping and saving images to S3  
- Training a SageMaker Image Classification model  
- Deploying a real-time endpoint  
- Testing Lambda invocations and capturing inference results  
- Visualizing model confidence trends and class distributions  

---

## 🌸 Visualizations

- A scatter plot showing model confidence vs. timestamp, including threshold line (0.94).
- Class distribution of predictions (to identify imbalance)

---

## 🌸 Technologies Used  

| Category | Tools / Services |
|-----------|------------------|
| **Cloud Services** | AWS Lambda, AWS Step Functions, Amazon SageMaker, Amazon S3 |
| **Programming** | Python (boto3, pandas, matplotlib, jsonlines) |
| **Model** | SageMaker Image Classification (ResNet) |
| **Visualization** | Matplotlib, JSONLines |
| **Security** | AWS IAM roles for least-privilege access |

---

## 🌸 Key Highlights  

- **Serverless Workflow** — Fully automated pipeline using Step Functions  
- **Multi-Class Support** — Added three extra CIFAR-100 classes: `poppy`, `lily`, and `willow`  
- **Dynamic Testing** — Random S3 image sampling for inference validation  
- **Confidence Monitoring** — Visuals to track threshold adherence  
- **Reusable Design** — Modular, extensible Lambda architecture  

---

## 🌸 Example Results  

- **Deployed Endpoint**:  
  `image-classification-2025-10-05-05-02-27-632`

- **Sample Input:**
  ```json
  {
    "image_data": "",
    "s3_bucket": "sagemaker-us-east-1-<no>",
    "s3_key": "test/bicycle_s_000513.png"
  }


