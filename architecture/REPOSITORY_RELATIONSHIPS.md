# `fanwaave` repository relationships

Generated from reviewed policy and the current **public** repository inventory.

- Public repositories declared: **2**
- Private repository names withheld: **0**
- Relationship edges: **3**

## Repository roles

| Repository | Role | Lifecycle |
|---|---|---|
| [`.github`](https://github.com/fanwaave/.github) | `organization_governance` | `active` |
| [`push-notification-server.rs`](https://github.com/fanwaave/push-notification-server.rs) | `domain_service` | `active` |

## Declared edges

| From | Relationship | To | Status/basis |
|---|---|---|---|
| `fanwaave/.github` | `governs` | `fanwaave/push-notification-server.rs` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `organization://fanwaave` | `deployed_via` | `platform://ORESoftware/k8s-cluster` | `platform-default` / `platform-policy`: immutable artifacts are promoted by digest through GitOps |
| `organization://fanwaave` | `packaged_via` | `platform://zed-pkg` | `platform-default` / `platform-policy`: Zed resolves artifacts while submodules compose editable source |

## Composition, service, and observability contract

Git submodules compose editable source; Zed packages resolve packages/artifacts; dual-managed commits must match. Production deploys immutable image digests, not runtime source builds. Cross-service access uses APIs/SDKs/events rather than another service database. MCP uses the product API/SDK. Services emit OpenTelemetry traces, bounded metrics, and correlated structured logs.

## Privacy boundary

This public registry deliberately omits private repository names and edges; the count above makes the boundary explicit.
