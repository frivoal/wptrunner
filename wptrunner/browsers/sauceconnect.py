# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from .sauce import check_args, browser_kwargs, executor_kwargs, SauceBrowser
from ..executors.executorseleniumremote import (SeleniumRemoteTestharnessExecutor,
                                                SeleniumRemoteRefTestExecutor)
from ..environment import LocalServerEnvironment

__wptrunner__ = {"product": "sauceconnect",
                 "check_args": "check_args",
                 "browser": "SauceBrowser",
                 "executor": {"testharness": "SeleniumRemoteTestharnessExecutor",
                              "reftest": "SeleniumRemoteRefTestExecutor"},
                 "env": "LocalServerEnvironment",
                 "browser_kwargs": "browser_kwargs",
                 "executor_kwargs": "executor_kwargs",
                 "env_options": "env_options"}

def env_options():
    return {"host": "web-platform.test",
            "bind_hostname": "true"}
