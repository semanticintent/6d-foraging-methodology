# Scoring Methodology

> **"The 3D lens makes impact measurable: Sound × Space × Time"**

Scoring a 6D case happens in two layers:

1. **Dimension scores.** Each dimension the evidence reaches gets a score from 0 to 100, set from cited evidence. Not every case scores all six. The 3D Lens, borrowed from the **Cormorant Foraging Framework**, is a way to think each score through: Sound (urgency), Space (scope) and Time (trajectory).
2. **The case score.** CAL turns the dimension scores into Chirp, DRIFT and FETCH, and compares FETCH with a threshold.

Earlier versions of this page also had severity bands with action deadlines, quick-score ranges and "cascade probability" rules. None of those came from published cases, and they have been removed.

## The 3D Lens

Every problem is scored across three independent factors:

| Lens | What It Measures | Cormorant Integration | Range |
|------|------------------|----------------------|-------|
| **Sound (ChirpIQX)** | **Urgency** — How immediate is the signal? | Aggressive tone, trigger keywords, immediate hooks | 1-10 |
| **Space (PerchIQX)** | **Scope** — How widespread is the impact? | Positioning, strategic framing, affected population | 1-10 |
| **Time (WakeIQX)** | **Trajectory** — Is it improving or degrading? | Past patterns, memory, trend direction | 1-10 |

### Formula

```
Dimension Score = (Sound × Space × Time) ÷ 10
```

**Why divide by 10?**
To put the result on the same 0-100 scale as a case's dimension scores, instead of 1-1000.

## Sound (ChirpIQX): Urgency

**Question:** How immediate is the problem?

| Score | Urgency Level | Characteristics | Example |
|-------|---------------|-----------------|---------|
| **1-3** | **Future Risk** | No immediate impact, theoretical concern | "For future planning...", "Best practice suggests..." |
| **4-6** | **Current Issue** | Active but not critical, manageable | "This is concerning", "We need to address" |
| **7-10** | **Active Crisis** | Immediate action required, severe consequences | "System down", "Legal threat", "Customer canceling" |

### Trigger Keyword Mapping

**High Urgency (Sound = 8-10):**
```
Customer: "canceling", "lawsuit", "unacceptable"
Employee: "I'm done", "burned out", "hostile"
Revenue: "penalty clause", "termination", "write-off"
Regulatory: "violation", "investigation", "subpoena"
Quality: "recall", "safety incident", "injury"
Operational: "system down", "outage", "data loss"
```

**Medium Urgency (Sound = 4-7):**
```
Customer: "disappointed", "reconsidering", "frustrated"
Employee: "overwhelmed", "understaffed", "thankless"
Revenue: "renegotiate", "discount", "delayed payment"
Regulatory: "audit finding", "non-compliance", "remediation required"
Quality: "defect", "rework", "failed inspection"
Operational: "workaround", "bottleneck", "blocked by"
```

**Low Urgency (Sound = 1-3):**
```
Customer: "just wondering", "any updates", "is this normal"
Employee: "just curious", "hypothetically", "work from home policy"
Revenue: "next fiscal year", "budget planning", "exploring options"
Regulatory: "new regulation", "best practice", "voluntary disclosure"
Quality: "workaround", "minor issue", "edge case"
Operational: "inefficient", "nice to have", "process improvement"
```

## Space (PerchIQX): Scope

**Question:** How widespread is the impact?

| Score | Scope Level | Affected Population | Example |
|-------|-------------|---------------------|---------|
| **1-3** | **Isolated** | One person, one customer, one process | Single user bug, individual complaint |
| **4-6** | **Department/Segment** | One team, customer segment, product line | All enterprise customers, entire support team |
| **7-10** | **Enterprise-Wide** | Cross-functional, market-wide, systemic | All customers, entire company, industry impact |

### Measurement Guide

**Customer:**
- 1-3: One customer
- 4-6: Customer segment (e.g., all mid-market)
- 7-10: Market-wide (competitors know, public)

**Employee:**
- 1-3: One person
- 4-6: One team or department
- 7-10: Cross-functional, company-wide

**Revenue:**
- 1-3: One deal
- 4-6: Product line or region
- 7-10: Company-wide revenue impact

