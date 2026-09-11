# Fanwaave communications provider boundaries

`push-notification-server.rs` is the shared non-auth communications plane for push notifications, application email, and application SMS. Product servers publish typed jobs or call its authenticated API instead of receiving SendGrid, Twilio, FCM, APNs, Expo, or Web Push credentials directly.

Authentication and security challenges are separate: Shared Auth owns numeric email OTP through SendGrid and phone enrollment/step-up through Twilio Verify. Fanwaave must not mint auth sessions, consume auth OTPs, or reuse Shared Auth provider credentials.

Provider keys are least-privilege, separately issued per service/environment, and injected by the protected deployment store. No full-access key is copied across repositories. Provider canaries must not print recipients, device endpoints, message bodies, callback secrets, authorization headers, or raw upstream responses.

Any credential exposed in chat, logs, tickets, or Git is revoked and replaced before production use; encrypting an already-exposed value is not remediation.
