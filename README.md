# NovaTerm APT Repository

APT package repository for [NovaTerm](https://github.com/novaterm-org/NovaTerm) — the Rust-powered, GPU-accelerated, AI-native Android terminal emulator.

## Repository URL

```
https://novaterm-org.github.io/novaterm-apt-repo
```

## Quick Setup

Add the repository to your NovaTerm terminal:

```bash
# Add repository source
echo "deb [trusted=yes] https://novaterm-org.github.io/novaterm-apt-repo novaterm main" > $PREFIX/etc/apt/sources.list.d/novaterm.list

# Update package lists
apt update

# Install packages
apt install <package>
```

### With GPG Verification (when signing is configured)

```bash
# Import the signing key
curl -fsSL https://novaterm-org.github.io/novaterm-apt-repo/pubkey.gpg | apt-key add -

# Add repository (without [trusted=yes] since we verify signatures)
echo "deb https://novaterm-org.github.io/novaterm-apt-repo novaterm main" > $PREFIX/etc/apt/sources.list.d/novaterm.list

apt update
```

## Supported Architectures

| Architecture | Description |
|---|---|
| `aarch64` | ARM64 (primary target, Android 11+) |
| `all` | Architecture-independent packages |

## Repository Structure

```
dists/
  novaterm/
    main/
      binary-aarch64/   — arm64 package index (Packages, Packages.xz)
      binary-all/        — arch-independent package index
    Contents-aarch64     — file-to-package mapping
    Release              — repository metadata (checksums, arch, components)
    InRelease            — GPG-signed release metadata
pool/
  main/
    a/                    — packages starting with 'a'
    b/                    — packages starting with 'b'
    ...                   — organized by first letter of package name
pubkey.gpg               — Repository GPG public key
```

## Adding Packages

### From novaterm-packages build system

1. Build packages in [novaterm-packages](https://github.com/novaterm-org/novaterm-packages)
2. Copy `.deb` files to `debs/` directory in this repository
3. Push to `main` branch — the deployment workflow will regenerate the repository metadata

### Manual package upload

```bash
# Copy .deb files to the debs/ directory
cp package_1.0-1_aarch64.deb debs/

# Commit and push
git add debs/
git commit -m "feat: add package v1.0"
git push
```

The GitHub Actions workflow will automatically:
1. Organize packages into `pool/` by package name
2. Generate `Packages`, `Packages.xz`, `Contents-*` files
3. Create `Release` with checksums
4. Sign with GPG (if key is configured)
5. Deploy to GitHub Pages

## GPG Signing Setup

To enable signed releases, configure these repository secrets:

1. `GPG_PRIVATE_KEY` — ASCII-armored GPG private key
2. `GPG_PASSPHRASE` — Passphrase for the GPG key (if encrypted)

```bash
# Generate a GPG key for the repository
gpg --full-generate-key

# Export the private key
gpg --export-secret-keys --armor KEY_ID > private.key

# Add as GitHub repository secret: Settings → Secrets → Actions → New secret
# Name: GPG_PRIVATE_KEY
# Value: contents of private.key
```

## Building Packages

Packages are built in the [novaterm-packages](https://github.com/novaterm-org/novaterm-packages) repository and published here via the `publish-repo` workflow.

Key packages:
- `nvterm-exec` — W^X bypass (LD_PRELOAD exec interception)
- `bash` — Shell
- `coreutils` — Core utilities
- `apt` — Package manager

## License

Apache License 2.0