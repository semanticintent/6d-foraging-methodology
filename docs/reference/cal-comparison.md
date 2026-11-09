# CAL vs Other Analytical Languages

> **"Complementary, not competitive — CAL fills a gap other DSLs weren't built for."**

CAL (Cascade Analysis Language) is the executable language behind every 6D case. It isn't the only structured language for describing risk or threats — this page positions it honestly against the established ones, including where CAL is still maturing.

## What CAL Is

- A PEG grammar with a small, fixed keyword set — deterministic parse, no ambiguity
- A published specification: [CAL spec v1.2.0](https://doi.org/10.5281/zenodo.24090152) (concept DOI [10.5281/zenodo.18905196](https://doi.org/10.5281/zenodo.18905196)). It defines the scoring: Chirp is the average of the scored dimensions, DRIFT = |Methodology − Performance|, FETCH = Chirp × DRIFT × Confidence, compared with a threshold T (default 1,000)
- A working runtime, [`@stratiqx/cal-runtime`](https://www.npmjs.com/package/@stratiqx/cal-runtime) on npm, computing DRIFT and FETCH directly from case inputs (not authored as literals; see [Scoring Methodology](../framework/scoring.md))
- Backing the published case library, [331 cases with a recorded cascade as of November 2026](https://uc-000.stratiqx.com). That library is the validation corpus for the language, not a separate demo set

## Comparative Analysis

### vs FAIR (Factor Analysis of Information Risk)

**FAIR** models risk *magnitude* in a single domain, using Monte Carlo simulation. Open Group certified, enterprise adopted, produces dollar-denominated loss distributions with confidence intervals.

**CAL** models risk *propagation across domains* — cross-dimensional cascade modeling, not single-domain magnitude.

**Relationship:** Complementary, not competitive. FAIR cannot model a cascade like [UC-039](https://uc-039.stratiqx.com)'s `D5>D1>D3>D4>D6>D2`, "The 48-Hour Cascade". CAL doesn't produce Monte Carlo loss distributions. A mature risk practice plausibly wants both.

### vs STIX/TAXII (Structured Threat Information Expression)

**STIX** is a data exchange format — it describes *what happened*. OASIS maintained, machine-first, broad adoption in threat-intel tooling.

**CAL** is an analytical language — it describes *how things cascade*. Narrower in scope, deeper in propagation logic.

**Relationship:** Different purposes entirely. STIX is broader but shallower for this specific question; CAL is narrower but deeper.

### vs Sigma Rules

**Sigma** detects specific events in SIEM logs — operational, real-time, single-signal.

**CAL** models systemic propagation — strategic, pattern-level, cross-dimensional.

**Analogy:** Sigma is the smoke detector. CAL is the fire investigator's report.

### vs System Dynamics (MIT/Forrester)

System Dynamics models feedback loops and propagation with real rigor — but with no lightweight DSL and no dimensional scoring. Building a model takes an expert modeler weeks; CAL cases compile in milliseconds and publish same-day. See [Intellectual Lineage](../framework/intellectual-lineage.md) for the fuller comparison.

### vs Bow-Tie Analysis

Bow-tie diagrams map causes through barriers to consequences — a mature, widely used safety-engineering tool. What it doesn't have is cross-dimensional propagation, or anything like [DRIFT](glossary.md#drift) (the gap between diagnosis and proof).

### vs MITRE ATT&CK

ATT&CK taxonomizes attack techniques with a structured, widely adopted vocabulary — the closest thing on this list to CAL's own approach of a formal, shared vocabulary for cascade patterns. The difference is scope: ATT&CK is cyber-specific by design. CAL is domain-agnostic — the same grammar scores a bank run, a labor dispute, and a semiconductor foundry bet.

## Genuine Strengths

1. **The corpus.** 331 published cases with a recorded cascade (November 2026), publicly cross-referenced, scored, and growing — see the [full library](https://uc-000.stratiqx.com). Most comparable DSLs and frameworks are validated against proprietary or unpublished analyses. This one is open.

2. **Dimensional propagation model.** No other DSL here models cross-dimensional cascade propagation with formal syntax and a scoring language attached to it.

3. **Dual human/machine readability.** CAL blocks are simultaneously analyst-readable and runtime-parseable. STIX is machine-first. FAIR spreadsheets are human-first. CAL threads that needle.

4. **DRIFT as a first-class concept.** Methodology minus Performance, expressed as a language construct, not a footnote. [UC-039](https://uc-039.stratiqx.com)'s DRIFT of 75 (Methodology 90, Performance 15) tells a story in one number that a traditional report takes pages to make the same point about.

5. **The combination.** Formal grammar + 6-dimension model + DRIFT/FETCH scoring + a large public corpus + cross-domain applicability, together, in one system. Individually, several of these exist elsewhere. Combined, this is the only place they do.

## Where CAL Is Still Maturing

Being straight about the gaps is part of the same standard this site holds every case to — see [why the site retired cost multipliers and "total impact"](glossary.md#retired-terms-multiplier-direct-cost-total-impact) for the same instinct applied elsewhere. The runtime is cleaning up the same way: in CAL runtime 1.5.0, `estimateMultiplier` and `calculateFinancialImpact` are deprecated, and `cascadeProbability` is being deprecated, with removal in 2.0.0.

1. **Community and governance.** No governance body, no certification program, no contributor ecosystem yet. One primary author. Enterprise adoption at scale typically wants institutional backing behind a spec, not just a working implementation.

2. **Independent implementations.** The [CAL spec v1.2.0](https://doi.org/10.5281/zenodo.24090152) is published, but the reference runtime is still the main way CAL gets run. A spec proves itself when others implement it independently, and that has not happened yet.

3. **Quantitative precision.** CAL produces ordinal scores (0–100) composed into FETCH. FAIR produces dollar-denominated loss estimates with confidence intervals. A CFO wanting actuarial-grade numbers won't get them from a FETCH score — that's a different question than the one CAL is built to answer.

**Bottom line:** the analytical architecture is done, and the validation corpus of 331 real, cited cases is unusual for a DSL this young. The remaining gap is community and independent implementations, which closes with adoption and time, not a redesign.

---

## Next Steps

<div class="next-steps">

**🧬 [Intellectual Lineage](../framework/intellectual-lineage.md)** — Where 6D's cascade logic actually comes from

**📊 [Scoring Methodology](../framework/scoring.md)** — How CHIRP, FETCH, and DRIFT are calculated

**📖 [Glossary](glossary.md)** — Every term defined, including what got removed and why

**📚 [Case Studies](../applications/case-studies.md)** — CAL applied to a real, cited case

</div>

<style>
.next-steps {
  background: #161b22;
  padding: 2rem;
  border-radius: 12px;
  margin: 3rem 0;
  border-left: 4px solid #f08080;
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
