# Cascade Mapping

How to trace problems as they multiply across dimensions.

---

## The Core Insight

Problems don't stay where they start. They cascade.

```
Traditional view:     What 6D reveals:
                      
    Problem              Problem
       │                    │
       ▼                    ▼
     Cost              ┌────┴────┐
                       │         │
                       ▼         ▼
                    Cost A    Cost B
                       │         │
                   ┌───┴───┐     │
                   ▼       ▼     ▼
                Cost A1  Cost A2  Cost B1
```

The **multiplier** is the ratio of total cascade cost to visible cost.

---

## Cascade Levels

### L0: Origin

The initial observable event or problem.

**Examples:**
- Layoffs announced
- System outage occurs
- Key customer churns
- Regulatory finding received

### L1: First-Order Effects

Direct, immediate consequences of the origin.

**Characteristics:**
- Clearly caused by L0
- Happen quickly (days to weeks)
- Usually predictable
- Often where traditional analysis stops

### L2: Second-Order Effects

Downstream consequences of L1 effects.

**Characteristics:**
- Caused by L1, not directly by L0
- Delayed onset (weeks to months)
- Less obvious causation
- Often cross dimensional boundaries

### L3: Third-Order Effects

Systemic ripples from the cascade.

**Characteristics:**
- Indirect relationship to origin
- Long-term manifestation (months to years)
- May be attributed to other causes
- Hardest to quantify but often largest

---

## Mapping Process

### Step 1: Identify the Origin (L0)

**Ask:**
- What's the visible event?
- When did it occur?
- Which dimension does it start in?

**Document:**
- Event description
- Date/timeframe
- Immediate visible cost
- Source dimension

### Step 2: Map First-Order Effects (L1)

**For each dimension, ask:**
- What happens immediately because of the origin?
- Who/what is directly impacted?
- What costs arise directly?

**Document for each affected dimension:**
- Observable signal
- Cost estimate (range)
- Confidence level

### Step 3: Trace Second-Order Effects (L2)

**For each L1 effect, ask:**
- What does this cause downstream?
- Which other dimensions does it impact?
- What's the time delay?

**Watch for dimension jumps:**
```
Employee (L1)       → Quality (L2)
Knowledge loss      → Defect rate increase
                    
Revenue (L1)        → Employee (L2)
Pressure to cut     → Layoffs/burnout
```

### Step 4: Identify Systemic Effects (L3)

**Ask:**
- What long-term patterns emerge?
- How does this affect competitive position?
- What cultural/structural changes result?

**These are often the largest but hardest to quantify.**

---

## Cascade Visualization

### Tree Format

```
L0: AI bypasses documentation [Operational]
│
├─ L1: Traffic down 40% [Operational]
│   └─ L2: No discovery → No conversion [Revenue]
│
├─ L1: Revenue down 80% [Revenue]
│   ├─ L2: Layoffs required [Employee]
│   │   └─ L3: Institutional knowledge lost [Quality]
│   └─ L2: No runway for investment [Operational]
│
└─ L1: Community backlash [Customer]
    └─ L2: "OSS unfriendly" narrative [Customer]
        └─ L3: Contributor exodus [Quality]
```

### Table Format

| Level | Dimension | Signal | Cost | Caused By |
|-------|-----------|--------|------|-----------|
| L0 | Operational | AI bypass | $300K | (Origin) |
| L1 | Revenue | 80% decline | $900K-1.4M | L0 |
| L1 | Employee | 75% layoff | $525K-1.05M | L0 |
| L1 | Quality | Skeleton crew | $300K-550K | L0 |
| L2 | Customer | Trust damaged | $250K-500K | L1 Employee |

### Matrix Format

```
            Customer  Employee  Revenue  Regulatory  Quality  Operational
Origin          -         -        -          -          -         L0
L1 Effects      -        L1       L1          -         L1         L1
L2 Effects     L2         -        -          -         L2          -
```

---

## Cross-Dimensional Patterns

Common cascade patterns to watch for:

### The Death Spiral

```
Revenue ↓ → Layoffs → Quality ↓ → Customers leave → Revenue ↓↓
```

### The Talent Drain

```
Leadership change → Uncertainty → Key people leave → Knowledge loss → Quality issues
```

### The Compliance Cascade

```
Regulatory finding → Remediation costs → Resource diversion → Delivery delays → Customer impact
```

### The Trust Collapse

```
Quality incident → Customer complaints → Social media → Brand damage → Sales cycle lengthens
```

---

## Quantifying Cascade Costs

### Estimation Methods

**1. Direct Calculation**
- Known costs (severance, penalties, etc.)
- Straightforward multiplication

**2. Industry Benchmarks**
- Average replacement cost = 1.5-2× salary
- Customer acquisition cost = known metric
- Downtime cost = revenue/hour

**3. Analogous Cases**
- Similar situations in same industry
- Historical data from organization

**4. Expert Judgment**
- Stakeholder estimates
- Range rather than point estimate

### Confidence Levels

Mark each estimate with confidence:

| Confidence | Meaning | Range |
|------------|---------|-------|
| High | Strong data support | ±20% |
| Medium | Some data, some judgment | ±50% |
| Low | Mostly judgment | ±100% |

### Range Estimation

Always estimate ranges, not points:

```
❌ Cost: $500,000
✅ Cost: $400,000 - $650,000 (Medium confidence)
```

---

## Calculating the Multiplier

### Formula

```
Multiplier = Total Cascade Cost ÷ Origin Visible Cost
```

### Example

```
Origin (L0):        $300,000
L1 Effects:       $1,725,000
L2 Effects:         $500,000
──────────────────────────────
Total:            $2,525,000

Multiplier = $2,525,000 ÷ $300,000 = 8.4×
```

### Typical Ranges

| Situation | Typical Multiplier |
|-----------|-------------------|
| Contained operational issue | 2-4× |
| Cross-functional problem | 4-7× |
| Organizational crisis | 7-15× |
| Industry disruption | 10-20×+ |

---

## Worked Example: Aviation MRO

**Origin:** Parts inventory management issues

### L0: Operational Origin
- Signal: Recurring stockouts, inventory discrepancies
- Visible cost: $119,000 (expedited shipping, manual workarounds)

### L1: First-Order Effects

| Dimension | Signal | Cost |
|-----------|--------|------|
| Quality | Aircraft downtime increased | $330,000 |
| Employee | Technician frustration, overtime | $370,000 |

### L2: Second-Order Effects

| Dimension | Signal | Cost | Caused By |
|-----------|--------|------|-----------|
| Customer | Airlines reconsidering contracts | $440,000 | Quality L1 |
| Revenue | Penalty clauses, lost contracts | $880,000 | Customer L2 |
| Regulatory | FAA documentation concerns | $61,000 | Quality L1 |

### Summary

```
Origin:     $119,000
L1 Total:   $700,000
L2 Total:   $1,381,000
──────────────────────
Total:      $2,200,000

Multiplier: 18.5×
Dimensions: 6 of 6 affected
```

---

## Common Mistakes

### Stopping at L1

Most analysis stops after first-order effects. Push to L2 and L3.

### Missing Cross-Dimensional Jumps

Effects often jump dimensions:
```
Employee burnout (Employee) → Quality drops (Quality) → Customer churn (Customer)
```

### Double-Counting

If the same cost appears in multiple paths, count it once.

### Ignoring Time Delays

L2 and L3 effects may take months to manifest. Include them anyway.

### Attributing to Wrong Cause

When L3 effects appear, they may be attributed to other causes. Trace back carefully.

---

*The cascade is always bigger than it looks. Your job is to see it.* 🐦
