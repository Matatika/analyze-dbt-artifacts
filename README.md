# analyze-dbt-artifacts

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) of Matatika datasets for dbt artifacts from [tap-dbt-artifacts](https://github.com/Matatika/tap-dbt-artifacts).

Files:
- [`analyze/datasets`](./bundle/analyze/datasets) (directory)

Add plugin to `discovery.yml`:
```yaml
files:
- name: analyze-dbt-artifacts
  namespace: tap_dbt-artifacts
  update:
    analyze/datasets: true
  repo: https://github.com/Matatika/analyze-dbt-artifacts
  pip_url: git+https://github.com/Matatika/analyze-dbt-artifacts.git
```

Add plugin to your Meltano project:
```bash
# Add only the file bundle
meltano add files analyze-dbt-artifacts
```