**Regulatory:**
- 1-3: One process or location
- 4-6: One department or business unit
- 7-10: Enterprise-wide compliance failure

**Quality:**
- 1-3: One unit or batch
- 4-6: One product or release
- 7-10: All production, systemic design flaw

**Operational:**
- 1-3: One process or system
- 4-6: One department's workflows
- 7-10: Cross-functional, business-critical systems

## Time (WakeIQX): Trajectory

**Question:** Is it getting better or worse?

| Score | Trajectory | Pattern | Example |
|-------|------------|---------|---------|
| **1-3** | **One-Time** | First occurrence, isolated incident | New issue, no history |
| **4-6** | **Recurring** | Pattern emerging, repeated occurrences | Happens weekly, multiple reports |
| **7-10** | **Accelerating** | Trend worsening, spreading, compounding | Exponential growth, viral spread |

### Trend Analysis

**Improving Trajectory (Lower Scores):**
- Issue occurred once, root cause understood
- Problem contained, not spreading
- Fix in progress, resolution visible

**Neutral Trajectory (Middle Scores):**
- Recurring at steady rate
- Pattern established but stable
- No acceleration or deceleration

**Degrading Trajectory (Higher Scores):**
- Frequency increasing
- Severity escalating
- Spreading to new areas/customers

## Dimension Score Calculation

1. **Score each factor (1-10).** Use the anchors above. Write down the evidence behind each one.
2. **Compute the dimension score.** `(Sound × Space × Time) ÷ 10`.
3. **Check it against the evidence.** The number has to be defensible from what you cited. If the evidence is thin, say so through Confidence later, not by nudging the score.

There is no fixed table that turns a dimension score into an action. What to do comes from the case score and the analyst's verdict, below.

## From Dimension Scores to a Verdict: DRIFT, FETCH, and THRESHOLD

Dimension scores tell you *how severe* each affected dimension is. They don't by themselves tell you *what to do*. That's a separate, second calculation — **FETCH** — and it needs two more inputs beyond the dimension scores: **DRIFT** and **CONFIDENCE**.

### DRIFT: the gap between diagnosis and proof

**DRIFT** measures the distance between a claim's *methodology* (how sound is the reasoning?) and its *performance* (how proven is the outcome, in practice, so far?):

```
DRIFT = |METHODOLOGY − PERFORMANCE|
```

Both METHODOLOGY and PERFORMANCE are scored 0–100. A **low** DRIFT means the reasoning and the proof are close together — either both strong (a validated, working thesis) or both weak (an unfounded guess, honestly scored as such). A **high** DRIFT means a real gap between what's diagnosed and what's demonstrated — often the most interesting cases, because they're making a real bet, not just describing what already happened.

### CHIRP: the single-number severity signal

**CHIRP** is the average of the scored dimensions. A dimension the case does not score is left out of the average.

### FETCH: the decision

```
FETCH = CHIRP × DRIFT × CONFIDENCE
```

**CONFIDENCE** (0–1) is the analyst's rating of evidence quality. It is about how good the *evidence* is, not how big the opportunity is. FETCH is then compared against a **THRESHOLD** T (default 1,000):

| FETCH level | When |
|-------------|------|
| **EXECUTE** | FETCH ≥ T (high priority at 2T or above) |
| **CONFIRM** | FETCH ≥ 0.75T |
| **QUEUE** | FETCH ≥ 0.5T |
| **WAIT** | below 0.5T |

