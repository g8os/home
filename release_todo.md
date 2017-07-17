# Release plan:

- Create release branches on all repos
- Create tag/release of the previous version ([script](https://github.com/Incubaid/dev_process/blob/master/scripts/createrelease.py))
- Run full test suite on the release branch
- Install full environment be-g8-3 and do manual tests
- Publish pypi packages
 - 0-core-client
 - 0-orchestrator
- Update Home repo: Move the release from `Release schedule` section to `Previous Releases`


### How to publish to pypi
```shell
python setup.py sdist bdist_wheel
twine upload dist/*
```
