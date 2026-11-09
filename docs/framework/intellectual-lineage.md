# Intellectual Lineage

> **"Cascades are not a new idea. Scoring them, and being falsifiable about it, is."**

The 6D Foraging Methodology didn't emerge from nowhere. It shares cognitive architecture with older traditions concerned with how change propagates through interconnected systems — traditions that predate business strategy entirely. This page traces that lineage and shows precisely what 6D kept, and what it added.

## Political Economy (18th–20th Century)

**Founders:** Adam Smith, David Ricardo, Karl Marx, John Stuart Mill

Political Economy's core premise: economic, political, and social systems are interconnected. A change in production cascades into labour relations, which cascades into political power, which cascades into institutional change. Marx's *Capital* is, structurally, a cascade analysis — capital accumulation cascading into labour exploitation, into class tension, into institutional pressure.

The methodology is cascade logic. The conclusions were ideological, and unfalsifiable by design. 6D inherits the cascade-tracing structure and discards the ideology — replacing predetermined conclusions with scored, cited evidence and a verdict the reader can check.

| Aspect | Political Economy | 6D Foraging |
|---|---|---|
| Cascade logic | Yes — material → social → political | Yes — origin dimension → L1 → L2 → L3 |
| Cross-dimensional | Yes — economics, politics, society, culture | Yes — 6 scored dimensions (D1–D6) |
| Scored | No | Yes — [CHIRP, FETCH, DRIFT](scoring.md) |
| Falsifiable | No — conclusions predetermined | Yes — dated review windows, named triggers |
| Executable | No — narrative/theoretical | Yes — [CAL runtime](https://www.npmjs.com/package/@stratiqx/cal-runtime), open source |
| Domain-specific | Yes — economics/politics | No — [applies across industries](../applications/industry-variants.md) |

A reader trained in Political Economy would recognize the cascade logic in 6D immediately — the structural DNA is genuinely shared. What's different is that 6D shed the ideology, added empirical scoring, added falsifiability, and shipped a runtime.

## PESTLE Analysis (1960s–Present)

**Dimensions:** Political, Economic, Social, Technological, Legal, Environmental

PESTLE has six dimensions. 6D has six dimensions. The structural resemblance ends there.

PESTLE is a **checklist** — each category is scanned independently, with no mechanism for how a Political pressure moves into a Social one. 6D is a **cascade engine** — every case identifies an origin dimension and traces how impact propagates through the others, scored at each step.

| Aspect | PESTLE | 6D Foraging |
|---|---|---|
| Structure | Checklist — "what exists in each category?" | Cascade — "what originated where, and how does it propagate?" |
| Interaction between categories | None — analyzed independently | Core feature — e.g. `D3 > D1+D5 > D2 > D6 > D4` |
| Scoring | None | [CHIRP, FETCH, DRIFT](scoring.md) with defined formulas |
| Origin tracing | No | Yes — every case names an origin dimension |
| Output | Bullet points per category | Scored, cited, falsifiable analysis |

PESTLE would tell you a company has labor pressure (Social) and a tech shift underway (Technological). 6D tells you the labor investment *is* the origin dimension, traces where it cascades, and scores the whole thing against a threshold — see [UC-246](https://uc-246.stratiqx.com) for a worked example.

## Porter's Five Forces (1979)

**Creator:** Michael Porter, Harvard Business School

Porter's Five Forces is the most widely taught strategic framework in business education — and the most static. It photographs an industry's competitive structure at a moment in time. It doesn't trace how pressures cascade, evolve, or reach into other industries.

6D addresses what Porter's framework, by design, cannot:

- **Temporal dynamics** — how forces evolve, captured by [DRIFT](../reference/glossary.md#drift)
- **Cross-sector cascades** — Porter analyzes one industry; 6D traces cascades *across* industries
- **Scoring** — Porter is qualitative; 6D produces numbers comparable across sectors and time

## Risk Matrices (ISO 31000)

**Structure:** Likelihood × Impact grid, typically 5×5

Risk matrices are the closest thing to "scored analysis" in mainstream enterprise practice — but each risk is scored in isolation. The matrix entry for "supply chain disruption" doesn't connect to the entry for "regulatory change," even when they're causally linked.

6D's FETCH score plays a comparable role to a risk-matrix severity rating, but with cascade logic embedded in it: it isn't just "how bad is this?" — it's "how far does this propagate across dimensions, and how confident are we?" A risk matrix scores an event once. 6D scores the cascade *between* events.

## What Each Predecessor Contributed

```
Political Economy (18th–19th C)     → Cascade logic: changes propagate across dimensions
Systems Dynamics (Forrester, 1950s) → Feedback loops: amplifying and balancing forces
Complexity Theory (Santa Fe, 1980s) → Emergence: system behavior ≠ sum of parts
Scenario Planning (Shell, 1970s)    → Forward-looking triggers and review windows
PESTLE (1960s–present)              → Multi-dimensional scanning: 6 categories matter
Porter's Five Forces (1979)         → Competitive pressure has direction, not just magnitude
Risk Matrices (ISO 31000)           → Numerical severity enables comparison
```

*(Systems Dynamics, Complexity Theory, and Scenario Planning are covered in depth on the [Framework Overview](index.md) — this page focuses on the lineage those don't share.)*

None of these traditions combined cascade logic, scoring, and falsifiability into one executable method. That combination — not any single ingredient — is what 6D adds.

## What 6D Added That None of Them Have

1. **Executable language.** [CAL](https://www.npmjs.com/package/@stratiqx/cal-runtime) is code, not narrative. Run it against the runtime, reproduce the result. No predecessor here ships source.
2. **Falsifiable predictions.** Prognostic cases carry a named review date and specific triggers — publicly checkable, not a hedge.
3. **Cross-sector velocity.** 300+ cases published since December 2025, across industries from banking to agriculture — see the [full library](https://uc-000.stratiqx.com). Systems Dynamics models take months to build; scenario sets take weeks. This methodology publishes same-day.
4. **A compounding library.** Every new case calibrates against every prior one — see [Pattern Transfer](../applications/pattern-transfer.md) for what that makes possible once the library is large enough.

## Positioning by Audience

**For a Political Economy background:** the cascade logic (material → social → political) is structurally the same instinct as origin-dimension → L1 → L2 → L3 — with ideology replaced by cited evidence and a scored verdict.

**For consultants:** this does what a PESTLE scan, a Five Forces analysis, or a risk matrix does — but connects the categories, scores the cascade between them, and ships the source so a client can verify it.

**For a general audience:** business events don't happen in isolation. This traces how they cascade across six dimensions, and scores it.

---

## Next Steps

<div class="next-steps">

**📊 [Scoring Methodology](scoring.md)** — How CHIRP, FETCH, and DRIFT actually get calculated

**🔄 [Cascade Pathways](cascade-pathways.md)** — Real cascade notation from published cases

**🔬 [Pattern Transfer](../applications/pattern-transfer.md)** — What a large-enough case library starts to predict

**📚 [Case Studies](../applications/case-studies.md)** — See the methodology applied to a real, cited case

</div>

<style>
.next-steps {
  background: #161b22;
  padding: 2rem;
  border-radius: 12px;
  margin: 3rem 0;
  border-left: 4px solid #dda0dd;
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
