# Fanwaave GitHub and Linear operating model

## Canonical systems

- GitHub organization: https://github.com/fanwaave
- GitHub Project: https://github.com/orgs/fanwaave/projects/1
- Linear project: https://linear.app/denman/project/githubcomfanwaave-6ba038b59dbc
- Migration issue: https://linear.app/denman/issue/DEN-1874
- Reliability issue: https://linear.app/denman/issue/DEN-1875

## Repository model

`fanwaave/push-notification-server.rs` owns push and contact delivery implementation, provider adapters, contracts, CI, security, and release artifacts. `fanwaave/.github` owns public organization context and shared community-health files.

## Delivery workflow

Changes move from Linear issue to feature branch to reviewed GitHub pull request to exact-head CI to merge. GitHub Project items provide the organization execution view; Linear remains the planning and cross-project source of record.
