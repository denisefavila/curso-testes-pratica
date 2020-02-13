import pytest

from dispatch.utils import get_checkin_geofence_radius

TRANSPORT_TYPE_MOTORCYCLE = 'motorcycle'
TRANSPORT_TYPE_VAN = 'van'
TRANSPORT_TYPE_WITH_DEFAULT_VALUE = 'car'


MAX_DISTANCE_MOTORCYCLE = 600
MAX_DISTANCE_VAN = 1500
MAX_DISTANCE_DEFAULT = 743.59


@pytest.mark.parametrize('transport_type, max_distance', [
    (TRANSPORT_TYPE_WITH_DEFAULT_VALUE, MAX_DISTANCE_DEFAULT),
    (TRANSPORT_TYPE_MOTORCYCLE, MAX_DISTANCE_MOTORCYCLE),
    (TRANSPORT_TYPE_VAN, MAX_DISTANCE_VAN)
])
def test_all_valid_transport_type_cases(transport_type, max_distance):

    max_distance = get_checkin_geofence_radius(transport_type)

    assert max_distance == max_distance
