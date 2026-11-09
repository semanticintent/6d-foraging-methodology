# Glossary

> **"Shared vocabulary enables shared understanding."**

This glossary defines key terms used in the 6D Foraging Methodology and Cormorant Foraging framework.

---

## Core Methodology Terms

### 6D Foraging Methodology
The comprehensive framework for analyzing unmeasured effects across six dimensions of business impact: Customer, Employee, Revenue, Regulatory, Quality, and Operational. Extends traditional analysis by mapping **cascade effects** and reaching a **cited, verifiable verdict** (scored in CAL with DRIFT and FETCH) rather than stopping at the origin dimension.

**Related:** [Framework Overview](../framework/index.md)

### 3D Lens
The analytical framework borrowed from Cormorant Foraging that evaluates any problem across three dimensions:
- **Sound (ChirpIQX):** Urgency — How immediate is the signal?
- **Space (PerchIQX):** Scope — How widespread is the impact?
- **Time (WakeIQX):** Trajectory — Is it improving or degrading?

**Formula:** `Dimension Score = (Sound × Space × Time) ÷ 10`

**Related:** [Cormorant Integration](../cormorant-integration/index.md)

---

## The Six Dimensions

### D1: Customer Impact
**Definition:** The effect of a problem on the people who pay for your products or services.

**Key observables:** Support ticket volume, NPS scores, churn signals, renewal hesitation, usage decline

**Related:** [Customer Dimension](../dimensions/customer.md)

### D2: Employee Impact
**Definition:** The effect of a problem on the people who work for your organization.

**Key observables:** Overtime hours, engagement scores, turnover, absenteeism, knowledge concentration

