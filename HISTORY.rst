.. :changelog:

History
-------

3.3.5 (2020-03-16)
------------------

* Added testing and support for Python versions up to 3.8, along with PyPy 3.
* Remove support for deprecated Python versions 2.6, 3.3, and 3.4.
* Fixed ``get_format()`` and ``get_formats()`` methods, to use the right endpoint.

3.3.4 (2016-05-05)
------------------

* Added new organizers endpoint (thanks tp @mgrdcm)
    * GET /organizers/:id/events/

3.3.3 (2015-08-24)
------------------

* Added 3 new user endpoints, thanks to @jon-ga (#29)

  * GET /users/:id/events/
  * GET /users/:id/venues/
  * GET /users/:id/organizers/

3.3.2  (2015-08-17)
-------------------

* Removed type mapping as it added unnecessary complexity preventing easy management of paginated responses.

3.2.1 (2015-08-10)
------------------

* Enabled webhooks
* Fixed ticket definitions in Event creation test
* Set input variable using input argument thanks to Bill So (#27).

3.2.0 (2015-07-07)
-------------------

* Added new publish and unpublish methods thanks to Ryan Bagwell.
* Eventbrite client now accepts an ``eventbrite_api_url`` argument.

3.1.0 (2015-05-11)
------------------

* Added control over expansion of response. Documentation at http://www.eventbrite.com/developer/v3/reference/expansions/

3.0.5 (2015-04-24)
------------------

* Removed 'content-type' header from all GET requests. Thank you @xxv for identifying the problem and contributing code.

3.0.4 (2015-03-12)
------------------

* Resolved the search result response problem where filtering did not work.


3.0.3 (2015-03-02)
------------------

* Fixed import issue with ``__version__``. Thank you @meshy  and @longjos for identifying the problem.

3.0.2 (2015-01-30)
------------------

* Event creation now working.
* Added feature allowing the use of Eventbrite API url at test servers. Should expedite development of tricky post actions.


3.0.1 (2015-01-30)
------------------

* Added reverse mapping for ``get_event_ticket_class()`` method.
* Added ``events`` mapping to provide GET access to the Event endpoint.
* Removed several deprecated JSON mappings.

3.0.0 (2015-01-28)
------------------

* Initial release of 3.0.0 client

3.0.0-alpha (2014-12-05)
------------------------


* Inception
