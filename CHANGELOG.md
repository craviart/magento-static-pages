# Changelog

## [1.0.0] - 2026-10-15

### Changed

- Added explicit full-width campaign-root and centred inner-container guidance for Magento CMS handoffs.
- Added a required container contract in `handoff.md`: target-theme width and gutters, container selector, and any approved asymmetric exception.
- Added visual review gates at 1440px, 1920px, and narrow width for centring, occupied grid tracks, and unexplained empty container space.
- Strengthened the dependency-free validator to require a full-width root and reject a root-level `max-width`.
- Updated the compliant fixture and its review preview to demonstrate the full-width section and centred inner-container pattern.
