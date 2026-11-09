# 6D Foraging Methodology™ — Observable Properties Framework

> **"What gets measured becomes manageable. What gets observed becomes measurable."**

**Version:** 2.0
**Created:** November 27, 2025
**Revised:** November 2026 (cost multipliers and invented cascade percentages removed; cascade patterns now counted from the published case library)
**Status:** Production Framework

---

## Executive Summary

The 6D Foraging Methodology™ traces how a problem spreads across six dimensions of an organization, using cited evidence at every step. This document provides the **Observable Properties Framework** — the concrete signals, metrics, trigger keywords, and cascade pathways that make each dimension measurable and actionable.

**The Gap This Fills:**
- **Before:** Abstract categories (Customer, Employee, Revenue, etc.)
- **After:** Specific observables, trigger keywords, data sources, and cascade maps

**Integration with Cormorant Foraging:**
Each dimension is analyzed through three lenses:
- **Sound (ChirpIQX):** Urgency — How immediate is the signal?
- **Space (PerchIQX):** Scope — How widespread is the impact?
- **Time (WakeIQX):** Trajectory — Is it improving or degrading?

---

## Framework Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    6D IMPACT METHODOLOGY™                       │
│                 Observable Properties Framework                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│   │CUSTOMER │ │EMPLOYEE │ │ REVENUE │ │REGULATORY│ │ QUALITY │ │OPERATION│
│   │   D1    │ │   D2    │ │   D3    │ │   D4    │ │   D5    │ │   D6    │
│   └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘
│        │           │           │           │           │           │
│        └───────────┴───────────┴─────┬─────┴───────────┴───────────┘
│                                      │
│                              ┌───────▼───────┐
│                              │   3D LENS     │
│                              ├───────────────┤
│                              │ Sound (Urgency)│
│                              │ Space (Scope)  │
│                              │ Time (Trend)   │
│                              └───────┬───────┘
│                                      │
│                              ┌───────▼───────┐
│                              │ CASCADE MAP   │
│                              │ + CAL SCORING │
│                              └───────────────┘
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Dimension 1: CUSTOMER IMPACT

> **Core Question:** How does this problem affect the people who pay us?

### Observable Signals

| Signal Type | Observable | Data Source | Detection Speed |
|-------------|------------|-------------|-----------------|
| **Immediate** | Support ticket spike | Helpdesk (Zendesk, ServiceNow) | Hours |
| **Behavioral** | Renewal hesitation | Sales notes, CRM | Days-Weeks |
| **Sentiment** | NPS/CSAT score drop | Survey platforms | Weekly |
| **Engagement** | Product usage decline | Analytics (Mixpanel, Amplitude) | Days |
| **Escalation** | Exec-level complaints | Email, meeting requests | Hours |
| **Silent** | Reduced feature adoption | Product analytics | Weeks |
| **Churn** | Cancellation requests | Billing/CRM | Immediate |
| **Trust** | Reference refusals | Sales team feedback | Variable |

### Trigger Keywords

**High Urgency (Sound = 8-10):**
```
"unacceptable"          "breach of contract"      "legal action"
"canceling"             "considering alternatives" "escalating"
"demand refund"         "not what we signed up for"
```

**Medium Urgency (Sound = 4-7):**
```
"disappointed"          "concerned about"         "need clarification"
"frustrating"           "expected better"         "reconsidering"
"will not renew"        "shopping around"
```

**Low Urgency / Early Warning (Sound = 1-3):**
```
"just wondering"        "any updates on"          "is this normal"
"thought it would be"   "not urgent but"          "for future reference"
```

### Metrics

| Metric Type | Metric Name | Calculation |
|-------------|-------------|-------------|
| **Leading** | Support ticket velocity | Tickets/day vs 30-day avg |
| **Leading** | NPS trend | Week-over-week delta |
| **Leading** | Feature adoption rate | New feature usage % |
| **Lagging** | Customer churn rate | Lost customers / Total |
| **Lagging** | Customer lifetime value | Revenue × Retention period |
| **Lagging** | Net revenue retention | (Start + Expansion - Churn) / Start |

### Cascade Pathways

How it can spread. These are mechanisms to look for, not a ranking of how often each path happens.

```
CUSTOMER IMPACT
      │
      ├──────────────────────────────────────┐
      ▼                                      ▼
   REVENUE                               EMPLOYEE
   (Lost renewals,                       (Morale hit from
   reduced expansion,                     angry customers,
   refund requests)                       support burnout)
      │                                      │
      ▼                                      ▼
   OPERATIONAL                           QUALITY
   (Resources diverted                   (Rushed fixes,
   to retention efforts)                  corners cut)
      │
      ▼
   REGULATORY
   (Breach of SLA,
   contract violations)
```

