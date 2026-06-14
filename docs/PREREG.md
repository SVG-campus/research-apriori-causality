# Preregistration — `research-apriori-causality`
 
**Pillar:** `research-apriori-causality`  
**Title:** Causal Text Queries Null Benchmark (ECT-2026-001)
**Date:** 2026-06-14  
**ORCID Identifier:** `0009-0004-9601-5617`

## Charter (one paragraph)

Discover and stress-test causal/compositional structure hypotheses for language and agents. This study establishes the baseline null performance for textual feature representations of causal queries. Specifically, it tests whether lexical features of a natural language causal question can act as spurious causal drivers of the physical effect sizes reported in those studies, validating that OCCA's Peter-Clark and Spectral MC engines correctly return empty skeletons for epistemic null controls.

## Primary question (Layer A)

- **Question:** Do lexical features of a causal query (char_count, token_count, unique_word_ratio, and keyword indicators like "confounding", "mediation", "collider") cause the physical effect size reported in the study?
- **Expected DAG:** Empty (no directed or undirected edges between textual features and physical effect sizes).
- **Primary metric:** Directed edges count and information coefficient.
- **Direction / threshold:** $\alpha = 0.05$ for PC algorithm. The number of discovered directed edges must equal 0. The absolute information coefficient of any nonlinear transformation must not beat the phase-shuffled Spectral MC null ($p > 0.05$).

## Null / negative controls

- **Null model:** Phase-shuffled Spectral Monte Carlo (FFT surrogate paths).
- **Caps:** Capped at $N = 25$ runs for local smokes (`runs/smoke.yaml`); $N = 1000$ for full remote promotion validation with run ID `charter_causal_text_prereg_run_01`.

## Truth scope & ethics

- **Scope:** Observational NLP metadata analysis. This serves as an epistemic control baseline under the **ECT-2026** standard.
- **Data rights:** Utilizes query metadata extracted from `syrgkanislab/CausalReasoningBenchmark` (Hugging Face).

## Promotion rules

Numbers enter `BEST_ANSWERS_OVERVIEW` (meta) only after `methodology_preamble.assert_run_card` passes in the same environment that produced the artifact. Follow the meta checklist [PROMOTION_CHECKLIST.md](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/PROMOTION_CHECKLIST.md) before editing canonical summaries.
