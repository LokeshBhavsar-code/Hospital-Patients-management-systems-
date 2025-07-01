# 🏥 Hospital Patients Management System

A robust, modular backend solution built with **FastAPI** that streamlines patient registration, appointment booking, electronic health records (EHR), wearable integration, and real-time remote monitoring. The project leverages **CSV-based storage** for simplicity and portability—ideal for small to medium-sized healthcare providers.

---

## 📚 Table of Contents

- [Abstract](#abstract)
- [Introduction](#introduction)
- [Necessity of the Project](#necessity-of-the-project)
- [Motivation](#motivation)
- [Objectives](#objectives)
- [Research Contribution](#research-contribution)
- [Literature Survey](#literature-survey)
- [Problem Definition & Requirements](#problem-definition--requirements)
- [System Design & Implementation](#system-design--implementation)
- [Workflow](#workflow)
- [API Functions](#api-functions)
- [Execution](#execution)
- [Conclusion](#conclusion)
- [References](#references)

---

## 🧠 Abstract

The Hospital Management System (HMS) addresses inefficiencies in traditional healthcare by integrating eight core FastAPI endpoints into a centralized backend. It facilitates real-time patient monitoring, efficient appointment booking, and scalable EHR management—all powered by lightweight CSV storage.

---

## 🩺 Introduction

### 1. Background

Traditional healthcare systems are siloed, resulting in errors, delays, and poor patient outcomes. HMS envisions a unified backend system that offers intelligent automation, centralized patient care, and real-time data integration.

### 2. Purpose

- Seamless registration, EHR management, appointment handling
- CSV-based data storage
- Modular API design with FastAPI
- Future-ready with IoT integration

---

## 🚨 Necessity of the Project

- ❌ Manual recordkeeping → prone to errors
- ❌ Disconnected departments → inefficiencies
- ✅ Unified system → better care and coordination

---

## ⚙️ Motivation

### 1. Digitization
Adoption of digital tools helps healthcare organizations meet compliance, improve speed, and ensure security.

### 2. Vision
Modular, open-source, API-driven healthcare system for remote and in-person care.

---

## 🎯 Objectives

- Build RESTful endpoints using FastAPI
- Enable CSV-based patient data management
- Implement wearable integration and chronic disease tracking
- Provide real-time monitoring and alerts

---

## 🧪 Research Contribution

- Unified API design across multiple healthcare operations
- Lightweight, file-based architecture (CSV instead of SQL)
- Real-time vital alert system for patient safety

---

## 📖 Literature Survey

- **Limitations of Existing HMS**: High cost, poor flexibility (e.g., Epic, Cerner)
- **Modern Trends**: IoT and real-time monitoring
- **Our Edge**: Open-source, accessible, modular backend

---

## 📝 Problem Definition & Requirements

- **Problem**: Scattered healthcare data → fragmented care
- **Inputs**: Patient info, doctor schedules, IoT health data
- **Outputs**: JSON responses, appointment confirmations, vitals
- **Tech Stack**:
  - Python 3.8+, FastAPI, Pandas
  - Swagger UI & Streamlit for frontend

---

## 🧰 System Design & Implementation

- Follows **Client-Server** model
- Uses **FastAPI**, **CSV**, **Pandas**, and **Pydantic**
- Organized into modules: `patients`, `ehr`, `appointments`, `referrals`, etc.

---

## 🔄 Workflow

1. **Register patient** → `/patients/register`
2. **Create/view EHR** → `/patients/{id}/ehr`
3. **Book appointment** → `/appointments/book`
4. **Monitor vitals** → `/monitoring/vitals`
5. **Log visits** → `/patients/{id}/visit-log`
6. **Chronic monitoring** → `/chronic/log`
7. **Wearables integration** → `/wearable/data`

---

## 🔌 API Functions

Each endpoint includes:
- Validation (`validate_patient_id`, `validate_input_fields`, etc.)
- Unique ID generation (`generate_unique_id`)
- CSV-based CRUD
- JSON responses

👉 Refer to `routes/` folder for full API definitions.

---

## 🏁 Execution

### 1. GitHub Repository  
[Hospital Management System GitHub](https://github.com/mohiava/Hospital-Patients-management-systems-.git)

### 2. File Structure

