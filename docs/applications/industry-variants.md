# Industry Variations

> **"The dimensions are universal. The observables are industry-specific."**

The 6D Foraging Methodology applies across all industries — but the **signals, metrics, and cascade patterns** vary by context. This guide shows you how to adapt the framework to your industry.

## Core Principle

**What stays the same:**
- The six dimensions (Customer, Employee, Revenue, Regulatory, Quality, Operational)
- The 3D lens (Sound × Space × Time)
- Cascade notation (origin > next layer > next layer)
- CAL scoring: Chirp, DRIFT, Confidence, FETCH against a threshold

**What changes:**
- Observable signals and data sources
- Trigger keywords and severity thresholds
- Metrics and targets
- Which cascade paths are worth checking first
- Regulatory complexity

## Healthcare

### Dimension Adaptations

| Standard Dimension | Healthcare Variation | Key Observable | Data Source |
|--------------------|---------------------|----------------|-------------|
| **Customer (D1)** | **Patient Outcomes** | Readmission rates, HCAHPS scores, patient complaints |
| **Employee (D2)** | **Clinical Staff** | Nurse-to-patient ratios, burnout scores, turnover |
| **Revenue (D3)** | **Reimbursement** | Claim denials, payer mix, revenue cycle days |
| **Regulatory (D4)** | **HIPAA/CMS Compliance** | Survey deficiencies, CMS stars, accreditation status |
| **Quality (D5)** | **Clinical Quality** | Infection rates, mortality rates, adverse events |
| **Operational (D6)** | **Care Delivery** | ED wait times, OR utilization, bed turnover |

### Healthcare-Specific Trigger Keywords

**High Urgency:**
```
"patient safety event"      "sentinel event"          "CMS survey"
"never event"               "mortality review"        "immediate jeopardy"
"license suspension"        "harm to patient"         "abuse/neglect"
```

**Medium Urgency:**
```
"readmission"               "hospital-acquired infection"  "medication error"
"falls"                     "pressure ulcer"          "near miss"
"claim denial"              "quality measure failure" "deficiency"
```

### Healthcare Cascade Example

**Problem:** Hospital-acquired infection spike (Quality issue)

```
QUALITY (Origin): HAI rate rises
    │
    ├── REGULATORY
    │   CMS quality measures fail
    │   Star rating drops
    │   Reimbursement penalties
    │
    ├── CUSTOMER/PATIENT
    │   Patient outcomes worsen
    │   HCAHPS scores drop
    │   Reputation damage
    │
    └── REVENUE
        Value-based purchasing penalties
        Reduced patient volume
        Payer contract risk
```

**Notation:** `D5>D4+D1+D3`. This is an illustration of what to check, not a published case.

**Why Regulatory can come early here:**
- CMS reimbursement penalties
- Accreditation risk
- Malpractice exposure
- Public reporting of quality measures

