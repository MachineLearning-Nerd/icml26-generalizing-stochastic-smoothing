---
title: "ICML 2026 collection — Generalizing Stochastic Smoothing"
emoji: 🎯
colorFrom: yellow
colorTo: red
sdk: static
pinned: false
tags:
  - icml2026-repro
  - stochastic-smoothing
  - gradient-estimation
  - open-experiment
---

# Generalizing Stochastic Smoothing for Differentiation and Gradient Estimation

This repository is the claim-by-claim reproduction and audit record for [Generalizing Stochastic Smoothing for Differentiation and Gradient Estimation](https://arxiv.org/abs/2410.08125).

The collection label is ICML 2026. The primary source is an arXiv preprint from 2024; the public OpenReview record is an ICLR 2025 submission. Those source labels are kept explicit so the collection name is not mistaken for the paper's publication metadata.

The current result is intentionally asymmetric:

- Claims 1–5 have finite, independently checked evidence.
- Claim 6 is BLOCKED because its four application demonstrations were not all executed at the disclosed scale with the exact author assets and protocol.
- The old challenge-generated repository and its experiment branches were normalized into one public main branch after their purposes were recorded below.

## Paper and repository record

| Field | Record |
| --- | --- |
| Paper | Generalizing Stochastic Smoothing for Differentiation and Gradient Estimation |
| Authors | Felix Petersen, Christian Borgelt, Aashwin Ananda Mishra, and Stefano Ermon |
| Primary paper | [arXiv:2410.08125](https://arxiv.org/abs/2410.08125) |
| Public review record | [OpenReview GBWqZNoeIk](https://openreview.net/forum?id=GBWqZNoeIk) |
| Source HTML used for the contracts | [ar5iv HTML](https://ar5iv.labs.arxiv.org/html/2410.08125) |
| Former repository | icml26-repro-okzQ1x71pS-generalizing-stochastic-smoothing-for-differentiation-and-gradient-estimatio |
| Normalized repository | [MachineLearning-Nerd/icml26-generalizing-stochastic-smoothing](https://github.com/MachineLearning-Nerd/icml26-generalizing-stochastic-smoothing) |
| Canonical branch | main |
| Fixed entrypoint | uv sync --frozen --no-dev && .venv/bin/python -m repro.run |
| Compute policy | Historical run used HF cpu-upgrade; no GPU was requested. Future runs require explicitly authorized compute. |

## Audit dossier

The repository has been normalized and published as
[MachineLearning-Nerd/icml26-generalizing-stochastic-smoothing](https://github.com/MachineLearning-Nerd/icml26-generalizing-stochastic-smoothing).
The detailed audit records are separated by purpose:

| File | Purpose |
| --- | --- |
| [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md) | Claim-by-claim production paths, evidence, status, and limitations. |
| [SOURCE_AUDIT.md](SOURCE_AUDIT.md) | Paper identity, source pins, cited repositories, and provenance boundaries. |
| [BRANCH_AUDIT.md](BRANCH_AUDIT.md) | Final branch policy and pointer to the detailed historical branch table. |
| [ENVIRONMENT.md](ENVIRONMENT.md) | Recorded runs, compute provenance, dependencies, and artifact hashes. |
| [REPORT.md](REPORT.md) | Scoped audit decision and publication boundary. |
| [claims.json](claims.json) | Machine-readable claim ledger. |
| [EVIDENCE_MANIFEST.json](EVIDENCE_MANIFEST.json) | Machine-readable evidence hashes and required paths. |
| [verify_final.py](verify_final.py) | Dependency-free publication verifier. |
| [CITATION.cff](CITATION.cff) | Citation metadata for the paper and this audit. |
| [AUTHOR_THANK_YOU.md](AUTHOR_THANK_YOU.md) | Author thank-you note and independence statement. |

The paper does not provide an author-maintained implementation link in the public source record. The reproduction therefore distinguishes independent reconstruction code from the external repositories cited by the paper:

- [martius-lab/blackbox-differentiation-combinatorial-solvers](https://github.com/martius-lab/blackbox-differentiation-combinatorial-solvers), pinned for the Warcraft data/model audit at commit 027e82ee818530f2823851d6530e0d2c8657bbcb.
- [Felix-Petersen/gendr](https://github.com/Felix-Petersen/gendr), pinned for the rendering capability audit at commit c89269cb38eef7a95be703154f676a56d791958f.
- [TEM Simulator](https://sourceforge.net/projects/tem-simulator/), whose public archives are authenticated in the Claim 6 evidence.

## What the paper is doing

The paper develops a stochastic-smoothing framework for differentiating black-box, possibly nondifferentiable functions. Instead of requiring a differentiable, full-support perturbation density, it derives score-based gradient identities under weaker assumptions, including absolutely continuous densities that may be nondifferentiable.

It then studies three orthogonal variance-reduction axes:

1. sampling distributions and randomized quasi-Monte Carlo;
2. covariates such as the function value and leave-one-out controls;
3. antithetic pairing when the distribution and sampling geometry permit it.

The empirical section tests differentiable sorting, shortest paths, rendering, and cryo-electron-tomography simulation. This repository reconstructs the theorem identities and the disclosed Section 4 benchmark independently, then audits the four applications with explicit scale, provenance, capability, and limitation checks.

## Claim ledger

The statuses below are evidence statuses, not claims that the paper's symbolic proofs have been re-proved numerically.

| Claim | Paper statement | How this repository produces evidence | Evidence and result |
| --- | --- | --- | --- |
| 1 | Lemma 3: under the paper's absolute-continuity, finiteness, and almost-everywhere score assumptions, the smoothed function is differentiable and its gradient is the score expectation. | repro/numerics.py evaluates the absolute-value test function at x=0.37 using unit Laplace and symmetric triangular perturbations. Independent quadrature is compared with closed form, and a deliberately wrong Gaussian score is used as a negative control. | evidence/run_cbb3de08/cumulative_result.json and the Claim 1 checker: Laplace error 0, triangular error 0, wrong-score error 0.053693967. VERIFIED |
| 2 | Theorem 7: location and scale-matrix gradients for the multivariate smoothed function. | repro/numerics.py computes the disclosed finite instance and compares analytic gradients with independent centered finite differences. | Location error 9.95e-12; scale error 1.53e-11. VERIFIED |
| 3 | Theorem 8: output-covariance derivatives. | The same numerical module evaluates the covariance construction and checks both input and scale derivatives against finite differences. | Input error 2.37e-11; scale error 5.20e-10. VERIFIED |
| 4 | Section 4 benchmarks six distributions and the feasible sampling, covariate, and antithetic combinations on hard sorting and shortest-path operators. | repro/section4.py reconstructs the operators, samples, independent sorting oracle, calibrated shortest-path oracle, official Warcraft data, controls, and all feasible cells. repro/check_section4.py checks the raw CSV independently. | evidence/run_cbb3de08/section4_raw.csv: exactly 447/447 cells, six distributions, official data integrity, non-vacuity, and oracle checks pass. VERIFIED |
| 5 | Cartesian RQMC with LOO and no antithetic pairing is within 1% of the cell minimum when feasible; triangular noise uses the paper's Latin-QMC exception. | The Section 4 result ranks every strategy cell against the paper target separately for sorting sizes n=3,5 and shortest-path sizes 8x8,12x12. | Target is within 1% of the minimum in all 12/12 sorting/distribution cases. VERIFIED |
| 6 | Sections 4.2–4.5 demonstrate smoothing on MNIST sorting, Warcraft shortest paths, Utah-teapot pose recovery, and TEM simulation optimization. | Four separate routes use repro/mnist_application.py, warcraft_application.py, rendering_application.py, and tem_application.py, each with an independent checker and an honest blocked outcome when the exact scale or source assets are unavailable. | evidence/run_cbb3de08/*_checker.json: all route checks pass, but the quantifier over all four full demonstrations is not satisfied. BLOCKED |

### Claim 6 route status

| Application | Disclosed protocol recorded | What was actually run | Why the claim remains blocked |
| --- | --- | --- | --- |
| MNIST | Four-digit sorting, n=5, 100,000 Adam steps, 12 seeds, batch 100, 256 Laplace randomized-Latin/LOO samples. | Official data and model shape were audited; 100 measured CPU steps produced a finite throughput projection. | It was not a 100,000-step, 12-seed run. The current JSON projects about 32.78 hours per seed on the selected CPU allocation. |
| Warcraft | Official 12x12 maps, first ResNet18 block, 50 epochs, five seeds, batch 70, Adam learning rate 0.001 with the disclosed schedule. | Official archive and model were audited; 20 optimizer steps and an independent shortest-path oracle were run. | This is a calibration, not the disclosed 50-epoch, five-seed experiment. |
| Utah teapot | Four camera degrees of freedom, 1,000 Adam steps, 768 seeds, cosine schedule, success within five degrees. | The cited GenDR source was pinned and its build/device requirements were audited. | The cited source requires CUDA and is not the paper's exact black-box application implementation; no substitute renderer is accepted. |
| TEM | TEM-simulator v1.3, 400x400 micrographs, two- and four-parameter searches, disclosed ground truth and optimizer assumptions. | Public archives were authenticated, manifests were audited, and a one-byte corruption control was rejected. | The exact author input deck, specimen mapping, smoothing implementation, initialization, learning rate, and horizon are unavailable; no assumption-satisfying counterexample was found. |

## How each claim is produced

The evidence pipeline is:

1. source_audit.md files extract assumptions, source anchors, numerical domains, and thresholds from the paper and cited primary archives.
2. Claims 1–3 use independent quadrature and finite differences rather than trusting one autodiff path.
3. Claims 4–5 reconstruct the actual hard operators, six perturbation distributions, all feasible strategy cells, path scale calibration, held-out non-vacuity checks, independent oracles, and negative controls.
4. Claim 6 keeps each application separate. A finite calibration, a capability probe, or a substitute implementation cannot silently become full claim evidence.
5. repro.run executes the cumulative route and writes raw JSON/CSV evidence. The repro/check_*.py programs validate the raw outputs independently and exit nonzero when a contract fails.

The canonical recorded cumulative run is cbb3de08-48e9-48a0-87c9-5ffb65d6e9cb, using pre-normalization scientific commit 75d1f2c6c76c2c642ba59319a097a79a4f5e504d. It used HF cpu-upgrade with an 8-vCPU cgroup quota, an 8-worker cap, no GPU, 2,287.09 seconds of scientific runtime, and an estimated scientific cost of $0.01906. These values describe the historical evidence already committed here; the repository cleanup did not rerun the campaign.

## Repository map

| Path | Responsibility |
| --- | --- |
| repro/numerics.py | Independent theorem/calibration numerics for Claims 1–3. |
| repro/section4.py | Sorting and shortest-path operators, sampling strategies, path calibration, and benchmark generation. |
| repro/check_section4.py | Independent raw CSV and contract checker for Claims 4–5. |
| repro/mnist_application.py | Exact-protocol MNIST throughput/calibration route. |
| repro/warcraft_application.py | Official Warcraft data/model/oracle calibration route. |
| repro/rendering_application.py | Pinned GenDR capability and protocol audit. |
| repro/tem_application.py | TEM primary-archive and falsification audit. |
| repro/run.py | Fixed cumulative entrypoint and checker orchestration. |
| evidence/run_cbb3de08/ | Canonical raw outputs and independent checker outputs. |
| reports/full-reproduction/report.md | Visual technical report. |
| .openresearch/artifacts/ | Claim contracts, source audits, methods, limitations, and historical rejected routes. |
| notebooks/reproduction.py | Self-contained evaluator-facing Marimo notebook. |
| branch-audit.md | Historical branch purpose and normalization record. |

## Reproduce the recorded workflow

From a clean environment with the required dependencies:

    uv sync --frozen --no-dev
    .venv/bin/python -m repro.run

The command is cumulative and writes generated evidence under evidence/. It is not a promise that a local laptop can reproduce the historical HF runtime. GPU, paid, and remote compute must be explicitly authorized before starting a new campaign.

For focused inspection, read the current verification pages:

- [Current verification](pages/current/page.md)
- [Claims 1–3](pages/current/claims-1-3.md)
- [Claims 4–5](pages/current/claims-4-5.md)
- [Claim 6](pages/current/claim-6.md)
- [Full technical report](reports/full-reproduction/report.md)
- [Release forecast](pages/current/release.md)

## Branch policy and history

The normalized repository has one canonical branch: main. Historical experiment branch purposes are preserved in [branch-audit.md](branch-audit.md); the old orx/ remote pointers were not part of the final publication surface.

Every reachable commit after normalization is attributed to MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>. The scientific run metadata retains its original commit SHA and experiment branch as provenance for the evidence, while the public repository history is normalized for maintainability.

The complete branch table is preserved in [branch-audit.md](branch-audit.md) and summarized in [BRANCH_AUDIT.md](BRANCH_AUDIT.md).

## Limitations

- Numerical checks corroborate finite identities; they do not replace the paper's symbolic proofs.
- Claims 4–5 are an independent reconstruction because the paper's exact implementation and all input tables are not published.
- Claim 6 is a conjunction over four applications. Partial calibration is reported as partial calibration.
- The current repository records evidence produced under an HF CPU allocation. It does not grant permission to run expensive or GPU workloads.
- Historical forecast language in the release pages is not a judge result.

## Citation

    @article{petersen2024generalizing,
      title         = {Generalizing Stochastic Smoothing for Differentiation and Gradient Estimation},
      author        = {Petersen, Felix and Borgelt, Christian and Mishra, Aashwin Ananda and Ermon, Stefano},
      journal       = {arXiv preprint arXiv:2410.08125},
      year          = {2024},
      doi           = {10.48550/arXiv.2410.08125}
    }

## Thank you

Thank you to Felix Petersen, Christian Borgelt, Aashwin Ananda Mishra, and Stefano Ermon for developing and documenting this framework. The paper's explicit assumptions, operator definitions, variance-reduction structure, and application details made an auditable independent reconstruction possible. This repository is offered as a respectful reproduction record, including its blocked results and limitations.
