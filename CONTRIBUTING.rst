============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/eventbrite/eventbrite-sdk-python/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

eventbrite-sdk-python could always use more documentation, whether as part of the
official eventbrite-sdk-python docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/eventbrite/eventbrite-sdk-python/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `eventbrite-sdk-python` for local development.

1. Fork the `eventbrite-sdk-python` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/eventbrite-sdk-python.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv eventbrite-sdk-python
    $ cd eventbrite-sdk-python/
    $ python setup.py develop
    $ pip install -e ".[testing]"

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox::

    $ flake8
    $ pytest
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Adding Environment Variables
------------------------------

In order to run the full test suite, you will need your USER_ID and OAUTH token from Eventbrite added as environment variables.

In your ``.bash_profile`` add::

    # Eventbrite envariables variables
    EVENTBRITE_USER_ID=XXXXXXXX
    EVENTBRITE_OAUTH_TOKEN=XXXXXXXX

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.7, 3.5, 3.6, 3.7, and 3.8, and for PyPy, and PyPy3.
   Check https://travis-ci.org/eventbrite/eventbrite-sdk-python/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

Running a subset of tests
~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ python -m unittest tests.test_eventbrite

Checking test coverage
~~~~~~~~~~~~~~~~~~~~~~

::

    $ make coverage

Running integration tests
~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to expedite development, by default these do not run.

1. Get an Eventbrite OAUTH token.

2. Via the Eventbrite website, create an event. Get the Event ID

3. Add those values as environment variables

::

    $ export EVENTBRITE_EVENT_ID=XXXXXXXXX
    $ export EVENTBRITE_OAUTH_TOKEN=XXXXXXXXXX

4. Run the test suite::

    make test
