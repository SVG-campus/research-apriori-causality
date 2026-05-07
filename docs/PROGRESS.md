# Pillar progress — `research-apriori-causality`

**Overall solution proximity (rubric v2): ~54%** toward a defensible, preregistered answer for this pillar’s charter.

Formula (same as meta `docs/PILLAR_PROGRESS.md`): `round(0.30×charter + 0.30×LayerA + 0.25×repro + 0.15×data)` on 0–100 subscores.

See the full rubric and sibling pillars: [meta `docs/PILLAR_PROGRESS.md`](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/PILLAR_PROGRESS.md).

## This pillar

| Axis | % | Note |
|------|---:|------|
| Charter + prereg | 56 | `docs/PREREG.md` + `METHODS.md` |
| Layer A / nulls | 40 | Permutation + bootstrap tests; CI includes `CHARTER_CAUSAL_BENCHMARK_SMOKE` (HF CausalReasoningBenchmark stream + y-shuffle null) |
| Reproducibility | 78 | `runs/smoke.yaml`, `runs/ci_notebooks.yaml`, `methodology_preamble`, pytest + headless CI (**six** enabled rows: three `SMOKE_*` + `CHARTER_SHELL` + `CHARTER_EXTENDED_LIGHT` + domain stream charter; see `runs/README.md`; disabled `FUTURE_CHARTER_SLOT`) |
| Domain data | 38 | `datasets.yaml` pins incl. `syrgkanislab/CausalReasoningBenchmark` + `reference_streams` |

## Links

- Preregistration template: [docs/PREREG.md](PREREG.md)
- Methodology skills (exact code): [Research-Apriori `skills/`](https://github.com/SVG-campus/Research-Apriori/tree/main/skills)
- Install: [CURSOR_SKILLS_INSTALL.md](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/CURSOR_SKILLS_INSTALL.md)
- Meta promotion + PR defaults: [`docs/PROMOTION_CHECKLIST.md`](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/PROMOTION_CHECKLIST.md) · [`.github/pull_request_template.md`](https://github.com/SVG-campus/Research-Apriori/blob/main/.github/pull_request_template.md)
