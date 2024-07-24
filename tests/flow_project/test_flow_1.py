from metaflow import FlowSpec, project


@project(name="test_flow_project")
class TestFlow1(FlowSpec):
    def start(self):
        self.next(self.end)

    def end(self):
        pass
