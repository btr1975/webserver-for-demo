@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 1.0.4
REM

IF "%1" == "build" (
    python -m build
    GOTO END
)

IF "%1" == "coverage" (
    pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%1" == "pylint" (
    pylint webserver_for_demo\
    GOTO END
)

IF "%1" == "pytest" (
    pytest --cov -vvv
    GOTO END
)

IF "%1" == "dev-run" (
    python -c "from webserver_for_demo import cli;cli()" start -p 8080 -r
    GOTO END
)


IF "%1" == "gh-pages" (
    rmdir /s /q docs\source\code
    sphinx-apidoc -o ./docs/source/code ./webserver_for_demo
    sphinx-build ./docs ./docs/gh-pages
    GOTO END
)


@ECHO make options
@ECHO     build     To build a distribution
@ECHO     coverage  To run coverage and display ASCII and output to htmlcov
@ECHO     dev-run   To run the app
@ECHO     pylint    To run pylint
@ECHO     pytest    To run pytest with verbose option
@ECHO     gh-pages  To create the GitHub pages

:END
