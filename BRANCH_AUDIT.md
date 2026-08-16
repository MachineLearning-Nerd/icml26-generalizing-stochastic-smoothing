# Branch audit

## Final branch policy

| Final branch | Former public refs | Purpose |
| --- | --- | --- |
| main | main plus fourteen retired orx experiment pointers | Complete publication surface: claims, raw evidence, evaluator release, and audit dossier. |

The final repository is main-only. The fourteen historical experiment branches
are not lost: their tips were ancestors of the pre-normalization main tip and
their purposes and outcomes are recorded in [branch-audit.md](branch-audit.md).
No orx branch is part of the final public branch inventory.

The branch work covered, in order, the judged baseline, the Section 4
operator benchmark, Cartesian RQMC and path-oracle calibration, MNIST
throughput calibration, official Warcraft data and CPU calibration, GenDR
capability auditing, TEM source/falsification work, evaluator packaging,
red-team checks, warning-free Marimo release checks, and final serialization.
The detailed table is authoritative for each former branch and its disposition.

## History and attribution

The pre-normalization publication tip was
75f7afea19f6a90a8ecb17280f773f64d4be5f34, with 25 reachable commits in the
current normalized history before this dossier commit. The dossier commit is
the only additional commit introduced by this audit.

- Repository: MachineLearning-Nerd/icml26-generalizing-stochastic-smoothing.
- Default and final branch: main.
- Author and committer: MachineLearning-Nerd
  <MachineLearning-Nerd@users.noreply.github.com>.
- Co-author trailers: none permitted.
- Legacy refs: no refs/original or retired remote branch is part of the final publication.

The scientific run metadata keeps its historical experiment branch and commit
SHA as evidence provenance. Those values do not indicate live Git branches.
verify_final.py checks the final branch inventory, canonical identities, and
absence of temporary rewrite refs.
