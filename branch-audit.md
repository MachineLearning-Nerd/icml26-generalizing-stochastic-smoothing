# Historical branch audit

The repository had one publication branch and fourteen remote experiment branches before normalization. Every listed branch tip was an ancestor of the pre-normalization main tip 75f7afea19f6a90a8ecb17280f773f64d4be5f34, so the experiment history is retained by main even after the branch pointers are retired.

| Former branch | Pre-normalization tip | Purpose and recorded outcome | Disposition |
| --- | --- | --- | --- |
| main | 75f7afea19f6a90a8ecb17280f773f64d4be5f34 | Final publication surface and pinned Marimo cell serialization. | Keep as canonical main |
| orx/judged-8-12-baseline-with-reproducible-environme | 448579491ffe35e7b113204da313cdcbc7405da0 | Freeze the judged 8/12 baseline and reproducible environment; Claims 1–3 verified, Claims 4–5 historical proxy only. | Retire pointer; history retained |
| orx/faithful-section-4-operator-variance-benchmark | 1deb3262fbb425f3ff53020c4e64e9cb661fa85f | Run the full Section 4 operator and variance benchmark. | Retire pointer; history retained |
| orx/correct-cartesian-rqmc-and-calibrated-path-oracl | de38f9648ac2de1edba31598b65784ff3beeaa9d | Correct Cartesian RQMC construction and calibrate path-oracle power. | Retire pointer; history retained |
| orx/calibrated-triangular-path-oracle-power | e708663b426d81bcd01691af488477525e9359f3 | Increase and calibrate the Triangular path-oracle block size. | Retire pointer; history retained |
| orx/exact-protocol-mnist-throughput-calibration | 4987217780b4ebaa2fc85a656d88f62bd636e149 | Measure the exact MNIST protocol's CPU throughput before deciding on a full run. | Retire pointer; history retained |
| orx/official-warcraft-inputs-and-non-vacuous-calibra | b2da30445b39e05ee7677e48b10995dc7c374405 | Switch to official Warcraft inputs and add non-vacuous path calibration. | Retire pointer; history retained |
| orx/official-warcraft-protocol-cpu-calibration | 10ab5598233c6c6885567059ff30cfffb9df3b49 | Repair official Warcraft map image handling and calibrate the CPU route. | Retire pointer; history retained |
| orx/pinned-gendr-cpu-capability-and-protocol-audit | 552b78becdb9a78629f679370b913c514c668eaa | Pin GenDR, audit CUDA capability, and distinguish the cited source from the paper protocol. | Retire pointer; history retained |
| orx/tem-primary-source-falsification-and-cumulative | 75d1f2c6c76c2c642ba59319a097a79a4f5e504d | Authenticate TEM sources, run the mandatory falsification route, and produce the cumulative Claims 1–6 evidence. | Retire pointer; evidence retained in main |
| orx/evaluator-visible-release-candidate | dd88a14505e222a19967fd560930e1b5080a7c37 | Prepare the first evaluator-visible candidate; scientific checks passed but release packaging failed. | Retire pointer; history retained |
| orx/repair-publication-gate-and-red-team-candidate | f2a974d677660fa7168072c3c710ccf15bdc9efa | Repair evaluator evidence, pin notebook validation, and add red-team checks. | Retire pointer; history retained |
| orx/final-evaluator-blind-release-regression | bf2249b2c963820f1989bf572efe5f4399450f22 | Run evaluator-blind release regression and warning checks. | Retire pointer; history retained |
| orx/canonical-warning-free-marimo-release-regression | 9530144b25927123ddd6e427db337cc3763afa6b | Make the final Marimo artifact warning-free. | Retire pointer; history retained |
| orx/formatter-exact-marimo-release-regression | 75f7afea19f6a90a8ecb17280f773f64d4be5f34 | Match the pinned Marimo cell serialization; same tip as main. | Retire duplicate pointer |

The branch names were generated experiment labels, not stable public API. The normalized publication surface uses only main. Branch-specific claims and outcomes remain inspectable through this audit and the committed evidence paths.

Before normalization, the branch tips were authored with the local Dinesh identity. The final history rewrite sets both author and committer to MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com> for every reachable commit.
