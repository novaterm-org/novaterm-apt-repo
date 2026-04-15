# NovaTerm APT Repository

APT package repository for [NovaTerm](https://github.com/novaterm-org/NovaTerm) — the Rust-powered, GPU-accelerated, AI-native Android terminal emulator.

## Repository URL

```
https://novaterm-org.github.io/novaterm-apt-repo
```

## Usage

Add to your NovaTerm terminal:

```bash
echo "deb [trusted=yes] https://novaterm-org.github.io/novaterm-apt-repo novaterm main" > $PREFIX/etc/apt/sources.list.d/novaterm.list
apt update
apt install <package>
```

## Architecture

- `aarch64` (arm64) — Primary target (Android 11+)
- `all` — Architecture-independent packages

## Repository Structure

```
dists/
  novaterm/
    main/
      binary-aarch64/   — arm64 packages
      binary-all/        — arch-independent packages
    InRelease            — GPG-signed release metadata
pool/                    — .deb package files
```

## Building Packages

Packages are built in the [novaterm-packages](https://github.com/novaterm-org/novaterm-packages) repository and published here via the `publish-repo` workflow.

## GPG Key

The repository is signed. Import the key:

```bash
curl -fsSL https://novaterm-org.github.io/novaterm-apt-repo/pubkey.gpg | apt-key add -
```