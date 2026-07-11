# AWS Cloud Security Monitoring & Auto-Remediation Lab
## Setup Guide

This guide explains how to deploy the AWS Cloud Security Monitoring & Auto-Remediation Lab using AWS Free Tier eligible services.

---

# Prerequisites

- AWS Account
- AWS Free Tier Eligible
- IAM User with Administrator Access (for lab deployment)
- Email address for SNS notifications
- Web browser

---

# AWS Services Used

- Amazon VPC
- Amazon EC2
- IAM
- Amazon S3
- AWS CloudTrail
- Amazon EventBridge
- AWS Lambda
- Amazon SNS
- Amazon CloudWatch

---

# Deployment Steps

## Step 1 – Create Secure VPC

Create:

- VPC
- Public Subnet
- Private Subnet
- Internet Gateway
- Route Tables

---

## Step 2 – Configure IAM

Create IAM Groups

- Admins
- Developers
- SecurityTeam
- Auditors

Create IAM Users

- admin-user
- developer-user
- security-user
- auditor-user

Assign least-privilege permissions.

---

## Step 3 – Configure Security Group

Create **WebServer-SG**

Inbound Rules

| Port | Source |
|------|---------|
| 22 | My IP |
| 80 | Anywhere |
| 443 | Anywhere |

---

## Step 4 – Deploy EC2

Launch

- Amazon Linux 2023
- t2.micro
- Public Subnet
- Auto Assign Public IP Enabled

Install Apache

```bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl enable httpd
sudo systemctl start httpd

echo '<h1>AWS Cloud Security Monitoring Lab</h1><p>Apache is working on EC2.</p>' | sudo tee /var/www/html/index.html
```

Verify

```
http://<Public-IP>
```

---

## Step 5 – Configure CloudTrail

- Multi-region Trail
- Management Events
- Log Validation Enabled
- Store Logs in Amazon S3

---

## Step 6 – Configure SNS

Create Topic

```
SecurityAlerts
```

Subscribe Email Endpoint.

Confirm subscription from email.

---

## Step 7 – Configure CloudWatch

Create Alarm

Metric

```
CPUUtilization
```

Threshold

```
>= 70%
```

Notification

```
SecurityAlerts
```

---

## Step 8 – Configure EventBridge

Create Rule

```
DetectS3PublicAccessChange
```

Monitor Events

- PutBucketAcl
- PutBucketPolicy

Target

```
AutoRemediateS3 Lambda
```

---

## Step 9 – Create Lambda

Function

```
AutoRemediateS3
```

Environment Variable

```
SNS_TOPIC_ARN
```

Execution Role

```
LambdaS3RemediationRole
```

---

# Validation

Verify

- CloudTrail is logging events
- EventBridge rule is enabled
- Lambda is deployed
- SNS email subscription is confirmed
- EC2 web page is accessible
- CloudWatch alarm is active

---

# Project Workflow

```
S3 Permission Change
        │
        ▼
CloudTrail Logs Event
        │
        ▼
EventBridge Detects Event
        │
        ▼
Lambda Executes
        │
        ├── Block Public Access
        └── Send SNS Notification
```

---

# Cleanup

To avoid unnecessary AWS charges

Delete:

- EC2 Instance
- Lambda Function
- CloudTrail Trail
- EventBridge Rule
- CloudWatch Alarm
- SNS Topic
- S3 Bucket
- IAM Test Users
- VPC (after deleting dependent resources)
