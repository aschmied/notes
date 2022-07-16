# Apache Beam

* [Beam Nuggets](https://github.com/mohaseeb/beam-nuggets)
    * Useful Apache Beam transforms that do not ship with the standard library
    * Examples: I/O for relational DBs, I/O for Kafka, reading CSVs, reading JSON
* Minimal stream test example in python

        import apache_beam as beam
        import pandas as pd
        from apache_beam.testing import test_stream
        from apache_beam.testing.test_pipeline import TestPipeline
        
        from merq_dataflow import transforms
        
        
        class Dump(beam.DoFn):
            def process(self, element):
                print(type(element))
                print(element)
        
        
        def test_it():
            stream = test_stream.TestStream()
            stream.add_elements([ts({"a": 2}, "12:00")])
            stream.add_elements([ts({"a.5": 2.5}, "12:00:01")])
            stream.add_elements([ts({"b": 3}, "12:01")])
            stream.add_elements([ts({"c": 4}, "12:03")])
            stream.advance_watermark_to_infinity()
        
            with TestPipeline() as p:
                output = (
                    p
                    | "stream" >> stream
                    | "window" >> beam.WindowInto(beam.window.FixedWindows(60))
                    | "add key" >> beam.Map(lambda elem: (None, elem))
                    | "group" >> beam.GroupByKey()
                    | "remove key" >> beam.Map(lambda elem: elem[1])
                    | "dump" >> beam.ParDo(Dump())
                )
        
        
        def ts(value, time_str):
            timestamp = pd.Timestamp(f"2000-01-01 {time_str}").timestamp()
            return beam.window.TimestampedValue(value, timestamp)

# DoFns

* Use the DoFn lifecycle (setup, start_bundle, finish_bundle, teardown)
  * e.g. to persist to an external API in finish_bundle
* Beware that a DoFn instance may be resued across different bundles, so be very careful about storing state in instance variables
* https://www.cloudskillsboost.google/course_sessions/615710/video/103666

# Watermarks

* Data freshness: the difference between wall time and output watermark time
* System latency: the maxmimum duration that an element has been processing or wating to be processed
* Triggers let you override the default "window emit" behaviour. They may emit based on
  * Event time (AfterWatermark. The default)
  * Processing time (AfterProcessingTime)
  * Composite of other trigger types (AfterCount)
  * Data (currently only option is to fire based on element count)
* Triggers are used to emit data early or to process late data
* Accumulation mode lets you control what happens when a window is re-triggered after late data (accumulate or discard)
  * A window may have *multiple triggers*. Accumulation mode is how you handle it
  * Discard is used when your calculation is associative and commutative

# Sources and Sinks

* "By default the BigQuery writer uses streaming writes"

# More refs

* M1-Module-Resources.pdf.pdf
* Course https://www.cloudskillsboost.google/course_sessions/615710/video/103680
