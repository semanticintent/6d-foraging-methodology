# Quick Reference Card

> **"Print this. Keep it on your desk. Use it when problems hit."**

This is your **field guide** to the 6D Foraging Methodology. It is built for quick reference during incident response, case analysis, or strategic planning.

## Dimension Checklist

Use this checklist to make sure you look at all six dimensions:

| ☑ | Dimension | Core Question | Key Metric |
|---|-----------|---------------|------------|
| □ | **D1: Customer** | How does this affect who pays us? | NPS, Churn Rate |
| □ | **D2: Employee** | How does this affect who works for us? | Turnover, Engagement |
| □ | **D3: Revenue** | How does this affect money coming in? | AR Aging, Margin |
| □ | **D4: Regulatory** | How does this affect our compliance? | Audit Findings, Fines |
| □ | **D5: Quality** | How does this affect what we deliver? | Defect Rate, Rework |
| □ | **D6: Operational** | How does this affect how we work? | Uptime, Cycle Time |

**Usage:** For any problem, check each box and write down the observable signals, with a source for each. Score each dimension you have evidence for from 0 to 100. Not every case scores all six; leave a dimension out rather than guess.

---

## 3D Quick Reference (Sound × Space × Time)

The 3D Lens is one way to build a dimension score:

| Lens | Question | Low (1-3) | Medium (4-6) | High (7-10) |
|------|----------|-----------|--------------|-------------|
| **Sound (Urgency)** | How urgent is this? | Future risk<br/>Minor issue<br/>No immediate action | Current issue<br/>Affecting operations<br/>Needs attention | Crisis<br/>Business-critical<br/>Immediate response |
| **Space (Scope)** | How widespread? | Isolated<br/>One person/customer<br/>Single system | Department<br/>Customer segment<br/>Multiple systems | Enterprise-wide<br/>All customers<br/>Market-wide |
| **Time (Trajectory)** | Getting better or worse? | One-time event<br/>Isolated incident<br/>First occurrence | Recurring pattern<br/>Happening monthly<br/>Sustained pressure | Accelerating trend<br/>Worsening quickly<br/>Chronic condition |

**Formula:** `Dimension Score = (Sound × Space × Time) ÷ 10`

**Example (hypothetical inputs):**
```
Problem: Customer complaint from enterprise account
Sound = 6 (direct complaint, not yet escalated)
Space = 5 (one customer, but enterprise tier)
Time = 4 (second occurrence this month)

Score = (6 × 5 × 4) ÷ 10 = 12
```

The lens helps you build and compare dimension scores. It does not set a priority on its own. The priority level comes from FETCH, below.

---

## Verdict Quick Reference (CAL)

