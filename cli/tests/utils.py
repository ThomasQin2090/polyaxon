#!/usr/bin/python
#
# Copyright 2019 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8
from __future__ import absolute_import, division, print_function

import os
import six

from collections import Mapping
from unittest import TestCase

import ujson


def assert_equal_dict(dict1, dict2):
    for k, v in six.iteritems(dict1):
        if v is None:
            continue
        if isinstance(v, Mapping):
            assert_equal_dict(v, dict2[k])
        else:
            assert v == dict2[k]


def assert_equal_feature_processors(fp1, fp2):
    # Check that they have same features
    assert list(six.iterkeys(fp1)) == list(six.iterkeys(fp2))

    # Check that all features have the same graph
    for feature in fp1:
        assert_equal_graphs(fp2[feature], fp1[feature])


def assert_tensors(tensor1, tensor2):
    if isinstance(tensor1, six.string_types):
        tensor1 = [tensor1, 0, 0]

    if isinstance(tensor2, six.string_types):
        tensor2 = [tensor2, 0, 0]

    assert tensor1 == tensor2


def assert_equal_graphs(result_graph, expected_graph):
    for i, input_layer in enumerate(expected_graph["input_layers"]):
        assert_tensors(input_layer, result_graph["input_layers"][i])

    for i, output_layer in enumerate(expected_graph["output_layers"]):
        assert_tensors(output_layer, result_graph["output_layers"][i])

    for layer_i, layer in enumerate(result_graph["layers"]):
        layer_name, layer_data = list(six.iteritems(layer))[0]
        assert layer_name in expected_graph["layers"][layer_i]
        for k, v in six.iteritems(layer_data):
            assert v == expected_graph["layers"][layer_i][layer_name][k]


def assert_equal_layers(config, expected_layer):
    result_layer = config.to_dict()
    for k, v in six.iteritems(expected_layer):
        if v is not None or k not in config.REDUCED_ATTRIBUTES:
            assert v == result_layer[k]
        else:
            assert k not in result_layer


class TestEnvVarsCase(TestCase):
    @staticmethod
    def check_empty_value(key, expected_function):
        os.environ.pop(key, None)
        assert expected_function() is None

    @staticmethod
    def check_non_dict_value(key, expected_function, value="non dict random value"):
        os.environ[key] = value
        assert expected_function() is None

    @staticmethod
    def check_valid_dict_value(key, expected_function, value):
        os.environ[key] = ujson.dumps(value)
        assert expected_function() == value

    def check_raise_for_invalid_value(self, key, expected_function, value, exception):
        os.environ[key] = ujson.dumps(value)
        with self.assertRaises(exception):
            expected_function()

    @staticmethod
    def check_valid_value(key, expected_function, value, expected_value=None):
        os.environ[key] = value
        expected_value = expected_value or value
        assert expected_function() == expected_value
