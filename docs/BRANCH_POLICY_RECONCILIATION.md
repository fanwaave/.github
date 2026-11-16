# Fanwaave feature-branch governance reconciliation

Status: **integration branches provisioned; protection controls unverified**.
Reviewed: 2026-11-14; read-only recheck: 2026-11-16.
Audience: repository maintainers, release engineering, and code-review agents.

The canonical `organization-policy.json` declares `dev` as the integration
branch and directs feature PRs to `dev`. Simply declaring this contract
does not create the branch or configure branch protection.

## Reconciliation performed

At the beginning of this audit, most of Fanwaave's 24 repositories lacked
`refs/heads/dev`; `fanwaave-flutter` already had `dev` but its history
diverged from `main`. In the user-authorized rollout, 23 missing `dev`
branches were created from each repository's `main`, without modifying or
merging production branches. All 24 new rollout draft PRs now target `dev`.
Flutter received a fresh dev-based, one-test-file draft rather than importing
unrelated main-branch history.

**Still outstanding:** creation of `dev` branches is not proof of protection.
The GitHub integration cannot read the branch-protection endpoint (403:
resource inaccessible by integration), and the inspected
`fanwaave-clients` repository returned no repository-level rulesets.
It is not safe to assume approval counts, required checks, or force-push
restrictions are enforced on the newly created branches.

## Verified follow-up snapshot (2026-11-16)

A new read-only GET of `/repos/fanwaave/<repo>/branches/dev` for **all
24 repositories** independently found `dev` present. Each response
reported `protected: false`. This is a concrete missing-positive-protection
signal, **not** proof that no organization rulesets or outside protections
exist: the integration lacks the administrative scope required to establish
complete effective rulesets and branch protection. Therefore every row below
remains **BLOCKED for automated promotion** until an authorized administrator
verifies and configures effective controls and required reviewer/check gates.

The SHAs are the observed `dev` tip commits for this dated snapshot,
**not PR heads, test results, or a request to pin these branch heads**.
Always refresh base and candidate heads before taking any action.

| Repository | Observed `dev` tip SHA | `protected` |
| --- | --- | --- |
| `fanwaave/fanwaave-pub-lib-core` | `1247079be6836f9628072c5c3d48302b2936865a` | `false` |
| `fanwaave/fanwaave-orm-core` | `bba2427eac7609b1b970efe32b9fb88ad63e229b` | `false` |
| `fanwaave/fanwaave-cli` | `6ff1922cd19ae0dd2ad086d7bc050dfdd101c659` | `false` |
| `fanwaave/fanwaave-assets` | `1d3d99047710c539c5dba8778f25bf0442b5c91e` | `false` |
| `fanwaave/fanwaave-interfaces` | `e070b70021f18c03344090a2d43a142003378c5c` | `false` |
| `fanwaave/fanwaave-clients` | `ffda2045ec1bb391e89d8c747d125ebc0258a2c3` | `false` |
| `fanwaave/fanwaave-docs` | `c8acaa65e010be631be75d3caaf615f857c8841c` | `false` |
| `fanwaave/fanwaave-infra` | `639772dcf2fb1054ddfd8f0820173a63345ba3ec` | `false` |
| `fanwaave/fanwaave-lib-core` | `1db7d079226763d3d6fa594c6a7d53999a39f18d` | `false` |
| `fanwaave/fanwaave-monorepo` | `2c175b80cc7ba837368b443cf74513eb8b8e3e11` | `false` |
| `fanwaave/fanwaave-sync` | `345375e7f1c934bda8506face28820bd1920eb0d` | `false` |
| `fanwaave/fanwaave-flutter` | `6058b35024c5a16969ac06d0e38b4755d87de7dc` | `false` |
| `fanwaave/fanwaave.github.io` | `9d063f1530d6d4e5ec7de8c2c7389998c1ca5e8d` | `false` |
| `fanwaave/fanwaave-sidecar.rs` | `33ab9ee7598e7e04b541abfcd5d204cc36596652` | `false` |
| `fanwaave/fanwaave-e2e` | `e3faacad80a526799f9c47b23f972a14998e19ec` | `false` |
| `fanwaave/fanwaave-web-server.rs` | `7b32aa87f22568ee7ea6210757603f7ba1fe48ac` | `false` |
| `fanwaave/fanwaave-mcp-server.rs` | `b1eac4619d9aa94d63d2b033f528bd15c5a2c6e1` | `false` |
| `fanwaave/fanwaave-desktop-app.rs` | `a3454a6ab6db1988969e64e8ccbc504402519bf1` | `false` |
| `fanwaave/fanwaave-admin-web-server.rs` | `2e487b80484ef5d45996c8259b2aa90761bafa96` | `false` |
| `fanwaave/fanwaave-admin-api-server.rs` | `2e6ea3bbdcd651a030c6237f3d5fee6e9538c9f3` | `false` |
| `fanwaave/fanwaave-contact-worker.rs` | `89291957354c59a8bda6e278df94badd135f648e` | `false` |
| `fanwaave/fanwaave-api-server.rs` | `f20a7970a641a5c7f40e820b0f330e5949609814` | `false` |
| `fanwaave/push-notification-server.rs` | `4eca298c68a7490e259f74eecad009ddeae01654` | `false` |
| `fanwaave/.github` | `07474a1722317c6f65b43d89d4002c35d3d379e1` | `false` |

This snapshot updates the initial branch-creation checkpoint; it does not
authorize a merge. For example, `fanwaave-contact-worker.rs#3` remains
non-draft with executed passing Rust CI at head
`faad7207fd61ca9ee121ff9ec13b424b658278d0`, but has no independent
submitted approval and its `dev` protections remain unverified.

## Required maintainer promotion gate

1. Check each `dev` branch's protection/rulesets with an authorized
   administrator. Configure required checks, reviews, and restrictions.
2. Confirm each draft PR changes only its intended files relative to `dev`.
   Revalidate exact head SHA after any push or base retarget.
3. Require passing exact-head CI, security/dependency gates, and applicable
   approvals. A Git-level mergeable status is insufficient.
4. Do not promote while private-dependency authentication, vulnerability
   advisories, missing contract authorities or Gitlink integrity remain
   unresolved.
5. Only merge to `dev` after all gates; follow the documented high-confidence
   integration-to-production GitOps promotion separately.
6. Record approved branch, head SHA, checks and reviewers for each merge.

This documents an integration-branch rollout, **not** an attestation that
the branch protections, integration tests or production delivery gates pass.
