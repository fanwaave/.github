# Fanwaave organization environment policy

Only `env/enc/dev.env.enc` and `env/enc/prod.env.enc` may be tracked; plaintext stays under ignored, owner-only `env/dec/`. This governance repository is not a secret owner, so ciphertext is normally unnecessary. The guard exists to prevent provider, database, signing, push-certificate, token, or cloud credentials from entering shared templates and policy documents.
