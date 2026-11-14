# Fanwaave feature-branch governance reconciliation

Status: **integration branches provisioned; protection controls unverified**.
Reviewed: 2026-11-14.
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
