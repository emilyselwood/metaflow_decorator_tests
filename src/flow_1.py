from metaflow import FlowSpec, project


@project(name="flow_project")
class Flow1(FlowSpec):
    def start(self):
        self.next(self.end)

    def end(self):
        pass
