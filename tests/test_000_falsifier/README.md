# tests/test_000_falsifier

Test suite for the `falsifier` package.

## Structure

```
test_000_falsifier/
├── __.py                # Test utilities (module cache, discovery)
├── __init__.py          # Test package marker
├── conftest.py          # Pytest configuration
├── test_000_package.py  # Package-level tests
├── test_010_base.py     # Base functionality tests
└── test_100_classes.py  # Falsifier class tests
```

## Test Function Numbering

Within each test module, functions are numbered by component:

- **000-099**: Basic functionality tests for the module
- **100-199, 200-299, etc.**: Each function/class gets its own 100-number block
- **Increments of 10-20**: For closely related test variations within a block

## Conventions

- Tests use cached module imports via `cache_import_module` to avoid
  re-import overhead
- Module discovery is automatic via `_discover_module_names`
- Test functions follow the pattern `test_NNN_descriptive_name`
