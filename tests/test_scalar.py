import pytest

from mozaggregator.scalar import Scalar


def test_int_scalar():
    name, value = 'telemetry.test.unsigned_int_kind', 8
    scalar = Scalar(name, value)

    assert scalar.get_value() == value
    assert scalar.get_name() == name
    assert scalar.get_definition().get('kind') == 'uint'
    assert Scalar.REQUIRED_FIELDS.issubset(scalar.get_definition().viewkeys())


def test_string_scalar():
    name, value = 'telemetry.test.string_kind', 'string'
    scalar = Scalar(name, value)

    assert scalar.get_value() == value
    assert scalar.get_name() == name
    assert scalar.get_definition().get('kind') == 'string'
    assert Scalar.REQUIRED_FIELDS.issubset(scalar.get_definition().viewkeys())


def test_boolean_scalar():
    name, value = 'telemetry.test.boolean_kind', True
    scalar = Scalar(name, value)

    assert scalar.get_value() == value
    assert scalar.get_name() == name
    assert scalar.get_definition().get('kind') == 'boolean'
    assert Scalar.REQUIRED_FIELDS.issubset(scalar.get_definition().viewkeys())


def test_int_addition():
    name, value = 'telemetry.test.unsigned_int_kind', 8
    scalar = Scalar(name, value) + Scalar(name, value)

    assert scalar.get_value() == value * 2
    assert scalar.get_name() == name
    assert Scalar.REQUIRED_FIELDS.issubset(scalar.get_definition().viewkeys())


def test_string_addition():
    name, value = 'telemetry.test.string_kind', 'string'

    with pytest.raises(AttributeError):
        Scalar(name, value) + Scalar(name, value)


def test_boolean_addition():
    name, value = 'telemetry.test.boolean_kind', True

    with pytest.raises(AttributeError):
        Scalar(name, value) + Scalar(name, value)


def test_release_channel():
    name, value = 'telemetry.test.unsigned_int_kind', 8
    scalar = Scalar(name, value, channel='release')

    assert scalar.get_value() == value
    assert scalar.get_name() == name
    assert Scalar.REQUIRED_FIELDS.issubset(scalar.get_definition().viewkeys())


def test_release_revision():
    name, value = 'telemetry.test.unsigned_int_kind', 8
    scalar = Scalar(name, value,
        revision='https://hg.mozilla.org/releases/mozilla-release/rev/tip')

    assert scalar.get_value() == value
    assert scalar.get_name() == name
    assert Scalar.REQUIRED_FIELDS.issubset(scalar.get_definition().viewkeys())


def test_release_url():
    name, value = 'telemetry.test.unsigned_int_kind', 8
    scalar = Scalar(name, value,
        scalars_url='https://hg.mozilla.org/releases/mozilla-release/raw-file/tip/toolkit/components/telemetry/Scalars.yaml')

    assert scalar.get_value() == value
    assert scalar.get_name() == name
    assert Scalar.REQUIRED_FIELDS.issubset(scalar.get_definition().viewkeys())


def test_channel_and_revision():
    name, value = 'telemetry.test.unsigned_int_kind', 8
    with pytest.raises(ValueError):
        Scalar(name, value, channel='nightly',
            revision='https://hg.mozilla.org/releases/mozilla-release/rev/tip')


def test_cache():
    name, value = 'telemetry.test.unsigned_int_kind', 8
    scalar = Scalar(name, value)
    scalar_2 = Scalar(name, value)

    assert scalar_2.get_value() == value
    assert scalar_2.get_name() == name
    assert Scalar.REQUIRED_FIELDS.issubset(scalar_2.get_definition().viewkeys())