These definitions belong to CAL: [CAL spec v1.2.0](https://doi.org/10.5281/zenodo.24090152) (concept DOI [10.5281/zenodo.18905196](https://doi.org/10.5281/zenodo.18905196)).

The case **verdict** is a separate thing: the analyst's reading of the cascade (for example **EXECUTE**, **MONITOR**, **WATCH** or **COUNTER**), recorded next to the score. It does not follow mechanically from FETCH: [UC-335](https://uc-335.stratiqx.com) scores 2,646 and its verdict is MONITOR.

A prognostic case also records triggers and a review date, so it can be graded later against what happened.

### Worked Example: UC-246, "The Actual Intelligence Bet" (Starbucks)

This is a real, [published case](https://uc-246.stratiqx.com) — every number below is exactly what that case computed, not an illustration.

**Origin dimension:** D3 — Employee, scored 88/100 (the $500M+ "coffeehouse coach" labor investment).

UC-246 was published under an earlier numbering, used in cases UC-244 to UC-302, where D3 was Employee and D2 was Revenue. This site now uses D2 Employee and D3 Revenue.

**METHODOLOGY 85** — the diagnosis is well-evidenced: CEO Brian Niccol's own stated reasoning ("Starbucks ran like a manufacturing facility") plus a documented, verifiable $500M+ commitment.
**PERFORMANCE 45** — the outcome is still resolving: comparable sales are recovering (+7.1% North America), but the investment is compressing near-term margins and the ROI hasn't fully proven out yet.

```
DRIFT = |85 − 45| = 40
```

A real, meaningful gap — the reasoning is well ahead of the proof, which is exactly right for a bet that's still playing out.

**CHIRP 76.5**, the average of the six dimension scores: (86 + 78 + 88 + 55 + 82 + 70) ÷ 6 = 76.5.
**CONFIDENCE 0.86** — high, because both halves of the story (the labor investment *and* the AI build happening alongside it) are independently, primary-sourced.

```
FETCH = 76.5 × 40 × 0.86 = 2,632
```

Against a **THRESHOLD of 1,000**, 2,632 is above 2T (2,000), so CAL's level is **EXECUTE, high priority**, and the case's written verdict is **EXECUTE, High Priority** too. The level is what the formula on the case's own page computes, cited to eight sources and [independently checkable](https://uc-246.stratiqx.com). The verdict happens to agree here. It does not always, as UC-335 shows.

## Quick Reference Scoring Guide

### Rapid Assessment (30 seconds)

1. **Is it urgent?** Push Sound up.
2. **Is it widespread?** Push Space up.
3. **Is it getting worse?** Push Time up.

Then go back and find the evidence for each answer.

### Detailed Assessment (5 minutes)

Use the full 3D lens with trigger keyword analysis:

1. **Sound:** Check for trigger keywords in communications
2. **Space:** Count affected entities (customers, employees, systems)
3. **Time:** Review historical data for trend direction

Calculate the dimension score and map cascades.

## Common Scoring Mistakes

### Mistake 1: Confusing Urgency with Importance

❌ **Wrong:** "This is strategically important" → Sound = 9
✅ **Right:** "Is it happening NOW?" → If no, Sound = 1-3

### Mistake 2: Over-Scoping

❌ **Wrong:** "Could eventually affect everyone" → Space = 10
✅ **Right:** "Who is affected TODAY?" → Actual count

### Mistake 3: Wishful Thinking on Trajectory

❌ **Wrong:** "We're working on it, so it's improving" → Time = 2
✅ **Right:** "Is the PROBLEM improving or degrading?" → Check data

### Mistake 4: Ignoring Silent Signals

❌ **Wrong:** "No complaints this week" → All scores low
✅ **Right:** Check leading indicators (usage drops, engagement declines)

## Integration with Cascade Analysis

A high dimension score does not predict how far a cascade will spread. The cascade is mapped separately, from evidence of each step. What the library can show is where cascades have actually gone. For example, in the published library (331 cases with a recorded cascade, as of November 2026, [index](https://uc-000.stratiqx.com)), Regulatory lands in the last layer in 158 cases. See [Cascade Pathways](cascade-pathways.md) for the full counts.

## Next Steps

<div class="next-steps">

**🔄 [Cascade Pathways](cascade-pathways.md)** — Map how problems spread

**📖 [Observable Properties](observable-properties.md)** — Signals that drive scoring

**🎯 [Six Dimensions](../dimensions/customer.md)** — Apply scoring to each dimension

**📊 [Case Studies](../applications/case-studies.md)** — See scoring in action

</div>

<style>
.next-steps {
  background: #161b22;
  padding: 2rem;
  border-radius: 12px;
  margin: 3rem 0;
  border-left: 4px solid #1a237e;
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

**Remember:** Score from evidence. Let CAL compute the level. Write the verdict yourself. 🪶
