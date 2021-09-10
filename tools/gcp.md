# GCP

## DataFlow

* [Finding logs for common failures](https://cloud.google.com/dataflow/docs/guides/common-errors). Example:

        logName:("dataflow.googleapis.com%2Fkubelet" OR "projects/<project>/logs/dataflow.googleapis.com%2Fworker" OR "projects/<project>/logs/dataflow.googleapis.com%2Fharness-startup" OR "projects/<project>/logs/dataflow.googleapis.com%2Fdocker")
