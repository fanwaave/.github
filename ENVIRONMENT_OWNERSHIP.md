# Fanwaave environment ownership

Fanwaave has two repositories in the current organization inventory:

| Repository | Classification | Allowed secret classes |
|---|---|---|
| `push-notification-server.rs` | communications runtime/provider owner | NATS auth, service auth, FCM/APNs/Expo/Web Push, SendGrid, Twilio, observability credentials as required by enabled adapters |
| `.github` | governance/templates | none |

The runtime uses the canonical SOPS/Nix/Just path contract for local/dev/test or explicitly reviewed operator profiles. Production values remain in the protected deployment secret store and are separately issued per provider, service, and environment. The governance repository must never contain provider values or ciphertext copied from the runtime.

Adding a new repository or credential class requires a reviewed update to this matrix before code, templates, or deployment manifests adopt it.
