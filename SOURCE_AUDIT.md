# Source audit

## Paper identity

| Source | Record |
| --- | --- |
| Primary paper | [arXiv:2410.08125](https://arxiv.org/abs/2410.08125) |
| Public review record | [OpenReview GBWqZNoeIk](https://openreview.net/forum?id=GBWqZNoeIk) |
| Public review context | ICLR 2025 submission 3968 |
| Collection label | ICML 2026 repository collection; not the paper's venue metadata |
| Source HTML | [ar5iv HTML](https://ar5iv.labs.arxiv.org/html/2410.08125) |
| Authors | Felix Petersen, Christian Borgelt, Aashwin Ananda Mishra, Stefano Ermon |

The local source record retains the ar5iv HTML SHA-256
053740ba5182819585699124d6672d9772e91b5d080cb3b047d74f7dd54dc8fd and the
arXiv source archive SHA-256
3412645ed7d51a75388b91252a3c2dfd74781806e5b73b0f97a944f0d95430bb.
The hashes are source pins recorded by the original audit; the source archive
is not silently replaced by a newer public revision.

## Implementation and data provenance

The public source record does not identify an author-maintained implementation
repository. This collection therefore distinguishes independent reconstruction
code from cited external sources:

- Warcraft data/model audit:
  martius-lab/blackbox-differentiation-combinatorial-solvers at
  027e82ee818530f2823851d6530e0d2c8657bbcb.
- Rendering capability audit:
  Felix-Petersen/gendr at
  c89269cb38eef7a95be703154f676a56d791958f.
- TEM archive audit:
  the public TEM Simulator SourceForge archives, authenticated by the
  committed source-audit and manifest records.

The independent producers are under repro/. The cited repositories and
archives are provenance inputs, not evidence that their entire upstream
experiments were rerun here.

## Evidence boundaries

- Claims 1–3 are finite numerical calibrations of Lemma 3 and Theorems 7–8.
- Claims 4–5 are an independent reconstruction of the disclosed Section 4
  benchmark and target ranking, with explicit feasibility and oracle checks.
- Claim 6 is a four-route conjunction. Missing author assets, CPU
  calibration, CUDA capability, or substitute implementations cannot be
  silently treated as completion or falsification.
- The historical evidence was produced with HF cpu-upgrade, an 8-vCPU cgroup
  quota, no GPU, and a declared cost record. The current cleanup did not
  rerun it.
- The exact source revision, code pins, input archives, and thresholds must be
  recorded before any future claim changes.
