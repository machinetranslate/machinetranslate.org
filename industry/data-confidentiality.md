---
nav_order: 15
title: Data confidentiality
description: Data confidentiality in machine translation
---

**Data confidentiality** terms or policies govern how machine translation providers use client data.

Some machine translation providers use client data to train and improve their translation systems.
Many data are confidential for machine translation.

- Client consumer user data
- Client business transaction data
- Client business data

Machine translation providers keep data confidential by complying with specific terms or policies:

- Contracts
- Laws, regulation, and standards, like HIPAA or GDPR
- Security reviews

### Data types

- [Training data](/customisation/training-data.md) – [parallel data](/customisation/parallel-data.md)
- Request data - original input


###  Approaches

- Client-specific – The data is not used to train models for any other clients.
- No-trace – The request data is never stored, but only in memory for the lifetime of the request.
- Encryption – The training and request data are not human-readable.
- Auto-delete – The request data is cached, and deleted after a set period, for example after 72 hours.
- Delete on request – The training data or request data is deleted upon the client’s request.
- On-premise deployment (“on-prem”)
- On-device models


### Risk types

In certain circumstances, confidential data can be exposed:

- Training data is accessed.
- Request data is accessed.
- Training data is included as part of translation output.
