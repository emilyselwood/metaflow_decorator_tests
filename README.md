# project trying to reproduce some strange behaviour in metaflow

Reproduction steps
1) run `poetry shell`
1) run `poetry install`
1) run `pytest`

expected: A message about finding no tests
Actual: 
```
=============================================================================================== test session starts ================================================================================================
platform darwin -- Python 3.10.12, pytest-7.4.4, pluggy-1.5.0
rootdir: /Users/emily.selwood/git/flows_in_tests_project
configfile: pyproject.toml
collected 0 items / 3 errors

====================================================================================================== ERRORS ======================================================================================================
________________________________________________________________________________ ERROR collecting tests/flow_project/test_flow_2.py ________________________________________________________________________________
tests/flow_project/test_flow_2.py:6: in <module>
    class TestFlowSFHGDFSHGDFJHJ2(FlowSpec):
.venv/lib/python3.10/site-packages/metaflow/decorators.py:416: in wrap
    return _base_flow_decorator(decofunc, f, **kwargs)
.venv/lib/python3.10/site-packages/metaflow/decorators.py:404: in _base_flow_decorator
    raise DuplicateFlowDecoratorException(decofunc.name)
E   metaflow.decorators.DuplicateFlowDecoratorException: Flow already has a decorator 'project'. You can specify each decorator only once.
________________________________________________________________________________ ERROR collecting tests/flow_project/test_flow_3.py ________________________________________________________________________________
tests/flow_project/test_flow_3.py:6: in <module>
    class TestFlow3(FlowSpec):
.venv/lib/python3.10/site-packages/metaflow/decorators.py:416: in wrap
    return _base_flow_decorator(decofunc, f, **kwargs)
.venv/lib/python3.10/site-packages/metaflow/decorators.py:404: in _base_flow_decorator
    raise DuplicateFlowDecoratorException(decofunc.name)
E   metaflow.decorators.DuplicateFlowDecoratorException: Flow already has a decorator 'trigger_on_finish'. You can specify each decorator only once.
________________________________________________________________________________ ERROR collecting tests/flow_project/test_flow_4.py ________________________________________________________________________________
tests/flow_project/test_flow_4.py:6: in <module>
    class TestFlow4(FlowSpec):
.venv/lib/python3.10/site-packages/metaflow/decorators.py:416: in wrap
    return _base_flow_decorator(decofunc, f, **kwargs)
.venv/lib/python3.10/site-packages/metaflow/decorators.py:404: in _base_flow_decorator
    raise DuplicateFlowDecoratorException(decofunc.name)
E   metaflow.decorators.DuplicateFlowDecoratorException: Flow already has a decorator 'trigger_on_finish'. You can specify each decorator only once.
================================================================================================= warnings summary =================================================================================================
tests/flow_project/test_flow_1.py:4
  /Users/emily.selwood/git/flows_in_tests_project/tests/flow_project/test_flow_1.py:4: PytestCollectionWarning: cannot collect test class 'TestFlow1' because it has a __init__ constructor (from: tests/flow_project/test_flow_1.py)
    @project(name="test_flow_project")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================================================================================= short test summary info ==============================================================================================
ERROR tests/flow_project/test_flow_2.py - metaflow.decorators.DuplicateFlowDecoratorException: Flow already has a decorator 'project'. You can specify each decorator only once.
ERROR tests/flow_project/test_flow_3.py - metaflow.decorators.DuplicateFlowDecoratorException: Flow already has a decorator 'trigger_on_finish'. You can specify each decorator only once.
ERROR tests/flow_project/test_flow_4.py - metaflow.decorators.DuplicateFlowDecoratorException: Flow already has a decorator 'trigger_on_finish'. You can specify each decorator only once.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 3 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
=========================================================================================== 1 warning, 3 errors in 0.63s ===========================================================================================
```