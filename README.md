# Reliable AI Inference Service

A lightweight, production-inspired AI inference system with reliability and fault tolerance mechanisms.

## Overview

As machine learning systems are increasingly deployed in real-world applications, ensuring reliable inference becomes a critical challenge.

Failures in inference systems can directly impact user-facing applications across domains such as housing, healthcare, and financial services.

This project demonstrates core system design patterns used in scalable AI infrastructure systems, with a focus on reliability and robustness.

## Key Features

- Async request handling
- Queue-based processing
- Request batching
- Retry mechanisms for failure recovery
- Timeout handling
- Fallback responses for degraded scenarios

## Architecture

Client → FastAPI → Request Queue → Batch Processor → Model → Response

## Why Reliability Matters

In production AI systems, inference failures can lead to degraded user experiences and system instability.

Designing reliable infrastructure is essential for:

- Maintaining system availability
- Handling unpredictable workloads
- Ensuring consistent performance under failure conditions

## Run Locally

```bash
pip install -r requirements.txt
bash run.sh