**In the published library:** Of the 50 cases that start in Customer, the next layer includes Revenue in 29, Quality in 26, Operational in 23, Employee in 5 and Regulatory in 2. Example: [UC-305](https://uc-305.stratiqx.com), `D1 > D3+D6 > D5 > D4`. These are counts from the published library (331 cases with a recorded cascade, as of November 2026, [index](https://uc-000.stratiqx.com)), not probabilities.

### Severity Factors

Things that tend to make the same signal more serious. Use them when setting the dimension score; they do not convert into a cost multiplier.

| Factor | Lower | Middle | Higher |
|--------|------------|-------------|------------|
| **Customer Size** | Small account | Mid-market | Enterprise/Strategic |
| **Contract Term** | Month-to-month | Annual | Multi-year |
| **Reference Value** | Unknown | Industry peer | Marquee logo |
| **Relationship Length** | <1 year | 1-3 years | >3 years |
| **Expansion Potential** | Maxed out | Moderate | Significant |

### 3D Scoring (Sound × Space × Time)

| Lens | Score 1-3 | Score 4-6 | Score 7-10 |
|------|-----------|-----------|------------|
| **Sound (Urgency)** | Feedback survey | Direct complaint | Legal threat |
| **Space (Scope)** | One customer | Customer segment | Market-wide |
| **Time (Trajectory)** | First occurrence | Recurring pattern | Accelerating trend |

**Dimension Score = Sound × Space × Time ÷ 10**

---

## Dimension 2: EMPLOYEE IMPACT

> **Core Question:** How does this problem affect the people who work for us?

### Observable Signals

| Signal Type | Observable | Data Source | Detection Speed |
|-------------|------------|-------------|-----------------|
| **Immediate** | Overtime hours spike | Timesheets, HRIS | Daily |
| **Behavioral** | Meeting no-shows | Calendar analytics | Days |
| **Sentiment** | Engagement score drop | Pulse surveys | Weekly |
| **Productivity** | Output decline | Project management tools | Weeks |
| **Turnover** | Resignation notices | HR system | Immediate |
| **Knowledge** | Bus factor = 1 | HEAT heatmap | Ongoing |
| **Health** | Sick day increase | HR data | Weeks |
| **Silent** | Reduced participation | Meeting notes, Slack activity | Weeks |

### Trigger Keywords

**High Urgency (Sound = 8-10):**
```
"I'm done"              "putting in notice"       "can't do this anymore"
"looking for other jobs" "burned out"             "hostile environment"
"discrimination"         "harassment"             "unsafe"
```

**Medium Urgency (Sound = 4-7):**
```
"overwhelmed"           "not sustainable"         "need help"
"understaffed"          "no work-life balance"    "thankless"
"underappreciated"      "dead end"               "no growth"
```

**Low Urgency / Early Warning (Sound = 1-3):**
```
"just curious about"    "any development opportunities"  "hypothetically"
"work from home policy" "how do other teams"             "is it just us"
```

### Metrics

| Metric Type | Metric Name | Calculation |
|-------------|-------------|-------------|
| **Leading** | Overtime hours | Hours > 40/week |
| **Leading** | Engagement pulse | Survey score (1-10) |
| **Leading** | Meeting attendance | Attended / Invited |
| **Leading** | PTO utilization | Days taken / Days available |
| **Lagging** | Voluntary turnover | Resignations / Headcount |
| **Lagging** | Time-to-fill | Days from req to hire |
| **Lagging** | Knowledge concentration | % of critical tasks with single owner |

### Cascade Pathways

How it can spread. These are mechanisms to look for, not a ranking of how often each path happens.

```
EMPLOYEE IMPACT
      │
      ├──────────────────────────────────────┐
      ▼                                      ▼
   QUALITY                               OPERATIONAL
   (Mistakes increase,                   (Slower delivery,
   attention drops,                       bottlenecks form,
   shortcuts taken)                       institutional knowledge lost)
      │                                      │
      ▼                                      ▼
   CUSTOMER                              REVENUE
   (Service quality                      (Productivity loss,
   degradation,                           hiring costs,
   responsiveness drops)                  training investment lost)
      │
      ▼
   REGULATORY
   (Compliance gaps,
   safety incidents,
   documentation failures)
```

**In the published library:** Of the 59 cases that start in Employee, the next layer includes Revenue in 31, Operational in 27, Quality in 18, Customer in 13 and Regulatory in 7. Example: [UC-334](https://uc-334.stratiqx.com), `D2 > D4+D5 > D6+D1`. These are counts from the published library (331 cases with a recorded cascade, as of November 2026, [index](https://uc-000.stratiqx.com)), not probabilities.

### Severity Factors

Things that tend to make the same signal more serious. Use them when setting the dimension score; they do not convert into a cost multiplier.

| Factor | Lower | Middle | Higher |
|--------|------------|-------------|------------|
| **Role Criticality** | Easily backfilled | Specialized | Irreplaceable expertise |
| **Knowledge Concentration** | Well-documented | Partially documented | Tribal knowledge only |
| **Team Size** | Large team (redundancy) | Medium team | Small/Solo |
| **Replacement Time** | <30 days | 30-90 days | >90 days |
| **Training Investment** | Entry level | Mid-level | Senior/Specialized |

### 3D Scoring (Sound × Space × Time)

| Lens | Score 1-3 | Score 4-6 | Score 7-10 |
|------|-----------|-----------|------------|
| **Sound (Urgency)** | Grumbling | Active complaints | Resignation |
| **Space (Scope)** | One person | One team | Cross-functional |
| **Time (Trajectory)** | Temporary stress | Sustained pressure | Chronic condition |

---

## Dimension 3: REVENUE IMPACT

> **Core Question:** How does this problem affect money coming in?

### Observable Signals

| Signal Type | Observable | Data Source | Detection Speed |
|-------------|------------|-------------|-----------------|
| **Immediate** | Invoice disputes | AR aging report | Days |
| **Behavioral** | Discount requests | Sales CRM | Days |
| **Pipeline** | Deal slippage | Forecast system | Weekly |
| **Penalty** | SLA breach payments | Contract management | Immediate |
| **Opportunity** | Lost bids | Sales post-mortems | Days |
| **Pricing** | Margin compression | Financial reports | Monthly |
| **Cash** | Payment cycle lengthening | Cash flow analysis | Weeks |
| **Silent** | Upsell/cross-sell decline | Revenue analytics | Months |

### Trigger Keywords

**High Urgency (Sound = 8-10):**
```
"penalty clause"        "breach of contract"      "demand refund"
"termination"           "lawsuit"                 "material breach"
"audit finding"         "revenue restatement"     "write-off"
```

**Medium Urgency (Sound = 4-7):**
```
"renegotiate"           "discount"                "credit"
"delayed payment"       "budget cut"              "procurement review"
"competitive bid"       "price matching"          "cost reduction"
```

**Low Urgency / Early Warning (Sound = 1-3):**
```
"next fiscal year"      "budget planning"         "exploring options"
"market conditions"     "strategic review"        "benchmarking"
```

### Metrics

| Metric Type | Metric Name | Calculation |
|-------------|-------------|-------------|
| **Leading** | Pipeline velocity | Days in stage vs benchmark |
| **Leading** | Discount rate | Avg discount % on closed deals |
| **Leading** | AR aging | % of receivables >60 days |
| **Leading** | Forecast accuracy | Actual / Forecasted |
| **Lagging** | Revenue growth | YoY change |
| **Lagging** | Gross margin | (Revenue - COGS) / Revenue |
| **Lagging** | Revenue per employee | Total revenue / Headcount |

### Cascade Pathways

How it can spread. These are mechanisms to look for, not a ranking of how often each path happens.

```
REVENUE IMPACT
      │
      ├──────────────────────────────────────┐
      ▼                                      ▼
   OPERATIONAL                           EMPLOYEE
   (Cost cutting,                        (Hiring freeze,
   resource constraints,                  layoffs,
   investment delays)                     morale impact)
      │                                      │
      ▼                                      ▼
   QUALITY                               CUSTOMER
   (Budget cuts to QA,                   (Reduced service,
   cheaper materials,                     slower response,
   reduced testing)                       feature cuts)
      │
      ▼
   REGULATORY
   (Compliance budget cuts,
   audit failures,
   certification lapses)
```

**In the published library:** Of the 96 cases that start in Revenue, the next layer includes Operational in 65, Customer in 43, Quality in 32, Regulatory in 20 and Employee in 16. Example: [UC-324](https://uc-324.stratiqx.com), `D3 > D6+D2 > D5+D1`. These are counts from the published library (331 cases with a recorded cascade, as of November 2026, [index](https://uc-000.stratiqx.com)), not probabilities.

### Severity Factors

Things that tend to make the same signal more serious. Use them when setting the dimension score; they do not convert into a cost multiplier.

| Factor | Lower | Middle | Higher |
|--------|------------|-------------|------------|
| **Revenue Concentration** | Diversified | Moderate concentration | A few customers carry most revenue |
| **Contract Type** | Transactional | Annual | Multi-year committed |
| **Margin Profile** | High margin | Average margin | Low margin |
| **Market Position** | Commodity | Differentiated | Monopoly/Niche |
| **Seasonality** | Evenly distributed | Some concentration | Highly seasonal |

### 3D Scoring (Sound × Space × Time)

| Lens | Score 1-3 | Score 4-6 | Score 7-10 |
|------|-----------|-----------|------------|
| **Sound (Urgency)** | Future risk | Current quarter impact | Immediate cash crisis |
| **Space (Scope)** | One deal | Product line | Company-wide |
| **Time (Trajectory)** | One-time hit | Quarterly pattern | Structural decline |

---

## Dimension 4: REGULATORY IMPACT

> **Core Question:** How does this problem affect our compliance and legal standing?

### Observable Signals

| Signal Type | Observable | Data Source | Detection Speed |
|-------------|------------|-------------|-----------------|
| **Immediate** | Audit finding | Compliance reports | Days |
| **Behavioral** | Documentation gaps | Process audits | Weeks |
| **Violation** | Non-compliance notice | Legal/Compliance | Immediate |
| **Exposure** | Missing certifications | Compliance tracker | Monthly |
| **Training** | Expired certifications | LMS/HR system | Ongoing |
| **Process** | Deviation from standard | Quality reviews | Weeks |
| **Silent** | Policy not followed | Internal audits | Months |
| **External** | Regulatory inquiry | Legal department | Immediate |

### Trigger Keywords

**High Urgency (Sound = 8-10):**
```
"violation"             "fine"                    "penalty"
"cease and desist"      "investigation"           "lawsuit"
"material weakness"     "regulatory action"       "license suspended"
"criminal"              "fraud"                   "subpoena"
```

**Medium Urgency (Sound = 4-7):**
```
"audit finding"         "non-compliance"          "remediation required"
"certification gap"     "documentation missing"   "policy violation"
"deadline approaching"  "renewal pending"         "inspection scheduled"
```

**Low Urgency / Early Warning (Sound = 1-3):**
```
"new regulation"        "industry guidance"       "best practice"
"peer comparison"       "voluntary disclosure"    "proactive review"
```

### Metrics

| Metric Type | Metric Name | Calculation |
|-------------|-------------|-------------|
| **Leading** | Open audit findings | Count of unresolved |
| **Leading** | Certification currency | Days until expiration |
| **Leading** | Policy acknowledgment | % of employees current |
| **Leading** | Training completion | Required training % |
| **Lagging** | Regulatory fines | Dollar amount / year |
| **Lagging** | Audit opinion | Clean / Qualified / Adverse |
| **Lagging** | Compliance incidents | Count per year |

### Cascade Pathways

How it can spread. These are mechanisms to look for, not a ranking of how often each path happens.

```
REGULATORY IMPACT
      │
      ├──────────────────────────────────────┐
      ▼                                      ▼
   REVENUE                               CUSTOMER
   (Fines, penalties,                    (Trust erosion,
   contract terminations,                 public disclosure,
   market access loss)                    reputation damage)
      │                                      │
      ▼                                      ▼
   OPERATIONAL                           EMPLOYEE
   (Remediation efforts,                 (Compliance burden,
   process changes,                       blame culture,
   system modifications)                  legal exposure)
      │
      ▼
   QUALITY
   (Rushed compliance fixes,
   resource diversion,
   attention split)
```

**In the published library:** Of the 57 cases that start in Regulatory, the next layer includes Revenue in 36, Operational in 29, Customer in 25, Quality in 14 and Employee in 11. Example: [UC-326](https://uc-326.stratiqx.com), `D4 > D6+D3 > D1+D2`. These are counts from the published library (331 cases with a recorded cascade, as of November 2026, [index](https://uc-000.stratiqx.com)), not probabilities.

### Severity Factors

Things that tend to make the same signal more serious. Use them when setting the dimension score; they do not convert into a cost multiplier.

| Factor | Lower | Middle | Higher |
|--------|------------|-------------|-------------|
| **Industry Regulation** | Light | Moderate | Heavily regulated (finance, healthcare) |
| **Violation Severity** | Administrative | Material | Criminal/Fraud |
| **Public Exposure** | Internal only | Industry disclosure | Public/Media |
| **Repeat Offense** | First occurrence | Pattern | Willful/Repeated |
| **Remediation Complexity** | Simple fix | Process change | Systemic overhaul |

### 3D Scoring (Sound × Space × Time)

| Lens | Score 1-3 | Score 4-6 | Score 7-10 |
|------|-----------|-----------|------------|
| **Sound (Urgency)** | Best practice gap | Audit finding | Active investigation |
| **Space (Scope)** | One process | One department | Enterprise-wide |
| **Time (Trajectory)** | First instance | Pattern emerging | Chronic non-compliance |

---

## Dimension 5: QUALITY IMPACT

> **Core Question:** How does this problem affect what we deliver?

### Observable Signals

| Signal Type | Observable | Data Source | Detection Speed |
|-------------|------------|-------------|-----------------|
| **Immediate** | Defect rate spike | QA system | Hours-Days |
| **Behavioral** | Rework hours increase | Timesheets | Days |
| **Customer** | Complaint volume up | Support system | Days |
| **Safety** | Incident reports | EHS system | Immediate |
| **Returns** | Product returns | Logistics/RMA | Days |
| **Process** | Specification deviations | Quality audits | Weeks |
| **Silent** | Workarounds created | Tribal knowledge, interviews | Months |
| **Inspection** | Rejection rate | Manufacturing QC | Immediate |

### Trigger Keywords

**High Urgency (Sound = 8-10):**
```
"recall"                "safety incident"         "injury"
"critical defect"       "system failure"          "data breach"
"contamination"         "fatality"                "major outage"
```

**Medium Urgency (Sound = 4-7):**
```
"defect"                "rework"                  "redo"
"didn't meet spec"      "out of tolerance"        "failed inspection"
"customer complaint"    "return"                  "warranty claim"
```

**Low Urgency / Early Warning (Sound = 1-3):**
```
"workaround"            "manual fix"              "known issue"
"tech debt"             "legacy limitation"       "needs improvement"
"minor issue"           "cosmetic defect"         "edge case"
```

### Metrics

| Metric Type | Metric Name | Calculation |
|-------------|-------------|-------------|
| **Leading** | First-pass yield | Good units / Total units |
| **Leading** | Defect detection rate | Defects found internally / Total |
| **Leading** | Code coverage | % of code with tests |
| **Leading** | Technical debt ratio | Debt remediation time / Dev time |
| **Lagging** | Customer-reported defects | Count per release/period |
| **Lagging** | Cost of quality | Prevention + Appraisal + Failure costs |
| **Lagging** | Warranty costs | Claims / Revenue |

### Cascade Pathways

How it can spread. These are mechanisms to look for, not a ranking of how often each path happens.

```
QUALITY IMPACT
      │
      ├──────────────────────────────────────┐
      ▼                                      ▼
   CUSTOMER                              OPERATIONAL
   (Dissatisfaction,                     (Rework cycles,
   trust erosion,                         resource diversion,
   churn risk)                            schedule delays)
      │                                      │
      ▼                                      ▼
   REVENUE                               EMPLOYEE
   (Warranty costs,                      (Frustration,
   refunds, penalties,                    overtime for fixes,
   lost sales)                            blame culture)
      │
      ▼
   REGULATORY
   (Safety violations,
   certification risk,
   mandatory recalls)
```

**In the published library:** Of the 81 cases that start in Quality, the next layer includes Operational in 45, Revenue in 39, Customer in 29, Regulatory in 13 and Employee in 12. Example: [UC-338](https://uc-338.stratiqx.com), `D5 > D3+D6 > D2+D1`. These are counts from the published library (331 cases with a recorded cascade, as of November 2026, [index](https://uc-000.stratiqx.com)), not probabilities.

### Severity Factors

Things that tend to make the same signal more serious. Use them when setting the dimension score; they do not convert into a cost multiplier.

| Factor | Lower | Middle | Higher |
|--------|------------|-------------|-------------|
| **Detection Point** | Internal QA | Customer-found | Field failure |
| **Safety Impact** | None | Potential | Actual injury |
| **Scope of Defect** | Single unit | Batch/Lot | Systemic design |
| **Fix Complexity** | Patch/Update | Rework | Recall/Replace |
| **Brand Sensitivity** | B2B commodity | Consumer product | Premium brand |

### 3D Scoring (Sound × Space × Time)

| Lens | Score 1-3 | Score 4-6 | Score 7-10 |
|------|-----------|-----------|------------|
| **Sound (Urgency)** | Cosmetic issue | Functional defect | Safety critical |
| **Space (Scope)** | One unit | Batch/Release | All production |
| **Time (Trajectory)** | Isolated incident | Recurring | Systemic/Chronic |

---

## Dimension 6: OPERATIONAL IMPACT

> **Core Question:** How does this problem affect how we work?

### Observable Signals

| Signal Type | Observable | Data Source | Detection Speed |
|-------------|------------|-------------|-----------------|
| **Immediate** | System downtime | Monitoring/APM | Minutes |
| **Behavioral** | Manual workarounds | Process documentation | Weeks |
| **Bottleneck** | Queue length increase | Workflow systems | Days |
| **Cycle** | Processing time up | Metrics dashboards | Days |
| **Resource** | Contention/Conflicts | Project management | Days |
| **Capacity** | Utilization spike | Resource planning | Days |
| **Silent** | Shadow processes | Interviews, observation | Months |
| **Integration** | Handoff failures | Cross-team metrics | Weeks |

### Trigger Keywords

**High Urgency (Sound = 8-10):**
```
"system down"           "outage"                  "critical failure"
"data loss"             "cannot operate"          "business stopped"
"disaster recovery"     "incident"                "P1/Sev1"
```

**Medium Urgency (Sound = 4-7):**
```
"workaround"            "manual process"          "bottleneck"
"waiting on"            "blocked by"              "delayed"
"capacity issue"        "resource conflict"       "slow"
```

**Low Urgency / Early Warning (Sound = 1-3):**
```
"inefficient"           "could be better"         "nice to have"
"tech debt"             "legacy system"           "someday"
"minor friction"        "slight delay"            "process improvement"
```

### Metrics

| Metric Type | Metric Name | Calculation |
|-------------|-------------|-------------|
| **Leading** | System uptime | Available time / Total time |
| **Leading** | Cycle time | Time from start to completion |
| **Leading** | Queue depth | Items waiting / Processing rate |
| **Leading** | Resource utilization | Allocated / Available |
| **Lagging** | Incidents per period | Count of P1/P2 incidents |
| **Lagging** | Mean time to recovery | Avg incident resolution time |
| **Lagging** | Process efficiency | Value-add time / Total time |

### Cascade Pathways

How it can spread. These are mechanisms to look for, not a ranking of how often each path happens.

```
OPERATIONAL IMPACT
      │
      ├─────────────────────────────────────────────────────┐
      ▼                          ▼                          ▼
   QUALITY                   EMPLOYEE                    REVENUE
   (Rushed work,             (Frustration,              (Delivery delays,
   corners cut,               overtime,                   penalties,
   reduced testing)           burnout)                    lost opportunities)
      │                          │                          │
      ▼                          ▼                          ▼
   CUSTOMER                  CUSTOMER                   REGULATORY
   (Late delivery,           (Poor service,             (Compliance gaps,
   quality issues)            slow response)             missed deadlines)
```

**In the published library:** Of the 74 cases that start in Operational, the next layer includes Revenue in 55, Quality in 35, Customer in 33, Employee in 11 and Regulatory in 11. Example: [UC-335](https://uc-335.stratiqx.com), `D6 > D2+D5 > D4+D1`. These are counts from the published library (331 cases with a recorded cascade, as of November 2026, [index](https://uc-000.stratiqx.com)), not probabilities.

### Severity Factors

Things that tend to make the same signal more serious. Use them when setting the dimension score; they do not convert into a cost multiplier.

| Factor | Lower | Middle | Higher |
|--------|------------|-------------|------------|
| **System Criticality** | Support system | Core business | Revenue-generating |
| **Dependency Chain** | Standalone | Some dependencies | Highly interconnected |
| **Recovery Options** | Quick failover | Manual recovery | No backup |
| **Business Timing** | Off-peak | Normal operations | Peak/Critical period |
| **Automation Level** | Highly automated | Partially automated | Manual processes |

### 3D Scoring (Sound × Space × Time)

| Lens | Score 1-3 | Score 4-6 | Score 7-10 |
|------|-----------|-----------|------------|
| **Sound (Urgency)** | Efficiency opportunity | Bottleneck | System down |
| **Space (Scope)** | One process | One department | Cross-functional |
| **Time (Trajectory)** | Temporary spike | Recurring issue | Chronic condition |

---

## CASCADE PATHWAY MASTER MAP

```
                         ┌─────────────────────────────────────────────────┐
                         │              PROBLEM ORIGIN                      │
                         │         (Identify starting dimension)            │
                         └─────────────────────────┬───────────────────────┘
                                                   │
           ┌───────────────────────────────────────┼───────────────────────────────────────┐
           │                                       │                                       │
           ▼                                       ▼                                       ▼
    ┌─────────────┐                        ┌─────────────┐                        ┌─────────────┐
    │  CUSTOMER   │◄──────────────────────►│  EMPLOYEE   │◄──────────────────────►│  REVENUE    │
    │     D1      │                        │     D2      │                        │     D3      │
    └──────┬──────┘                        └──────┬──────┘                        └──────┬──────┘
           │                                      │                                      │
           │         ┌────────────────────────────┼────────────────────────────┐         │
           │         │                            │                            │         │
           │         ▼                            ▼                            ▼         │
           │  ┌─────────────┐              ┌─────────────┐              ┌─────────────┐  │
           └─►│ REGULATORY  │◄────────────►│  QUALITY    │◄────────────►│ OPERATIONAL │◄─┘
              │     D4      │              │     D5      │              │     D6      │
              └─────────────┘              └─────────────┘              └─────────────┘

                         ┌─────────────────────────────────────────────────┐
                         │               CASCADE SPREAD                    │
                         │                                                 │
                         │   Each dimension can trigger any other          │
                         │   Pathway strength varies by problem type       │
                         │   Multiple simultaneous cascades possible       │
                         │                                                 │
                         └─────────────────────────────────────────────────┘
```

### What the Published Library Shows

Counts from the published library (331 cases with a recorded cascade, as of November 2026, [index](https://uc-000.stratiqx.com)). These are counts of what was recorded, not probabilities.

| Dimension | Origin of | Reached in (any layer) | Lands in the last layer |
|---|---|---|---|
| D1 Customer | 50 | 301 of 331 | 65 of 331 |
| D2 Employee | 59 | 295 of 331 | 132 of 331 |
| D3 Revenue | 96 | 304 of 331 | 18 of 331 |
| D4 Regulatory | 57 | 285 of 331 | 158 of 331 |
| D5 Quality | 81 | 294 of 331 | 49 of 331 |
| D6 Operational | 74 | 312 of 331 | 33 of 331 |

| Origin | Next layer includes (count of cases) |
|---|---|
| D1 Customer (50) | Revenue 29, Quality 26, Operational 23, Employee 5, Regulatory 2 |
| D2 Employee (59) | Revenue 31, Operational 27, Quality 18, Customer 13, Regulatory 7 |
| D3 Revenue (96) | Operational 65, Customer 43, Quality 32, Regulatory 20, Employee 16 |
| D4 Regulatory (57) | Revenue 36, Operational 29, Customer 25, Quality 14, Employee 11 |
| D5 Quality (81) | Operational 45, Revenue 39, Customer 29, Regulatory 13, Employee 12 |
| D6 Operational (74) | Revenue 55, Quality 35, Customer 33, Employee 11, Regulatory 11 |

A case can have more than one origin, and a layer often holds two dimensions, so rows can add up to more than their totals. Regulatory lands last more often than any other dimension. Revenue is the most common origin but rarely the last stop.

---

## SCORING METHODOLOGY

### Step 1: Identify Observable Signals

For each dimension, document observed signals:

```
┌─────────────────────────────────────────────────────────┐
│ Dimension: [NAME]                                       │
├─────────────────────────────────────────────────────────┤
│ Signals Observed:                                       │
│ □ Immediate: _________________________________          │
│ □ Behavioral: ________________________________          │
│ □ Silent: ____________________________________          │
│                                                         │
│ Trigger Keywords Found:                                 │
│ □ High Urgency: ______________________________          │
│ □ Medium Urgency: ____________________________          │
│ □ Low Urgency: _______________________________          │
│                                                         │
│ Data Sources Checked:                                   │
│ □ ____________________________________________          │
│ □ ____________________________________________          │
└─────────────────────────────────────────────────────────┘
```

### Step 2: Score Each Dimension (0-100)

Score each dimension the evidence reaches. The 3D Lens is one way to think the score through. Leave out dimensions the evidence does not reach; not every case scores all six.

| Dimension | Sound (1-10) | Space (1-10) | Time (1-10) | Dimension Score | Evidence |
|-----------|--------------|--------------|-------------|-----------------|----------|
| Customer | | | | | |
| Employee | | | | | |
| Revenue | | | | | |
| Regulatory | | | | | |
| Quality | | | | | |
| Operational | | | | | |

**Dimension Score = (Sound × Space × Time) ÷ 10**

### Step 3: Map the Cascade

Trace the order the problem spreads in, layer by layer, with evidence for each step:

```
ORIGIN: [Dimension] — score ___/100
   │
   ├── Next layer: [Dimension] — score ___/100
   │       └── Evidence: _______________________ (cited, not assumed)
   │
   ├── Next layer: [Dimension] — score ___/100
   │       └── Evidence: _______________________
   │
   └── Later layer: [Dimension] — score ___/100
           └── Evidence: _______________________

Notation: origin > first layer > next layer   (e.g. D5 > D2+D6 > D4+D1)
```

### Step 4: Score with CAL

The scoring belongs to CAL ([spec v1.2.0](https://doi.org/10.5281/zenodo.24090152)):

```
Chirp      = average of the scored dimensions
DRIFT      = |Methodology − Performance|      (each 0-100)
Confidence = the analyst's 0-1 rating of evidence quality
FETCH      = Chirp × DRIFT × Confidence
```

| FETCH level | When |
|-------------|------|
| **EXECUTE** | FETCH ≥ T (high priority at 2T or above) |
| **CONFIRM** | FETCH ≥ 0.75T |
| **QUEUE** | FETCH ≥ 0.5T |
| **WAIT** | below 0.5T |

T is the threshold, 1,000 by default.

### Step 5: Write the Verdict

The written verdict (EXECUTE, MONITOR, WATCH, COUNTER…) is the analyst's own reading of the cascade. It can differ from the FETCH level. A prognostic case also records triggers and a review date, so it can be graded later.

Earlier versions of this framework had a multiplier step and a "total impact" dollar step. Neither came from published cases and both have been removed.

---

## APPLICATION EXAMPLE: UC-335

[UC-335](https://uc-335.stratiqx.com), "Thirty-Six to Find One", a published case about an AI-assisted survey of the Nazca geoglyphs.

### Dimension Scores

| Dimension | Score |
|-----------|-------|
| Customer (D1) | 58 |
| Employee (D2) | 76 |
| Revenue (D3) | not scored |
| Regulatory (D4) | 64 |
| Quality (D5) | 78 |
| Operational (D6) | 82 (origin) |

### Cascade

```
D6 > D2+D5 > D4+D1
```

Operational first, then Employee and Quality, then Regulatory and Customer.

### CAL Score

```
Chirp      = (58 + 76 + 64 + 78 + 82) ÷ 5 = 71.6
DRIFT      = |90 − 46| = 44           (Methodology 90, Performance 46)
Confidence = 0.84
FETCH      = 71.6 × 44 × 0.84 = 2,646
```

2,646 is above 2T, so the FETCH level is EXECUTE at high priority. The analyst's verdict is **MONITOR**. That is the verdict being a separate reading, as Step 5 describes.

---

## QUICK REFERENCE CARD

### Dimension Checklist

| D | Dimension | Core Question | Key Metric |
|---|-----------|---------------|------------|
| 1 | **Customer** | How does this affect who pays us? | NPS, Churn Rate |
| 2 | **Employee** | How does this affect who works for us? | Turnover, Engagement |
| 3 | **Revenue** | How does this affect money coming in? | AR Aging, Margin |
| 4 | **Regulatory** | How does this affect our compliance? | Audit Findings, Fines |
| 5 | **Quality** | How does this affect what we deliver? | Defect Rate, Rework |
| 6 | **Operational** | How does this affect how we work? | Uptime, Cycle Time |

### 3D Quick Reference

| Lens | Question | Low (1-3) | Medium (4-6) | High (7-10) |
|------|----------|-----------|--------------|-------------|
| **Sound** | How urgent? | Future risk | Current issue | Crisis |
| **Space** | How widespread? | Isolated | Department | Enterprise |
| **Time** | Getting better or worse? | One-time | Recurring | Accelerating |

### CAL Quick Reference

| Term | Definition |
|------|------------|
| **Chirp** | Average of the scored dimensions |
| **DRIFT** | \|Methodology − Performance\| |
| **Confidence** | Analyst's 0-1 rating of evidence quality |
| **FETCH** | Chirp × DRIFT × Confidence |
| **Levels** | EXECUTE ≥ T (high priority ≥ 2T), CONFIRM ≥ 0.75T, QUEUE ≥ 0.5T, WAIT below; T defaults to 1,000 |

---

## INTEGRATION WITH CORMORANT FORAGING

The 6D Observable Properties Framework extends the Cormorant Foraging methodology:

| Cormorant (3D) | 6D Impact Application |
|----------------|----------------------|
| **Sound (ChirpIQX)** | Urgency scoring for each dimension |
| **Space (PerchIQX)** | Scope mapping across dimensions |
| **Time (WakeIQX)** | Trajectory tracking over cascade levels |

**Formula:**

```
Dimension Score = (Sound × Space × Time) ÷ 10

Where each factor is scored 1-10:
- Sound = Urgency of signals
- Space = Scope of impact
- Time  = Trajectory (1 = one-time, 10 = accelerating)
```

Dimension scores then feed CAL's Chirp, the average of the scored dimensions. There is no weighted 6D total.

**The void has structure. This framework measures it.** 🪶

---

## APPENDIX: INDUSTRY VARIATIONS

### Healthcare

| Standard Dimension | Healthcare Variation | Key Observable |
|--------------------|---------------------|----------------|
| Customer | **Patient Outcomes** | Readmission rates, HCAHPS scores |
| Quality | **Clinical Quality** | Infection rates, mortality rates |
| Regulatory | **HIPAA/CMS Compliance** | Audit findings, reimbursement risk |

### Financial Services

| Standard Dimension | FinServ Variation | Key Observable |
|--------------------|-------------------|----------------|
| Customer | **Client Trust** | AUM flows, relationship tenure |
| Regulatory | **SEC/FINRA/OCC** | Examination findings, capital ratios |
| Quality | **Trade Accuracy** | Error rates, break resolution time |

### Manufacturing

| Standard Dimension | Manufacturing Variation | Key Observable |
|--------------------|------------------------|----------------|
| Quality | **Production Quality** | First-pass yield, scrap rate |
| Operational | **Production Efficiency** | OEE, changeover time |
| Regulatory | **Safety/Environmental** | OSHA incidents, EPA compliance |

### SaaS/Technology

| Standard Dimension | SaaS Variation | Key Observable |
|--------------------|----------------|----------------|
| Customer | **User Experience** | Adoption rate, feature usage |
| Operational | **System Reliability** | Uptime, incident frequency |
| Quality | **Technical Debt** | Code coverage, bug escape rate |

---

**End of 6D Observable Properties Framework**

**Version:** 2.0
**Feedback:** Document learnings from field application

---

*"Most analysis stops at the visible cost. They miss the cascade. Now you can see it."*

**6D Foraging Methodology™ — StratIQX**
