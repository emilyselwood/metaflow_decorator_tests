from metaflow import FlowSpec, project, trigger_on_finish


@project(name="test_flow_project")
@trigger_on_finish(flows=["TestFlow2", "TestFlow3"])
class TestFlow4(FlowSpec):
    def start(self):
        self.next(self.end)

    def end(self):
        pass
