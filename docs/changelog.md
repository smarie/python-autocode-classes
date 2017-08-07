### 1.4.0 - Added validation feature

 * New: `@validate` annotation allowing to implement input validation. Comes with a bunch of built-in validators.

### 1.3.1 - Documentation and Travis integration 2

 * Improved documentation
 * Automatic test report generation in travis
 * Automatic PyPI deployment on tags in travis

### 1.3.0 - Project renaming

 * `classtools-autocode` Project was renamed `autoclass` for clarity
 * Travis configuration was updated accordingly

### 1.2.0 - Performance and documentation

 * improved examples in the documentation
 * improved performance of var_checker (lessons learnt from parsyfiles)

### 1.1.0 - Mkdocs and enforce

 * now using mkdocs to generate the documentation from markdown
 * `@autoprops`: generated getters and setters now have correct PEP484 signature, which makes the library compliant with `enforce`
 * updated documentation accordingly
 
### 1.0.0 - First public working version with PyContracts