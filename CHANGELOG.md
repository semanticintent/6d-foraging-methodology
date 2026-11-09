# Changelog

All notable changes to the 6D Foraging Methodology will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2026-11-09

The methodology now describes what the published cases actually do. This is a major version because the cost multiplier and cascade probabilities are removed.

### Changed

- The repository is a snapshot of the website, [6d.semanticintent.dev](https://6d.semanticintent.dev), in `docs/`. `scripts/snapshot_from_site.py` makes each new snapshot.
- Scoring is defined by the CAL specification v1.2.0 ([10.5281/zenodo.18905196](https://doi.org/10.5281/zenodo.18905196)): Chirp is the average of the scored dimensions, DRIFT is |Methodology − Performance|, Confidence is the analyst's 0–1 rating of evidence quality, and FETCH = Chirp × DRIFT × Confidence sets a level (EXECUTE at the threshold or more, high priority from twice the threshold; CONFIRM, QUEUE or WAIT below).
- A case's written verdict (EXECUTE, MONITOR, WATCH, COUNTER…) is described as the analyst's reading, separate from the computed FETCH level.
- Prognostic cases carry triggers and a review date and are graded when reviewed.
- Dimension numbering is D1 Customer, D2 Employee, D3 Revenue, D4 Regulatory, D5 Quality, D6 Operational throughout. Cases UC-244 to UC-302 were published with D2 and D3 the other way round; their pages name each dimension, and the case index now uses the current numbering.

### Added

- `data/counted-patterns.md` and `scripts/count_patterns.py`: counts from the published case library of which dimension each cascade started in, what the next layer included, and where cascades ended (331 cascades, as of November 2026).
- Real worked examples from published cases (UC-246, UC-335, UC-342 and others) in place of invented ones.

### Removed

- **The cost multiplier** (dimensions × depth → "2–11×"), "total impact" and direct-cost dollar cascades. No published case derived a figure this way, and the multiplier had no evidence behind it. Cases published before this release that state a multiplier keep it as part of their dated record.
- **Cascade probabilities** such as "Employee → Quality (80% of cases)". The published cases contradict them: Employee is the origin in 59 cascades and Quality is in the next layer in 18; Revenue is in 31.
- **The "70–90% of costs are hidden" claim** as a stated fact.
- **The fictional aviation maintenance example** and the v1 case write-ups (`cases/`), and the v1 files `DIMENSIONS.md`, `3D-LENS.md`, `CASCADE-MAPPING.md`, `QUICK-REFERENCE.md` and `EXAMPLES.md`, all replaced by `docs/`. Version 1.0.0 remains at [10.5281/zenodo.18209946](https://doi.org/10.5281/zenodo.18209946) and under the `v1.0.0` tag.
- Unsourced metric targets and priority bands built on the removed system.

---

## [1.0.0] - 2026-01-10

### Added

- Initial public release of 6D Foraging Methodology
- Six dimensions defined: Customer, Employee, Revenue, Regulatory, Quality, Operational
- 3D Lens scoring system (Sound/Space/Time - ChirpIQX/PerchIQX/WakeIQX)
- Cascade mapping framework (L0-L3 levels)
- Multiplier calculation methodology
- Case studies: Tailwind CSS, Aviation MRO
- Quick reference card for practitioners
- Full documentation suite
- CC BY 4.0 licensing
- CITATION.cff for academic citation
- Connection to PACE Pattern and Semantic Intent ecosystem

### Documentation

- README.md - Framework overview
- DIMENSIONS.md - Detailed dimension breakdowns
- 3D-LENS.md - Scoring system guide
- CASCADE-MAPPING.md - How to trace cascades
- EXAMPLES.md - Case studies and patterns
- QUICK-REFERENCE.md - Practitioner cheat sheet
- CONTRIBUTING.md - Contribution guidelines

---

## [Unreleased]

### Planned

- Additional industry-specific case studies
- Scoring calibration guidelines
- Integration guide for StratIQX platform
- Workshop facilitation materials
- Video walkthrough content

---

## Version Numbering

- **Major version (X.0.0):** Fundamental changes to the methodology
- **Minor version (0.X.0):** New dimensions, lenses, or significant additions
- **Patch version (0.0.X):** Clarifications, corrections, additional examples

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose changes to the methodology.
