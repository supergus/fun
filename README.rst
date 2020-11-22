Having Fun with Fun!
====================

The ``fun`` package contains utilities that are entertaining yet somewhat useful. Maybe.


Installation
-------------

To install locally in 'editable mode' with all dependencies, clone the `GitHub repo`_
and run:

    ``$ pip install -e /path/to/package/fun``

Contact `me`_ if you have any questions. This is a fun project (obviously!) and I cannot
guarantee a response, sorry.

.. _GitHub repo: https://github.com/supergus/fun
.. _repo admin: mailto:christopher.couch@gmail.com

Package Contents
----------------

The ``fun`` repository contains three folders:

* ``communications``: Use E.T's communicator to send emails and SMS messages with a single command.
* ``printing``:  Print fancy, formatted text to the console and flaunt your style.
* ``bin``:  Executable examples.

After importing ``fun`` into your code, the utilities should be called directly using
``fun.<function>``. See examples below.

Caution
-------

The communications module requires an email account to establish an SMTP session.
You must configure the credentials listed at the top of ``fun/communications/communicator.py``.

How to Have Fun with E.T.'s Communicator!
-----------------------------------------

First, import the package:

.. code-block:: python

    import fun

Try sending some messages. The communicator *should* work regardless of whether you are inside a
company's managed network or not, assuming you are running from an authenticated session.

.. code-block:: python

    # Using arbitrary phone numbers or emails:
    fun.et.phone_home('Howdy, this is my message to you.', '734-555-5555', subject='Test message from Chris')

    # Using the JSON directory in fun/communications/contact_list.json to target users:
    fun.et.phone_home('There can never be too much foo.', 'joe', subject='Foo')

    # Using the JSON directory to target groups:
    fun.et.phone_home('Fear is the mindkiller.', ['admin', 'physics'], subject='I must not fear')

When using users or groups from the JSON directory, by default E.T. will send messages via email and SMS
to each targeted person. You can modify this behavior by toggling the boolean options ``disable_sms`` and
``disable_email``.

When providing explicit phone numbers or email addresses, you don't need to worry about toggling the options -
it's handled automatically. Phone numbers can be any format, including an integer, but they must contain 10 digits
after any leading 0s or 1s.

The contact directory is located at ``fun/communications/contact_list.json`` and can be edited freely.

Let's use the directory and select either email or SMS:

.. code-block:: python

    # Only send emails to the group 'physics', no SMS:
    fun.et.phone_home('Need those reports today.', 'physics', subject='TPS Reports', disable_sms=True)

    # Only send SMS messages to the user 'joe', no emails:
    fun.et.phone_home('There is no try.', 'joe', subject='Do or do not', disable_email=True)



Finally, you can add attachments to emails:

.. code-block:: python

    # Send email with attachment:
    target='/documents/tps_report.xlsx'     # A Path-like object
    fun.et.phone_home('Check this out!', 'chris@somewhere.com', subject='Report', attachment=target)

How to Have Fun with Fancy Printing!
------------------------------------

After importing the package, try printing some formatted text to the stdout console:

.. code-block:: python

    # See the docstring of fancy_print() for description of all options.
    fun.fancy_print('I like pretty things', fg='light_pink', bold=True, framed=True)

Run the built-in demo to see everything the Fancy Printer can do:

.. code-block:: python

    # Run the built-in demo
    fun.fancy_print('Foo Fighters Rule', demo=True)

That's all for now. Be sure to have some Fun!