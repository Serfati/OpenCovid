import unittest

from OpenCovid.lib.opencovid import OpenCoVid


def stub_callback(frame):
    pass

class StubNotAnalyzeFilter:
    def foo(self):
        pass

class StubNotAnalyzeFilterNoParameter:
    def detect(self):
        pass

class StubAnalyzeFilter:
    def detect(self,frame):
        pass

class OpenCovidTestCase(unittest.TestCase):
    def setUp(self):
        self.ocv_none = OpenCoVid(callback=None,video_src=None)
        self.ocv = OpenCoVid(callback=stub_callback)


    def test_reset(self):

        self.ocv.add_analyze_filter(StubAnalyzeFilter())
        self.ocv.add_analyze_filter(StubAnalyzeFilter())
        self.ocv.reset()
        self.assertEqual(len(self.ocv.pipeline_filters),0,"Filter list Should be empty")
        self.ocv.reset()
        self.assertEqual(len(self.ocv.pipeline_filters), 0, "Filter list Should be empty")

        pass

    def test_set_frame_src(self):
        self.ocv.set_frame_src(None)
        self.ocv.set_frame_src("blabla")
        self.ocv.set_frame_src(0)
        pass

    def test_add_analyze_filter(self):
        self.ocv.add_analyze_filter(StubNotAnalyzeFilter())
        self.assertEqual(len(self.ocv.pipeline_filters), 0, "Filter list Should be empty")
        self.ocv.add_analyze_filter(StubNotAnalyzeFilterNoParameter())
        self.assertEqual(len(self.ocv.pipeline_filters), 0, "Filter list Should be empty")
        self.ocv.add_analyze_filter(StubAnalyzeFilter())
        self.assertEqual(len(self.ocv.pipeline_filters), 1, "Filter Should be added")
        self.ocv.add_analyze_filter(None)
        self.assertEqual(len(self.ocv.pipeline_filters), 1, "None Should not be added")


    def test_stop_analyze(self):
        pass

    def test_apply_pipeline(self):
        pass

    def test_analyze(self):
        pass

    def tearDown(self):
        pass