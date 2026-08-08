# .github

Organization-wide GitHub, branching, agent, and delivery policy for Fanwaave.

## Canonical systems

- Organization: https://github.com/fanwaave
- Push notification server: https://github.com/fanwaave/push-notification-server.rs
- GitHub Project: https://github.com/orgs/fanwaave/projects/1
- Linear project: https://linear.app/denman/project/githubcomfanwaave-6ba038b59dbc

This repository preserves Fanwaave's durable engineering, repository-boundary, GitFlow/GitOps, security, and semantic-conflict policies while providing the public organization profile and shared community-health defaults.

Start with:

- [`BRANCHING_AND_DEPLOYMENT.md`](BRANCHING_AND_DEPLOYMENT.md)
- [`GOVERNANCE.md`](GOVERNANCE.md)
- [`REPOSITORY_BOUNDARIES.md`](REPOSITORY_BOUNDARIES.md)
- [`CONTRIBUTING.md`](CONTRIBUTING.md)
- [`SECURITY.md`](SECURITY.md)
- [`docs/ORGANIZATION_HANDBOOK.md`](docs/ORGANIZATION_HANDBOOK.md)
- [`docs/PROJECTS.md`](docs/PROJECTS.md)
- [`docs/OPERATING_MODEL.md`](docs/OPERATING_MODEL.md)

<!-- ore-org-baseline:begin -->
## Organization-wide defaults

This public repository is the canonical source for GitHub-supported community-health fallbacks, organization profile content, contribution guidance, public security/support policy, issue and pull-request templates, and agent-governance declarations for [`fanwaave`](https://github.com/fanwaave).

## Canonical organization links

- GitHub organization: https://github.com/fanwaave
- Public organization defaults: https://github.com/fanwaave/.github
- Canonical Linear project: https://linear.app/denman/project/githubcomfanwaave-6ba038b59dbc
- Fleet tracking issue: https://github.com/ORESoftware/k8s-cluster/issues/1222

## Safety baseline

All Git conflicts must be resolved semantically with full historical, repository-wide, organization-wide, and relevant external-organization context. Automated agents are hard-denied from destructive or history-rewriting operations, including all forms of `git stash`, `git reset`, `git clean`, `git filter-repo`, force pushing, destructive deletion, data or infrastructure teardown, credential revocation, and policy bypass.

## GitHub inheritance boundary

GitHub can use supported community-health files from a public organization `.github` repository as fallbacks and can render `profile/README.md` on the organization page. `agents.md`, `AGENTS.md`, Copilot instructions, workflows, settings, rulesets, branch protections, permissions, and secrets are not automatically inherited merely because they exist here. Each repository must carry or synchronize compatible local policy and explicitly call reusable workflows where enforcement is required.

Generated managed-policy version: `2026-08-08`.
<!-- ore-org-baseline:end -->
