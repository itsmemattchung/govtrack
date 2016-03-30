GovTrack Python
===============

Compatible with 2.X, 3.X

Bills
-----

.. code:: python

   import future
   import govtrack

   bill = govtrack.bill(id=76414)
   bills = govtrack.bills()
   for bill in bills:
       print('{b.congress} {b.current_status}'.format(b=bill)
