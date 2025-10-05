# Scones Unlimited — Automated Image Classification Workflow (AWS Machine Learning Nanodegree)

## Overview

This repository contains the complete project files for the AWS Machine Learning Nanodegree Program, focused on building, deploying, and automating a machine learning workflow using AWS Lambda, Step Functions, and SageMaker.

The goal of this project is to design and implement an end-to-end serverless ML pipeline capable of classifying delivery driver images as bicycle or motorcycle (and extended here to include poppy, tulip, and willow tree) using the CIFAR-100 dataset and AWS cloud services.

## Project Description

The project demonstrates the following key machine learning and AWS engineering concepts:

- Data Preparation: Extracting and filtering CIFAR-100 dataset classes
- Model Training: Using a SageMaker Image Classification model
- Endpoint Deployment: Deploying the trained model as a real-time endpoint
- Workflow Automation: Creating a Step Functions state machine to automate the process across multiple Lambda functions
- Inference and Evaluation: Capturing inference results, confidence thresholds, and visualizing performance metrics
- Serverless Integration: Orchestrating end-to-end ML tasks without any manual intervention

## 📁 Repository Structure

```
├── README.md                             # This file — detailed project overview
├── Cutiepies.asl.json                    # AWS Step Functions workflow definition (ASL model)
├── Workflow execution.png                # Screenshot of workflow execution summary
├── Workflow - Lambda functions!.png      # Screenshot showing successful Lambda executions
├── lambda_functions.py                   # Python script containing all 3 Lambda functions
├── starter.ipynb                         # Complete Jupyter Notebook (data prep, training, deployment, & tests)
```

