# ChirpIQX: Sound (Urgency)

> **"The loudest signals demand immediate attention. Learn to distinguish the chirp from the noise."**

**ChirpIQX** is the **urgency dimension** of the 3D lens. It measures how immediate, critical, or time-sensitive a signal is across any of the six dimensions.

::: tip Not the same as CAL's Chirp
In CAL scoring, **Chirp** is the average of a case's scored dimensions, one input to FETCH. **ChirpIQX** is the Sound lens on this page. They share a name, not a formula. See the [Glossary](../reference/glossary.md#chirp).
:::

## What is Sound/Urgency?

**Core question:** How urgent is this signal?

**Named for:** The "chirp" of the cormorant's call — sharp, immediate, cutting through ambient noise to demand attention.

**In business context:** The urgency of a problem determines response speed:
- **High urgency (8-10):** Drop everything, executive escalation, war room
- **Medium urgency (4-7):** Plan response, manager involvement
- **Low urgency (1-3):** Monitor, log for patterns, address in normal workflow

## The Sound Scale (1-10)

```
┌──────────────────────────────────────────────────────────┐
│                    CHIRP IQX SCALE                       │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  10 │ CRITICAL EMERGENCY                                │
│     │ • System failure preventing business operations   │
│     │ • Imminent safety threat, life-threatening        │
│     │ • Legal deadline about to expire                  │
│     │ • Customer threatening lawsuit/termination        │
│     │ Action: All-hands, immediate executive escalation │
│     │                                                    │
│   9 │ SEVERE URGENCY                                    │
│     │ • Major system degradation affecting customers    │
│     │ • Regulatory violation with immediate consequences│
│     │ • Key employee resignation (critical role)        │
│     │ • Enterprise customer escalation to C-suite       │
│     │ Action: War room, executive sponsor assigned      │
│     │                                                    │
│   8 │ HIGH URGENCY                                      │
│     │ • Significant operational bottleneck              │
│     │ • Quality defect customer-reported                │
│     │ • Revenue risk current quarter                    │
│     │ • Compliance deadline close                       │
│     │ Action: Senior management review                  │
│     │                                                    │
│   7 │ ELEVATED URGENCY                                  │
│     │ • Customer complaint (direct, actionable)         │
│     │ • Employee burnout signals (overtime pattern)     │
│     │ • Audit finding (remediation required)            │
│     │ • Quality trend worsening                         │
│     │ Action: Manager review                            │
│     │                                                    │
│   6 │ MODERATE-HIGH URGENCY                             │
│     │ • Renewal hesitation from customer                │
│     │ • Process inefficiency causing delays             │
│     │ • Technical debt impacting velocity               │
│     │ • Revenue pipeline slippage                       │
│     │ Action: Team lead review                          │
│     │                                                    │
│   5 │ MODERATE URGENCY                                  │
│     │ • Customer feedback (constructive)                │
│     │ • Employee morale concern (manageable)            │
│     │ • Minor quality issue (internal catch)            │
│     │ • Process improvement opportunity                 │
│     │ Action: Plan in next sprint/planning cycle        │
│     │                                                    │
│   4 │ LOW-MODERATE URGENCY                              │
│     │ • Feature request (nice-to-have)                  │
│     │ • Efficiency optimization opportunity             │
│     │ • Minor compliance gap (no deadline)              │
│     │ • Employee suggestion                             │
│     │ Action: Backlog prioritization                    │
│     │                                                    │
│   3 │ LOW URGENCY                                       │
│     │ • Future planning inquiry                         │
│     │ • Process documentation need                      │
│     │ • Tech debt (not blocking)                        │
│     │ • Cosmetic defect                                 │
│     │ Action: Quarterly review, log for patterns        │
│     │                                                    │
│   2 │ MINIMAL URGENCY                                   │
│     │ • General inquiry                                 │
│     │ • Long-term strategic question                    │
│     │ • Informational request                           │
│     │ • Nice-to-have enhancement                        │
│     │ Action: Standard response, no escalation          │
│     │                                                    │
│   1 │ NO URGENCY                                        │
│     │ • Hypothetical scenario                           │
│     │ • Distant future consideration                    │
│     │ • Idle curiosity                                  │
│     │ • Already resolved                                │
│     │ Action: Acknowledge only, no action               │
│     │                                                    │
└──────────────────────────────────────────────────────────┘
```

