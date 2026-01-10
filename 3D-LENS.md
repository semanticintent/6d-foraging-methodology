# The 3D Lens: Scoring System

How to score dimensions using Sound, Space, and Time.

---

## Overview

The 3D Lens provides a structured way to evaluate each dimension. Rather than subjective "high/medium/low" assessments, it forces analysis across three distinct lenses.

The metaphor comes from cormorant foraging behavior:
- **Sound (ChirpIQX)** — The urgency call
- **Space (PerchIQX)** — The surveying perch
- **Time (WakeIQX)** — The wake left behind

---

## The Three Lenses

### Sound (ChirpIQX) — Urgency

**Question:** How immediate is this signal?

| Score | Meaning | Indicator |
|-------|---------|-----------|
| 1-2 | Background noise | Theoretical concern, no active signals |
| 3-4 | Early warning | First signals appearing |
| 5-6 | Active concern | Clear signals requiring attention |
| 7-8 | Urgent | Signals demanding immediate action |
| 9-10 | Critical | Crisis-level urgency |

**Ask:**
- Is this happening now or might happen later?
- Are alarms going off?
- Does leadership know?
- Is there time pressure?

---

### Space (PerchIQX) — Scope

**Question:** How widespread is the impact?

| Score | Meaning | Indicator |
|-------|---------|-----------|
| 1-2 | Isolated | Single person/team/instance |
| 3-4 | Contained | One department or product line |
| 5-6 | Spreading | Multiple departments affected |
| 7-8 | Widespread | Organization-wide impact |
| 9-10 | Systemic | Industry/ecosystem-level |

**Ask:**
- Who is affected?
- How many customers/employees/processes?
- Is it contained or spreading?
- Are there geographic or divisional boundaries?

---

### Time (WakeIQX) — Trajectory

**Question:** Is this improving or degrading?

| Score | Meaning | Indicator |
|-------|---------|-----------|
| 1-2 | Resolving | Clear improvement trend |
| 3-4 | Stabilizing | Situation contained, not worsening |
| 5-6 | Static | No clear direction |
| 7-8 | Degrading | Getting worse over time |
| 9-10 | Accelerating | Rapidly worsening |

**Ask:**
- Is the trend line up or down?
- How has this changed over past 30/60/90 days?
- Are interventions working?
- What does the forecast show?

---

## The Scoring Formula

```
Dimension Score = (Sound × Space × Time) ÷ 10
```

### Score Ranges

| Score Range | Interpretation | Action |
|-------------|----------------|--------|
| 0-10 | Low concern | Monitor |
| 11-30 | Moderate concern | Investigate |
| 31-50 | Significant concern | Plan intervention |
| 51-70 | High concern | Immediate action |
| 71-100 | Critical | Crisis response |

### Examples

**Example 1: Minor Issue**
- Sound: 3 (early warning)
- Space: 2 (isolated)
- Time: 4 (stabilizing)
- Score: (3 × 2 × 4) ÷ 10 = **2.4** (Low concern)

**Example 2: Growing Problem**
- Sound: 6 (active concern)
- Space: 5 (spreading)
- Time: 7 (degrading)
- Score: (6 × 5 × 7) ÷ 10 = **21.0** (Moderate concern)

**Example 3: Crisis**
- Sound: 9 (critical)
- Space: 8 (widespread)
- Time: 9 (accelerating)
- Score: (9 × 8 × 9) ÷ 10 = **64.8** (High concern)

---

## Scoring Each Dimension

Apply the 3D lens to each of the six dimensions:

```
┌────────────────┬───────┬───────┬───────┬───────┐
│ Dimension      │ Sound │ Space │ Time  │ Score │
├────────────────┼───────┼───────┼───────┼───────┤
│ Customer       │       │       │       │       │
│ Employee       │       │       │       │       │
│ Revenue        │       │       │       │       │
│ Regulatory     │       │       │       │       │
│ Quality        │       │       │       │       │
│ Operational    │       │       │       │       │
└────────────────┴───────┴───────┴───────┴───────┘
```

---

## Scoring Tips

### Be Evidence-Based

Don't guess. Each score should tie to observable signals:

| Instead of... | Use... |
|---------------|--------|
| "Customers seem unhappy" | "NPS dropped 15 points in 60 days" |
| "Employees are stressed" | "Overtime up 40%, 3 resignations pending" |
| "Revenue is concerning" | "Pipeline velocity down 25% QoQ" |

### Calibrate Across Dimensions

Ensure consistent scoring across dimensions. A "7" in Customer should represent similar severity as a "7" in Employee.

### Document Reasoning

For each score, note:
- What signals support this score?
- What data sources were used?
- What assumptions were made?

### Rescore Regularly

Situations change. Rescore dimensions:
- After major events
- At regular intervals (weekly/monthly)
- When new data emerges

---

## Aggregate Scoring

### Total Dimension Impact

Sum all dimension scores for overall picture:

```
Total Impact Score = Σ(All Dimension Scores)

Example:
Customer:    25.2
Employee:    50.4
Revenue:     72.0
Regulatory:  11.0
Quality:     29.4
Operational: 57.6
─────────────────
Total:      245.6
```

### Dimensions Affected

Count how many dimensions score above threshold (e.g., >10):

```
Dimensions Affected: 5 of 6
```

### Highest Severity

Identify the dimension with highest score for priority focus:

```
Highest: Revenue (72.0)
```

---

## Worked Example: Tailwind CSS

From the [Tailwind case study](https://uc-002.stratiqx.com):

| Dimension | Sound | Space | Time | Score |
|-----------|-------|-------|------|-------|
| Operational (Origin) | 8 | 8 | 9 | 57.6 |
| Employee | 7 | 8 | 9 | 50.4 |
| Revenue | 9 | 8 | 10 | 72.0 |
| Quality | 7 | 7 | 6 | 29.4 |
| Customer | 6 | 7 | 6 | 25.2 |
| Regulatory | — | — | — | N/A |

**Analysis:**
- Revenue is highest concern (72.0) — lifetime license model + 80% decline
- Employee is critical (50.4) — 75% layoff, knowledge loss
- Operational is the origin (57.6) — AI bypass broke the funnel
- 5 of 6 dimensions affected

---

## Common Scoring Mistakes

### Conflating Lenses

❌ **Wrong:** "It's really bad so I'll give it 8/8/8"

✅ **Right:** Evaluate each lens independently:
- Is it urgent (Sound)?
- Is it widespread (Space)?
- Is it getting worse (Time)?

### Anchoring on Origin

❌ **Wrong:** Origin dimension always gets highest score

✅ **Right:** Cascade effects can exceed origin impact

### Ignoring Low Scores

❌ **Wrong:** Only focus on dimensions scoring >50

✅ **Right:** Low-scoring dimensions may be early warning for future cascade

---

*Sound tells you when. Space tells you where. Time tells you which way.* 🐦
