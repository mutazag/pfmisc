# from typing import List
# from promptflow import tool


# @tool
# def aggregate(processed_results: List[dict]):
#     from promptflow import log_metric
#     """
#     This tool aggregates the processed result of all lines and log metric.

#     :param processed_results: List of the output of line_process node.
#     """

#     # Add your aggregation logic here

#     aggregated_results = {}



#     # Log metric


#     for m in processed_results: 
#         for k,v  in m.items(): 
#             log_metric(key=k, value=v)
#             if aggregated_results.get(k) is None:
#                 aggregated_results[k] = [v]
#             else:
#                 aggregated_results[k].append(v)


#     return aggregated_results


from typing import List
from promptflow import tool, log_metric
import numpy as np


@tool
def aggregate_variants_results(results: List[dict]):
    aggregate_results = {}
    for result in results:
        for name, value in result.items():
            if name not in aggregate_results.keys():
                aggregate_results[name] = []
            try:
                float_val = float(value)
            except Exception:
                float_val = np.nan
            aggregate_results[name].append(float_val)

    for name, value in aggregate_results.items():
        metric_name = name
        aggregate_results[name] = np.nanmean(value)
        if 'pass_rate' in metric_name:
            metric_name = metric_name + "(%)"
            aggregate_results[name] = aggregate_results[name] * 100.0
        aggregate_results[name] = round(aggregate_results[name], 2)
        log_metric(metric_name, aggregate_results[name])

    return aggregate_results