## Sound Scoring by Dimension

Each dimension has unique urgency indicators. Here's how to score urgency in each:

### D1: Customer (ChirpIQX)

| Sound | Signal Type | Example |
|-------|-------------|---------|
| **10** | Legal threat, immediate termination | "Our attorney will contact you" |
| **9** | Executive escalation, public threat | "I'm calling your CEO", "Going to social media" |
| **8** | Contract breach claim, churn notice | "This violates our SLA", "Canceling effective immediately" |
| **7** | Direct complaint, renewal risk | "Very disappointed", "Reconsidering renewal" |
| **6** | Service concern, hesitation | "Not meeting expectations", "Concerned about quality" |
| **5** | Constructive feedback | "Could be improved", "Feature request" |
| **4** | Minor inquiry | "How does this work?", "Question about..." |
| **3** | General question | "Just wondering", "For future reference" |
| **2** | Positive feedback | "Working well", "Thank you" |
| **1** | Idle curiosity | "What if...", "Hypothetically..." |

**Measurement sources:**
- Support ticket severity tags
- Email sentiment analysis
- Sales call notes (CRM)
- NPS verbatim comments
- Customer health score

### D2: Employee (ChirpIQX)

| Sound | Signal Type | Example |
|-------|-------------|---------|
| **10** | Safety incident, harassment claim | "Unsafe working conditions", "Hostile environment" |
| **9** | Resignation (critical role) | "Putting in my two weeks", "Accepted another offer" |
| **8** | Burnout / breaking point | "Can't do this anymore", "At my limit" |
| **7** | Sustained stress, overtime pattern | "Overwhelmed", "No work-life balance" |
| **6** | Workload concern, support needed | "Need help", "Understaffed" |
| **5** | Morale issue, recognition gap | "Underappreciated", "Not valued" |
| **4** | Career development inquiry | "Growth opportunities?", "Training available?" |
| **3** | Policy question | "Remote work policy?", "PTO accrual?" |
| **2** | General engagement | "How's everyone doing?", Team feedback |
| **1** | Casual conversation | Water cooler talk, non-work topics |

**Measurement sources:**
- Overtime hours (HRIS)
- Pulse survey responses
- 1:1 meeting notes
- Resignation notices
- Exit interview data

### D3: Revenue (ChirpIQX)

| Sound | Signal Type | Example |
|-------|-------------|---------|
| **10** | Payment stopped, lawsuit | "Wire reversed", "Withholding payment pending legal" |
| **9** | Contract termination, write-off | "Terminating for cause", "Uncollectible" |
| **8** | Invoice dispute, penalty invoked | "We're not paying this", "Invoking penalty clause" |
| **7** | Discount demanded, payment delayed | "Need better pricing", "Extending payment terms" |
| **6** | Renegotiation request | "Let's discuss pricing", "Budget pressure" |
| **5** | Procurement review | "Vendor assessment", "Cost analysis" |
| **4** | Budget planning inquiry | "Next fiscal year pricing?", "Volume discounts?" |
| **3** | Renewal discussion (early) | "Contract expires next year", Planning conversation |
| **2** | Upsell opportunity | "What else do you offer?", Expansion interest |
| **1** | General inquiry | "How does billing work?", Informational only |

**Measurement sources:**
- AR aging reports (overdue invoices)
- Payment velocity tracking
- Sales pipeline stage changes
- Contract renewal dates
- Discount approval requests

### D4: Regulatory (ChirpIQX)

| Sound | Signal Type | Example |
|-------|-------------|---------|
| **10** | Enforcement action, license suspension | "Operating authority suspended", "Cease operations" |
| **9** | Investigation launched, subpoena | "SEC investigation", "Subpoena received" |
| **8** | Violation notice, fine assessed | "NOV issued", "Penalty assessed" |
| **7** | Audit finding (critical), deadline imminent | "Material weakness", "Remediate within 30 days" |
| **6** | Non-compliance identified | "Gap found in audit", "Deficiency noted" |
| **5** | Certification lapse approaching | "Renewal due in 60 days", "Training expiring" |
| **4** | Policy update needed | "New regulation published", "Guidance issued" |
| **3** | Best practice gap | "Industry standard not met", "Voluntary improvement" |
| **2** | Proactive review | "Self-assessment", "Internal audit scheduled" |
| **1** | Informational | "Proposed rule (comment period)", Future regulation |

