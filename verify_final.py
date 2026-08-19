#!/usr/bin/env python3
"""Fail-closed checks for the published stochastic-smoothing audit."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_REPOSITORY = "MachineLearning-Nerd/icml26-generalizing-stochastic-smoothing"
CANONICAL_NAME = "MachineLearning-Nerd"
CANONICAL_EMAIL = "MachineLearning-Nerd@users.noreply.github.com"
EXPECTED_BRANCHES = {"main"}
EXPECTED_COMMIT_COUNT = 28
EXPECTED_OVERALL_VERDICT = "VERIFIED_SCOPED_CLAIMS_1_TO_5_CLAIM_6_BLOCKED"
EXPECTED_CLAIMS = {
    "C1": "VERIFIED",
    "C2": "VERIFIED",
    "C3": "VERIFIED",
    "C4": "VERIFIED",
    "C5": "VERIFIED",
    "C6": "BLOCKED",
}
EXPECTED_HASHES = {
    "evidence/run_cbb3de08/cumulative_result.json": "c731d9bb0f0fc3a24d87cdbad8f10b8e130d4c3ee62106a93438516c0856eac9",
    "evidence/run_cbb3de08/section4_raw.csv": "07ff1d244eea4412ee1dda84ec20370bbf6808fe314836dba6b5b8527a66c619",
    "evidence/run_cbb3de08/section4_checker.json": "1b1215bc96d177c7e36e552f9e432dbf10b3ef8c545a1cf6197fcfd40aede933",
    "evidence/run_cbb3de08/mnist_result.json": "71fc0c56f5cb2f6c053fbe2b0172b86738663bae2ee6540aae1638a177f1b119",
    "evidence/run_cbb3de08/warcraft_result.json": "1ccfacabba41fb252761494db398a1642249b8b7a90ef31a317be85bab93af61",
    "evidence/run_cbb3de08/rendering_result.json": "23d2055328fde5ab30e62ae652a2a4282aa9fd077b73a11fa2c47afd442b5f10",
    "evidence/run_cbb3de08/tem_result.json": "609ad038391913f9fef8675bdcd7f9a796a29b6e8df6c19c2934045c7517f09c",
    "evidence/run_174c64f5/cumulative_result.json": "9fb7c58e5f87c6488c020ef5a88e60059623859d92552a49b374a63b4c03ac40",
    "evidence/run_174c64f5/release_checker.json": "1bb09415c8681433956c3a3ed92778f82e96b1e7f93a87b6c539bcb9a085b2c2",
    "evidence/run_174c64f5/run_metadata.json": "869719b05a092838701380a02c62ce21721711b54ea428768139a553ed43f202",
    "logbook.json": "1e8138e803a34717c654dc090fede67132107b6b7ab94faf5bb94abe9bac9c11",
    "notebooks/reproduction.py": "2c1f5fde326a7e2c50746bea4f0cc7c3a66f843bb70b7973066fc4b2acae36de",
    "pyproject.toml": "db69c7243b94fd2b9c5c9857caa30888f100a9243e2ab4238945c40dd81aae5b",
    "uv.lock": "481c3d6f9eb6bd123130322fb126fbf579d48f118a140bb597d14a3bbf3b3afa",
    "README.md": "fc30331f1e262f3d276848421777693e20fc60d59e1885d0d9ff88e5096a7cad",
    "STATUS.md": "055345c42320d9f56083987f4c53644f19707a9f9c806218c88049d3a8ee7262",
    "REPORT.md": "1b7b1e6e7dd569bf4edeacbd4fb67a67ee7075c0094ef77b61d6937c10d8950b",
    "claims.json": "5e98424960e0dafe4dee674016f2885d1992e54ea876de3c0875f169a1c03616",
    "reproduction_verdicts.json": "a1bc4d48bc0a5b69d46f24d23f70a298777e104db78c0cba17c7cd18648e0d67",
    "AUTONOMOUS_STATE.json": "565138e4c7c38d07e87699c893f4df67b6423db5ba556d2dc4f66a1554194795",
}
REQUIRED_FILES = {
    "README.md",
    "STATUS.md",
    "REPORT.md",
    "CLAIM_EVIDENCE.md",
    "SOURCE_AUDIT.md",
    "BRANCH_AUDIT.md",
    "ENVIRONMENT.md",
    "AUTHOR_THANK_YOU.md",
    "CITATION.cff",
    "claims.json",
    "reproduction_verdicts.json",
    "AUTONOMOUS_STATE.json",
    "EVIDENCE_MANIFEST.json",
    "verify_final.py",
}
REQUIRED_EVIDENCE_PATHS = {
    "branch-audit.md",
    "logbook.json",
    "pages/current/page.md",
    "pages/current/claims-1-3.md",
    "pages/current/claims-4-5.md",
    "pages/current/claim-6.md",
    "evidence/run_cbb3de08/cumulative_result.json",
    "evidence/run_cbb3de08/section4_raw.csv",
    "evidence/run_cbb3de08/section4_checker.json",
    "evidence/run_cbb3de08/mnist_result.json",
    "evidence/run_cbb3de08/warcraft_result.json",
    "evidence/run_cbb3de08/rendering_result.json",
    "evidence/run_cbb3de08/tem_result.json",
    "evidence/run_174c64f5/cumulative_result.json",
    "evidence/run_174c64f5/release_checker.json",
    "release/upload_allowlist.txt",
    "release/upload_manifest.sha256",
    "repro/check_release.py",
    "pyproject.toml",
    "uv.lock",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def run(*args: str) -> str:
    result = subprocess.run(args, cwd=ROOT, check=True, capture_output=True, text=True)
    return result.stdout


def read_json(relative_path: str) -> object:
    with (ROOT / relative_path).open(encoding="utf-8") as handle:
        return json.load(handle)


def sha256(relative_path: str) -> str:
    digest = hashlib.sha256()
    with (ROOT / relative_path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def local_branches() -> set[str]:
    refs = run("git", "for-each-ref", "refs/heads", "--format=%(refname:strip=2)")
    return {ref.strip() for ref in refs.splitlines() if ref.strip()}


def remote_branches() -> set[str]:
    prefix = "refs/remotes/origin/"
    refs = run("git", "for-each-ref", "refs/remotes/origin", "--format=%(refname)")
    return {
        ref.strip()[len(prefix):]
        for ref in refs.splitlines()
        if ref.strip().startswith(prefix) and ref.strip() != prefix + "HEAD"
    }


def verify_history() -> None:
    records = run("git", "log", "--all", "--format=%an%x00%ae%x00%cn%x00%ce").splitlines()
    if not records:
        fail("no reachable commits")
    expected = f"{CANONICAL_NAME}\x00{CANONICAL_EMAIL}\x00{CANONICAL_NAME}\x00{CANONICAL_EMAIL}"
    unexpected = sorted({record for record in records if record != expected})
    if unexpected:
        fail(f"non-canonical reachable identities: {unexpected}")
    if "Co-authored-by:" in run("git", "log", "--all", "--format=%B"):
        fail("co-author trailer found")
    count = int(run("git", "rev-list", "--count", "--all").strip())
    if count != EXPECTED_COMMIT_COUNT:
        fail(f"expected {EXPECTED_COMMIT_COUNT} reachable commits, found {count}")
    if run("git", "for-each-ref", "refs/original", "--format=%(refname)").strip():
        fail("temporary refs/original remain")


def verify_remote() -> None:
    remote = run("git", "config", "--get", "remote.origin.url").strip()
    normalized = remote.removesuffix(".git").rstrip("/")
    if not normalized.endswith(EXPECTED_REPOSITORY):
        fail(f"origin is {remote!r}, expected {EXPECTED_REPOSITORY!r}")


def verify_release_manifest() -> None:
    allowlist = [
        line.strip()
        for line in (ROOT / "release/upload_allowlist.txt").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if len(allowlist) != 93 or len(set(allowlist)) != 93:
        fail("upload allowlist is not the recorded 93 unique paths")
    manifest: dict[str, str] = {}
    for line in (ROOT / "release/upload_manifest.sha256").read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        digest, path = line.split("  ", 1)
        manifest[path] = digest
    expected_paths = set(allowlist) - {"release/upload_manifest.sha256"}
    if set(manifest) != expected_paths:
        fail("upload manifest does not cover the allowlist")
    for path, digest in manifest.items():
        if not (ROOT / path).is_file():
            fail(f"allowlist path is missing: {path}")
        if sha256(path) != digest:
            fail(f"upload manifest hash mismatch: {path}")


def verify_evidence() -> None:
    for relative_path, expected_hash in EXPECTED_HASHES.items():
        if sha256(relative_path) != expected_hash:
            fail(f"evidence hash mismatch: {relative_path}")
    cumulative = read_json("evidence/run_cbb3de08/cumulative_result.json")
    if cumulative.get("all_regressions_passed") is not True:
        fail("canonical cumulative run did not pass all regressions")
    observed_verdicts = [
        cumulative["claims"][str(index)]["verdict"] for index in range(1, 7)
    ]
    if observed_verdicts != ["VERIFIED", "VERIFIED", "VERIFIED", "VERIFIED", "VERIFIED", "BLOCKED"]:
        fail(f"unexpected cumulative verdicts: {observed_verdicts}")
    release = read_json("evidence/run_174c64f5/release_checker.json")
    if release.get("passed") is not True or not all(release.get("checks", {}).values()):
        fail("publication-gate release checker is not fully passing")
    with (ROOT / "evidence/run_cbb3de08/section4_raw.csv").open(newline="", encoding="utf-8") as handle:
        if len(list(csv.DictReader(handle))) != 447:
            fail("Section 4 raw CSV does not contain 447 rows")


def verify_ledgers() -> None:
    claims = read_json("claims.json")
    manifest = read_json("EVIDENCE_MANIFEST.json")
    if not isinstance(claims, dict) or not isinstance(manifest, dict):
        fail("claims and manifest must be JSON objects")
    for record in (claims, manifest):
        if record.get("repository") != EXPECTED_REPOSITORY:
            fail("repository marker is wrong")
        if record.get("overall_status") != "VERIFIED_CLAIMS_1_TO_5_BLOCKED_CLAIM_6":
            fail("overall status is wrong")
        if record.get("overall_verdict") != EXPECTED_OVERALL_VERDICT:
            fail("overall verdict is wrong")
        if (
            record.get("publication_allowed") is not False
            or record.get("score_claim") is not False
            or record.get("official_author_endorsement") is not False
        ):
            fail("publication boundary is wrong")
    observed = {row.get("id"): row.get("status") for row in claims.get("claims", [])}
    if observed != EXPECTED_CLAIMS:
        fail(f"claim ledger statuses are wrong: {observed}")
    if manifest.get("claim_statuses") != EXPECTED_CLAIMS:
        fail("manifest claim statuses are wrong")
    manifest_hashes = {
        item.get("path"): item.get("sha256")
        for item in manifest.get("content_addressed_artifacts", [])
        if isinstance(item, dict)
    }
    if any(manifest_hashes.get(path) != digest for path, digest in EXPECTED_HASHES.items()):
        fail("manifest artifact hashes do not match")
    if set(manifest.get("required_audit_files", [])) != REQUIRED_FILES:
        fail("manifest audit-file list is wrong")
    if manifest.get("branches", {}).get("expected_final") != ["main"]:
        fail("manifest branch policy is wrong")
    if manifest.get("attribution", {}).get("email") != CANONICAL_EMAIL:
        fail("manifest attribution is wrong")

    reproduction = read_json("reproduction_verdicts.json")
    if reproduction.get("repository") != EXPECTED_REPOSITORY:
        fail("reproduction repository marker is wrong")
    if reproduction.get("overall_verdict") != EXPECTED_OVERALL_VERDICT:
        fail("reproduction overall verdict is wrong")
    if (
        reproduction.get("publication_allowed") is not False
        or reproduction.get("score_claim") is not False
        or reproduction.get("official_author_endorsement") is not False
    ):
        fail("reproduction publication boundary is wrong")
    reproduction_claims = {
        row.get("id"): row.get("status")
        for row in reproduction.get("claims", [])
    }
    if reproduction_claims != EXPECTED_CLAIMS:
        fail(f"reproduction claim statuses are wrong: {reproduction_claims}")

    state = read_json("AUTONOMOUS_STATE.json")
    if state.get("repository") != EXPECTED_REPOSITORY:
        fail("state repository marker is wrong")
    if state.get("overall_verdict") != EXPECTED_OVERALL_VERDICT:
        fail("state overall verdict is wrong")
    if (
        state.get("publication_allowed") is not False
        or state.get("score_claim") is not False
        or state.get("official_author_endorsement") is not False
        or state.get("branch_count") != 1
    ):
        fail("state publication boundary is wrong")


def main() -> int:
    missing = sorted(path for path in REQUIRED_FILES | REQUIRED_EVIDENCE_PATHS if not (ROOT / path).exists())
    if missing:
        fail(f"missing required paths: {missing}")
    verify_ledgers()
    verify_evidence()
    verify_release_manifest()
    verify_remote()
    if local_branches() != EXPECTED_BRANCHES:
        fail(f"local branches differ: {sorted(local_branches())}")
    if remote_branches() != EXPECTED_BRANCHES:
        fail(f"remote branches differ: {sorted(remote_branches())}")
    verify_history()

    branch_audit = (ROOT / "branch-audit.md").read_text(encoding="utf-8")
    if branch_audit.count("| orx/") != 14:
        fail("historical branch table does not contain fourteen orx branches")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for marker in (
        "CLAIM_EVIDENCE.md",
        "SOURCE_AUDIT.md",
        "BRANCH_AUDIT.md",
        "ENVIRONMENT.md",
        "CITATION.cff",
        "AUTHOR_THANK_YOU.md",
        "VERIFIED",
        "BLOCKED",
        "reproduction_verdicts.json",
        "AUTONOMOUS_STATE.json",
        "publication_allowed",
        "verify_final.py",
    ):
        if marker not in readme:
            fail(f"README is missing marker {marker!r}")
    print("PASS: paper dossier, claim ledger, evidence hashes, release manifest, main-only branches, and canonical history verified")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, subprocess.CalledProcessError, OSError, json.JSONDecodeError, ValueError) as error:
        print(f"FAIL: {error}")
        raise SystemExit(1)
