# Cormorant Foraging Integration

> **"The cormorant doesn't just see the fish. It sees depth, current, and trajectory. So should you."**

The 6D Foraging Methodology extends the **Cormorant Foraging** framework — a 3D analytical methodology that evaluates information across **Sound, Space, and Time**.

## What is Cormorant Foraging?

**Cormorant Foraging** is a strategic analysis framework inspired by the hunting patterns of cormorant birds. Just as cormorants analyze their environment across multiple dimensions before diving for prey, the methodology teaches you to analyze information and opportunities across three fundamental lenses:

```
┌─────────────────────────────────────────────┐
│        CORMORANT FORAGING FRAMEWORK         │
├─────────────────────────────────────────────┤
│                                             │
│  🔊 SOUND (ChirpIQX)     → Urgency          │
│     How loud is the signal?                 │
│     How immediate is the need?              │
│                                             │
│  📍 SPACE (PerchIQX)     → Reach/Scope      │
│     How widespread is the impact?           │
│     What is the addressable population?     │
│                                             │
│  ⏱️  TIME (WakeIQX)      → Trajectory       │
│     What is the momentum?                   │
│     Is it growing or declining?             │
│                                             │
└─────────────────────────────────────────────┘
```

**Origin:** Developed for strategic content analysis and business intelligence, the Cormorant Foraging methodology provides a systematic way to evaluate signals, opportunities, and threats.

**Biomimicry principle:** Cormorants hunt by:
1. **Listening** for surface disturbances (Sound)
2. **Observing** fish school size and location (Space)
3. **Tracking** movement patterns and momentum (Time)

## How 6D Extends Cormorant Foraging

The 6D Foraging Methodology applies the **3D lens** (Sound × Space × Time) to each of the **six dimensions** of business impact:

```
┌──────────────────────────────────────────────────────────┐
│              6D + CORMORANT INTEGRATION                  │
├──────────────────────────────────────────────────────────┤
│                                                          │
│      SIX DIMENSIONS          ×        3D LENS            │
│                                                          │
│  ┌─────────────────┐         ┌──────────────────┐       │
│  │ D1: Customer    │         │ Sound (Urgency)  │       │
│  │ D2: Employee    │    ×    │ Space (Scope)    │   =   │
│  │ D3: Revenue     │         │ Time (Trajectory)│       │
│  │ D4: Regulatory  │         └──────────────────┘       │
│  │ D5: Quality     │                                    │
│  │ D6: Operational │         Dimension Score            │
│  └─────────────────┘         (Impact Quantification)    │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**How it combines:**
- Each **dimension** is evaluated through the **3D lens**
- **Sound** measures urgency of signals in that dimension
- **Space** measures scope of impact in that dimension
- **Time** measures trajectory of issues in that dimension

## The 3D Formula

```
Dimension Score = (Sound × Space × Time) ÷ 10

Where:
  Sound = Urgency (1-10)
  Space = Scope (1-10)
  Time = Trajectory (1-10)

Result: Dimension impact score (0.1 - 100)
```

### Example: Customer Dimension Analysis

**Scenario (hypothetical):** Several enterprise customers report billing accuracy concerns

```
Sound (ChirpIQX) = 6
  → Direct complaints (not yet escalated to legal)
  → Medium urgency

Space (PerchIQX) = 7
  → Affecting the whole enterprise customer segment

Time (WakeIQX) = 6
  → Pattern emerging over several weeks
  → Complaints increasing

