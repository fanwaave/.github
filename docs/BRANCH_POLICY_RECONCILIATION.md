# Fanwaave feature-branch governance reconciliation

Status: **requires maintainer decision**. Reviewed: 2026-11-14.
Audience: repository maintainers, release engineering, and code-review agents.

The canonical `organization-policy.json` declares the `dev` integration
branch and directs feature PRs to `dev`. This declaration does **not**
provision a `dev` branch in each repository.

## Verified discrepancy

At review time, sampled repositories including `.github`, `fanwaave-cli`,
`fanwaave-infra`, `fanwaave-monorepo`, `fanwaave-sync`,
`fanwaave-desktop-app.rs`, `fanwaave-clients`,
`fanwaave-docs`, `fanwaave-mcp-server.rs`,
`fanwaave-admin-api-server.rs`, and `fanwaave-assets`
did not expose `refs/heads/dev`. `fanwaave-flutter` did.

## Safe promotion process

1. Inventory branch heads and protected/ruleset requirements for every
   repository. Verify live GitHub branch state; this document is a dated snapshot.
2. A maintainer must explicitly choose to provision `dev` per repository or
   revise `organization-policy.json` through its governed change process.
3. Do not silently target `main` just because `dev` is absent. Existing
   main-targeted drafts must be triaged and reconciled before promotion.
4. Require passing exact-head CI, security/dependency gates, and applicable
   approvals. A Git-level mergeable status alone is not evidence of readiness.
5. Do not force-update protected branches, skip required checks, or reinterpret
   an unavailable private dependency as a passing test.
6. Record the approved target branch and commit SHA for each promoted PR.

This is a documented policy gap, **not** permission to bypass GitFlow or GitOps.