**Measurement sources:**
- Compliance management system
- Audit reports (internal/external)
- Legal correspondence
- Regulatory filings
- Certification tracking

### D5: Quality (ChirpIQX)

| Sound | Signal Type | Example |
|-------|-------------|---------|
| **10** | Safety incident, recall | "Injury occurred", "Recall initiated" |
| **9** | Critical defect (customer-impacting) | "Data loss", "System failure" |
| **8** | Major defect, customer complaint | "Product doesn't work", "Complete failure" |
| **7** | Functional defect, rework required | "Out of spec", "Failed inspection" |
| **6** | Quality issue (customer-reported) | "Bug reported", "Not as expected" |
| **5** | Quality issue (internal catch) | "Defect found in QA", "Needs rework" |
| **4** | Process deviation (minor) | "Workaround used", "Non-standard approach" |
| **3** | Quality improvement opportunity | "Could be better", "Optimization idea" |
| **2** | Cosmetic issue | "Minor visual defect", "Doesn't affect function" |
| **1** | Enhancement idea | "Nice-to-have feature", Future improvement |

**Measurement sources:**
- Defect tracking system (JIRA, etc.)
- Customer complaints (support tickets)
- QA test results
- Inspection reports
- RMA/return data

### D6: Operational (ChirpIQX)

| Sound | Signal Type | Example |
|-------|-------------|---------|
| **10** | System down, business halted | "Production stopped", "Cannot operate" |
| **9** | Critical system failure | "P1 incident", "Data corruption" |
| **8** | Major bottleneck, significant delay | "Line down", "All hands required" |
| **7** | System degradation, workaround needed | "Performance issues", "Manual process required" |
| **6** | Process inefficiency, delays | "Bottleneck forming", "Capacity constraint" |
| **5** | Resource contention | "Waiting on...", "Blocked by..." |
| **4** | Optimization opportunity | "Could be faster", "Automation candidate" |
| **3** | Process improvement idea | "Streamlining opportunity", "Tech debt" |
| **2** | Minor friction | "Slight delay", "Small inefficiency" |
| **1** | Informational | "How does this work?", Process question |

**Measurement sources:**
- APM / monitoring tools
- Incident management system
- Process metrics dashboards
- Resource utilization reports
- Project management tools

## Trigger Keywords → Sound Mapping

Use this quick reference to map keywords to Sound scores:

### Sound = 10 (Critical)
```
"system down"          "data loss"            "safety incident"
"life-threatening"     "lawsuit filed"        "license suspended"
"immediate jeopardy"   "critical failure"     "cannot operate"
```

### Sound = 9 (Severe)
```
"investigation"        "resignation"          "P1/Sev1"
"major incident"       "breach"               "violation"
"escalating to CEO"    "data breach"          "all-hands"
```

### Sound = 8 (High)
```
"canceling"            "unacceptable"         "critical defect"
"invoice dispute"      "deadline this week"   "audit failure"
"material weakness"    "contract breach"      "major outage"
```

### Sound = 7 (Elevated)
```
"disappointed"         "concerned about"      "audit finding"
"rework required"      "bottleneck"           "burnout"
"compliance gap"       "defect reported"      "overtime pattern"
```

### Sound = 6 (Moderate-High)
```
"reconsidering"        "need help"            "delayed"
"frustrated"           "not meeting spec"     "capacity issue"
"budget pressure"      "renewal risk"         "quality concern"
```

### Sound = 5 (Moderate)
```
"could be better"      "feedback"             "suggestion"
"improvement"          "optimization"         "concerned"
"renegotiate"          "minor issue"          "needs attention"
```

### Sound = 4-1 (Low to None)
```
"nice to have"         "future"               "just wondering"
"someday"              "hypothetically"       "curious"
"long-term"            "cosmetic"             "minor"
```

## Contextual Adjustments

