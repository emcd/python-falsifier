Remove immutability on ``Falsifier`` class as it may cause metaclass conflicts
on derived classes. Developers may use a separate mixin, such as
``frigid.ImmutableObject`` to achieve immutability on derived classes.
