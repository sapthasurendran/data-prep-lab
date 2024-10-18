# (C) Copyright IBM Corp. 2024.
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

from data_processing.test_support.transform import NOOPFolderTransform, NOOPTransformConfiguration
from data_processing.utils import get_logger
from data_processing_spark.runtime.spark import SparkTransformLauncher
from data_processing_spark.runtime.spark import SparkTransformRuntimeConfiguration, DefaultSparkTransformRuntime
from data_processing.data_access import DataAccess


logger = get_logger(__name__)


class NOOPFolderSparkRuntime(DefaultSparkTransformRuntime):
    def get_folders(self, data_access: DataAccess) -> list[str]:
        """
        Get folders to process
        :param data_access: data access
        :return: list of folders to process
        """
        return [data_access.get_input_folder()]


class NOOPFolderSparkTransformConfiguration(SparkTransformRuntimeConfiguration):
    """
    Implements the SparkTransformConfiguration for NOOP as required by the PythonTransformLauncher.
    NOOP does not use a RayRuntime class so the superclass only needs the base
    python-only configuration.
    """

    def __init__(self):
        """
        Initialization
        """
        super().__init__(transform_config=NOOPTransformConfiguration(clazz=NOOPFolderTransform),
                         runtime_class=NOOPFolderSparkRuntime)


if __name__ == "__main__":
    # create launcher
    launcher = SparkTransformLauncher(runtime_config=NOOPFolderSparkTransformConfiguration())
    logger.info("Launching noop transform")
    # Launch the ray actor(s) to process the input
    launcher.launch()