Scoring belongs to CAL, the Cascade Analysis Language ([CAL spec v1.2.0](https://doi.org/10.5281/zenodo.24090152); concept DOI [10.5281/zenodo.18905196](https://doi.org/10.5281/zenodo.18905196)).

```
Chirp      = average of the scored dimensions (0-100)
DRIFT      = |Methodology − Performance|
Confidence = your 0-1 rating of evidence quality
FETCH      = Chirp × DRIFT × Confidence
```

Compare FETCH with a threshold **T** (default 1,000):

| FETCH level | Rule | At T = 1,000 |
|-------------|------|--------------|
| **EXECUTE** (high priority) | FETCH ≥ 2T | 2,000 or more |
| **EXECUTE** | FETCH ≥ T | 1,000 or more |
| **CONFIRM** | FETCH ≥ 0.75T | 750 or more |
| **QUEUE** | FETCH ≥ 0.5T | 500 or more |
| **WAIT** | below 0.5T | under 500 |

**Real example:** [UC-246](https://uc-246.stratiqx.com) (Starbucks) scored FETCH 2,632 against T = 1,000. That is above 2T, so the level is EXECUTE, high priority.

**The verdict is separate.** A case's written verdict (EXECUTE, MONITOR, WATCH, COUNTER…) is the analyst's reading of the cascade. It can differ from the FETCH level. Prognostic cases also record triggers and a review date, and get graded later.

---

## Cascade Pathway Quick Map

Write the cascade in notation: origin first, then each layer it reaches. `>` means "cascades to", `+` means "in the same layer". Example: `D5>D2+D6>D4+D1`.

Where cascades went next in the published library ([331 cases with a recorded cascade, as of November 2026](https://uc-000.stratiqx.com)). These are counts, not probabilities:

| Origin | Cases | Next layer most often includes |
|--------|-------|--------------------------------|
| **D1 Customer** | 50 | Revenue 29 · Quality 26 · Operational 23 |
| **D2 Employee** | 59 | Revenue 31 · Operational 27 · Quality 18 |
| **D3 Revenue** | 96 | Operational 65 · Customer 43 · Quality 32 |
| **D4 Regulatory** | 57 | Revenue 36 · Operational 29 · Customer 25 |
| **D5 Quality** | 81 | Operational 45 · Revenue 39 · Customer 29 |
| **D6 Operational** | 74 | Revenue 55 · Quality 35 · Customer 33 |

A case can name more than one origin, and a layer can hold several dimensions, so the counts overlap.

**Where cascades end:** Regulatory lands in the last layer in 158 of 331 cases, more than any other dimension. Operational is reached in some layer in 312 of 331.

**Usage:** Start with the origin dimension. Use the table as a list of where to look next, then cite what you actually find. A count tells you where earlier cases went, not where yours will go.

---

## Trigger Keyword Urgency Guide

Quick reference for keyword severity scoring:

### High Urgency (Sound = 8-10)
```
"unacceptable"      "breach"           "lawsuit"
"canceling"         "violation"        "investigation"
"recall"            "system down"      "data breach"
"injury"            "fraud"            "immediate jeopardy"
"P1/Sev1"           "outage"           "critical"
```
**Action:** Escalate to leadership now.

### Medium Urgency (Sound = 4-7)
```
"disappointed"      "concerned"        "audit finding"
"rework"            "defect"           "delayed"
"bottleneck"        "frustrated"       "non-compliance"
"bug"               "downtime"         "overtime"
```
**Action:** Manager review soon.

### Low Urgency (Sound = 1-3)
```
"just wondering"    "for future"       "nice to have"
"minor issue"       "cosmetic"         "inefficient"
"tech debt"         "someday"          "could be better"
```
**Action:** Track the pattern over time.

---

## Analysis Decision Tree

```
Problem Detected
      │
      ▼
┌─────────────────┐
│ Which           │   Check all six. Record a cited
│ dimensions show │   signal for each one you score.
│ evidence?       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Score each      │   0-100 from evidence
│ dimension       │   (3D Lens is one route)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Write the       │   e.g. D5>D2+D6>D4+D1
│ cascade         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Chirp, DRIFT,   │   FETCH = Chirp × DRIFT
│ Confidence      │           × Confidence
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ FETCH vs T      │   EXECUTE ≥ T (high ≥ 2T)
│                 │   CONFIRM ≥ 0.75T
│                 │   QUEUE ≥ 0.5T, else WAIT
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Write your      │   Can differ from the level.
│ verdict         │   Prognostic? Add triggers
│                 │   and a review date.
└─────────────────┘
```

---

## 5-Minute Analysis Template

Use this for rapid assessment:

```
PROBLEM: _______________________________________

ORIGIN DIMENSION: □ Customer  □ Employee  □ Revenue
                  □ Regulatory □ Quality  □ Operational

AFFECTED DIMENSIONS (score only those with evidence, 0-100):
  □ D1: Customer     Score: ___  Evidence: _______________
  □ D2: Employee     Score: ___  Evidence: _______________
  □ D3: Revenue      Score: ___  Evidence: _______________
  □ D4: Regulatory   Score: ___  Evidence: _______________
  □ D5: Quality      Score: ___  Evidence: _______________
  □ D6: Operational  Score: ___  Evidence: _______________

CASCADE: ___ > ___ > ___   (e.g. D5>D2+D6>D4+D1)

SCORING (CAL):
  Chirp (average of scored dimensions): ___
  Methodology (0-100): ___   Performance (0-100): ___
  DRIFT = |Methodology − Performance| = ___
  Confidence (0-1, evidence quality): ___
  ═══════════════════════
  FETCH = Chirp × DRIFT × Confidence = ___
  Threshold T: ___ (default 1,000)

FETCH LEVEL:
  □ EXECUTE (≥ T; high priority ≥ 2T)
  □ CONFIRM (≥ 0.75T)
  □ QUEUE   (≥ 0.5T)
  □ WAIT    (below 0.5T)

VERDICT (your reading): _______________
  Prognostic? Triggers: ___________  Review date: ________
```

---

## Industry-Specific Quick Adjustments

### Healthcare
- **Customer → Patient Outcomes** (HCAHPS, readmissions)
- **Cascade worth checking early:** Quality → Regulatory

### Financial Services
- **Customer → Client Trust** (AUM flows)
- **Cascade worth checking early:** Quality → Customer

### Manufacturing
- **Operational → Production Efficiency** (OEE)
- **Cascade worth checking early:** Operational → Revenue

### SaaS
- **Customer → User Experience** (NPS, adoption)
- **Cascade worth checking early:** Operational → Customer

These are starting points for your own checks, not measured industry rates. See [Industry Variations](../applications/industry-variants.md).

---

## Common Analysis Mistakes (Avoid These)

| ❌ Don't | ✅ Do |
|---------|------|
| Stop at the origin dimension | Trace the cascade as far as the evidence goes |
| Score a dimension you have no evidence for | Leave it out; not every case scores all six |
| Put a probability on a cascade path | Record what you cited; use library counts only as a guide |
| Multiply a direct cost into a "total impact" | Score each dimension 0-100 and let FETCH weigh them |
| Use Confidence for how big the issue is | Confidence rates evidence quality only |
| Treat the FETCH level as the verdict | Write your verdict separately; it can differ |

---

## Printable Version

<div class="printable-card">

### 6D IMPACT QUICK CARD

**DIMENSIONS:** D1 Customer | D2 Employee | D3 Revenue | D4 Regulatory | D5 Quality | D6 Operational (each 0-100 from cited evidence)

**3D LENS:** Sound (Urgency) × Space (Scope) × Time (Trajectory) ÷ 10

**CAL SCORING:**
- Chirp = average of scored dimensions
- DRIFT = |Methodology − Performance|
- FETCH = Chirp × DRIFT × Confidence
- T default 1,000: EXECUTE ≥ T (high ≥ 2T), CONFIRM ≥ 0.75T, QUEUE ≥ 0.5T, else WAIT
- Verdict is the analyst's reading and can differ

**URGENCY:**
- High (8-10): "lawsuit", "breach", "system down", "P1"
- Medium (4-7): "defect", "delayed", "concerned", "audit"
- Low (1-3): "minor", "someday", "inefficient", "tech debt"

**NEXT LAYER, BY ORIGIN (counts from 331 published cases):**
- Customer (50): Revenue 29, Quality 26
- Employee (59): Revenue 31, Operational 27
- Revenue (96): Operational 65, Customer 43
- Regulatory (57): Revenue 36, Operational 29
- Quality (81): Operational 45, Revenue 39
- Operational (74): Revenue 55, Quality 35
- Regulatory is the last layer in 158 of 331

</div>

<style>
.printable-card {
  background: white;
  color: black;
  padding: 2rem;
  border: 2px solid #333;
  margin: 2rem 0;
  font-family: monospace;
  page-break-inside: avoid;
}

@media print {
  .printable-card {
    page-break-before: always;
  }
}
</style>

---

## Digital Quick Tools

### Bookmarklet (Add to Browser)

```javascript
javascript:(function(){
  var c=parseFloat(prompt("Chirp (average of scored dimensions)?"));
  var d=parseFloat(prompt("DRIFT (|Methodology - Performance|)?"));
  var k=parseFloat(prompt("Confidence (0-1)?"));
  var t=parseFloat(prompt("Threshold T?","1000"));
  var f=Math.round(c*d*k);
  var l=f>=2*t?"EXECUTE (high priority)":f>=t?"EXECUTE":f>=0.75*t?"CONFIRM":f>=0.5*t?"QUEUE":"WAIT";
  alert("FETCH: "+f.toLocaleString()+"\nLevel: "+l);
})();
```

**Instructions:** Drag to bookmarks bar, click when scoring a case.

---

## Next Steps

<div class="next-steps">

**📊 [Full Scoring Methodology](../framework/scoring.md)** — Detailed scoring process

**🔍 [Observable Properties](../framework/observable-properties.md)** — Complete signal catalog

**📖 [Cascade Analysis Guide](../applications/cascade-analysis.md)** — Step-by-step cascade mapping

**📚 [Case Studies](../applications/case-studies.md)** — A real, cited case worked through

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

**Remember:** Speed matters in incident response. This card gets you to a first, cited read fast. 🪶
