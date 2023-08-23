from setuptools import setup, find_packages

setup(
    name="analyze-tap-dbt-artifacts",
    version="0.1.0",
    description="Meltano project file bundle of Matatika artifacts for analysis of your dbt artifacts ",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/channels/*.yml",
            "pipelines/*.yml",
            "analyze/datasets/dbt-test-results/*.yml"
        ]
    },
)
