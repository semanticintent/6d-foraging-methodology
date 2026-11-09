# 6D Foraging Methodology™
## Strategic Dimensional Discovery

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18209945.svg)](https://doi.org/10.5281/zenodo.18209945)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**A method for tracing how one event spreads across six dimensions of an organization or sector, with every step tied to cited evidence.**

**Version 2.0.0** · November 2026 · Website: [6d.semanticintent.dev](https://6d.semanticintent.dev)

---

## What it is

An event rarely stays in one place. A layoff reaches quality, quality reaches customers, customers reach revenue. The 6D Foraging Methodology describes how to trace that movement:

- **Six dimensions:** D1 Customer, D2 Employee, D3 Revenue, D4 Regulatory, D5 Quality, D6 Operational. Each dimension a case reaches is scored 0 to 100 from cited evidence. Not every case reaches all six.
- **The cascade:** where the event started (the origin) and the layers it moved through, written in a short notation such as `D5 > D2+D6 > D4+D1`.
- **Four kinds of case:** diagnostic (something broke), amplifying (something is working), at risk (a weakness inside success), prognostic (a prediction with named triggers and a review date).
- **The verdict:** the analyst's written reading of the cascade, for example EXECUTE, MONITOR, WATCH or COUNTER.
- **The review loop:** prognostic cases are reopened on their review date and graded, including the ones that did not hold.

Scoring is defined by **CAL**, the Cascade Analysis Language, not by this repository: Chirp (the average of the scored dimensions), DRIFT (|Methodology − Performance|), Confidence (the analyst's 0–1 rating of evidence quality), and FETCH = Chirp × DRIFT × Confidence, compared with a threshold to give a level (EXECUTE, CONFIRM, QUEUE or WAIT). See the [CAL specification](https://cal.semanticintent.dev) ([10.5281/zenodo.18905196](https://doi.org/10.5281/zenodo.18905196)). The computed level and the written verdict are different things and can disagree.

## Evidence

The method is applied in a public library of case studies at [uc-000.stratiqx.com](https://uc-000.stratiqx.com). [`data/counted-patterns.md`](data/counted-patterns.md) counts what those cases recorded: which dimension each cascade started in, what the next layer included, and where cascades ended. For example, Regulatory lands in the last layer in 158 of 331 cascades, more than any other dimension. These are counts, not probabilities. Regenerate them with:

```bash
python3 scripts/count_patterns.py
```

## Contents

| Folder | What is in it |
|---|---|
| [`docs/`](docs/) | The methodology, a snapshot of [6d.semanticintent.dev](https://6d.semanticintent.dev): [getting started](docs/getting-started.md), the [framework](docs/framework/index.md), each [dimension](docs/dimensions/customer.md), [scoring](docs/framework/scoring.md), [cascade pathways](docs/framework/cascade-pathways.md), applications and reference pages |
| [`data/`](data/) | Counted cascade patterns from the published cases |
| [`scripts/`](scripts/) | `count_patterns.py` (regenerates the counts) and `snapshot_from_site.py` (copies the website's pages into `docs/` for a release) |

The website is the working copy; each release of this repository is a snapshot of it.

## What changed in 2.0.0

Version 1.0.0 (January 2026) taught a cost multiplier ("2–11× hidden costs"), cascade probabilities and a fictional worked example. None of these were used by, or supported by, the published cases, and the counted patterns contradict the probabilities. Version 2.0.0 removes them and describes the method the cases actually use. Details in [CHANGELOG.md](CHANGELOG.md). Version 1.0.0 remains available at [10.5281/zenodo.18209946](https://doi.org/10.5281/zenodo.18209946) and under the `v1.0.0` tag.

## Citation

Cite the concept DOI to refer to the methodology, or a version DOI for a specific release. See [CITATION.cff](CITATION.cff).

> Shatny, M. (2026). *6D Foraging Methodology: Strategic Dimensional Discovery* (Version 2.0.0). Zenodo. https://doi.org/10.5281/zenodo.18209945

**Author:** Michael Shatny · ORCID [0009-0006-2011-3258](https://orcid.org/0009-0006-2011-3258)
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · **Trademark:** 6D Foraging Methodology™

## Related

- CAL specification: [cal.semanticintent.dev](https://cal.semanticintent.dev) · [10.5281/zenodo.18905196](https://doi.org/10.5281/zenodo.18905196)
- CAL runtime: [`@stratiqx/cal-runtime`](https://www.npmjs.com/package/@stratiqx/cal-runtime) · [10.5281/zenodo.18905192](https://doi.org/10.5281/zenodo.18905192)
- Case library: [stratiqx.com](https://stratiqx.com)
