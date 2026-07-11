# Security Incident Report

## Project

AWS Cloud Security Monitoring & Auto-Remediation Lab

---

# Incident Summary

A simulated cloud security incident was performed to validate the automated monitoring and remediation workflow.

An Amazon S3 bucket configuration change was introduced to simulate a potentially insecure permission modification.

The event was successfully detected, logged, and remediated using native AWS security services.

---

# Incident Details

| Field | Value |
|--------|-------|
| Incident Type | S3 Permission Change |
| Severity | Medium |
| Detection Method | Amazon EventBridge |
| Log Source | AWS CloudTrail |
| Response Method | AWS Lambda |
| Notification | Amazon SNS Email |

---

# Timeline

### Detection

CloudTrail recorded the API activity.

↓

### Monitoring

EventBridge matched the S3 permission change event.

↓

### Response

Lambda function executed automatically.

↓

### Remediation

S3 Block Public Access configuration applied.

↓

### Notification

Security team received email alert via SNS.

---

# AWS Services Involved

- Amazon S3
- AWS CloudTrail
- Amazon EventBridge
- AWS Lambda
- Amazon SNS
- Amazon CloudWatch

---

# Root Cause

The simulated incident involved modifying an S3 bucket permission through an AWS API operation.

This represents a common cloud security risk where storage resources may unintentionally become publicly accessible due to configuration changes.

---

# Impact

Potential unauthorized access to data stored within the S3 bucket.

No actual data exposure occurred because automated remediation restored the secure configuration immediately.

---

# Response Actions

- Event detected through EventBridge
- Lambda executed automatically
- Public access blocked
- Security notification sent
- Event logged for auditing

---

# Outcome

✅ Detection Successful

✅ Automated Remediation Successful

✅ Email Notification Delivered

✅ Security Controls Verified

---

# Lessons Learned

- CloudTrail provides effective audit visibility.
- EventBridge enables near real-time event detection.
- AWS Lambda simplifies automated incident response.
- Amazon SNS provides rapid security notifications.
- Defense-in-depth reduces the impact of cloud misconfigurations.

---

# Recommendations

- Enable AWS Config for continuous compliance.
- Integrate Amazon GuardDuty for threat detection.
- Use AWS Security Hub for centralized visibility.
- Apply Infrastructure as Code (Terraform/CloudFormation).
- Implement automated compliance reporting.

---

# Conclusion

The simulated incident validated the effectiveness of the cloud security monitoring architecture.

The environment successfully demonstrated event logging, automated detection, serverless remediation, and real-time notification using AWS native security services while remaining compatible with AWS Free Tier.