Customer Dimension Score = (6 × 7 × 6) ÷ 10 = 25.2
```

**Interpretation:** The lens gives you a dimension score you can compare with the others in the same case. It does not set a priority on its own; that comes from FETCH (see below). Whether this reaches Revenue is something to check and cite, not assume.

## Sound, Space, Time — Explained

### Sound (ChirpIQX) — The Urgency Dimension

**Question:** How urgent is this signal?

**Named for:** The "chirp" of the cormorant's call — immediate, attention-grabbing, demanding response.

**In business context:**
- High urgency (8-10): Crisis, immediate action required
- Medium urgency (4-7): Current issue, needs planning
- Low urgency (1-3): Future risk, monitoring needed

**Measurement:**
- Trigger keyword severity
- Customer escalation level
- System criticality
- Regulatory deadline proximity

**Example:** "System down" = Sound 10. "Could be better" = Sound 2.

**Deep dive:** [ChirpIQX (Sound)](chirp.md)

---

### Space (PerchIQX) — The Scope Dimension

**Question:** How widespread is the impact?

**Named for:** The cormorant's perch — the vantage point from which it surveys the entire hunting ground.

**In business context:**
- Wide scope (8-10): Enterprise-wide, all customers, market-wide
- Medium scope (4-7): Department, customer segment, multiple systems
- Narrow scope (1-3): One person/customer, single system, isolated

**Measurement:**
- Number of people/customers affected
- Percentage of systems impacted
- Geographic reach
- Market penetration

**Example:** All customers affected = Space 10. One customer affected = Space 2 or 3.

**Deep dive:** [PerchIQX (Space)](perch.md)

---

### Time (WakeIQX) — The Trajectory Dimension

**Question:** Is it getting better or worse?

**Named for:** The "wake" left by fish — the trail that reveals direction and momentum.

**In business context:**
- Accelerating (8-10): Chronic, worsening, pattern established
- Recurring (4-7): Sustained pressure, happening regularly
- One-time (1-3): Isolated incident, first occurrence

**Measurement:**
- Trend analysis (improving vs. degrading)
- Frequency of occurrence
- Pattern duration
- Velocity of change

**Example:** Issue recurring weekly for 3 months = Time 7. First-time occurrence = Time 2.

**Deep dive:** [WakeIQX (Time)](wake.md)

## From Dimension Scores to a Verdict

The 3D Lens builds dimension scores. Turning them into a case score is CAL's job ([CAL spec v1.2.0](https://doi.org/10.5281/zenodo.24090152); concept DOI [10.5281/zenodo.18905196](https://doi.org/10.5281/zenodo.18905196)):

```
Chirp      = average of the scored dimensions (0-100)
DRIFT      = |Methodology − Performance|
Confidence = the analyst's 0-1 rating of evidence quality
FETCH      = Chirp × DRIFT × Confidence

Threshold T (default 1,000):
  EXECUTE  FETCH ≥ T   (high priority at ≥ 2T)
  CONFIRM  FETCH ≥ 0.75T
  QUEUE    FETCH ≥ 0.5T
  WAIT     below 0.5T
```

There is no weighted sum of Sound × Space × Time across dimensions. Score only the dimensions you have evidence for; not every case scores all six. The written verdict (EXECUTE, MONITOR, WATCH, COUNTER…) is the analyst's own reading and can differ from the FETCH level.

**Name clash to watch:** CAL's **Chirp** (the average of dimension scores) is not **ChirpIQX** (the Sound lens).

**Real example:** [UC-246](https://uc-246.stratiqx.com) (Starbucks) scored FETCH 2,632 against T = 1,000: EXECUTE, high priority. See the [Case Studies](../applications/case-studies.md) page.

## Why This Integration Works

### 1. Consistency Across Dimensions

The 3D lens provides a **universal scoring method** that works for all six dimensions:
- Customer urgency vs. Regulatory urgency? Both use Sound (1-10).
- Employee scope vs. Operational scope? Both use Space (1-10).
- Quality trajectory vs. Revenue trajectory? Both use Time (1-10).

**Benefit:** Apples-to-apples comparison across different problem types.

### 2. Captures unmeasured patterns

Traditional analysis asks: "How much did this cost?"

**Cormorant Foraging + 6D asks:**
- How **urgent** is this across all dimensions? (Sound)
- How **widespread** is the impact? (Space)
- Is it **accelerating** or stabilizing? (Time)

**Benefit:** Shows the spread before it turns up in hard costs.

### 3. Predictive, Not Just Reactive

The **Time (WakeIQX)** dimension makes analysis forward-looking:
- Isolated incident (Time = 2) → Monitor
- Recurring pattern (Time = 6) → Act now
- Accelerating crisis (Time = 9) → Emergency response

**Benefit:** Intervention before cascade reaches maximum depth.

## Practical Application

### Step 1: Identify Affected Dimensions

Check all six dimensions for observable signals:

```
□ Customer: Support tickets, NPS, churn signals
□ Employee: Overtime, engagement, turnover
□ Revenue: AR aging, discounts, pipeline
□ Regulatory: Audit findings, compliance gaps
□ Quality: Defects, rework, complaints
□ Operational: Downtime, bottlenecks, workarounds
```

### Step 2: Apply 3D Lens to Each

For each affected dimension, score:

```
Sound (1-10): ___ [How urgent?]
Space (1-10): ___ [How widespread?]
Time (1-10):  ___ [Improving or worsening?]

