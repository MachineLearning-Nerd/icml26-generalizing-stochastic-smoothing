# Environment and artifact record

## Recorded scientific runs

### Canonical cumulative run

- Run ID: cbb3de08-48e9-48a0-87c9-5ffb65d6e9cb
- Command: uv sync --frozen --no-dev && .venv/bin/python -m repro.run
- Backend/flavor: HF cpu-upgrade
- Hardware: 8 declared and cgroup vCPUs, worker limit 8, no GPU
- Interpreter: Python 3.12.12
- Platform: Linux-6.12.90-120.164.amzn2023.x86_64-x86_64-with-glibc2.36
- Scientific runtime: 2287.0881601369474 seconds
- Estimated scientific cost: 0.019059068001141228 USD
- Source experiment branch/SHA: historical orx/tem-primary-source-falsification-and-cumulative at 75d1f2c6c76c2c642ba59319a097a79a4f5e504d

### Publication-gate run

- Run ID: 174c64f5-4aba-4818-a515-0ee0c9479741
- Command: uv sync --frozen --no-dev && .venv/bin/python -m repro.run
- Backend/flavor: HF cpu-upgrade; 8 cgroup vCPUs; no GPU
- Interpreter: Python 3.12.12
- Scientific runtime: 2611.389107635943 seconds
- Estimated scientific cost: 0.021761575896966194 USD
- Release checker: passed; all regressions passed; Marimo checker returned zero

These are historical provenance records. A new run requires explicit compute
authorization and must create a new evidence record.

## Dependencies

The project is pinned by pyproject.toml and uv.lock:

- Python >=3.12,<3.13
- marimo 0.23.1
- NumPy 2.3.2
- pandas 2.3.1
- scikit-image 0.25.2
- scipy 1.16.1
- torch 2.7.1+cpu
- torchvision 0.22.1+cpu

## Content-addressed evidence

The complete evaluator upload surface is covered by
release/upload_manifest.sha256. Selected immutable evidence hashes are:

| Artifact | SHA-256 |
| --- | --- |
| evidence/run_cbb3de08/cumulative_result.json | c731d9bb0f0fc3a24d87cdbad8f10b8e130d4c3ee62106a93438516c0856eac9 |
| evidence/run_cbb3de08/section4_raw.csv | 07ff1d244eea4412ee1dda84ec20370bbf6808fe314836dba6b5b8527a66c619 |
| evidence/run_cbb3de08/section4_checker.json | 1b1215bc96d177c7e36e552f9e432dbf10b3ef8c545a1cf6197fcfd40aede933 |
| evidence/run_cbb3de08/mnist_result.json | 71fc0c56f5cb2f6c053fbe2b0172b86738663bae2ee6540aae1638a177f1b119 |
| evidence/run_cbb3de08/warcraft_result.json | 1ccfacabba41fb252761494db398a1642249b8b7a90ef31a317be85bab93af61 |
| evidence/run_cbb3de08/rendering_result.json | 23d2055328fde5ab30e62ae652a2a4282aa9fd077b73a11fa2c47afd442b5f10 |
| evidence/run_cbb3de08/tem_result.json | 609ad038391913f9fef8675bdcd7f9a796a29b6e8df6c19c2934045c7517f09c |
| evidence/run_174c64f5/cumulative_result.json | 9fb7c58e5f87c6488c020ef5a88e60059623859d92552a49b374a63b4c03ac40 |
| evidence/run_174c64f5/release_checker.json | 1bb09415c8681433956c3a3ed92778f82e96b1e7f93a87b6c539bcb9a085b2c2 |
| evidence/run_174c64f5/run_metadata.json | 869719b05a092838701380a02c62ce21721711b54ea428768139a553ed43f202 |
| logbook.json | 1e8138e803a34717c654dc090fede67132107b6b7ab94faf5bb94abe9bac9c11 |
| notebooks/reproduction.py | 2c1f5fde326a7e2c50746bea4f0cc7c3a66f843bb70b7973066fc4b2acae36de |
| pyproject.toml | db69c7243b94fd2b9c5c9857caa30888f100a9243e2ab4238945c40dd81aae5b |
| uv.lock | 481c3d6f9eb6bd123130322fb126fbf579d48f118a140bb597d14a3bbf3b3afa |
