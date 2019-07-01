from typing import Any, Iterable, Union

from hestia.bool_utils import to_bool
from hestia.list_utils import to_list

from query.builder import (
    ArrayCondition,
    CallbackCondition,
    ComparisonCondition,
    DateTimeCondition,
    SearchCondition,
    ValueCondition
)
from query.managers.base import BaseQueryManager
from query.parser import (
    parse_datetime_operation,
    parse_scalar_operation,
    parse_search_operation,
    parse_value_operation
)


def _indepenent_condition(queryset: Any, params: Union[str, Iterable], negation: bool) -> Any:
    params = to_list(params)
    if len(params) == 1 and to_bool(params[0]) is True:
        return queryset.filter(experiment_group__isnull=True)
    return queryset


class ExperimentQueryManager(BaseQueryManager):
    NAME = 'experiment'
    FIELDS_PROXY = {
        'metric': 'last_metric',
        'metrics': 'last_metric',
        'declarations': 'params',
        'status': 'status__status',
        'group': 'experiment_group',
        'build': 'build_job',
        'commit': 'code_reference__commit',
    }
    PARSERS_BY_FIELD = {
        # Id
        'id': parse_value_operation,
        # Dates
        'created_at': parse_datetime_operation,
        'updated_at': parse_datetime_operation,
        'started_at': parse_datetime_operation,
        'finished_at': parse_datetime_operation,
        # Name
        'name': parse_search_operation,
        # Description
        'description': parse_search_operation,
        # User
        'user': parse_value_operation,
        # Status
        'status': parse_value_operation,
        # Project
        'project': parse_value_operation,
        # Groups
        'group': parse_value_operation,
        # Builds
        'build': parse_value_operation,
        # Backend
        'backend': parse_value_operation,
        # Framework
        'framework': parse_value_operation,
        # Commit
        'commit': parse_value_operation,
        # Params
        'declarations': parse_value_operation,
        'params': parse_value_operation,
        # Tags
        'tags': parse_value_operation,
        # Metrics
        'metric': parse_scalar_operation,
        'metrics': parse_scalar_operation,
        # Idependent
        'independent': parse_value_operation,
    }
    CONDITIONS_BY_FIELD = {
        # Id
        'id': ValueCondition,
        # Dates
        'created_at': DateTimeCondition,
        'updated_at': DateTimeCondition,
        'started_at': DateTimeCondition,
        'finished_at': DateTimeCondition,
        # Name
        'name': SearchCondition,
        # Description
        'description': SearchCondition,
        # User
        'user': ValueCondition,
        # Status
        'status': ValueCondition,
        # Project
        'project': ValueCondition,
        # Groups
        'group': ValueCondition,
        # Builds
        'build': ValueCondition,
        # Backend
        'backend': ValueCondition,
        # Framework
        'framework': ValueCondition,
        # Commit
        'commit': ValueCondition,
        # Params
        'declarations': ValueCondition,
        'params': ValueCondition,
        # Tags
        'tags': ArrayCondition,
        # Metrics
        'metric': ComparisonCondition,
        'metrics': ComparisonCondition,
        # Independent
        'independent': CallbackCondition(_indepenent_condition),
    }