Base Sound score can be **adjusted** based on context:

How far to move the score is your judgment. Write down the reason, so someone else can check it.

### Amplifiers (raise Sound)
- **Repeated occurrence:** "This is the third time..."
- **Time pressure:** "Deadline tomorrow"
- **Stakeholder level:** "Board is asking..."
- **Public visibility:** "On social media"
- **Financial materiality:** a large amount at stake

### Dampeners (lower Sound)
- **Hypothetical:** "What if..."
- **Future-dated:** "Next year..."
- **Already resolved:** "Was an issue, now fixed"
- **Uncertain:** "Might happen"
- **Non-critical timing:** "When you get a chance"

### Example: Context Changes Score

**Base scenario:** Customer says "disappointed" (Sound 7 on the D1 table above)

**With amplifiers, Sound goes up:**
- "Disappointed **for the third time** this month"
- "Disappointed and **escalating to your CEO**" (Sound 9 on the D1 table)

**With dampeners, Sound goes down:**
- "**Might be** disappointed if..."
- "Was disappointed, **but you fixed it**"

## Urgency Decay Over Time

Unanswered urgency tends to **escalate**, not fade:

```
Customer complaint            (Sound 7)
No response → escalation      (Sound 9)
Still no action → canceling   (Sound 8-10)
```

**Lesson:** High Sound scores demand **speed**. Delay amplifies urgency.

## Multi-Signal Urgency

When **multiple signals** appear in one dimension:

**Rule:** Use the **highest** Sound score, not average.

**Example:**
- Signal A: "Minor issue" (Sound = 3)
- Signal B: "System down" (Sound = 10)

**Dimension Sound score:** 10 (not 6.5 average)

**Why:** One critical signal demands critical response, regardless of other minor signals.

## ChirpIQX in Cascade Analysis

A high Sound score tells you to look fast. It does not tell you how fast the cascade will move or where it will go. Earlier versions of this page had a table mapping Sound to "time to next dimension". Those timings were invented and have been removed.

What the evidence can tell you is **where earlier cascades went next**. In the [published library](https://uc-000.stratiqx.com) (331 cases with a recorded cascade, as of November 2026), 74 cases start in Operational; the next layer includes Revenue in 55 of them and Customer in 33. These are counts, not probabilities. See the full table on the [Quick Reference Card](../reference/quick-card.md#cascade-pathway-quick-map).

## Sound Scoring Checklist

Use this checklist when scoring urgency:

```
□ What trigger keywords are present? (See keyword table)
□ What is the escalation level? (Team → Manager → Executive)
□ What is the time constraint? (Hours, days, weeks, none)
□ Is this affecting customers right now? (Yes = raise)
□ Is this legally/regulatorily mandated? (Yes = raise)
□ Is this a repeat occurrence? (Yes = raise)
□ Is there financial materiality? (Yes = raise)
□ Is there public/market visibility? (Yes = raise)

Base Sound: ___
Adjustments: ___ (amplifiers/dampeners, with reasons)
───────────────
Final Sound: ___
```

## Common Sound Scoring Mistakes

| Mistake | Impact | Correction |
|---------|--------|------------|
| **Averaging multiple signals** | Underestimates urgency | Use highest signal |
| **Ignoring context** | Misses amplifiers | Apply contextual adjustments |
| **Confusing urgency with importance** | Misprioritizes | Urgency = time pressure, Importance = strategic value |
| **Not updating as situation evolves** | Stale scoring | Rescore as new information emerges |

## Next Steps

<div class="next-steps">

**📍 [PerchIQX (Space)](perch.md)** — Measure scope and reach

**⏱️ [WakeIQX (Time)](wake.md)** — Analyze trajectories and patterns

**🔍 [Trigger Keywords](../reference/trigger-keywords.md)** — Complete keyword catalog by urgency

**📊 [Scoring Methodology](../framework/scoring.md)** — Apply Sound in full 3D scoring

</div>

<style>
.next-steps {
  background: #161b22;
  padding: 2rem;
  border-radius: 12px;
  margin: 3rem 0;
  border-left: 4px solid #90ee90;
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

**Remember:** Urgency without action is just noise. Hear the chirp, then act. 🪶