**Real example:** [UC-246](https://uc-246.stratiqx.com) — Starbucks' $500M+ "coffeehouse coach" investment, scored 88/100 as the origin dimension.

**Related:** [Employee Dimension](../dimensions/employee.md)

### D3: Revenue Impact
**Definition:** The effect of a problem on money coming into the organization.

**Key observables:** Invoice disputes, AR aging, discount requests, pipeline slippage, margin compression

**Related:** [Revenue Dimension](../dimensions/revenue.md)

### D4: Regulatory Impact
**Definition:** The effect of a problem on compliance, legal standing, and regulatory obligations.

**Key observables:** Audit findings, compliance gaps, violations, fines, certification status

**Related:** [Regulatory Dimension](../dimensions/regulatory.md)

### D5: Quality Impact
**Definition:** The effect of a problem on what the organization delivers (products, services, outputs).

**Key observables:** Defect rates, rework hours, customer complaints, warranty claims, returns

**Related:** [Quality Dimension](../dimensions/quality.md)

### D6: Operational Impact
**Definition:** The effect of a problem on how the organization works (processes, systems, workflows).

**Key observables:** System downtime, bottlenecks, manual workarounds, cycle time increases, capacity issues

**Related:** [Operational Dimension](../dimensions/operational.md)

*Note: earlier versions of this glossary listed a "primary cascade" probability percentage per dimension (e.g. "Customer → Revenue, 70%"). Those percentages were invented, not measured. Real cascade paths are case-specific and cited. For how often each path actually appears in the published library, see [Counted Pattern](#counted-pattern).*

---

## Signal Detection Terms

### Observable Signal
A **measurable indicator** that a problem exists in a particular dimension. Signals can be:
- **Immediate:** Detected in real-time (hours)
- **Behavioral:** Detected through pattern changes (days-weeks)
- **Silent:** Not directly visible, requires investigation (weeks-months)

**Example:** A support ticket spike is an immediate observable signal of Customer impact.

**Related:** [Observable Properties Framework](../framework/observable-properties.md)

### Trigger Keyword
A **specific word or phrase** that indicates severity level and dimension impact. Used for automated detection and human escalation.

**Urgency levels:**
- **High (8-10):** "lawsuit", "breach", "system down", "critical"
- **Medium (4-7):** "defect", "delayed", "concerned", "audit finding"
- **Low (1-3):** "minor", "someday", "inefficient", "could be better"

**Example:** The keyword "canceling" in a customer email is a high-urgency trigger indicating Customer dimension impact with Sound score of 8-10.

**Related:** [Trigger Keywords Reference](trigger-keywords.md)

### Data Source
The **system, tool, or repository** where observable signals are detected.

**Examples:**
- Customer dimension: CRM (Salesforce), Helpdesk (Zendesk), Survey platform (Qualtrics)
- Employee dimension: HRIS (Workday), Pulse surveys, Timesheets
- Operational dimension: APM tools (Datadog, New Relic), JIRA, Process dashboards

**Related:** [Observable Properties by Dimension](../framework/observable-properties.md)

### Detection Speed
The **time lag** between when a problem occurs and when it becomes observable in your systems.

**Categories:**
- **Real-time:** Minutes to hours
- **Fast:** Hours to days
- **Medium:** Days to weeks
- **Slow:** Weeks to months
- **Delayed:** Months to quarters

**Example:** System downtime has a detection speed of minutes (APM alerts). Employee morale degradation has a detection speed of weeks (pulse survey cycles).

---

## Cascade Analysis Terms

### Cascade Pathway
The **route** a problem or event follows as it propagates from one dimension to another, expressed as cited **cascade notation**, not a predicted probability.

**Structure:** `Origin > Target+Target > Target` (`>` reads "cascades to," `+` reads "simultaneously")

**Example:** [UC-246](https://uc-246.stratiqx.com): `D3 > D1+D5 > D2 > D6 > D4` — Starbucks' Employee investment cascading through Customer and Quality, then Revenue, Operational, and Regulatory. The case page uses an older numbering (D3 = Employee, D2 = Revenue); in current numbering it reads `D2 > D1+D5 > D3 > D6 > D4`.

**Related:** [Cascade Pathways](../framework/cascade-pathways.md)

### Cascade Depth
The **number of levels** a cascade propagates through.

**Levels:**
- **Level 0:** Origin dimension (where problem starts)
- **Level 1:** Primary cascades (direct impacts on other dimensions)
- **Level 2:** Secondary cascades (impacts from Level 1 dimensions)
- **Level 3+:** Tertiary and beyond

**Example:** [UC-305](https://uc-305.stratiqx.com) records `D1>D3+D6>D5>D4`: Customer is the origin, then three more layers.

**Related:** [Cascade Analysis Guide](../applications/cascade-analysis.md)

### Cascade Velocity
The **speed** at which a problem propagates from one dimension to another. Some cascades show up within hours (a system outage reaching customers). Others take months (a regulatory change reaching market reputation).

The published library records the **order** in which dimensions were reached, not the time between them. Treat velocity as something you observe and cite in your own case, not a standard figure.

**Related:** [Cascade Pathways - Velocity Section](../framework/cascade-pathways.md#cascade-velocity)

### Counted Pattern
A **count** of how often something happened across the published case library, used in place of a probability.

**Example:** In the published library ([331 cases with a recorded cascade, as of November 2026](https://uc-000.stratiqx.com)), 81 cases start in Quality (D5). In 45 of those 81, the next layer includes Operational (D6). Regulatory (D4) lands in the last layer in 158 of 331 cases.

A count says where earlier cases went. It does not say where your case will go.

**Related:** [Quick Reference Card](quick-card.md#cascade-pathway-quick-map)

### Why There's No "Cascade Probability" Term Here

Earlier versions of this glossary defined **Cascade Probability**, **Primary Cascade**, **Secondary Cascade**, and **Tertiary Cascade** as percentage-based categories (e.g. "Employee → Quality, 80% probability, Primary"). Those percentages were invented. They were never measured. What replaced them is real, cited cascade notation from published cases, plus [counted patterns](#counted-pattern) across the library. CAL runtime 1.5.0 is deprecating its `cascadeProbability` function, with removal planned for 2.0.0.

**Related:** [Cascade Pathways](../framework/cascade-pathways.md), [Cascade Analysis](../applications/cascade-analysis.md)

---

## Scoring and Quantification Terms

### Dimension Score
The **quantified severity** of impact in a particular dimension, scored 0–100 against cited evidence — the 3D Lens is one way to build this score, not the only one.

**Formula (3D Lens variant):** `(Sound × Space × Time) ÷ 10`

**Range:** 0–100

Not every case scores all six dimensions. A dimension without evidence is left out.

**Real example:** [UC-246](https://uc-246.stratiqx.com)'s origin dimension (Employee) scores 88/100, backed by cited evidence.

**Related:** [Scoring Methodology](../framework/scoring.md)

### CAL
The **Cascade Analysis Language**, where 6D scoring is defined. Spec v1.2.0, DOI [10.5281/zenodo.24090152](https://doi.org/10.5281/zenodo.24090152); concept DOI [10.5281/zenodo.18905196](https://doi.org/10.5281/zenodo.18905196).

**Related:** [CAL vs Other Analytical Languages](cal-comparison.md)

### Chirp
In CAL, the **average of the scored dimensions** (0–100). Not to be confused with ChirpIQX, the Sound lens below.

**Related:** [Scoring Methodology](../framework/scoring.md)

### DRIFT
The **gap between diagnosis and proof**: `DRIFT = |METHODOLOGY − PERFORMANCE|`, both scored 0–100. A low DRIFT means the reasoning and the evidence for it are close together. A high DRIFT means a real, unresolved gap. Those are often the more interesting cases, because they are a genuine bet rather than a description of something already settled.

**Related:** [Scoring Methodology](../framework/scoring.md)

### Confidence
The analyst's **0–1 rating of evidence quality**. It measures how well sourced the analysis is, not how big the issue is.

### FETCH
The **score**: `FETCH = Chirp × DRIFT × Confidence`, compared against a **threshold T** (default 1,000). Per the CAL spec, the FETCH level is:

| Level | Rule |
|-------|------|
| **EXECUTE** | FETCH ≥ T (high priority at ≥ 2T) |
| **CONFIRM** | FETCH ≥ 0.75T |
| **QUEUE** | FETCH ≥ 0.5T |
| **WAIT** | below 0.5T |

**Real example:** [UC-246](https://uc-246.stratiqx.com): FETCH 2,632 vs. T = 1,000. That is above 2T, so the level is EXECUTE, high priority.

**Related:** [Scoring Methodology](../framework/scoring.md), [Cascade Analysis Guide](../applications/cascade-analysis.md)

### Verdict
The analyst's **written reading** of a case (EXECUTE, MONITOR, WATCH, COUNTER…). It is separate from the FETCH level and can differ from it.

### Prognostic Case
A case that makes a forward call. It records **triggers** and a **review date**, and is graded later against what happened.

**Related:** [Case Studies](../applications/case-studies.md)

### Retired Terms: Multiplier, Direct Cost, Total Impact
Earlier versions of this glossary defined **Direct Cost**, **Cascade Cost**, **Total Impact** and a cost **Multiplier** (dimensions × depth → "N×"). These were invented, with no evidence behind them, and are gone. No published case multiplies a direct cost by a factor or sums cascade dollars into a total; summing also risks counting the same dollars twice. In CAL runtime 1.5.0, `estimateMultiplier` and `calculateFinancialImpact` are deprecated.

**Related:** [Scoring Methodology](../framework/scoring.md)

---

## Cormorant Foraging Integration

### Cormorant Foraging
The **3D analytical methodology** developed for content analysis that evaluates information across Sound (urgency), Space (reach), and Time (trajectory). 6D Foraging Methodology extends this framework to business impact analysis.

**Origin:** Biomimicry of cormorant bird hunting patterns

**Application:** Strategic analysis, content evaluation, business intelligence

**Related:** [Cormorant Integration](../cormorant-integration/index.md)

### ChirpIQX (Sound)
The **urgency dimension** of the 3D lens. Measures how immediate or critical a signal is.

**Scale:** 1-10 (low to high urgency)

**In 6D context:**
- 1-3: Future risk, monitoring needed
- 4-6: Current issue, plan response
- 7-10: Crisis, immediate action required

**Mapping to trigger keywords:** High-urgency keywords score 8-10, medium 4-7, low 1-3.

**Not the same as CAL's Chirp.** ChirpIQX is the Sound lens. [Chirp](#chirp) in CAL is the average of the scored dimensions.

**Related:** [ChirpIQX Deep Dive](../cormorant-integration/chirp.md)

### PerchIQX (Space)
The **scope dimension** of the 3D lens. Measures how widespread an impact is.

**Scale:** 1-10 (isolated to enterprise-wide)

**In 6D context:**
- 1-3: One person/customer, single system
- 4-6: Department, customer segment
- 7-10: Enterprise-wide, all customers, market-wide

**Measurement:** Population counting, system coverage, customer base percentage

**Related:** [PerchIQX Deep Dive](../cormorant-integration/perch.md)

### WakeIQX (Time)
The **trajectory dimension** of the 3D lens. Measures whether a situation is improving or degrading over time.

**Scale:** 1-10 (one-time event to accelerating crisis)

**In 6D context:**
- 1-3: Isolated incident, first occurrence
- 4-6: Recurring pattern, sustained pressure
- 7-10: Accelerating trend, chronic condition

**Analysis:** Trend lines, pattern recognition, momentum indicators

**Related:** [WakeIQX Deep Dive](../cormorant-integration/wake.md)

---

## Metrics and Measurement Terms

### Leading Indicator
A **predictive metric** that signals potential problems before they fully manifest.

**Characteristics:**
- Real-time or near-real-time
- Actionable (can intervene)
- Directly observable

**Examples:**
- Support ticket velocity (predicts customer churn)
- Overtime hours (predicts employee burnout)
- Code coverage (predicts quality issues)

**Related:** [Dimension-Specific Metrics](../dimensions/customer.md#metrics)

### Lagging Indicator
A **historical metric** that confirms a problem has occurred.

**Characteristics:**
- Backward-looking
- Harder to act on
- Often reported monthly/quarterly

**Examples:**
- Actual churn rate
- Voluntary turnover
- Revenue growth rate

**Related:** [Observable Signals by Dimension](../framework/observable-properties.md)

### Bus Factor
The **number of people** who would need to be "hit by a bus" before a project/process becomes critically impaired.

**Risk levels:**
- Bus factor = 1: High risk (single point of failure)
- Bus factor = 2-3: Medium risk
- Bus factor = 4+: Low risk (good redundancy)

**6D Relevance:** Employee dimension. Knowledge held by one person is a signal worth recording.

**Tool:** HEAT heatmap (Human Expertise & Accountability Topology)

**Related:** [Employee Dimension](../dimensions/employee.md)

---

## Industry-Specific Terms

### HCAHPS (Hospital Consumer Assessment of Healthcare Providers and Systems)
Patient satisfaction survey used in healthcare to measure Customer (Patient) dimension.

**Related:** [Healthcare Variations](../applications/industry-variants.md#healthcare)

### NRR (Net Revenue Retention)
SaaS metric measuring revenue retention + expansion from existing customers. Key Revenue dimension metric.

**Formula:** `(Starting ARR + Expansion - Churn) / Starting ARR × 100%`

**Target:** >100% (indicates expansion exceeds churn)

**Related:** [Revenue Impact](../dimensions/revenue.md), [SaaS Variations](../applications/industry-variants.md#saas--technology)

### OEE (Overall Equipment Effectiveness)
Manufacturing metric measuring Operational dimension efficiency.

**Formula:** `Availability × Performance × Quality`

**Related:** [Manufacturing Variations](../applications/industry-variants.md#manufacturing)

### AUM (Assets Under Management)
Financial services metric measuring Customer (Client) dimension in wealth management.

**6D Relevance:** Client trust issues cascade to AUM outflows, often disproportionately given how concentrated wealth-management relationships tend to be

**Related:** [Financial Services Variations](../applications/industry-variants.md#financial-services)

---

## Analysis Process Terms

### Origin Dimension
The **dimension where a problem first occurs** — the starting point for cascade analysis.

**Identification:** Look for earliest observable signals, root cause analysis

**Example:** A billing calculation error originates in Operational dimension (system/process issue).

**Related:** [Step 1: Identify Origin](../applications/cascade-analysis.md#step-1-identify-the-origin-dimension)

### Cascade Mapping
The **process** of tracing how a problem propagates from origin dimension through multiple cascade pathways.

**Steps:**
1. Identify the origin dimension
2. Score the origin
3. Map primary cascade pathways (cited evidence, not predicted probability)
4. Map further cascades, as far as the evidence actually reaches
5. Score with CAL (Chirp, DRIFT, Confidence, FETCH vs. threshold), then write your verdict

**Related:** [5-Step Cascade Mapping Process](../applications/cascade-analysis.md#the-5-step-cascade-mapping-process)

### Evidence
**Observable data or signals** that confirm a cascade pathway is occurring.

**Types:**
- Quantitative: Metrics, counts, measurements
- Qualitative: Keywords, feedback, observations
- Systems data: Logs, reports, tickets

**Example:** Evidence of a Quality → Customer cascade: support tickets that name the defect, and customers raising it in account reviews. Cite each one.

**Related:** [Step 3: Map Primary Cascades](../applications/cascade-analysis.md#step-3-map-primary-cascade-pathways)

---

## Action and Response Terms

### Containment Strategy
**Tactical actions** taken to prevent or limit cascade propagation.

**Examples:**
- Customer → Revenue: Proactive retention outreach
- Employee → Quality: Temporary quality checks
- Operational → Employee: Overtime limits, resource reallocation

**Related:** [Cascade Pathways](../framework/cascade-pathways.md)

### Preventive Measures
**Systemic changes** implemented to prevent future occurrences or reduce cascade likelihood.

**Categories:**
- Detection (earlier warning signals)
- Containment (circuit breakers)
- Elimination (fix root cause)

**Example:** Reconciling billing daily instead of monthly shortens the time before an error is noticed.

**Related:** [Cascade Pathways](../framework/cascade-pathways.md)

---

## Quick Lookup

**Most Common Searches:**

| Looking for... | See term... |
|---------------|-------------|
| How to calculate impact score | [Dimension Score](#dimension-score) |
| How a case reaches a verdict | [Chirp](#chirp), [DRIFT](#drift), [Confidence](#confidence), [FETCH](#fetch), [Verdict](#verdict) |
| How often cascades go where | [Counted Pattern](#counted-pattern) |
| Multiplier, total impact, cascade probability | [Retired Terms](#retired-terms-multiplier-direct-cost-total-impact) |
| How problems spread | [Cascade Pathway](#cascade-pathway) |
| What keywords mean | [Trigger Keyword](#trigger-keyword) |
| Sound/Space/Time explained | [3D Lens](#3d-lens), [ChirpIQX](#chirpiqx-sound), [PerchIQX](#perchiqx-space), [WakeIQX](#wakeiqx-time) |
| Where to find signals | [Observable Signal](#observable-signal), [Data Source](#data-source) |
| Industry-specific terms | [Industry variations section](#industry-specific-terms) |

---

## Contributing to Glossary

Found a term that needs clarification? [Get in touch](https://stratiqx.com/contact).

---

## Next Steps

<div class="next-steps">

**📖 [Quick Reference Card](quick-card.md)** — Field guide with essential formulas

**🔍 [Observable Properties](../framework/observable-properties.md)** — Complete catalog of signals

**📊 [Cascade Analysis Guide](../applications/cascade-analysis.md)** — Apply these terms in practice

**📚 [Case Studies](../applications/case-studies.md)** — See terms used in real examples

</div>

<style>
.next-steps {
  background: #161b22;
  padding: 2rem;
  border-radius: 12px;
  margin: 3rem 0;
  border-left: 4px solid #58a6ff;
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

**Remember:** Precision in language creates precision in analysis. 🪶
