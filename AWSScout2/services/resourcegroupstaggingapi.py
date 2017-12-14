# -*- coding: utf-8 -*-

import json

from AWSScout2.configs.regions import RegionalServiceConfig, RegionConfig



########################################
# ResourceGroupsTaggingApiRegionConfig
########################################

class ResourceGroupsTaggingApiRegionConfig(RegionConfig):


     pass


########################################
# ResourceGroupsTaggingApiConfig
########################################

class ResourceGroupsTaggingApiConfig(RegionalServiceConfig):
    region_config_class = ResourceGroupsTaggingApiRegionConfig

    def __init__(self, service_metadata, thread_config = 4):
        super(ResourceGroupsTaggingApiConfig, self).__init__(service_metadata, thread_config)
