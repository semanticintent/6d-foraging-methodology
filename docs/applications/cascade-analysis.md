# Cascade Analysis Guide

> **"The origin is what you see. The cascade is what you live with."**

This guide shows you **how to map and analyze cascades** — how a single dimension, followed honestly, turns into a full, cited, six-dimension picture (see [UC-246](https://uc-246.stratiqx.com) below for a real one).

## Why Cascade Analysis Matters

Most cost analysis stops at the **visible problem**:

- IT issue? Count IT labor hours.
- Customer complaint? Track support tickets.
- Quality defect? Measure rework time.

**They miss the cascade:**

- IT issue → Employee overtime → Quality degradation → Customer churn
- Customer complaint → Revenue risk → Employee morale → More quality issues
- Quality defect → Customer trust loss → Regulatory scrutiny → Operational overhaul

**Cascade analysis reveals the full impact.**

## The 5-Step Cascade Mapping Process

Walked through here using a real, published case — [UC-246](https://uc-246.stratiqx.com), Starbucks' "coffeehouse coach" bet — so every number is checkable, not illustrative.

### Step 1: Identify the Origin Dimension

**Question:** Where did the problem (or the bet, or the event) originate?

| Dimension | Core Signal | Data Source |
|-----------|-------------|-------------|
| **Customer (D1)** | Support tickets, NPS drop, churn notices | CRM, helpdesk |
| **Employee (D2)** | Overtime spike, engagement drop, resignations | HRIS, pulse surveys |
| **Revenue (D3)** | Invoice disputes, payment delays, margin compression | AR aging, financial reports |
| **Regulatory (D4)** | Audit findings, compliance gaps, violations | Compliance tracker, legal |
| **Quality (D5)** | Defect rate spike, customer complaints, rework | QA system, support tickets |
| **Operational (D6)** | System downtime, bottlenecks, manual workarounds | APM, process metrics |

**UC-246:** Starbucks' deliberate, large-scale labor investment.
- **Origin Dimension:** Employee (D3)
- **Direct Signal:** Up to 8,000 "coffeehouse coaches" hired/promoted (~90% internal), on top of a $500M+ "Green Apron Service" labor commitment — Starbucks' largest ever
- **Origin Dimension Score:** 88/100, evidence cited to Starbucks' own newsroom and trade press

### Step 2: Score the Origin

A dimension score can be built from the **3D Lens** (Sound × Space × Time ÷ 10 — see [Scoring Methodology](../framework/scoring.md) for the full mechanics), or scored directly from the evidence against a 0–100 rubric. Either way, what gets published is the **final dimension score with its cited evidence** — not necessarily the specific inputs that produced it, since different cases arrive at their score by whatever route the available evidence actually supports.

Not every case scores all six dimensions. Score the ones you have evidence for, and leave the rest out.

**UC-246's D3 score: 88** — "the entire cascade starts with putting experienced human leaders back on the floor," per the case's own dimension evidence.

### Step 3: Map Primary Cascade Pathways

Real cascades don't carry a probability percentage (see [Cascade Pathways](../framework/cascade-pathways.md) for why assigning one would be false precision). What they carry is **cited evidence at each dimension the cascade actually reaches:**

```
D3 EMPLOYEE (Origin) — score 88
│
├── D1 CUSTOMER — score 86
│   Evidence: the "third place" experience Schultz first saw in Milan;
│   pilot reported "improved customer experiences"
│
└── D5 QUALITY — score 82
    Evidence: on-floor leadership converts effort into consistency;
    pilot reported "more consistent performance"
```

**Where to look next.** The published library ([331 cases with a recorded cascade, as of November 2026](https://uc-000.stratiqx.com)) shows where earlier cascades went. For example, 59 cases start in Employee (D2), and in 31 of them the next layer includes Revenue (D3). Use these counts as a checklist, not a forecast. The full table is on the [Quick Reference Card](../reference/quick-card.md#cascade-pathway-quick-map).

### Step 4: Map Further Cascades

Cascades propagate as far as the evidence actually takes them — for UC-246, two more levels:

```
D1+D5 (Level 1) 
│
└── D2 REVENUE — score 78
    Evidence: Q2 FY2026 comparable sales +6.2% global, +7.1% N. America,
    transactions +3.8% — while the $500M+ investment compresses margins
    │
    └── D6 OPERATIONAL — score 70
        Evidence: Deep Brew (~30% ROI), Green Dot Assist (up to 25%
        faster orders) — where the AI actually lives in this story
        │
        └── D4 REGULATORY — score 55
            Evidence: labor relations backdrop, ~$1B restructuring
            (store closures, layoffs) running in parallel
```

**Cascade notation:** `D3 > D1+D5 > D2 > D6 > D4` — 6 of 6 dimensions, exactly as [published](https://uc-246.stratiqx.com). The case page uses an older numbering (D3 = Employee, D2 = Revenue); in current numbering it reads `D2 > D1+D5 > D3 > D6 > D4`.

### Step 5: Reach a Verdict

This is the step the fictional dollar-multiplier framework skipped entirely — real cases don't sum cascade dollars into a "total impact." They compute **DRIFT** and **FETCH**:

```
METHODOLOGY 85   (the diagnosis is well-evidenced — Niccol's own stated reasoning)
PERFORMANCE 45   (the outcome is still resolving — comps recovering, margins compressed)
DRIFT = |85 − 45| = 40

CHIRP 76.5        (the average of the six dimension scores above)
CONFIDENCE 0.86   (both halves of the story are independently, primary-sourced)
FETCH = 76.5 × 40 × 0.86 = 2,632
```

CAL ([spec v1.2.0](https://doi.org/10.5281/zenodo.24090152)) sets the FETCH level against a threshold T, here the default 1,000: EXECUTE at T or above (high priority at 2T or above), CONFIRM at 0.75T, QUEUE at 0.5T, WAIT below that. FETCH 2,632 is above 2T: **EXECUTE, High Priority**, which is also the verdict this case reached. The verdict is the analyst's own reading, and in other cases it can differ from the level. Full mechanics on [Scoring Methodology](../framework/scoring.md); full narrative on [the case study page](case-studies.md).

## Cascade Analysis Template

Use this template for your own cascade analysis — every field here is something a real, published case actually fills in:

```markdown
# Cascade Analysis: [Event Name]

## Origin Dimension: [Dimension Name]

**Root Cause / Signal:** ________________________________
**Origin Dimension Score (0–100):** ___
**Evidence (cited):** ________________________________

## Cascade Path

### Cascades to: [Dimension]
- **Score (0–100):** ___
- **Evidence (cited):** ________________________________

[Repeat for each dimension the cascade actually reaches — no fixed number of "levels" required]

**Cascade notation:** [e.g. D2 > D1+D5 > D3 > D6 > D4]

## Reaching a Verdict

- **METHODOLOGY (0–100):** ___   (how sound is the reasoning?)
- **PERFORMANCE (0–100):** ___   (how proven is the outcome so far?)
- **DRIFT** = |METHODOLOGY − PERFORMANCE| = ___
- **CHIRP:** ___   (overall severity across the affected dimensions)
- **CONFIDENCE (0–1):** ___   (how well-sourced is the whole analysis?)
- **FETCH** = CHIRP × DRIFT × CONFIDENCE = ___
- **THRESHOLD:** ___ (commonly 1,000)
- **FETCH level:** ___ (EXECUTE ≥ T, high priority ≥ 2T; CONFIRM ≥ 0.75T; QUEUE ≥ 0.5T; WAIT below)
- **Verdict:** ___________ (your reading of the cascade, e.g. EXECUTE, MONITOR, WATCH or COUNTER; it can differ from the FETCH level)
- **If prognostic:** Triggers: ___________  Review date: ___________ (the case gets graded against these later)

## Recommendations

1. ________________________________________
2. ________________________________________
3. ________________________________________
```

## Common Cascade Analysis Mistakes

| Mistake | Impact | How to Avoid |
|---------|--------|--------------|
| **Stopping at the origin dimension** | Misses the actual cascade entirely | Trace evidence to every dimension it genuinely reaches |
| **Assigning a probability to a cascade path** | False precision — implies a repeatable statistic no single case can support | State what's cited, not a likelihood estimate |
| **Inventing a dollar total across dimensions** | Real risk of double-counting the same dollars twice | Score each dimension 0–100; let FETCH weigh them, don't sum them |
| **Skipping METHODOLOGY / PERFORMANCE** | No way to compute DRIFT, so no real FETCH | Always score both explicitly before computing DRIFT |
| **Confidence measuring opportunity size, not evidence quality** | Conflates "this matters a lot" with "this is well-proven" | CONFIDENCE reflects sourcing quality only |

## When to Conduct Cascade Analysis

### High-Priority Scenarios

- **Major incidents** (system outages, security breaches)
- **Customer escalations** (executive complaints, churn threats)
- **Regulatory issues** (audit findings, compliance violations)
- **Strategic decisions** (restructuring, acquisitions, platform migrations)

### Regular Practice

- **Quarterly business reviews** — Analyze the top issues from the quarter
- **Post-incident reviews** — Include cascade analysis in retrospectives
- **Budget planning** — Map which dimensions a known risk could reach
- **Vendor selection** — Trace where a vendor failure would cascade

## Next Steps

<div class="next-steps">

**📊 [Cascade Pathways](../framework/cascade-pathways.md)** — Master map of all cascade patterns

**📖 [Case Studies](case-studies.md)** — More real-world cascade examples

**🔍 [Observable Properties](../framework/observable-properties.md)** — Detect cascade signals early

**🎯 [Scoring Methodology](../framework/scoring.md)** — Calculate dimension scores, DRIFT, and FETCH

</div>

<style>
.next-steps {
  background: #161b22;
  padding: 2rem;
  border-radius: 12px;
  margin: 3rem 0;
  border-left: 4px solid #87ceeb;
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

**Remember:** The dimension you don't check is the one that surprises you. Map the cascade. 🪶
