---
name: update-dependencies
description: Update pixi.toml dependencies to match the latest igrafx-mining-sdk version on PyPI
user_invocable: true
---

# Update KNIME Connector Dependencies

Update all dependencies in `pixi.toml` to be compatible with the latest version of `igrafx-mining-sdk` on PyPI.

## Step 1: Read current state

1. Read the project's `pixi.toml` to get current dependency versions and constraints.
2. Query PyPI for the latest `igrafx-mining-sdk` version: `https://pypi.org/pypi/igrafx-mining-sdk/json`
3. Fetch the SDK's full dependency list from PyPI for that version: `https://pypi.org/pypi/igrafx-mining-sdk/<version>/json` — extract all `requires_dist` entries with their version constraints, and the `requires_python` value.

## Step 2: Identify required changes

Compare each SDK dependency against the current `pixi.toml` constraints. Check both sections:
- `[dependencies]` — conda dependencies (resolved first by pixi, these take precedence)
- `[pypi-dependencies]` — pypi dependencies (resolved second, cannot override conda)
- `[target.<platform>.dependencies]` — platform-specific conda dependencies

**Critical constraint**: `knime-python-base` is a conda package on the KNIME channel that hard-pins transitive dependencies like `pandas` and `numpy` to exact versions. The pixi.toml conda constraints must accept these pinned versions. The SDK's dependency ranges must also accept them.

For each SDK dependency:
1. If the SDK pins an exact version (e.g., `requests==2.32.5`), ensure pixi.toml's range includes it.
2. If the SDK uses a range (e.g., `pandas>=2.0.3,<4.0.0`), ensure pixi.toml's range overlaps.
3. If there's a conflict with knime-python-base's hard pins, flag it — the SDK version cannot be used until the SDK relaxes its constraints.

## Step 3: Report findings

Present a table showing:

```
| Dependency       | Current (pixi.toml)    | SDK requires           | Proposed change        | Notes               |
|------------------|------------------------|------------------------|------------------------|----------------------|
| igrafx-mining-sdk| >=2.38.1,<3.0.0       | -                      | >=X.Y.Z,<3.0.0       |                      |
| networkx         | >=3.3.0, <3.6.1       | >=3.3.0,<3.6.1        | no change              | Already compatible   |
| ...              | ...                    | ...                    | ...                    | ...                  |
```

Flag any conflicts where the SDK's requirements are incompatible with knime-python-base.

Wait for user confirmation before proceeding.

## Step 4: Apply updates

After user confirms, update `pixi.toml`:
- Update the `igrafx-mining-sdk` version range in `[pypi-dependencies]`
- Update any conda or pypi dependency version ranges that need changing
- Update Python version constraint if the SDK requires a newer minimum
- Ensure changes are applied consistently across all platform-specific sections

## Step 5: Validate

Run the following commands sequentially:

```bash
rm -f pixi.lock
```
Delete the existing lockfile to force a clean resolution.

```bash
pixi lock
```
If `pixi lock` fails, diagnose the conflict. Common issues:
- A conda package pins a transitive dependency (e.g., `knime-python-base` pins `pandas==2.0.3`) that conflicts with the SDK's requirement. In this case, the SDK version is incompatible and cannot be used.
- A conda-resolved version of a package (e.g., `urllib3`) conflicts with the SDK's exact pin. Fix by adding or adjusting the pin in `[dependencies]`.

```bash
pixi install
```
Verify the environment installs successfully.

```bash
pixi run python -c "import igrafx_mining_sdk; print(f'SDK {igrafx_mining_sdk.__version__} imported successfully')"
```
Verify the SDK imports correctly in the resolved environment.

Report results to the user.
