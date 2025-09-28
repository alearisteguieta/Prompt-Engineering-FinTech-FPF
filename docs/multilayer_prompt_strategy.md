# Multilayer Prompt Strategy

## Layer 1 – Strategic (Master)
**Objective**: Define scope, high-level architecture, technology stack.  
**Prompt Example**: Master Architecture FPF.  
**Deliverables**: `System_Architecture.md`, `API_Specifications.json`, `Base_DB_Schema.sql`:contentReference[oaicite:14]{index=14}.  

---

## Layer 2 – Development (Intermediate)
**Objective**: Generate coherent financial logic modules based on Layer 1.  
**Prompts**:  
- MPT Module  
- Categorization Engine  
- Tax-Loss Harvesting Module  
**Deliverables**: Functional code modules (Python/Node.js).  

---

## Layer 3 – Refinement (Detail)
**Objective**: Ensure quality, security, testing, and documentation.  
**Prompts**:  
- Security Implementation (MFA, Encryption)  
- Test Generation (unit tests)  
- AWS/Terraform Configuration  
**Deliverables**: Test scripts, infrastructure configs, security functions:contentReference[oaicite:15]{index=15}.  

---

## Timeline
1. Architecture → DB Schema  
2. Backend Logic (MPT → Tax-Loss)  
3. Security Implementation  
4. Validation & Frontend  
5. Deployment:contentReference[oaicite:16]{index=16}  
