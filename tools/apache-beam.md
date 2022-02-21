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
