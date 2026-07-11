# 🔐 AWS Cloud Security Monitoring & Auto-Remediation Lab

<p align="center">

![AWS](https://img.shields.io/badge/AWS-Free%20Tier-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cloud Security](https://img.shields.io/badge/Cloud-Security-red)
![Serverless](https://img.shields.io/badge/AWS-Lambda-green)
![Monitoring](https://img.shields.io/badge/CloudWatch-Monitoring-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

---

# 📖 Overview

This project demonstrates the implementation of a **secure AWS cloud environment** that continuously monitors infrastructure activities, detects potentially risky changes to Amazon S3 permissions, automatically remediates security misconfigurations, and notifies the security team in real time.

The project follows **AWS security best practices** including **least privilege IAM**, **network segmentation**, **audit logging**, **continuous monitoring**, and **serverless incident response**, while remaining compatible with the **AWS Free Tier**.

---

# 🎯 Objectives

- Design a secure AWS network architecture
- Implement Identity & Access Management (IAM)
- Deploy a secure EC2 web server
- Configure CloudTrail for audit logging
- Monitor AWS resources using CloudWatch
- Detect security events using EventBridge
- Automatically remediate risky S3 permission changes using AWS Lambda
- Send real-time security alerts using Amazon SNS

---

# ☁ AWS Services Used

| Service | Purpose |
|----------|----------|
| IAM | Identity & Access Management |
| VPC | Secure Network Architecture |
| EC2 | Web Server |
| Security Groups | Network Firewall |
| S3 | CloudTrail Log Storage |
| CloudTrail | Audit Logging |
| CloudWatch | Infrastructure Monitoring |
| SNS | Email Notifications |
| EventBridge | Event Detection |
| Lambda | Automated Security Remediation |

---

# 🔒 Security Controls Implemented

- ✅ IAM Least Privilege Access
- ✅ Role-Based Access Control (RBAC)
- ✅ Secure VPC Architecture
- ✅ Public & Private Subnets
- ✅ Security Groups
- ✅ CloudTrail Audit Logging
- ✅ CloudWatch Monitoring
- ✅ Event-Driven Security Detection
- ✅ Automated Remediation
- ✅ Email Alerting
- ✅ Serverless Incident Response

---

# 📂 Project Structure

```
cloudsentinel-aws-security-monitoring/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── architecture/
│   ├── README.md
│   └── architecture-diagram.png
│
├── docs/
│   ├── setup-guide.md
│   └── incident-report.md
│
├── lambda/
│   └── AutoRemediateS3.py
│
└── screenshots/
```

# 🚀 Implementation Steps

## Step 1 — Create Secure VPC

- Created custom VPC
- Created Public Subnet
- Created Private Subnet
- Attached Internet Gateway
- Configured Route Tables

---

## Step 2 — Configure IAM

Created IAM Groups

- Admins
- Developers
- SecurityTeam
- Auditors

Created IAM Users

- admin-user
- developer-user
- security-user
- auditor-user

Assigned least-privilege permissions using AWS managed policies.

---

## Step 3 — Configure Security Groups

Created **WebServer-SG**

Inbound Rules

- SSH (22) → My IP
- HTTP (80) → Anywhere
- HTTPS (443) → Anywhere

---

## Step 4 — Deploy EC2 Web Server

- Amazon Linux 2023
- t2.micro (Free Tier)
- Apache HTTP Server Installed
- Hosted demo security webpage

---

## Step 5 — Configure CloudTrail

- Multi-region Trail
- Log Validation Enabled
- Logs Stored in Amazon S3
- Management Events Enabled

---

## Step 6 — Configure Amazon SNS

Created Topic

```
SecurityAlerts
```

Subscribed email endpoint to receive security notifications.

---

## Step 7 — Configure CloudWatch

Created CPU Utilization Alarm

Threshold

```
CPU >= 70%
```

Notification Target

```
SecurityAlerts SNS Topic
```

---

## Step 8 — Configure EventBridge

Created Rule

```
DetectS3PublicAccessChange
```

Monitored CloudTrail Events

- PutBucketAcl
- PutBucketPolicy

---

## Step 9 — Create Lambda Function

Created

```
AutoRemediateS3
```

Responsibilities

- Detect public S3 bucket changes
- Remove insecure configuration
- Send SNS notification

---

# 🔄 Security Workflow

```
User modifies S3 Bucket
            │
            ▼
CloudTrail Records API Call
            │
            ▼
EventBridge Detects Event
            │
            ▼
Lambda Function Executes
            │
     ┌──────┴────────┐
     │               │
     ▼               ▼
Remove Public     Send SNS
Bucket Access      Alert
     │
     ▼
Security Team Notified
```

---

# 🧪 Testing

### Test 1 — EC2 Deployment

✅ Successfully hosted Apache web server.

---

### Test 2 — CloudWatch Alarm

Generated CPU activity and verified alarm configuration.

---

### Test 3 — SNS Notifications

Verified email subscription and notification delivery.

---

### Test 4 — EventBridge Detection

Verified detection of CloudTrail management events.

---

### Test 5 — Lambda Automation

Verified automatic invocation through EventBridge.

---

# 🛠 Challenges & Troubleshooting

## Issue 1 — EC2 Public IP Not Accessible

### Root Cause

Apache HTTP Server was not installed.

### Solution

```bash
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
```

---

## Issue 2 — Webpage Not Loading

### Error

```
tee: var/www/h: No such file or directory
```

### Root Cause

Incorrect web root path.

### Fix

```bash
echo '<h1>AWS Cloud Security Monitoring Lab</h1>' | sudo tee /var/www/html/index.html
```

---

## Issue 3 — No SSH Access

### Root Cause

EC2 launched without a Key Pair.

### Solution

Used **EC2 Instance Connect** to access the instance securely.

---

## Issue 4 — Internet Connectivity Failure

### Root Cause

Route Table contained a **Blackhole Route**.

### Solution

Attached the correct Internet Gateway and updated the Route Table.

---

# 📈 Skills Demonstrated

- AWS Cloud Security
- AWS IAM
- Amazon VPC
- EC2 Administration
- Security Groups
- Amazon S3
- CloudTrail
- CloudWatch
- Amazon SNS
- Amazon EventBridge
- AWS Lambda
- Incident Response
- Serverless Security
- Least Privilege
- Security Monitoring
- Cloud Auditing
- Infrastructure Security

---

# 🚀 Future Enhancements

- AWS Config Rules
- Amazon GuardDuty
- AWS Security Hub
- AWS WAF
- Amazon Inspector
- Systems Manager Automation
- Infrastructure as Code (Terraform / CloudFormation)
- CI/CD Integration
- Multi-Account Security Monitoring

---

# 👨‍💻 Author

**Akash Deep**

Cloud Security | IAM | GRC | AWS | Azure | Zero Trust | Security Monitoring

LinkedIn: *(https://www.linkedin.com/in/akash-deep-ism/)*

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
