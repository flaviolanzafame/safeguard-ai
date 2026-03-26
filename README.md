# 🛡️ SafeGuard AI — RiseVET AI Project

![SafeGuard AI Logo](assets/safeguardai-logo.png)

**“The security that knows when it really matters.”**  
*Fewer false alarms. More control. True peace of mind.*

---

## 👥 Project Team

**Developed by:**  
- Flavio Lanzafame  
- Luigi Larecchiuta  
- Carmelo Vicari  
- Carmelo Vicari  

**Context:** This project was created as part of the **Artificial Intelligence course within the RiseVET program**.  
RiseVET is an educational initiative that supports innovation, skill development, and experimentation in emerging technologies.  
Student groups create practical projects and prototypes, exploring AI, IoT, and smart home concepts. SafeGuard AI is one such prototype.

---

## 🚀 About SafeGuard AI

SafeGuard AI is a **Smart Home Security system** designed to reduce false alarms while maintaining real protection.

**Problem:** Traditional security systems trigger alarms for any movement, even harmless events (like pets), causing stress and unnecessary alerts.

**Solution:** SafeGuard AI analyzes **motion, sound, and temperature/fume sensors** using **machine learning** to classify events and alert users **only when necessary**.

![SafeGuard AI Product Concept](assets/safeguardai-product.png)

---

## 🎯 Target Audience

SafeGuard AI is designed for:  

- Families  
- Homeowners  
- Professionals  

Especially useful in **homes with pets or dynamic environments**, reducing false alarms.

---

## ⚠️ The Problem

Traditional home security systems:  

- Do not understand context  
- Trigger frequent false alarms  
- Cause unnecessary interventions  
- Reduce trust in the system  

---

## 💡 The Solution

SafeGuard AI uses **multi-sensor analysis + Random Forest ML** to classify events:

1. **Context Interpretation** – Understands what is happening  
2. **Event Classification** – Detects humans, animals, emergencies  
3. **Intelligent Action** – Alerts only when needed  

> Discreet, intelligent, reliable protection that restores confidence and control.

---

## 🧰 Technologies

- **IoT Sensors:** Motion, sound, temperature/fume  
- **Machine Learning:** Random Forest Classifier  
- **Edge Computing:** Local processing for fast response  

---

## 🛠️ How It Works (Python Demo)

**Workflow:**

1. **Dataset:** 400 simulated events labeled `NORMAL`, `ANIMAL`, `PERSON`, `EMERGENCY`  
2. **EDA:** Visualizes average sensor values per event type  
3. **ML Model:** Random Forest Classifier predicts event type  
4. **Simulator:** Test new events and receive actionable alerts  

![SafeGuard AI Simulator Example](assets/safeguardai-use.png)

**Example output:**

```text
'Falling leaf' → NORMAL: No action needed.
'Cat on the sofa' → ANIMAL: Logged. No alarm triggered.
'Possible fire' → EMERGENCY: ALERT — Call emergency services!
