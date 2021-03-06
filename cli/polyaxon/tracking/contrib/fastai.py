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

from polyaxon import settings
from polyaxon.exceptions import PolyaxonClientException
from polyaxon.tracking import Run

try:
    from fastai.callbacks import TrackerCallback
except ImportError:
    raise PolyaxonClientException("Fastai is required to use PolyaxonFastai")


class PolyaxonFastai(TrackerCallback):
    def __init__(self, learn, run=None, monitor="val_loss", mode="auto"):
        super(PolyaxonFastai, self).__init__(learn, monitor=monitor, mode=mode)
        self.run = run
        if settings.CLIENT_CONFIG.is_managed:
            self.run = self.run or Run()

    def on_epoch_end(self, epoch, smooth_loss, last_metrics, **kwargs):
        if not self.experiment:
            return
        metrics = {
            name: stat
            for name, stat in list(
                zip(self.learn.recorder.names, [epoch, smooth_loss] + last_metrics)
            )[1:]
        }

        self.run.log_metrics(**metrics)
