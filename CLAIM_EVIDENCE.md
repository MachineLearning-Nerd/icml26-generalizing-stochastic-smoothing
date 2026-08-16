# Claim-to-evidence map

The repository reports evidence statuses, not a claim that finite numerical
checks replace the paper's symbolic proofs. Each row below identifies the
paper anchor, producer, raw evidence, controls, and the boundary of the
result.

## Common production graph

    paper anchor -> source assumptions -> independent producer
                 -> raw output -> independent checker/control -> status

The canonical cumulative run is
evidence/run_cbb3de08/cumulative_result.json. A later publication-gate run is
retained under evidence/run_174c64f5. Neither run is silently rerun by the
repository cleanup.

## C1 - Score identity for absolute-continuity smoothing

- Paper anchor: Lemma 3.
- Claim: for the declared assumptions, the smoothed gradient equals the
  expectation of the function multiplied by the perturbation score.
- Producer: repro/numerics.py evaluates f(x)=|x| at x=0.37 with unit Laplace
  and symmetric triangular perturbations, using independent quadrature and
  closed-form comparisons.
- Evidence: evidence/run_cbb3de08/cumulative_result.json,
  mnist-independent Claim 1 artifacts under
  .openresearch/artifacts/claim_1/, and the release checker.
- Controls: the Laplace score is replaced with a deliberately wrong Gaussian
  score. The correct errors are 0.0 and the wrong-score error is
  0.05369396702682416.
- Status: VERIFIED finite theorem/calibration check.
- Boundary: this is a finite numerical corroboration at the declared point,
  not a proof for every admissible density and function.

## C2 - Location and scale-matrix gradients

- Paper anchor: Theorem 7.
- Claim: the location and scale-matrix derivatives of the multivariate
  smoothed function follow the stated score identities.
- Producer: repro/numerics.py computes the disclosed finite instance and
  compares both analytic derivatives against independent centered finite
  differences.
- Evidence: cumulative_result.json and the Claim 1–3 contract/checker pages.
- Recorded errors: location 9.952129398360654e-12; scale
  1.5252021867695476e-11.
- Status: VERIFIED finite theorem/calibration check.
- Boundary: finite dimensions and finite-difference step; no universal proof.

## C3 - Output-covariance derivatives

- Paper anchor: Theorem 8.
- Claim: the output-covariance derivative construction agrees with the
  stated formula.
- Producer: the independent numerical module evaluates input and scale
  derivatives and compares both with centered finite differences.
- Evidence: cumulative_result.json and the Claim 1–3 contract/checker pages.
- Recorded errors: input 2.3664403769885212e-11; scale
  5.203468766978858e-10.
- Status: VERIFIED finite theorem/calibration check.
- Boundary: finite calibration only; it does not replace symbolic derivation.

## C4 - Six-distribution Section 4 benchmark

- Paper anchor: Section 4 benchmark and the disclosed sorting/shortest-path
  operator comparisons.
- Claim: the stated sampling distributions and feasible variance-reduction
  combinations can be evaluated over the complete benchmark cells.
- Producer: repro/section4.py reconstructs sorting and shortest-path
  operators, six distributions, MC/QMC/RQMC strategies, covariates,
  antithetic feasibility, calibrated path oracles, and official Warcraft
  inputs. repro/check_section4.py independently checks the raw CSV.
- Evidence: evidence/run_cbb3de08/section4_raw.csv,
  section4_checker.json, the claims_4_5 contract, and the 447-cell release
  surface.
- Controls: official data integrity, path validity, non-vacuity, independent
  sorting/path oracles, and a wrong-score negative control all pass.
- Status: VERIFIED finite benchmark reconstruction across 447/447 cells.
- Boundary: the authors' unreleased implementation is unavailable; this is an
  independent reconstruction with explicit source and feasibility limits.

## C5 - Paper-target ranking

- Paper anchor: the Section 4 target-strategy conclusion.
- Claim: the paper's Cartesian RQMC plus LOO target is within 1% of the cell
  minimum when feasible, with the declared Latin-QMC exception for Triangular
  noise.
- Producer: the Section 4 checker ranks the target against the minimum
  separately for sorting sizes n=3,5 and shortest-path sizes 8x8,12x12.
- Evidence: section4_raw.csv, section4_checker.json, and the Claims 4–5
  contract/limitations pages.
- Recorded result: 12/12 target cases are within 1% of the cell minimum.
- Status: VERIFIED scoped paper-target ranking.
- Boundary: no broad optimizer or real-world superiority claim is made.

## C6 - Four application demonstrations

- Paper anchor: Sections 4.2–4.5: MNIST sorting, Warcraft shortest paths,
  Utah-teapot rendering, and TEM simulation optimization.
- Claim: all four demonstrations run under their disclosed protocols.
- Producers: repro/mnist_application.py, warcraft_application.py,
  rendering_application.py, and tem_application.py, each paired with an
  independent checker.
- Evidence: the four raw/checker JSON pairs under
  evidence/run_cbb3de08 and the Claim 6 contract, methods, source audits, and
  limitations.
- Recorded route status: MNIST and Warcraft have finite CPU calibrations but
  not the full disclosed runs; the Utah route is blocked by CUDA/source
  capability; TEM assets/configuration are incomplete and its corruption
  control rejects altered archives.
- Status: BLOCKED. No route supplies a valid full-scale falsification, and
  partial calibration is not promoted to complete claim evidence.
- Boundary: the conjunction over all four applications remains open.

## Overall interpretation

Claims 1–5 are supported at the finite, explicitly scoped levels above. Claim
6 remains blocked. No current judge score or universal theorem proof is
claimed. The historical HF CPU run and evaluator release checks are provenance
for the recorded evidence, not authorization for a new expensive run.
