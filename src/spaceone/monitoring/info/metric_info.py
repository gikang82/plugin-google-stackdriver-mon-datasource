import functools
from spaceone.api.monitoring.plugin import metric_pb2
from spaceone.core.pygrpc.message_type import *

__all__ = ['MetricsInfo', 'MetricDataInfo']


def MetricInfo(metric):
    info = {
        'key': metric['key'],
        'name': metric['name'],
        'unit': change_struct_type(metric['unit']),
        'chart_type': metric['chart_type']
    }

    if 'chart_options' in metric:
        info.update({
            'chart_options': change_struct_type(metric['chart_options'])
        })

    return metric_pb2.MetricInfo(**info)


def MetricsInfo(result):
    info = {
        'metrics': [MetricInfo(metric) for metric in result['metrics']]
    }

    return metric_pb2.MetricsInfo(**info)


def MetricDataInfo(metric_data):
    info = {
        'labels': change_list_value_type(metric_data.get('labels', [])),
        'resource_values': change_struct_type(metric_data['resource_values'])
    }
    return metric_pb2.MetricDataInfo(**info)