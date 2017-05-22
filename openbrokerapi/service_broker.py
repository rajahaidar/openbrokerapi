from typing import List

from openbrokerapi.catalog import Service


class ProvisionDetails:
    def __init__(self,
                 service_id: str,
                 plan_id: str,
                 organization_guid: str,
                 space_guid: str,
                 parameters=None):
        if parameters is None:
            parameters = {}

        self.service_id = service_id
        self.plan_id = plan_id
        self.organization_guid = organization_guid
        self.space_guid = space_guid
        self.parameters = parameters


class ProvisionedServiceSpec:
    def __init__(self,
                 # is_async: bool,
                 dashboard_url: str,
                 operation: str
                 ):
        self.is_async = False
        self.dashboard_url = dashboard_url
        self.operation = operation


class DeprovisionDetails:
    def __init__(self,
                 plan_id: str,
                 service_id: str
                 ):
        self.plan_id = plan_id
        self.service_id = service_id


class DeprovisionServiceSpec:
    def __init__(self,
                 is_async: bool,
                 operation: str
                 ):
        self.is_async = is_async
        self.operation = operation


class UpdateDetails:
    def __init__(self,
                 service_id: str,
                 plan_id: str,
                 parameters: str,
                 previous_values: str
                 ):
        self.service_id = service_id
        self.plan_id = plan_id
        self.parameters = parameters
        self.previous_values = previous_values


class UpdateServiceSpec:
    def __init__(self,
                 is_async: bool,
                 operation: str):
        self.is_async = is_async
        self.operation = operation


class BindResource:
    def __init__(self,
                 app_guid: str = None,
                 route: str = None
                 ):
        self.app_guid = app_guid
        self.route = route


class BindDetails:
    def __init__(self,
                 service_id: str,
                 plan_id: str,
                 app_guid: str = None,
                 bind_resource: BindResource = None,
                 parameters: dict = None
                 ):
        self.app_guid = app_guid
        self.plan_id = plan_id
        self.service_id = service_id
        self.bind_resource = bind_resource
        self.parameters = parameters


class SharedDevice:
    def __init__(self,
                 volume_id: str,
                 mount_config: dict
                 ):
        self.volume_id = volume_id
        self.mount_config = mount_config


class VolumeMount:
    def __init__(self,
                 driver: str,
                 container_dir: str,
                 mode: str,
                 device_type: str,
                 device: SharedDevice
                 ):
        self.driver = driver
        self.container_dir = container_dir
        self.mode = mode
        self.device_type = device_type
        self.device = device


class Binding:
    def __init__(self,
                 credentials: dict = None,
                 syslog_drain_url: str = None,
                 route_service_url: str = None,
                 volume_mounts: List[VolumeMount] = None
                 ):
        self.credentials = credentials
        self.syslog_drain_url = syslog_drain_url
        self.route_service_url = route_service_url
        self.volume_mounts = volume_mounts


class UnbindDetails:
    def __init__(self,
                 plan_id: str,
                 service_id: str
                 ):
        self.plan_id = plan_id
        self.service_id = service_id


class ServiceBroker:
    def catalog(self) -> List[Service]:
        """
        Returns the Catalog of all services that are provided by this broker.
        
        :return: List[Service] 
        """
        raise NotImplementedError()

    def provision(self, instance_id: str, service_details: ProvisionDetails,
                  async_allowed: bool) -> ProvisionedServiceSpec:
        """
        Further readings `CF Broker API#Provisioning <https://docs.cloudfoundry.org/services/api.html#provisioning>`_
        
        :param instance_id: Instance id provided by the platform
        :param service_details: Details about the service to create
        :param async_allowed: Client allows async creation
        :return: ProvisionedServiceSpec
        :raises ErrInstanceAlreadyExists: If instance already exists
        :raises ErrAsyncRequired: If async is required but not supported
        """
        raise NotImplementedError()

    def update(self, instance_id: str, details: UpdateDetails, async_allowed: bool) -> UpdateServiceSpec:
        """
        Further readings `CF Broker API#Update <https://docs.cloudfoundry.org/services/api.html#updating_service_instance>`_
        
        :param instance_id: Instance id provided by the platform
        :param details: Details about the service to update
        :param async_allowed: Client allows async creation
        :return: UpdateServiceSpec
        :raises ErrAsyncRequired: If async is required but not supported
        """
        raise NotImplementedError()

    def deprovision(self, instance_id: str, details: DeprovisionDetails,
                    async_allowed: bool) -> DeprovisionServiceSpec:
        """
        Further readings `CF Broker API#Deprovisioning <https://docs.cloudfoundry.org/services/api.html#deprovisioning>`_

        :param instance_id: Instance id provided by the platform
        :param details: Details about the service to delete
        :param async_allowed: Client allows async creation
        :return: DeprovisionServiceSpec
        :raises ErrInstanceDoesNotExist: If instance does not exists
        :raises ErrAsyncRequired: If async is required but not supported
        """
        raise NotImplementedError()

    def bind(self, instance_id: str, binding_id: str, details: BindDetails) -> Binding:
        """
        Further readings `CF Broker API#Binding <https://docs.cloudfoundry.org/services/api.html#binding>`_

        :param instance_id: Instance id provided by the platform
        :param binding_id: Binding id provided by the platform
        :param details: Details about the binding to create
        :return: Binding
        :raises ErrBindingAlreadyExists: If binding already exists
        :raises ErrAppGuidNotProvided: If AppGuid is required but not provided
        """
        raise NotImplementedError()

    def unbind(self, instance_id: str, binding_id: str, details: UnbindDetails):
        """
        Further readings `CF Broker API#Unbinding <https://docs.cloudfoundry.org/services/api.html#unbinding>`_

        :param instance_id: Instance id provided by the platform
        :param binding_id: Binding id provided by the platform
        :param details: Details about the binding to delete
        :return: UnbindDetails
        :raises ErrBindingAlreadyExists: If binding already exists
        """
        raise NotImplementedError()