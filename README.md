# 6D Foraging Methodology™
## Strategic Dimensional Discovery

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18209946.svg)](https://doi.org/10.5281/zenodo.18209946)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![GitHub](https://img.shields.io/badge/GitHub-semanticintent%2F6d--foraging--methodology-blue)](https://github.com/semanticintent/6d-foraging-methodology)

**A strategic analysis framework for discovering cost multipliers others miss.**

> *"Diving deep across six dimensions to discover the 70-90% traditional analysis leaves behind."*

---

## Abstract

The **6D Foraging Methodology™** is a strategic analysis framework that maps how problems cascade across six business dimensions. Like cormorants diving beneath the surface for fish, this methodology forages deep to find hidden costs that traditional analysis misses.

Most organizations see only 10-30% of their true problem costs. The visible issue—a layoff, a system failure, a market shift—is just the surface. Beneath it lies a cascade of consequences across Customer, Employee, Revenue, Regulatory, Quality, and Operational dimensions.

The 6D framework quantifies this cascade, revealing multipliers of 2-11× between visible costs and total impact.

**Author:** Michael Shatny  
**ORCID:** [0009-0006-2011-3258](https://orcid.org/0009-0006-2011-3258)  
**Date:** January 2026  
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)  
**Trademark:** 6D Foraging Methodology™

---

## The Problem This Solves

Traditional business analysis tends to:

- Focus on the visible, immediate problem
- Stop at the first-order effects
- Miss cascading consequences across departments
- Underestimate total cost by 70-90%

```
Traditional Analysis:
┌─────────────────────────────────────┐
│  Problem: Layoffs announced         │
│  Cost: $300K severance              │
│  Analysis: Complete ✓               │
└─────────────────────────────────────┘

6D Foraging Analysis:
┌─────────────────────────────────────┐
│  Visible Cost: $300K                │
│         ↓                           │
│  Employee cascade: $525K-1.05M      │
│  Revenue cascade: $900K-1.4M        │
│  Quality cascade: $300K-550K        │
│  Customer cascade: $250K-500K       │
│         ↓                           │
│  Total Impact: $2.1M-3.4M           │
│  Multiplier: 7-11×                  │
└─────────────────────────────────────┘
```

---

## The Six Dimensions

| Dimension | Symbol | What It Measures |
|-----------|--------|------------------|
| **Customer** | 👤 | Trust erosion, churn signals, lifetime value loss |
| **Employee** | 👥 | Turnover risk, burnout, knowledge concentration |
| **Revenue** | 💰 | Payment delays, contract penalties, opportunity loss |
| **Regulatory** | ⚖️ | Compliance gaps, audit findings, legal exposure |
| **Quality** | ✨ | Defect rates, rework cycles, safety incidents |
| **Operational** | ⚙️ | Schedule delays, resource waste, system downtime |

Each dimension is analyzed for:
- **Observable signals** — Concrete, measurable indicators
- **Cascade depth** — How far the effects propagate (L1, L2, L3)
- **Cost quantification** — Dollar ranges based on evidence

---

## The 3D Lens (Scoring System)

Each dimension is scored using three lenses, inspired by cormorant foraging behavior:

| Lens | Name | What It Measures | Range |
|------|------|------------------|-------|
| **Sound** | ChirpIQX | Urgency — How immediate is the signal? | 1-10 |
| **Space** | PerchIQX | Scope — How widespread is the impact? | 1-10 |
| **Time** | WakeIQX | Trajectory — Is it improving or degrading? | 1-10 |

### Scoring Formula

```
Dimension Score = (Sound × Space × Time) ÷ 10

Example:
- Sound (Urgency): 7
- Space (Scope): 8  
- Time (Trajectory): 6
- Score: (7 × 8 × 6) ÷ 10 = 33.6
```

Scores range from 0.1 (minimal concern) to 100 (critical across all lenses).

---

## Cascade Mapping

Problems don't stay isolated—they multiply. The 6D framework maps cascade depth:

```
L0: Origin
 └── L1: First-order effects (direct consequences)
      └── L2: Second-order effects (downstream impact)
           └── L3: Third-order effects (systemic ripples)
```

### Example: Tailwind CSS Case Study

**Visible Event:** AI coding assistants bypass documentation → Revenue down 80%

| Dimension | Level | Observable Signal | Cascade Cost |
|-----------|-------|-------------------|--------------|
| Operational (Origin) | L0 | AI bypass breaks funnel | ~$300K |
| Employee | L1 | 75% layoff, knowledge loss | $525K-1.05M |
| Revenue | L1 | Lifetime license = no recurring | $900K-1.4M |
| Quality | L1 | Skeleton crew for 75M downloads | $300K-550K |
| Customer | L2 | Community trust damaged | $250K-500K |

**Total Cascade:** $2.1M-3.4M
**Multiplier:** 7-11×
**Dimensions Affected:** 5 of 6

[Full case study →](cases/tailwind-css.md)

---

## Quick Start

### 1. Identify the Origin

What's the visible problem? This becomes your Operational (L0) starting point.

### 2. Score Each Dimension

For each of the 6 dimensions, assess:
- What signals are you observing?
- Score Sound/Space/Time (1-10 each)
- Calculate dimension score

### 3. Map the Cascade

- What are the first-order effects (L1)?
- What downstream effects follow (L2, L3)?
- Which dimensions are affected?

### 4. Quantify Costs

For each affected dimension, estimate cost ranges based on:
- Industry benchmarks
- Historical data
- Comparable situations

### 5. Calculate the Multiplier

```
Multiplier = Total Cascade Cost ÷ Visible Cost
```

---

## Repository Structure

```
6d-foraging-methodology/
├── README.md                 # This file - framework overview
├── DIMENSIONS.md             # Deep dive on each dimension
├── 3D-LENS.md                # Scoring system details
├── SCORING.md                # Formulas and calculations
├── CASCADE-MAPPING.md        # How to map cascade effects
├── EXAMPLES.md               # Case studies and applications
├── QUICK-REFERENCE.md        # Cheat sheet for practitioners
├── CITATION.cff              # Machine-readable citation metadata
├── CHANGELOG.md              # Version history
├── CONTRIBUTING.md           # How to contribute
├── LICENSE                   # CC BY 4.0 license
└── cases/
    ├── tailwind-css.md       # Tailwind Labs case study
    └── aviation-mro.md       # Aviation maintenance case study
```

---

## Connection to Ecosystem

6D Foraging Methodology is part of the **Cormorant Foraging** ecosystem:

```
Cormorant Foraging (Philosophy)
├── 6D Foraging Methodology (Analysis Framework) ← You are here
│   └── StratIQX (Implementation Platform)
└── PACE Pattern (UX Framework)
    └── MillPond (Implementation Platform)
```

**Related Projects:**
- [StratIQX](https://stratiqx.ai) — AI-powered strategic analysis platform
- [PACE Pattern](https://github.com/semanticintent/pace-pattern) — Conversational UX framework (DOI: 10.5281/zenodo.18049371)
- [Semantic Intent](https://semanticintent.dev) — Philosophy layer

---

## Citation

If you use or reference 6D Foraging Methodology in your work, please cite:

### APA Style

Shatny, M. (2026). 6D Foraging Methodology: Strategic Dimensional Discovery. Zenodo. https://doi.org/10.5281/zenodo.18209946

### BibTeX

```bibtex
@misc{shatny20266d,
  author = {Shatny, Michael},
  title = {6D Foraging Methodology: Strategic Dimensional Discovery},
  year = {2026},
  publisher = {Zenodo},
  url = {https://github.com/semanticintent/6d-foraging-methodology},
  doi = {10.5281/zenodo.18209946},
  note = {ORCID: 0009-0006-2011-3258}
}
```

---

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to:
- **Share** — copy and redistribute in any medium or format
- **Adapt** — remix, transform, and build upon for any purpose

Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.

**6D Foraging Methodology™** is a trademark of Michael Shatny.

---

## Author

**Michael Shatny**  
Ontario, Canada  
ORCID: [0009-0006-2011-3258](https://orcid.org/0009-0006-2011-3258)

Part of the [Cormorant Foraging](https://cormorantforaging.dev) ecosystem.

---

*"Most analysis stops at the visible cost. They miss the cascade. Now you can see it."* 🐦
