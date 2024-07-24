from metaflow import FlowSpec, project, trigger_on_finish


@project(name="test_flow_project")
@trigger_on_finish(flow="TestFlow1")
class TestFlow3(FlowSpec):
    def start(self):
        self.next(self.end)

    def end(self):
        pass