Dimension Score = (Sound × Space × Time) ÷ 10
```

### Step 3: Map Cascades

Write the cascade in notation, origin first: e.g. `D5>D2+D6>D4+D1`. A high lens score does not tell you where the cascade goes; the evidence does.

For a starting checklist, use the counts from the [published library](https://uc-000.stratiqx.com) (331 cases with a recorded cascade, as of November 2026). For example, 74 cases start in Operational, and the next layer includes Revenue in 55 of them. These are counts, not probabilities. Full table on the [Quick Reference Card](../reference/quick-card.md#cascade-pathway-quick-map).

### Step 4: Score the Case

Use CAL to turn the dimension scores into Chirp, DRIFT, Confidence and FETCH, then compare FETCH with the threshold (see [above](#from-dimension-scores-to-a-verdict)).

## ChirpIQX, PerchIQX, WakeIQX — The Names

### ChirpIQX (Sound)
**"Chirp"** = The audible signal, the call to attention

**Meaning:** Intelligence for urgency signals.

### PerchIQX (Space)
**"Perch"** = The elevated vantage point, the surveying position

**Meaning:** Intelligence for scope assessment.

### WakeIQX (Time)
**"Wake"** = The trail left behind, the momentum indicator

**Meaning:** Intelligence for trajectory analysis.

## Integration Benefits Summary

| Benefit | How Cormorant Foraging Delivers |
|---------|--------------------------------|
| **Objectivity** | Numerical scoring (1-10) reduces subjective bias |
| **Completeness** | 3D lens ensures no dimension overlooked (urgency, scope, trajectory) |
| **Comparability** | Same scale across all six dimensions |
| **Predictiveness** | Time dimension reveals accelerating patterns |
| **Speed** | Simple formula, rapid assessment |
| **Communication** | "Sound 8, Space 7, Time 6" is clear and actionable |

## Real-World Example: Integration in Action

Earlier versions of this page used a made-up resignation scenario with invented costs and a "total 6D score". It has been removed. Here is what an Employee-origin cascade looks like in the published library instead:

- [UC-341: Three Stars, Three Exits](https://uc-341.stratiqx.com): `D2>D4+D3>D6+D1` (diagnostic)
- [UC-320: Less Heads, More Heads](https://uc-320.stratiqx.com): `D2>D3+D6` (diagnostic)

Across the library, 59 cases start in Employee. The next layer includes Revenue in 31 of them, Operational in 27, Quality in 18 and Customer in 13.

**How the lens fits in:** For each dimension a case reaches, Sound, Space and Time help you reason about urgency, scope and trajectory before you settle on a 0-100 score. The case's score, level and verdict then come from CAL, and every step is cited.

## Next Steps: Deep Dives

<div class="next-steps">

**🔊 [ChirpIQX (Sound)](chirp.md)** — Master urgency scoring across dimensions

**📍 [PerchIQX (Space)](perch.md)** — Measure scope and reach accurately

**⏱️ [WakeIQX (Time)](wake.md)** — Analyze trajectories and predict momentum

**📊 [Scoring Methodology](../framework/scoring.md)** — Apply 3D lens in practice

**🔍 [Observable Properties](../framework/observable-properties.md)** — Detect signals for each dimension

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

**Remember:** The cormorant doesn't dive blind. It reads the water. You shouldn't analyze blind either. Read the signals. 🪶