**What the library shows:** Across the [published library](https://uc-000.stratiqx.com) (331 cases with a recorded cascade, as of November 2026), 81 cases start in Quality. The next layer includes Regulatory in only 13 of those 81; Operational (45 of 81) and Revenue (39 of 81) are more common. Regulatory more often arrives at the end: it lands in the last layer in 158 of 331 cases. In healthcare, check whether it shows up sooner.

### Healthcare Metrics

| Dimension | Leading Indicator | Lagging Indicator |
|-----------|------------------|-------------------|
| **Patient Outcomes** | Real-time safety event reports | 30-day readmission rate |
| **Clinical Quality** | Hand hygiene compliance | CLABSI/CAUTI rates |
| **Regulatory** | Mock survey findings | CMS deficiencies |
| **Revenue** | Claim denial rate | Days in AR |

---

## Financial Services

### Dimension Adaptations

| Standard Dimension | FinServ Variation | Key Observable | Data Source |
|--------------------|------------------|----------------|-------------|
| **Customer (D1)** | **Client Trust** | AUM flows, relationship tenure, referrals |
| **Employee (D2)** | **Advisor/Banker** | Series 7 turnover, production metrics |
| **Revenue (D3)** | **Fee/Interest Income** | Net interest margin, fee compression, wallet share |
| **Regulatory (D4)** | **SEC/FINRA/OCC** | Examination findings, capital ratios, suspicious activity |
| **Quality (D5)** | **Trade Accuracy** | Error rates, break resolution, reconciliation gaps |
| **Operational (D6)** | **Transaction Processing** | STP rates, settlement failures, custody breaks |

### FinServ-Specific Trigger Keywords

**High Urgency:**
```
"SEC investigation"         "FINRA sanction"          "capital violation"
"material weakness"         "wire fraud"              "insider trading"
"suspicious activity"       "AML violation"           "Wells notice"
```

**Medium Urgency:**
```
"exam finding"              "deficiency letter"       "consent order"
"customer complaint"        "trade error"             "break"
"reconciliation issue"      "control gap"             "policy exception"
```

### Financial Services Cascade Example

**Problem:** Trade error affecting high-net-worth client (Quality issue)

```
QUALITY (Origin): Trade error on a client account
    │
    ├── CUSTOMER/CLIENT
    │   Trust erosion
    │   AUM outflow risk
    │   Referral pipeline damage
    │
    ├── REGULATORY
    │   FINRA reporting required
    │   Best execution review
    │   Form ADV amendment
    │
    └── REVENUE
        Client reimbursement
        Relationship manager time
        Legal/compliance costs
```

**Notation:** `D5>D1+D4+D3`. This is an illustration of what to check, not a published case.

**Why client trust matters here:**
- AUM is often concentrated in a few relationships
- Clients refer other clients
- A pattern of errors can draw regulatory scrutiny
- Reputation travels in a small community

**What the library shows:** Across the [published library](https://uc-000.stratiqx.com) (331 cases with a recorded cascade, as of November 2026), 81 cases start in Quality, and the next layer includes Customer in 29 of them.

### Financial Services Metrics

| Dimension | Leading Indicator | Lagging Indicator |
|-----------|------------------|-------------------|
| **Client Trust** | Client contact frequency | AUM flows, net new relationships |
| **Trade Accuracy** | Pre-settlement breaks | Trade error rate |
| **Regulatory** | Control testing results | Exam findings |
| **Operational** | Straight-through processing % | Settlement fails |

---

## Manufacturing

### Dimension Adaptations

| Standard Dimension | Manufacturing Variation | Key Observable | Data Source |
|--------------------|------------------------|----------------|-------------|
| **Customer (D1)** | **OEM/Distributor** | On-time delivery %, quality claims, forecast accuracy |
| **Employee (D2)** | **Production Workers** | Absenteeism, safety incidents, grievances |
| **Revenue (D3)** | **Production Revenue** | Contribution margin, capacity utilization, backlog |
| **Regulatory (D4)** | **Safety/Environmental** | OSHA incidents, EPA compliance, ISO certifications |
| **Quality (D5)** | **Production Quality** | First-pass yield, scrap rate, customer PPM |
| **Operational (D6)** | **Production Efficiency** | OEE, changeover time, downtime |

### Manufacturing-Specific Trigger Keywords

**High Urgency:**
```
"line down"                 "safety incident"         "recall"
"OSHA citation"             "environmental release"   "customer stop-ship"
"major defect"              "contamination"          "equipment failure"
```

**Medium Urgency:**
```
"scrap"                     "rework"                  "downtime"
"changeover delay"          "quality hold"            "supplier issue"
"capacity constraint"       "maintenance overdue"     "yield drop"
```

### Manufacturing Cascade Example

**Problem:** Production line equipment failure (Operational issue)

```
OPERATIONAL (Origin): Line down
    │
    ├── REVENUE
    │   Production capacity lost
    │   Customer penalties for late delivery
    │   Margin impact from expediting
    │
    ├── QUALITY
    │   Rushed startup after repair
    │   First-pass yield drops
    │   Scrap increases
    │
    └── CUSTOMER
        Late deliveries
        Allocation decisions
        Relationship strain
```

**Notation:** `D6>D3+D5+D1`. This is an illustration of what to check, not a published case.

**Why Operational issues spread here:**
- Fixed costs keep running while the line is down
- Customer penalty clauses for late delivery
- Bottlenecks spread to other production lines
- Expediting costs (air freight, overtime)

**What the library shows:** Across the [published library](https://uc-000.stratiqx.com) (331 cases with a recorded cascade, as of November 2026), 74 cases start in Operational. The next layer includes Revenue in 55 of them, Quality in 35 and Customer in 33. Real examples: [UC-319](https://uc-319.stratiqx.com) and [UC-315](https://uc-315.stratiqx.com), both `D6>D3+D5`.

### Manufacturing Metrics

| Dimension | Leading Indicator | Lagging Indicator |
|-----------|------------------|-------------------|
| **Customer** | Customer scorecard | On-time delivery % |
| **Production Quality** | In-process inspection results | First-pass yield |
| **Safety/Environmental** | Near-miss reports | OSHA recordable rate |
| **Efficiency** | Real-time OEE | Overall equipment effectiveness |

---

## SaaS / Technology

### Dimension Adaptations

| Standard Dimension | SaaS Variation | Key Observable | Data Source |
|--------------------|---------------|----------------|-------------|
| **Customer (D1)** | **User Experience** | Adoption rate, feature usage, NPS, churn signals |
| **Employee (D2)** | **Engineering/CS** | Deployment frequency, on-call burden, turnover |
| **Revenue (D3)** | **ARR/MRR** | Net revenue retention, expansion rate, CAC payback |
| **Regulatory (D4)** | **SOC2/GDPR/HIPAA** | Security findings, data breaches, compliance gaps |
| **Quality (D5)** | **Technical Debt** | Code coverage, bug escape rate, tech debt ratio |
| **Operational (D6)** | **System Reliability** | Uptime, incident frequency, MTTR |

### SaaS-Specific Trigger Keywords

**High Urgency:**
```
"system down"               "data breach"             "P1 incident"
"security vulnerability"    "customer escalation"     "churn notice"
"data loss"                 "outage"                  "rollback"
```

**Medium Urgency:**
```
"bug"                       "performance degradation" "integration failure"
"tech debt"                 "deployment blocked"      "on-call fatigue"
"feature request"           "competitive pressure"    "usage decline"
```

### SaaS Cascade Example

**Problem:** Major platform outage (Operational issue)

```
OPERATIONAL (Origin): Platform outage
    │
    ├── CUSTOMER
    │   Cannot access product
    │   Productivity loss
    │   Trust erosion
    │
    ├── REVENUE
    │   SLA credits issued
    │   Churn acceleration
    │   Expansion pipeline stalled
    │
    └── EMPLOYEE
        All-hands incident response
        Engineering burnout
        Support team overwhelmed
```

**Notation:** `D6>D1+D3+D2`. This is an illustration of what to check, not a published case.

**Why availability issues spread here:**
- The whole customer base can be affected at once
- Outages are public and get discussed on social media
- One outage can prompt customers to review the account
- Customers who were hit may hold off on expanding

**What the library shows:** Across the [published library](https://uc-000.stratiqx.com) (331 cases with a recorded cascade, as of November 2026), 74 cases start in Operational. The next layer includes Revenue in 55 of them, Customer in 33 and Employee in 11.

### SaaS Metrics

| Dimension | Leading Indicator | Lagging Indicator |
|-----------|------------------|-------------------|
| **User Experience** | Daily active users, feature adoption | Net Promoter Score |
| **System Reliability** | Error rate, latency p95 | Uptime % |
| **Revenue** | Expansion pipeline, usage trends | Net revenue retention |
| **Technical Debt** | Code coverage, static analysis | Bug escape rate |

---

## Industry Comparison Matrix

| Factor | Healthcare | Financial Services | Manufacturing | SaaS |
|--------|-----------|-------------------|---------------|------|
| **Cascade worth checking early** | Quality → Regulatory | Quality → Customer | Operational → Revenue | Operational → Customer |
| **Fast-moving events to watch** | Patient safety events | Trade errors | Line down | System outage |
| **Regulatory Complexity** | Very High (CMS, HIPAA, TJC) | Very High (SEC, FINRA, OCC) | Medium (OSHA, EPA) | Medium (SOC2, GDPR) |
| **Detection Difficulty** | Medium (clinical data lag) | Low (real-time trade data) | Low (sensor data) | Very Low (APM, logs) |

## Adapting 6D to Your Industry

### Step 1: Map Your Dimensions

For each dimension, identify:
1. **Industry-specific name** (e.g., Customer → Patient)
2. **Key observables** specific to your context
3. **Data sources** you already have
4. **Trigger keywords** your teams actually use

### Step 2: Calibrate Cascade Pathways

Study your historical incidents:
- Which dimension is the **most common origin** of problems?
- Which **cascade path** appears most frequently?
- Which cascades have the **highest severity**?

Write each one in cascade notation and **count** them, the way the published library does. Report counts ("31 of 59"), not probabilities. Compare your counts with the library's on the [Quick Reference Card](../reference/quick-card.md#cascade-pathway-quick-map).

### Step 3: Score With CAL, Not Multipliers

Score each dimension you have evidence for from 0 to 100, then use CAL ([spec v1.2.0](https://doi.org/10.5281/zenodo.24090152)):
- **Chirp** = average of the scored dimensions
- **DRIFT** = |Methodology − Performance|
- **Confidence** = your 0-1 rating of evidence quality
- **FETCH** = Chirp × DRIFT × Confidence, against a threshold T (default 1,000)

Industry context belongs in the evidence and the dimension scores. Cost multipliers are not part of the method; see [Retired Terms](../reference/glossary.md#retired-terms-multiplier-direct-cost-total-impact).

### Step 4: Align Metrics to Industry Standards

Use metrics your industry already tracks:
- Healthcare: CMS measures, HCAHPS, CLABSI rates
- FinServ: AUM flows, NIM, STP rates
- Manufacturing: OEE, first-pass yield, on-time delivery
- SaaS: NRR, uptime, deployment frequency

**Don't invent new metrics. Map 6D to what you already measure.**

## Industry-Specific Resources

### Healthcare
- **CMS Quality Programs**: Hospital Value-Based Purchasing, Hospital Readmissions Reduction
- **Patient Safety**: AHRQ Common Formats, National Database of Nursing Quality Indicators (NDNQI)
- **Regulatory**: The Joint Commission standards, CMS Conditions of Participation

### Financial Services
- **SEC**: Form ADV, Custody Rule, Reg BI
- **FINRA**: Rule 3110 (Supervision), Rule 4530 (Reporting)
- **Banking**: FDICIA, CAMELS ratings, OCC guidance

### Manufacturing
- **Quality**: ISO 9001, IATF 16949 (automotive), AS9100 (aerospace)
- **Safety**: OSHA 300 logs, Process Safety Management (PSM)
- **Efficiency**: SEMI E10 (equipment), OEE standards

### SaaS
- **Security**: SOC 2 Type II, ISO 27001
- **Privacy**: GDPR, CCPA, HIPAA (for health tech)
- **Reliability**: SRE principles, SLA best practices

## Next Steps

<div class="next-steps">

**📖 [Observable Properties](../framework/observable-properties.md)** — Adapt signals to your industry

**📊 [Cascade Pathways](../framework/cascade-pathways.md)** — Calibrate cascades to your context

**🎯 [Scoring Methodology](../framework/scoring.md)** — Score dimensions and compute FETCH

**📖 [Case Studies](case-studies.md)** — See cross-industry examples

</div>

<style>
.next-steps {
  background: #161b22;
  padding: 2rem;
  border-radius: 12px;
  margin: 3rem 0;
  border-left: 4px solid #ffd700;
}

.next-steps a {
  color: #58a6ff;
  text-decoration: none;
  font-weight: 600;
}

.next-steps a:hover {
  text-decoration: underline;
}
</style>

---

**Remember:** Your industry is unique, but the dimensions are universal. Adapt the observables, not the framework. 🪶
